#!/usr/bin/env python3
"""Deterministic checks for the experimental M3 responsibility gateway."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from rpe_kernel import (
    evaluate_gateway_request,
    evaluate_governed_action,
    evaluate_risk_conditions,
    evaluate_transition,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"

FORBIDDEN_OPERATIONAL_KEYS = {
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


def assert_bounded(result: dict) -> None:
    assert result["contract_version"] == "0.1.0-exp", result
    assert result["authority_effect"] == "none", result
    assert result["execution_effect"] == "none", result
    assert result["downstream_executor_required"] is True, result
    assert not (FORBIDDEN_OPERATIONAL_KEYS & set(result)), result
    route = result.get("route_target")
    if route is not None:
        assert route["dispatch_effect"] == "none", route
        assert route["authority_effect"] == "none", route
    transition = result["responsibility_transition"]
    assert transition["authority"]["effect"] == "none", transition
    assert transition["authority"]["downstream_authority_required"] is True, transition
    assert transition["dispatch_effect"] == "none", transition


def assert_gateway_bounded(result: dict) -> None:
    assert result["contract_version"] == "0.1.0-exp", result
    assert result["authority_effect"] == "none", result
    assert result["execution_effect"] == "none", result
    assert_bounded(result["transition_result"])


def _graph(*conditions: dict) -> dict:
    return {"conditions": list(conditions)}


def main() -> int:
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))

    allowed_evaluation = evaluate_governed_action(base, today=date(2026, 9, 1))
    allowed = evaluate_transition(allowed_evaluation)
    assert allowed["control_action"] == "allow", allowed
    assert allowed["route_target"] is None, allowed
    assert_bounded(allowed)

    routed = evaluate_transition(
        allowed_evaluation,
        requested_route={
            "kind": "verifier",
            "target_id": "independent-verifier",
            "purpose": "second_check",
        },
    )
    assert routed["control_action"] == "route", routed
    assert routed["route_target"]["kind"] == "verifier", routed
    assert routed["responsibility_transition"]["destination"] == routed["route_target"], routed
    assert_bounded(routed)

    constrained = evaluate_transition(
        allowed_evaluation,
        constraints=["max_targets=1", "no_delegation"],
    )
    assert constrained["control_action"] == "allow_with_constraints", constrained
    assert constrained["constraints"] == ["max_targets=1", "no_delegation"], constrained
    assert_bounded(constrained)

    clear_risk = evaluate_risk_conditions(
        _graph(
            {
                "condition_id": "target_known",
                "status": "clear",
                "required_controls": [],
                "evidence_refs": ["target-binding"],
            }
        )
    )
    assert clear_risk["graph_status"] == "clear", clear_risk
    assert clear_risk["scalar_score"] is None, clear_risk
    clear = evaluate_transition(allowed_evaluation, risk_result=clear_risk)
    assert clear["control_action"] == "allow", clear
    assert_bounded(clear)

    authority_graph = _graph(
        {
            "condition_id": "authority_scope_mismatch",
            "status": "triggered",
            "required_controls": ["require_authority"],
            "evidence_refs": ["authority-binding"],
        }
    )
    authority_risk = evaluate_risk_conditions(authority_graph)
    assert authority_risk["graph_status"] == "triggered", authority_risk
    require_authority = evaluate_transition(allowed_evaluation, risk_result=authority_risk)
    assert require_authority["control_action"] == "require_authority", require_authority
    assert require_authority["candidate_controls"] == ["require_authority"], require_authority
    assert_bounded(require_authority)

    route_risk = evaluate_risk_conditions(
        _graph(
            {
                "condition_id": "independent_verification_route",
                "status": "triggered",
                "required_controls": ["route"],
            }
        )
    )
    route_without_target = evaluate_transition(allowed_evaluation, risk_result=route_risk)
    assert route_without_target["control_action"] == "hold", route_without_target
    assert "RPE-M3-ROUTE-TARGET-REQUIRED" in route_without_target["reason_codes"], route_without_target
    assert_bounded(route_without_target)

    route_with_target = evaluate_transition(
        allowed_evaluation,
        risk_result=route_risk,
        requested_route={
            "kind": "sandbox",
            "target_id": "bounded-sandbox",
            "purpose": "evidence_gathering",
        },
    )
    assert route_with_target["control_action"] == "route", route_with_target
    assert route_with_target["route_target"]["kind"] == "sandbox", route_with_target
    assert_bounded(route_with_target)

    competing_risk = evaluate_risk_conditions(
        _graph(
            {
                "condition_id": "missing_independent_evidence",
                "status": "triggered",
                "required_controls": ["require_evidence"],
            },
            {
                "condition_id": "autonomy_envelope_expansion",
                "status": "triggered",
                "required_controls": ["downgrade_autonomy"],
                "depends_on": ["missing_independent_evidence"],
            },
        )
    )
    assert competing_risk["required_controls"] == ["downgrade_autonomy", "require_evidence"], competing_risk
    assert "RPE-M3-CONTROL-SELECTION-REQUIRED" in competing_risk["reason_codes"], competing_risk
    competing = evaluate_transition(allowed_evaluation, risk_result=competing_risk)
    assert competing["control_action"] == "hold", competing
    assert "RPE-M3-CONTROL-SELECTION-REQUIRED" in competing["reason_codes"], competing
    assert_bounded(competing)

    unknown_risk = evaluate_risk_conditions(
        _graph(
            {
                "condition_id": "relationship_integrity",
                "status": "unknown",
                "required_controls": ["isolate"],
            }
        )
    )
    assert unknown_risk["graph_status"] == "unresolved", unknown_risk
    unknown = evaluate_transition(allowed_evaluation, risk_result=unknown_risk)
    assert unknown["control_action"] == "hold", unknown
    assert "RPE-M3-RISK-CONDITION-UNKNOWN" in unknown["reason_codes"], unknown
    assert_bounded(unknown)

    invalid_dependency = evaluate_risk_conditions(
        _graph(
            {
                "condition_id": "trajectory_scope_expansion",
                "status": "triggered",
                "required_controls": ["downgrade_autonomy"],
                "depends_on": ["missing-node"],
            }
        )
    )
    assert invalid_dependency["graph_status"] == "invalid", invalid_dependency
    invalid_risk_transition = evaluate_transition(allowed_evaluation, risk_result=invalid_dependency)
    assert invalid_risk_transition["control_action"] == "hold", invalid_risk_transition
    assert "RPE-M3-RISK-CONDITION-UNKNOWN-DEPENDENCY" in invalid_risk_transition["reason_codes"], invalid_risk_transition
    assert_bounded(invalid_risk_transition)

    missing_evidence_input = copy.deepcopy(base)
    missing_evidence_input["request"]["context"]["human_approval_present"] = False
    missing_evidence_input["request"]["evidence_scope"] = {
        "available": [],
        "missing": ["approval-record"],
    }
    missing_evaluation = evaluate_governed_action(missing_evidence_input, today=date(2026, 9, 1))
    need_evidence = evaluate_transition(missing_evaluation, risk_result=authority_risk)
    assert need_evidence["control_action"] == "require_evidence", need_evidence
    assert need_evidence["unmet_conditions"] == ["approval-record"], need_evidence
    assert_bounded(need_evidence)

    human_gate_without_missing = {
        "decision": "human_gate",
        "reason_codes": ["RPE-M3-DEMO-HUMAN-REVIEW"],
        "human_return": {"role": "review_owner"},
        "responsibility_handoff": {
            "evaluation_evidence_scope": {"available": [], "missing": []},
            "human_return": {"role": "review_owner"},
        },
    }
    handoff = evaluate_transition(human_gate_without_missing, risk_result=authority_risk)
    assert handoff["control_action"] == "handoff", handoff
    assert handoff["route_target"]["kind"] == "human", handoff
    assert handoff["route_target"]["target_id"] == "review_owner", handoff
    assert_bounded(handoff)

    denied = evaluate_transition({"decision": "deny", "reason_codes": ["RPE-M3-DEMO-DENY"]}, risk_result=clear_risk)
    assert denied["control_action"] == "deny", denied
    assert denied["route_target"] is None, denied
    assert_bounded(denied)

    invalid_route = evaluate_transition(
        allowed_evaluation,
        requested_route={"kind": "unbounded_magic_router", "target_id": "x"},
    )
    assert invalid_route["control_action"] == "hold", invalid_route
    assert "RPE-M3-ROUTE-UNSUPPORTED-KIND" in invalid_route["reason_codes"], invalid_route
    assert_bounded(invalid_route)

    unsupported = evaluate_transition({"decision": "maybe", "reason_codes": []})
    assert unsupported["control_action"] == "hold", unsupported
    assert "RPE-M3-GATEWAY-UNSUPPORTED-EVALUATION-DECISION" in unsupported["reason_codes"], unsupported
    assert_bounded(unsupported)

    thin = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "risk_graph": authority_graph,
            "constraints": ["no_delegation"],
        },
        today=date(2026, 9, 1),
    )
    assert thin["evaluation_result"]["decision"] == "allow", thin
    assert thin["risk_condition_result"]["required_controls"] == ["require_authority"], thin
    assert thin["transition_result"]["control_action"] == "require_authority", thin
    assert_gateway_bounded(thin)

    thin_invalid_version = evaluate_gateway_request(
        {
            "contract_version": "9.9.9",
            "governed_evaluation": base,
        },
        today=date(2026, 9, 1),
    )
    assert thin_invalid_version["evaluation_result"] is None, thin_invalid_version
    assert thin_invalid_version["transition_result"]["control_action"] == "hold", thin_invalid_version
    assert "RPE-M3-GATEWAY-REQUEST-INCOMPATIBLE-VERSION" in thin_invalid_version["transition_result"]["reason_codes"], thin_invalid_version
    assert_gateway_bounded(thin_invalid_version)

    thin_unknown_field = evaluate_gateway_request(
        {
            "contract_version": "0.1.0-exp",
            "governed_evaluation": base,
            "dispatch_now": True,
        },
        today=date(2026, 9, 1),
    )
    assert thin_unknown_field["transition_result"]["control_action"] == "hold", thin_unknown_field
    assert "RPE-M3-GATEWAY-REQUEST-UNKNOWN-FIELD" in thin_unknown_field["transition_result"]["reason_codes"], thin_unknown_field
    assert_gateway_bounded(thin_unknown_field)

    print("M3 experimental responsibility gateway checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
