"""Experimental M3 risk-condition graph evaluator.

The graph preserves condition relationships and control requirements without
collapsing them into a scalar risk score.  It does not grant authority, dispatch
an action, or choose between conflicting policy controls.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

RISK_GRAPH_CONTRACT_VERSION = "0.1.0-exp"

CONDITION_STATUSES = frozenset({"clear", "triggered", "unknown"})
CONTROL_ACTIONS = frozenset(
    {
        "allow_with_constraints",
        "route",
        "require_evidence",
        "require_authority",
        "downgrade_autonomy",
        "sandbox",
        "observe_only",
        "budget_limit",
        "isolate",
        "handoff",
        "hold",
        "deny",
        "emergency_stop",
    }
)


def evaluate_risk_conditions(graph: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate a declarative condition graph without inventing policy.

    Each node declares its own status and the controls required when triggered.
    Unknown nodes are preserved as unresolved.  Invalid dependencies or control
    names make the graph invalid.  If multiple different controls are required,
    this function returns all of them and leaves selection to an explicit policy
    or authority layer.
    """
    if not isinstance(graph, Mapping):
        return {
            "contract_version": RISK_GRAPH_CONTRACT_VERSION,
            "graph_status": "invalid",
            "triggered_conditions": [],
            "unknown_conditions": [],
            "required_controls": ["hold"],
            "reason_codes": ["RPE-M3-RISK-GRAPH-INVALID"],
            "scalar_score": None,
        }

    if set(graph) - {"conditions"}:
        return {
            "contract_version": RISK_GRAPH_CONTRACT_VERSION,
            "graph_status": "invalid",
            "triggered_conditions": [],
            "unknown_conditions": [],
            "required_controls": ["hold"],
            "reason_codes": ["RPE-M3-RISK-GRAPH-UNKNOWN-FIELD"],
            "scalar_score": None,
        }

    nodes = graph.get("conditions")
    if not isinstance(nodes, list):
        return {
            "contract_version": RISK_GRAPH_CONTRACT_VERSION,
            "graph_status": "invalid",
            "triggered_conditions": [],
            "unknown_conditions": [],
            "required_controls": ["hold"],
            "reason_codes": ["RPE-M3-RISK-GRAPH-MISSING-CONDITIONS"],
            "scalar_score": None,
        }

    normalized: dict[str, dict[str, Any]] = {}
    reasons: list[str] = []
    for raw in nodes:
        if not isinstance(raw, Mapping):
            reasons.append("RPE-M3-RISK-CONDITION-INVALID")
            continue
        if set(raw) - {"condition_id", "status", "required_controls", "depends_on", "evidence_refs"}:
            reasons.append("RPE-M3-RISK-CONDITION-UNKNOWN-FIELD")
            continue
        condition_id = raw.get("condition_id")
        status = raw.get("status")
        raw_controls = raw.get("required_controls")
        # The schema requires a string array. Do not silently discard malformed
        # controls: doing so could turn a triggered condition into an allow.
        if (
            not isinstance(raw_controls, list)
            or any(not isinstance(item, str) or not item for item in raw_controls)
            or len(set(raw_controls)) != len(raw_controls)
        ):
            reasons.append("RPE-M3-RISK-CONDITION-INVALID-CONTROLS")
            continue
        controls = raw_controls
        # Optional relationship/evidence fields still have strict array shapes.
        # Dropping an invalid dependency can conceal an unresolved risk.
        related: dict[str, list[str]] = {}
        invalid_optional = False
        for key, reason in (
            ("depends_on", "RPE-M3-RISK-CONDITION-INVALID-DEPENDENCIES"),
            ("evidence_refs", "RPE-M3-RISK-CONDITION-INVALID-EVIDENCE-REFS"),
        ):
            raw_values = raw.get(key, [])
            if (
                not isinstance(raw_values, list)
                or any(not isinstance(item, str) or not item for item in raw_values)
                or len(set(raw_values)) != len(raw_values)
            ):
                reasons.append(reason)
                invalid_optional = True
            else:
                related[key] = raw_values
        if invalid_optional:
            continue
        depends_on = related["depends_on"]
        evidence_refs = related["evidence_refs"]
        if not isinstance(condition_id, str) or not condition_id:
            reasons.append("RPE-M3-RISK-CONDITION-MISSING-ID")
            continue
        if condition_id in normalized:
            reasons.append("RPE-M3-RISK-CONDITION-DUPLICATE-ID")
            continue
        if not isinstance(status, str) or status not in CONDITION_STATUSES:
            reasons.append("RPE-M3-RISK-CONDITION-INVALID-STATUS")
            continue
        unsupported = sorted(set(controls) - CONTROL_ACTIONS)
        if unsupported:
            reasons.append("RPE-M3-RISK-CONDITION-UNSUPPORTED-CONTROL")
            continue
        normalized[condition_id] = {
            "condition_id": condition_id,
            "status": status,
            "required_controls": sorted(set(controls)),
            "depends_on": sorted(set(depends_on)),
            "evidence_refs": sorted(set(evidence_refs)),
        }

    for node in normalized.values():
        for dependency in node["depends_on"]:
            if dependency not in normalized:
                reasons.append("RPE-M3-RISK-CONDITION-UNKNOWN-DEPENDENCY")

    if reasons:
        return {
            "contract_version": RISK_GRAPH_CONTRACT_VERSION,
            "graph_status": "invalid",
            "conditions": list(normalized.values()),
            "triggered_conditions": [],
            "unknown_conditions": [],
            "required_controls": ["hold"],
            "reason_codes": sorted(set(reasons)),
            "scalar_score": None,
        }

    triggered = [node for node in normalized.values() if node["status"] == "triggered"]
    unknown = [node for node in normalized.values() if node["status"] == "unknown"]
    required_controls = sorted(
        {
            control
            for node in triggered
            for control in node["required_controls"]
        }
    )

    graph_status = "unresolved" if unknown else ("triggered" if triggered else "clear")
    reason_codes: list[str] = []
    if unknown:
        reason_codes.append("RPE-M3-RISK-CONDITION-UNKNOWN")
    if len(required_controls) > 1:
        reason_codes.append("RPE-M3-CONTROL-SELECTION-REQUIRED")

    return {
        "contract_version": RISK_GRAPH_CONTRACT_VERSION,
        "graph_status": graph_status,
        "conditions": list(normalized.values()),
        "triggered_conditions": [node["condition_id"] for node in triggered],
        "unknown_conditions": [node["condition_id"] for node in unknown],
        "required_controls": required_controls,
        "reason_codes": sorted(set(reason_codes)),
        "scalar_score": None,
    }
