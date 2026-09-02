#!/usr/bin/env python3
"""Deterministic checks for the experimental M3 responsibility gateway."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from rpe_kernel import evaluate_governed_action
from rpe_kernel.gateway import evaluate_transition

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

    transition = result["responsibility_transition"]
    assert transition["authority"] == {
        "effect": "none",
        "downstream_authority_required": True,
    }, transition
    assert transition["dispatch_effect"] == "none", transition
    assert transition["residual_owner_role"], transition

    route = result.get("route_target")
    if route is not None:
        assert route["authority_effect"] == "none", route
        assert route["dispatch_effect"] == "none", route
        assert transition["destination"] == route, transition


def main() -> int:
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))

    allowed_evaluation = evaluate_governed_action(base, today=date(2026, 9, 1))
    allowed = evaluate_transition(allowed_evaluation)
    assert allowed["control_action"] == "allow", allowed
    assert allowed["route_target"] is None, allowed
    assert allowed["responsibility_transition"]["evidence"] == {
        "available": ["approval-record"],
        "missing": [],
    }, allowed
    assert allowed["responsibility_transition"]["residual_owner_role"] == "downstream_execution_owner", allowed
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
    assert routed["responsibility_transition"]["purpose"] == "second_check", routed
    assert_bounded(routed)

    missing_evidence_input = copy.deepcopy(base)
    missing_evidence_input["request"]["context"]["human_approval_present"] = False
    missing_evidence_input["request"]["evidence_scope"] = {
        "available": [],
        "missing": ["approval-record"],
    }
    missing_evaluation = evaluate_governed_action(missing_evidence_input, today=date(2026, 9, 1))
    need_evidence = evaluate_transition(missing_evaluation)
    assert need_evidence["control_action"] == "require_evidence", need_evidence
    assert need_evidence["unmet_conditions"] == ["approval-record"], need_evidence
    assert need_evidence["responsibility_transition"]["evidence"]["missing"] == ["approval-record"], need_evidence
    assert_bounded(need_evidence)

    human_gate_without_missing = {
        "request_id": "review-request",
        "decision": "human_gate",
        "reason_codes": ["RPE-M3-DEMO-HUMAN-REVIEW"],
        "human_return": {"role": "review_owner"},
        "responsibility_handoff": {
            "evaluation_evidence_scope": {"available": [], "missing": []},
            "human_return": {"role": "review_owner"},
            "downstream_obligations": {"residual_owner_role": "review_owner"},
        },
    }
    handoff = evaluate_transition(human_gate_without_missing)
    assert handoff["control_action"] == "handoff", handoff
    assert handoff["route_target"]["kind"] == "human", handoff
    assert handoff["route_target"]["target_id"] == "review_owner", handoff
    assert handoff["responsibility_transition"]["source"]["request_id"] == "review-request", handoff
    assert handoff["responsibility_transition"]["residual_owner_role"] == "review_owner", handoff
    assert_bounded(handoff)

    denied = evaluate_transition({"decision": "deny", "reason_codes": ["RPE-M3-DEMO-DENY"]})
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

    constrained = evaluate_transition(
        allowed_evaluation,
        constraints=["max_targets=1", "no_delegation"],
    )
    assert constrained["control_action"] == "allow_with_constraints", constrained
    assert constrained["constraints"] == ["max_targets=1", "no_delegation"], constrained
    assert_bounded(constrained)

    print("M3 experimental responsibility gateway checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
