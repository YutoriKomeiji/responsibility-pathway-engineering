"""Python-only additive composition for experimental M3 responsibility guards.

This module composes caller-declared integrity and Human Return readiness checks
into ordinary Risk Condition nodes before invoking the existing M3 gateway. It
keeps REST/MCP/OpenAPI adapter contracts unchanged until those surfaces are
versioned together.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date
from typing import Any

from .gateway import evaluate_gateway_request, evaluate_integrity_guarded_gateway_request, evaluate_transition
from .human_return import evaluate_human_return_readiness, human_return_result_to_risk_condition
from .risk_conditions import CONTROL_ACTIONS


def _strings(value: Any) -> list[str]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return sorted({item for item in value if isinstance(item, str) and item})


def _fail_closed(payload: Mapping[str, Any], reason_code: str, *, today: date | None) -> dict[str, Any]:
    """Return the ordinary gateway response shape with a fail-closed transition."""
    baseline = evaluate_gateway_request(payload, today=today)
    evaluation = baseline.get("evaluation_result")
    if not isinstance(evaluation, Mapping):
        return baseline

    risk_result = {
        "graph_status": "unresolved",
        "reason_codes": [reason_code],
        "required_controls": ["hold"],
        "triggered_conditions": [],
        "unknown_conditions": ["guard-validation"],
        "evaluated_conditions": [],
    }
    baseline["risk_condition_result"] = risk_result
    baseline["transition_result"] = evaluate_transition(
        evaluation,
        requested_route=payload.get("requested_route") if isinstance(payload.get("requested_route"), Mapping) else payload.get("requested_route"),
        constraints=payload.get("constraints") if isinstance(payload.get("constraints"), Sequence) else None,
        risk_result=risk_result,
    )
    return baseline


def _human_return_conditions(
    checks: Sequence[Mapping[str, Any]],
) -> tuple[list[dict[str, Any]], str | None]:
    conditions: list[dict[str, Any]] = []
    for entry in checks:
        if not isinstance(entry, Mapping) or set(entry) - {"return", "required_controls"}:
            return [], "RPE-M3-HUMAN-RETURN-CHECK-ENTRY-INVALID"
        return_payload = entry.get("return")
        controls = _strings(entry.get("required_controls"))
        if not isinstance(return_payload, Mapping):
            return [], "RPE-M3-HUMAN-RETURN-CHECK-ENTRY-INVALID"
        if not controls:
            return [], "RPE-M3-HUMAN-RETURN-CHECK-CONTROL-REQUIRED"
        if any(control not in CONTROL_ACTIONS for control in controls):
            return [], "RPE-M3-HUMAN-RETURN-CHECK-UNSUPPORTED-CONTROL"

        result = evaluate_human_return_readiness(return_payload)
        conditions.append(
            human_return_result_to_risk_condition(
                result,
                required_controls=controls,
            )
        )
    return conditions, None


def _payload_with_extra_conditions(
    payload: Mapping[str, Any],
    extra_conditions: Sequence[Mapping[str, Any]],
) -> dict[str, Any] | None:
    merged = dict(payload)
    if not extra_conditions:
        return merged

    risk_graph = payload.get("risk_graph")
    if risk_graph is None:
        merged["risk_graph"] = {"conditions": [dict(item) for item in extra_conditions]}
        return merged
    if not isinstance(risk_graph, Mapping):
        return None
    nodes = risk_graph.get("conditions")
    if not isinstance(nodes, Sequence) or isinstance(nodes, (str, bytes, bytearray)):
        return None
    merged["risk_graph"] = {
        "conditions": list(nodes) + [dict(item) for item in extra_conditions],
    }
    return merged


def evaluate_responsibility_guarded_gateway_request(
    payload: Mapping[str, Any],
    *,
    integrity_checks: Sequence[Mapping[str, Any]] = (),
    human_return_checks: Sequence[Mapping[str, Any]] = (),
    today: date | None = None,
) -> dict[str, Any]:
    """Compose bounded M3 guard observations into one Python gateway call.

    Each check remains descriptive until a caller/policy layer supplies explicit
    controls. Multiple triggered controls are not ranked here; the ordinary Risk
    Condition evaluator requires explicit selection and otherwise fails closed.
    The returned object is the existing GatewayEvaluateResponse shape and creates
    neither execution nor authority.
    """
    if not isinstance(payload, Mapping):
        return evaluate_gateway_request(payload, today=today)
    if not isinstance(integrity_checks, Sequence) or isinstance(integrity_checks, (str, bytes, bytearray)):
        return _fail_closed(payload, "RPE-M3-INTEGRITY-CHECKS-INVALID", today=today)
    if not isinstance(human_return_checks, Sequence) or isinstance(human_return_checks, (str, bytes, bytearray)):
        return _fail_closed(payload, "RPE-M3-HUMAN-RETURN-CHECKS-INVALID", today=today)

    return_conditions, error = _human_return_conditions(human_return_checks)
    if error is not None:
        return _fail_closed(payload, error, today=today)

    guarded_payload = _payload_with_extra_conditions(payload, return_conditions)
    if guarded_payload is None:
        return _fail_closed(payload, "RPE-M3-RISK-GRAPH-INVALID", today=today)

    return evaluate_integrity_guarded_gateway_request(
        guarded_payload,
        integrity_checks=integrity_checks,
        today=today,
    )
