"""Experimental M3 responsibility-gateway transformation.

This module is additive to the M2 evaluation pipeline. It transforms an
existing evaluation result into bounded continuation metadata; it does not
perform routing, dispatch, external-effect verification, retry, repair, or
resume operations.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Mapping, Sequence

from .pipeline import evaluate_governed_action
from .risk_conditions import CONTROL_ACTIONS, evaluate_risk_conditions

M3_GATEWAY_CONTRACT_VERSION = "0.1.0-exp"

ROUTE_TARGET_KINDS = frozenset(
    {
        "human",
        "agent",
        "verifier",
        "saas",
        "legacy_system",
        "institution",
        "workflow",
        "queue",
        "sandbox",
        "simulator",
        "hold",
        "stop",
    }
)

FORBIDDEN_OPERATIONAL_KEYS = frozenset(
    {
        "dispatch_state",
        "effect_state",
        "retry_state",
        "reconciliation_state",
        "repair_state",
        "resume_state",
        "execution_authority",
        "repair_authority",
        "resume_authority",
    }
)


def _normalized_strings(value: Any) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [item for item in value if isinstance(item, str) and item]


def normalize_route_target(value: Mapping[str, Any] | None) -> tuple[dict[str, Any] | None, list[str]]:
    """Validate a descriptive route target without dispatching to it."""
    if value is None:
        return None, []
    if not isinstance(value, Mapping):
        return None, ["RPE-M3-ROUTE-INVALID-TARGET"]

    kind = value.get("kind")
    target_id = value.get("target_id")
    purpose = value.get("purpose")

    if kind not in ROUTE_TARGET_KINDS:
        return None, ["RPE-M3-ROUTE-UNSUPPORTED-KIND"]
    if target_id is not None and (not isinstance(target_id, str) or not target_id):
        return None, ["RPE-M3-ROUTE-INVALID-TARGET-ID"]
    if purpose is not None and (not isinstance(purpose, str) or not purpose):
        return None, ["RPE-M3-ROUTE-INVALID-PURPOSE"]

    return {
        "kind": kind,
        "target_id": target_id,
        "purpose": purpose,
        "authority_effect": "none",
        "dispatch_effect": "none",
    }, []


def _missing_evidence(evaluation_result: Mapping[str, Any]) -> list[str]:
    handoff = evaluation_result.get("responsibility_handoff")
    if isinstance(handoff, Mapping):
        evidence = handoff.get("evaluation_evidence_scope")
        if isinstance(evidence, Mapping):
            return _normalized_strings(evidence.get("missing"))

    evidence = evaluation_result.get("evidence_scope")
    if isinstance(evidence, Mapping):
        return _normalized_strings(evidence.get("missing"))
    return []


def _available_evidence(evaluation_result: Mapping[str, Any]) -> list[str]:
    handoff = evaluation_result.get("responsibility_handoff")
    if isinstance(handoff, Mapping):
        evidence = handoff.get("evaluation_evidence_scope")
        if isinstance(evidence, Mapping):
            return _normalized_strings(evidence.get("available"))
    return []


def _residual_owner_role(evaluation_result: Mapping[str, Any]) -> str:
    handoff = evaluation_result.get("responsibility_handoff")
    if isinstance(handoff, Mapping):
        obligations = handoff.get("downstream_obligations")
        if isinstance(obligations, Mapping):
            role = obligations.get("residual_owner_role")
            if isinstance(role, str) and role:
                return role

    human_return = evaluation_result.get("human_return")
    if isinstance(human_return, Mapping):
        role = human_return.get("role")
        if isinstance(role, str) and role:
            return role
    return "downstream_execution_owner"


def _human_route(evaluation_result: Mapping[str, Any]) -> dict[str, Any]:
    human_return = evaluation_result.get("human_return")
    if not isinstance(human_return, Mapping):
        handoff = evaluation_result.get("responsibility_handoff")
        if isinstance(handoff, Mapping):
            human_return = handoff.get("human_return")

    role = human_return.get("role") if isinstance(human_return, Mapping) else None
    return {
        "kind": "human",
        "target_id": role if isinstance(role, str) and role else None,
        "purpose": "responsibility_return",
        "authority_effect": "none",
        "dispatch_effect": "none",
    }


def _transition_descriptor(
    evaluation_result: Mapping[str, Any],
    *,
    route_target: dict[str, Any] | None,
    missing: list[str],
) -> dict[str, Any]:
    return {
        "source": {
            "kind": "rpe_evaluation",
            "request_id": evaluation_result.get("request_id"),
        },
        "destination": route_target,
        "purpose": route_target.get("purpose") if isinstance(route_target, dict) else None,
        "authority": {
            "effect": "none",
            "downstream_authority_required": True,
        },
        "evidence": {
            "available": _available_evidence(evaluation_result),
            "missing": missing,
        },
        "residual_owner_role": _residual_owner_role(evaluation_result),
        "dispatch_effect": "none",
    }


def _risk_controls(risk_result: Mapping[str, Any] | None) -> tuple[str | None, list[str], list[str]]:
    """Return one explicit control only when selection is unambiguous."""
    if risk_result is None:
        return None, [], []
    if not isinstance(risk_result, Mapping):
        return "hold", ["RPE-M3-RISK-RESULT-INVALID"], []

    status = risk_result.get("graph_status")
    reasons = _normalized_strings(risk_result.get("reason_codes"))
    controls = sorted(set(_normalized_strings(risk_result.get("required_controls"))))

    if status in {"invalid", "unresolved"}:
        return "hold", reasons or ["RPE-M3-RISK-GRAPH-UNRESOLVED"], controls
    if any(control not in CONTROL_ACTIONS for control in controls):
        return "hold", reasons + ["RPE-M3-RISK-RESULT-UNSUPPORTED-CONTROL"], controls
    if len(controls) > 1:
        return "hold", reasons + ["RPE-M3-CONTROL-SELECTION-REQUIRED"], controls
    if len(controls) == 1:
        return controls[0], reasons, controls
    return None, reasons, []


def evaluate_transition(
    evaluation_result: Mapping[str, Any],
    *,
    requested_route: Mapping[str, Any] | None = None,
    constraints: Sequence[str] | None = None,
    risk_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Derive an experimental bounded continuation from an RPE evaluation result.

    The M2 evaluation decision remains the baseline. A risk-condition result may
    only narrow an M2 ``allow`` result; it cannot override an M2 Human Gate,
    deny, or hold. The returned object is evaluation metadata only and cannot
    grant authority or execute the requested route.
    """
    if not isinstance(evaluation_result, Mapping):
        evaluation_result = {}

    reason_codes = _normalized_strings(evaluation_result.get("reason_codes"))
    normalized_route, route_reasons = normalize_route_target(requested_route)
    normalized_constraints = _normalized_strings(constraints)
    missing = _missing_evidence(evaluation_result)
    decision = evaluation_result.get("decision")
    risk_control, risk_reasons, risk_candidates = _risk_controls(risk_result)
    reason_codes.extend(risk_reasons)
    control_action: str
    route_target = normalized_route

    if route_reasons:
        control_action = "hold"
        reason_codes.extend(route_reasons)
        route_target = None
    elif decision == "allow":
        if risk_control == "hold":
            control_action = "hold"
            route_target = None
        elif risk_control is not None:
            control_action = risk_control
            if control_action in {"route", "handoff"} and route_target is None:
                control_action = "hold"
                reason_codes.append("RPE-M3-ROUTE-TARGET-REQUIRED")
        elif normalized_route is not None:
            control_action = "route"
        elif normalized_constraints:
            control_action = "allow_with_constraints"
        else:
            control_action = "allow"
    elif decision == "human_gate":
        if missing:
            control_action = "require_evidence"
        else:
            control_action = "handoff"
            if route_target is None:
                route_target = _human_route(evaluation_result)
    elif decision == "deny":
        control_action = "deny"
        route_target = None
    elif decision == "hold":
        control_action = "hold"
    else:
        control_action = "hold"
        reason_codes.append("RPE-M3-GATEWAY-UNSUPPORTED-EVALUATION-DECISION")
        route_target = None

    result = {
        "contract_version": M3_GATEWAY_CONTRACT_VERSION,
        "control_action": control_action,
        "source_evaluation_decision": decision,
        "authority_effect": "none",
        "execution_effect": "none",
        "route_target": route_target,
        "responsibility_transition": _transition_descriptor(
            evaluation_result,
            route_target=route_target,
            missing=missing,
        ),
        "constraints": normalized_constraints,
        "unmet_conditions": missing,
        "risk_condition_result": dict(risk_result) if isinstance(risk_result, Mapping) else None,
        "candidate_controls": risk_candidates,
        "reason_codes": sorted(set(reason_codes)),
        "downstream_executor_required": True,
    }

    assert not (FORBIDDEN_OPERATIONAL_KEYS & set(result))
    return result


