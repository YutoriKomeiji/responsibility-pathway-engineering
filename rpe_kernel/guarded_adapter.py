"""Versioned experimental M3 guarded adapter core.

This module defines the 0.2.0-exp request/response behavior for bounded guard
observations. It does not expose a network surface by itself. REST/MCP/OpenAPI
may adopt this core only when their contracts are revised together.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date
from typing import Any

from .guarded_gateway import evaluate_responsibility_guarded_gateway_request
from .human_return import evaluate_human_return_readiness
from .integrity import compare_integrity_binding
from .risk_conditions import CONTROL_ACTIONS

GUARDED_ADAPTER_CONTRACT_VERSION = "0.2.0-exp"
_BASE_GATEWAY_VERSION = "0.1.0-exp"


def _strings(value: Any) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return sorted({item for item in value if isinstance(item, str) and item})


def _invalid(reason_code: str) -> dict[str, Any]:
    return {
        "contract_version": GUARDED_ADAPTER_CONTRACT_VERSION,
        "evaluation_result": None,
        "guard_observations": {
            "integrity_results": [],
            "human_return_results": [],
        },
        "risk_condition_result": {
            "graph_status": "unresolved",
            "triggered_conditions": [],
            "unknown_conditions": ["guarded-adapter-validation"],
            "required_controls": ["hold"],
            "reason_codes": [reason_code],
            "scalar_score": None,
        },
        "transition_result": {
            "contract_version": _BASE_GATEWAY_VERSION,
            "control_action": "hold",
            "source_evaluation_decision": "hold",
            "authority_effect": "none",
            "execution_effect": "none",
            "route_target": None,
            "responsibility_transition": {
                "source": {"kind": "rpe_evaluation", "request_id": None},
                "destination": None,
                "purpose": "guarded_adapter_validation",
                "authority": {"effect": "none", "downstream_authority_required": True},
                "evidence": {"available": [], "missing": []},
                "residual_owner_role": "downstream_execution_owner",
                "dispatch_effect": "none",
            },
            "constraints": [],
            "unmet_conditions": [],
            "risk_condition_result": None,
            "candidate_controls": ["hold"],
            "reason_codes": [reason_code],
            "downstream_executor_required": True,
        },
        "authority_effect": "none",
        "execution_effect": "none",
    }


def _validate_entries(
    value: Any,
    *,
    kind: str,
) -> tuple[list[Mapping[str, Any]], list[dict[str, Any]], str | None]:
    if value is None:
        return [], [], None
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return [], [], f"RPE-M3-{kind}-CHECKS-INVALID"

    normalized: list[Mapping[str, Any]] = []
    observations: list[dict[str, Any]] = []
    for entry in value:
        if not isinstance(entry, Mapping) or set(entry) - {"check", "required_controls"}:
            return [], [], f"RPE-M3-{kind}-CHECK-ENTRY-INVALID"
        check = entry.get("check")
        controls = _strings(entry.get("required_controls"))
        if not isinstance(check, Mapping):
            return [], [], f"RPE-M3-{kind}-CHECK-ENTRY-INVALID"
        if not controls:
            return [], [], f"RPE-M3-{kind}-CHECK-CONTROL-REQUIRED"
        if any(control not in CONTROL_ACTIONS for control in controls):
            return [], [], f"RPE-M3-{kind}-CHECK-UNSUPPORTED-CONTROL"

        if kind == "INTEGRITY":
            observation = compare_integrity_binding(check)
            normalized.append({"check": dict(check), "required_controls": controls})
        else:
            observation = evaluate_human_return_readiness(check)
            normalized.append({"return": dict(check), "required_controls": controls})
        observations.append(observation)
    return normalized, observations, None


def evaluate_guarded_adapter_request(
    payload: Mapping[str, Any],
    *,
    today: date | None = None,
) -> dict[str, Any]:
    """Evaluate the experimental 0.2.0-exp guarded adapter contract.

    Guard observations remain descriptive. Policy consequences are accepted only
    through explicit caller-supplied required_controls. The result creates no
    authority or execution effect.
    """
    if not isinstance(payload, Mapping):
        return _invalid("RPE-M3-GUARDED-ADAPTER-REQUEST-INVALID")

    allowed = {
        "contract_version",
        "governed_evaluation",
        "risk_graph",
        "integrity_checks",
        "human_return_checks",
        "requested_route",
        "constraints",
    }
    if set(payload) - allowed:
        return _invalid("RPE-M3-GUARDED-ADAPTER-REQUEST-UNKNOWN-FIELD")
    if payload.get("contract_version") != GUARDED_ADAPTER_CONTRACT_VERSION:
        return _invalid("RPE-M3-GUARDED-ADAPTER-REQUEST-INCOMPATIBLE-VERSION")
    governed = payload.get("governed_evaluation")
    if not isinstance(governed, Mapping):
        return _invalid("RPE-M3-GUARDED-ADAPTER-REQUEST-MISSING-EVALUATION")

    integrity_entries, integrity_results, error = _validate_entries(
        payload.get("integrity_checks"), kind="INTEGRITY"
    )
    if error is not None:
        return _invalid(error)
    return_entries, return_results, error = _validate_entries(
        payload.get("human_return_checks"), kind="HUMAN-RETURN"
    )
    if error is not None:
        return _invalid(error)

    base_payload: dict[str, Any] = {
        "contract_version": _BASE_GATEWAY_VERSION,
        "governed_evaluation": dict(governed),
    }
    for key in ("risk_graph", "requested_route", "constraints"):
        if key in payload:
            base_payload[key] = payload.get(key)

    result = evaluate_responsibility_guarded_gateway_request(
        base_payload,
        integrity_checks=integrity_entries,
        human_return_checks=return_entries,
        today=today,
    )

    return {
        "contract_version": GUARDED_ADAPTER_CONTRACT_VERSION,
        "evaluation_result": result.get("evaluation_result"),
        "guard_observations": {
            "integrity_results": integrity_results,
            "human_return_results": return_results,
        },
        "risk_condition_result": result.get("risk_condition_result"),
        "transition_result": result.get("transition_result"),
        "authority_effect": "none",
        "execution_effect": "none",
    }
