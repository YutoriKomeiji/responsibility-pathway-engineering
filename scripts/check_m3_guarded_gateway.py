#!/usr/bin/env python3
"""Deterministic checks for combined M3 responsibility guards."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from rpe_kernel import evaluate_responsibility_guarded_gateway_request

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def main() -> int:
    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))
    base = {"contract_version": "0.1.0-exp", "governed_evaluation": governed}

    clear = evaluate_responsibility_guarded_gateway_request(
        base,
        integrity_checks=[
            {
                "check": {
                    "check_id": "config",
                    "kind": "configuration",
                    "expected": {"configuration_id": "cfg-1"},
                    "observed": {"configuration_id": "cfg-1"},
                },
                "required_controls": ["require_authority"],
            }
        ],
        human_return_checks=[
            {
                "return": {
                    "return_id": "review-1",
                    "owner_role": "review_owner",
                    "authority_reference": "auth-1",
                    "capability_status": "available",
                    "response_window_status": "available",
                    "next_decision_scope": "approve_or_deny_current_request",
                    "evidence_scope": {"available": ["request"], "missing": []},
                },
                "required_controls": ["downgrade_autonomy"],
            }
        ],
        today=date(2026, 9, 1),
    )
    assert clear["evaluation_result"]["decision"] == "allow", clear
    assert clear["risk_condition_result"]["graph_status"] == "clear", clear
    assert clear["transition_result"]["control_action"] == "allow", clear
    assert clear["authority_effect"] == "none", clear
    assert clear["execution_effect"] == "none", clear

    return_unresolved = evaluate_responsibility_guarded_gateway_request(
        base,
        human_return_checks=[
            {
                "return": {
                    "return_id": "review-2",
                    "owner_role": "review_owner",
                    "authority_reference": None,
                    "capability_status": "available",
                    "response_window_status": "available",
                    "next_decision_scope": "approve_or_deny_current_request",
                    "evidence_scope": {"available": ["request"], "missing": []},
                },
                "required_controls": ["hold"],
            }
        ],
        today=date(2026, 9, 1),
    )
    assert return_unresolved["risk_condition_result"]["graph_status"] == "unresolved", return_unresolved
    assert return_unresolved["transition_result"]["control_action"] == "hold", return_unresolved

    competing = evaluate_responsibility_guarded_gateway_request(
        base,
        integrity_checks=[
            {
                "check": {
                    "check_id": "config",
                    "kind": "configuration",
                    "expected": {"configuration_id": "cfg-1"},
                    "observed": {"configuration_id": "cfg-2"},
                },
                "required_controls": ["require_authority"],
            }
        ],
        human_return_checks=[
            {
                "return": {
                    "return_id": "review-3",
                    "owner_role": "review_owner",
                    "authority_reference": "auth-3",
                    "capability_status": "limited",
                    "response_window_status": "available",
                    "next_decision_scope": "bounded_review",
                    "evidence_scope": {"available": ["request"], "missing": []},
                },
                "required_controls": ["downgrade_autonomy"],
            }
        ],
        today=date(2026, 9, 1),
    )
    assert competing["risk_condition_result"]["required_controls"] == ["downgrade_autonomy", "require_authority"], competing
    assert "RPE-M3-CONTROL-SELECTION-REQUIRED" in competing["risk_condition_result"]["reason_codes"], competing
    assert competing["transition_result"]["control_action"] == "hold", competing

    missing_policy = evaluate_responsibility_guarded_gateway_request(
        base,
        human_return_checks=[
            {
                "return": {
                    "return_id": "review-4",
                    "owner_role": "review_owner",
                    "authority_reference": None,
                    "capability_status": "unknown",
                    "response_window_status": "unknown",
                    "next_decision_scope": "review",
                    "evidence_scope": {"available": [], "missing": ["request"]},
                },
                "required_controls": [],
            }
        ],
        today=date(2026, 9, 1),
    )
    assert missing_policy["transition_result"]["control_action"] == "hold", missing_policy
    assert "RPE-M3-HUMAN-RETURN-CHECK-CONTROL-REQUIRED" in missing_policy["transition_result"]["reason_codes"], missing_policy

    assert set(clear) == {
        "contract_version",
        "evaluation_result",
        "risk_condition_result",
        "transition_result",
        "authority_effect",
        "execution_effect",
    }, clear


    # Composing a guard must not erase invalid fields from the caller's graph:
    # doing so could turn an invalid request into a clear/allowed transition.
    clear_integrity_check = {
        "check": {
            "check_id": "graph-preservation",
            "kind": "configuration",
            "expected": {"configuration_id": "same"},
            "observed": {"configuration_id": "same"},
        },
        "required_controls": ["require_authority"],
    }
    clear_return_check = {
        "return": {
            "return_id": "graph-preservation-review",
            "owner_role": "review_owner",
            "authority_reference": "auth-1",
            "capability_status": "available",
            "response_window_status": "available",
            "next_decision_scope": "review",
            "evidence_scope": {"available": ["request"], "missing": []},
        },
        "required_controls": ["require_authority"],
    }
    for guards in (
        {"integrity_checks": [clear_integrity_check]},
        {"human_return_checks": [clear_return_check]},
    ):
        malformed_envelope = evaluate_responsibility_guarded_gateway_request(
            {**base, "risk_graph": {"conditions": [], "dispatch_now": True}},
            today=date(2026, 9, 1),
            **guards,
        )
        assert malformed_envelope["risk_condition_result"]["graph_status"] == "invalid", malformed_envelope
        assert "RPE-M3-RISK-GRAPH-UNKNOWN-FIELD" in malformed_envelope["risk_condition_result"]["reason_codes"], malformed_envelope
        assert malformed_envelope["transition_result"]["control_action"] == "hold", malformed_envelope

    malformed_list = evaluate_responsibility_guarded_gateway_request(
        {**base, "risk_graph": {"conditions": ()}},
        integrity_checks=[clear_integrity_check],
        today=date(2026, 9, 1),
    )
    assert malformed_list["risk_condition_result"]["graph_status"] == "invalid", malformed_list
    assert malformed_list["transition_result"]["control_action"] == "hold", malformed_list


    # Direct Python guard paths must reject mixed-type, non-array, or
    # duplicate policy controls instead of silently filtering values.
    for field, valid_guard, reason in (
        ("integrity_checks", clear_integrity_check, "RPE-M3-INTEGRITY-CHECK-INVALID-CONTROLS"),
        ("human_return_checks", clear_return_check, "RPE-M3-HUMAN-RETURN-CHECK-INVALID-CONTROLS"),
    ):
        for bad_controls in (["require_authority", None], ["require_authority", "require_authority"], "require_authority"):
            invalid_entry = {**valid_guard, "required_controls": bad_controls}
            rejected = evaluate_responsibility_guarded_gateway_request(
                base, today=date(2026, 9, 1), **{field: [invalid_entry]}
            )
            assert rejected["transition_result"]["control_action"] == "hold", rejected
            assert reason in rejected["transition_result"]["reason_codes"], rejected

    print("M3 combined responsibility guard checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
