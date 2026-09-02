"""Experimental M3 responsibility-gateway transformation.

This module is additive to the M2 evaluation pipeline. It transforms an
existing evaluation result into bounded continuation metadata; it does not
perform routing, dispatch, external-effect verification, retry, repair, or
resume operations.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

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


def evaluate_transition(
    evaluation_result: Mapping[str, Any],
    *,
    requested_route: Mapping[str, Any] | None = None,
    constraints: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Derive an experimental bounded continuation from an RPE evaluation result.

    The returned object is evaluation metadata only. It cannot grant authority
    or execute the requested route.
    """
    if not isinstance(evaluation_result, Mapping):
        evaluation_result = {}

    reason_codes = _normalized_strings(evaluation_result.get("reason_codes"))
    normalized_route, route_reasons = normalize_route_target(requested_route)
    normalized_constraints = _normalized_strings(constraints)
    missing = _missing_evidence(evaluation_result)
    decision = evaluation_result.get("decision")
    control_action: str
    route_target = normalized_route

    if route_reasons:
        control_action = "hold"
        reason_codes.extend(route_reasons)
        route_target = None
    elif decision == "allow":
        if normalized_route is not None:
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
        "reason_codes": sorted(set(reason_codes)),
        "downstream_executor_required": True,
    }

    assert not (FORBIDDEN_OPERATIONAL_KEYS & set(result))
    return result