def _invalid_gateway_request(reason_code: str) -> dict[str, Any]:
    transition = evaluate_transition(
        {
            "decision": "hold",
            "reason_codes": [reason_code],
            "request_id": None,
        }
    )
    return {
        "contract_version": M3_GATEWAY_CONTRACT_VERSION,
        "evaluation_result": None,
        "risk_condition_result": None,
        "transition_result": transition,
        "authority_effect": "none",
        "execution_effect": "none",
    }


def evaluate_gateway_request(
    payload: Mapping[str, Any],
    *,
    today: date | None = None,
) -> dict[str, Any]:
    """Evaluate one experimental M3 gateway request through the M2 governed path.

    This is the thin-adoption entry point. A caller supplies one governed M2
    evaluation envelope plus optional risk graph, requested route, and bounded
    constraints. RPE returns evaluation and transition metadata only.
    """
    if not isinstance(payload, Mapping):
        return _invalid_gateway_request("RPE-M3-GATEWAY-REQUEST-INVALID")

    allowed_keys = {
        "contract_version",
        "governed_evaluation",
        "risk_graph",
        "requested_route",
        "constraints",
    }
    if set(payload) - allowed_keys:
        return _invalid_gateway_request("RPE-M3-GATEWAY-REQUEST-UNKNOWN-FIELD")
    if payload.get("contract_version") != M3_GATEWAY_CONTRACT_VERSION:
        return _invalid_gateway_request("RPE-M3-GATEWAY-REQUEST-INCOMPATIBLE-VERSION")

    governed_evaluation = payload.get("governed_evaluation")
    if not isinstance(governed_evaluation, Mapping):
        return _invalid_gateway_request("RPE-M3-GATEWAY-REQUEST-MISSING-EVALUATION")

    risk_graph = payload.get("risk_graph")
    risk_result = evaluate_risk_conditions(risk_graph) if risk_graph is not None else None
    evaluation_result = evaluate_governed_action(dict(governed_evaluation), today=today)
    transition_result = evaluate_transition(
        evaluation_result,
        requested_route=payload.get("requested_route") if isinstance(payload.get("requested_route"), Mapping) else payload.get("requested_route"),
        constraints=payload.get("constraints") if isinstance(payload.get("constraints"), Sequence) else None,
        risk_result=risk_result,
    )

    return {
        "contract_version": M3_GATEWAY_CONTRACT_VERSION,
        "evaluation_result": evaluation_result,
        "risk_condition_result": risk_result,
        "transition_result": transition_result,
        "authority_effect": "none",
        "execution_effect": "none",
    }
