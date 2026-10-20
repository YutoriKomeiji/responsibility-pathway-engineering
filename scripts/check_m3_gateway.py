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

    # Direct Python entry must reject malformed controls even when callers
    # bypass the JSON Schema validator. Silent filtering could wrongly allow.
    for invalid_controls in ("deny", ["deny", 17], [None], ["deny", "deny"]):
        malformed_risk = evaluate_risk_conditions(
            _graph(
                {
                    "condition_id": "blocked_transition",
                    "status": "triggered",
                    "required_controls": invalid_controls,
                }
            )
        )
        assert malformed_risk["graph_status"] == "invalid", malformed_risk
        assert "RPE-M3-RISK-CONDITION-INVALID-CONTROLS" in malformed_risk["reason_codes"], malformed_risk
        malformed_transition = evaluate_transition(allowed_evaluation, risk_result=malformed_risk)
        assert malformed_transition["control_action"] == "hold", malformed_transition
        assert_bounded(malformed_transition)

    # Schema and direct Python ingestion must agree: a malformed relationship
    # or unexpected field cannot be normalized away and lead to continuation.
    invalid_graphs = (
        ({"conditions": [], "dispatch_now": True}, "RPE-M3-RISK-GRAPH-UNKNOWN-FIELD"),
        ({"conditions": ()}, "RPE-M3-RISK-GRAPH-MISSING-CONDITIONS"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "dispatch_now": True}),
         "RPE-M3-RISK-CONDITION-UNKNOWN-FIELD"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "depends_on": [None]}),
         "RPE-M3-RISK-CONDITION-INVALID-DEPENDENCIES"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "depends_on": "missing"}),
         "RPE-M3-RISK-CONDITION-INVALID-DEPENDENCIES"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "depends_on": ["c", "c"]}),
         "RPE-M3-RISK-CONDITION-INVALID-DEPENDENCIES"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "evidence_refs": ["evidence", 42]}),
         "RPE-M3-RISK-CONDITION-INVALID-EVIDENCE-REFS"),
        (_graph({"condition_id": "c", "status": "triggered", "required_controls": ["deny"], "evidence_refs": ["same", "same"]}),
         "RPE-M3-RISK-CONDITION-INVALID-EVIDENCE-REFS"),
        (_graph({"condition_id": "c", "status": ["triggered"], "required_controls": ["deny"]}),
         "RPE-M3-RISK-CONDITION-INVALID-STATUS"),
    )
    for invalid_graph, expected_reason in invalid_graphs:
        invalid_risk = evaluate_risk_conditions(invalid_graph)
        assert invalid_risk["graph_status"] == "invalid", invalid_risk
        assert expected_reason in invalid_risk["reason_codes"], invalid_risk
        blocked = evaluate_transition(allowed_evaluation, risk_result=invalid_risk)
        assert blocked["control_action"] == "hold", blocked
        assert_bounded(blocked)

    # A well-formed relation must still retain its evidence and block no
    # otherwise valid evaluation when all its conditions are clear.
    valid_related = evaluate_risk_conditions(_graph(
        {"condition_id": "source", "status": "clear", "required_controls": [],
         "evidence_refs": ["source-readback"]},
        {"condition_id": "dependent", "status": "clear", "required_controls": [],
         "depends_on": ["source"], "evidence_refs": ["dependent-readback"]},
    ))
    assert valid_related["graph_status"] == "clear", valid_related
    assert valid_related["conditions"][1]["depends_on"] == ["source"], valid_related
    assert evaluate_transition(allowed_evaluation, risk_result=valid_related)["control_action"] == "allow"

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

    # An explicit M2 Human Gate may not be laundered into a handoff to an
    # AI agent, verifier, queue or sandbox through caller-supplied routing.
    for forbidden_kind in ("agent", "verifier", "queue", "sandbox", "stop"):
        forbidden_route = {"kind": forbidden_kind, "target_id": "alternate-destination"}
        blocked_human_gate = evaluate_transition(
            human_gate_without_missing, requested_route=forbidden_route
        )
        assert blocked_human_gate["control_action"] == "hold", blocked_human_gate
        assert "RPE-M3-HUMAN-GATE-INVALID-ROUTE-KIND" in blocked_human_gate["reason_codes"], blocked_human_gate
        assert blocked_human_gate["route_target"] is None, blocked_human_gate
        assert_bounded(blocked_human_gate)

    # Human/institution is necessary for such a handoff but does NOT
    # authenticate the destination or grant any approval.
    institutional = evaluate_transition(
        human_gate_without_missing,
        requested_route={"kind": "institution", "target_id": "review-office"},
    )
    assert institutional["control_action"] == "handoff", institutional
    assert institutional["route_target"]["kind"] == "institution", institutional
    assert_bounded(institutional)

    # The Thin adapter must retain the Human Gate boundary as well.
    misrouted_thin = evaluate_gateway_request(
        {"contract_version": "0.1.0-exp", "governed_evaluation": missing_evidence_input,
         "requested_route": {"kind": "agent", "target_id": "unauthorized-agent"}},
        today=date(2026, 9, 1),
    )
    assert misrouted_thin["evaluation_result"]["decision"] == "human_gate", misrouted_thin
    assert misrouted_thin["transition_result"]["control_action"] == "hold", misrouted_thin
    assert "RPE-M3-HUMAN-GATE-INVALID-ROUTE-KIND" in misrouted_thin["transition_result"]["reason_codes"], misrouted_thin
    assert_gateway_bounded(misrouted_thin)

    denied = evaluate_transition({"decision": "deny", "reason_codes": ["RPE-M3-DEMO-DENY"]}, risk_result=clear_risk)
    assert denied["control_action"] == "deny", denied
    assert denied["route_target"] is None, denied
    assert_bounded(denied)

    # Upstream M2 deny stays deny even when a later caller supplies malformed
    # M3 route/constraint data. Retain diagnostic codes without downgrading.
    for options, expected_reason in (
        ({"requested_route": {"kind": ["agent"]}}, "RPE-M3-ROUTE-UNSUPPORTED-KIND"),
        ({"requested_route": {"kind": "agent", "dispatch_now": True}}, "RPE-M3-ROUTE-UNKNOWN-FIELD"),
        ({"constraints": ["no_delegation", None]}, "RPE-M3-CONSTRAINTS-INVALID"),
    ):
        denied_with_invalid_options = evaluate_transition(
            {"decision": "deny", "reason_codes": ["RPE-M3-DEMO-DENY"]}, **options
        )
        assert denied_with_invalid_options["control_action"] == "deny", denied_with_invalid_options
        assert "RPE-M3-DEMO-DENY" in denied_with_invalid_options["reason_codes"], denied_with_invalid_options
        assert expected_reason in denied_with_invalid_options["reason_codes"], denied_with_invalid_options
        assert denied_with_invalid_options["route_target"] is None, denied_with_invalid_options
        assert_bounded(denied_with_invalid_options)

    invalid_route = evaluate_transition(
        allowed_evaluation,
        requested_route={"kind": "unbounded_magic_router", "target_id": "x"},
    )
    assert invalid_route["control_action"] == "hold", invalid_route
    assert "RPE-M3-ROUTE-UNSUPPORTED-KIND" in invalid_route["reason_codes"], invalid_route
    assert_bounded(invalid_route)

    # Route and constraints are decision-bearing inputs. Unsupported shape
    # cannot be silently ignored by a direct Python caller or a Thin adapter.
    for malformed_route, expected_reason in (
        ({"kind": ["agent"]}, "RPE-M3-ROUTE-UNSUPPORTED-KIND"),
        ({"kind": "agent", "execution_authority": True}, "RPE-M3-ROUTE-UNKNOWN-FIELD"),
    ):
        direct = evaluate_transition(allowed_evaluation, requested_route=malformed_route)
        assert direct["control_action"] == "hold", direct
        assert expected_reason in direct["reason_codes"], direct
        assert direct["route_target"] is None, direct
        assert_bounded(direct)
        through_gateway = evaluate_gateway_request(
            {"contract_version": "0.1.0-exp", "governed_evaluation": base,
             "requested_route": malformed_route},
            today=date(2026, 9, 1),
        )
        assert through_gateway["transition_result"]["control_action"] == "hold", through_gateway
        assert expected_reason in through_gateway["transition_result"]["reason_codes"], through_gateway
        assert_gateway_bounded(through_gateway)

    for invalid_constraints in ("no_delegation", [None], [42], ["max_targets=1", ""], {"stop": True}):
        direct = evaluate_transition(allowed_evaluation, constraints=invalid_constraints)
        assert direct["control_action"] == "hold", direct
        assert "RPE-M3-CONSTRAINTS-INVALID" in direct["reason_codes"], direct
        assert_bounded(direct)
        through_gateway = evaluate_gateway_request(
            {"contract_version": "0.1.0-exp", "governed_evaluation": base,
             "constraints": invalid_constraints},
            today=date(2026, 9, 1),
        )
        assert through_gateway["transition_result"]["control_action"] == "hold", through_gateway
        assert "RPE-M3-CONSTRAINTS-INVALID" in through_gateway["transition_result"]["reason_codes"], through_gateway
        assert_gateway_bounded(through_gateway)

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
