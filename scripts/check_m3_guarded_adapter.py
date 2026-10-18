#!/usr/bin/env python3
"""Deterministic checks for the M3 0.2.0-exp guarded adapter core."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from rpe_kernel.guarded_adapter import evaluate_guarded_adapter_request

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"
REQUEST_SCHEMA = ROOT / "schemas/m3/guarded-adapter-request.schema.json"
RESPONSE_SCHEMA = ROOT / "schemas/m3/guarded-adapter-response.schema.json"


def main() -> int:
    governed = json.loads(FIXTURE.read_text(encoding="utf-8"))
    request_schema = json.loads(REQUEST_SCHEMA.read_text(encoding="utf-8"))
    response_schema = json.loads(RESPONSE_SCHEMA.read_text(encoding="utf-8"))
    request_validator = Draft202012Validator(request_schema)
    response_validator = Draft202012Validator(response_schema)

    payload = {
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed,
        "integrity_checks": [
            {
                "check": {
                    "check_id": "configuration-binding",
                    "kind": "configuration",
                    "expected": {"configuration_id": "cfg-a"},
                    "observed": {"configuration_id": "cfg-b"},
                    "evidence_refs": ["configuration-readback"],
                },
                "required_controls": ["require_authority"],
            }
        ],
        "human_return_checks": [
            {
                "check": {
                    "return_id": "review-route",
                    "owner_role": "review_owner",
                    "authority_reference": "authority-record",
                    "capability_status": "available",
                    "response_window_status": "available",
                    "next_decision_scope": "bounded_review",
                    "evidence_scope": {"available": ["decision-record"], "missing": []},
                },
                "required_controls": ["require_authority"],
            }
        ],
    }
    request_validator.validate(payload)
    result = evaluate_guarded_adapter_request(payload, today=date(2026, 9, 1))
    response_validator.validate(result)
    assert result["contract_version"] == "0.2.0-exp", result
    assert result["guard_observations"]["integrity_results"][0]["status"] == "triggered", result
    assert result["guard_observations"]["integrity_results"][0]["independent_authentication_claim"] is False, result
    assert result["guard_observations"]["human_return_results"][0]["readiness"] == "ready_for_review", result
    assert result["guard_observations"]["human_return_results"][0]["authority_validity_claim"] is False, result
    assert result["transition_result"]["control_action"] == "require_authority", result
    assert result["authority_effect"] == "none", result
    assert result["execution_effect"] == "none", result

    unresolved = dict(payload)
    unresolved["integrity_checks"] = []
    unresolved["human_return_checks"] = [
        {
            "check": {
                "return_id": "review-route-2",
                "owner_role": "review_owner",
                "authority_reference": None,
                "capability_status": "unknown",
                "response_window_status": "unknown",
                "next_decision_scope": "bounded_review",
                "evidence_scope": {"available": [], "missing": ["decision-record"]},
            },
            "required_controls": ["hold"],
        }
    ]
    request_validator.validate(unresolved)
    unresolved_result = evaluate_guarded_adapter_request(unresolved, today=date(2026, 9, 1))
    response_validator.validate(unresolved_result)
    assert unresolved_result["guard_observations"]["human_return_results"][0]["readiness"] == "unresolved", unresolved_result
    assert unresolved_result["transition_result"]["control_action"] == "hold", unresolved_result

    invalid = evaluate_guarded_adapter_request(
        {"contract_version": "0.2.0-exp", "governed_evaluation": governed, "dispatch_now": True},
        today=date(2026, 9, 1),
    )
    response_validator.validate(invalid)
    assert invalid["evaluation_result"] is None, invalid
    assert invalid["transition_result"]["control_action"] == "hold", invalid
    assert "RPE-M3-GUARDED-ADAPTER-REQUEST-UNKNOWN-FIELD" in invalid["transition_result"]["reason_codes"], invalid

    no_policy = evaluate_guarded_adapter_request(
        {
            "contract_version": "0.2.0-exp",
            "governed_evaluation": governed,
            "integrity_checks": [
                {
                    "check": {
                        "check_id": "configuration-binding",
                        "kind": "configuration",
                        "expected": {"configuration_id": "cfg-a"},
                        "observed": {"configuration_id": "cfg-b"},
                    },
                    "required_controls": [],
                }
            ],
        },
        today=date(2026, 9, 1),
    )
    response_validator.validate(no_policy)
    assert no_policy["transition_result"]["control_action"] == "hold", no_policy
    assert "RPE-M3-INTEGRITY-CHECK-CONTROL-REQUIRED" in no_policy["transition_result"]["reason_codes"], no_policy

    # Guarded 0.2.0-exp uses the same M3 transition evaluator. Invalid
    # restrictions must not disappear at this adapter boundary.
    for field, invalid_value, reason in (
        ("constraints", ["no_delegation", None], "RPE-M3-CONSTRAINTS-INVALID"),
        ("requested_route", {"kind": ["agent"]}, "RPE-M3-ROUTE-UNSUPPORTED-KIND"),
        ("requested_route", {"kind": "agent", "dispatch_now": True}, "RPE-M3-ROUTE-UNKNOWN-FIELD"),
    ):
        malformed = {"contract_version": "0.2.0-exp", "governed_evaluation": governed, field: invalid_value}
        assert not request_validator.is_valid(malformed), malformed
        result = evaluate_guarded_adapter_request(malformed, today=date(2026, 9, 1))
        response_validator.validate(result)
        assert result["transition_result"]["control_action"] == "hold", result
        assert reason in result["transition_result"]["reason_codes"], result
        assert result["authority_effect"] == "none", result
        assert result["execution_effect"] == "none", result

    # An M2 decision requiring a human cannot be redirected to a machine
    # by the guarded adapter's caller-supplied route target.
    missing_approval = copy.deepcopy(governed)
    missing_approval["request"]["context"]["human_approval_present"] = False
    missing_approval["request"]["evidence_scope"] = {
        "available": [], "missing": ["approval-record"],
    }
    misrouted_human_gate = {
        "contract_version": "0.2.0-exp",
        "governed_evaluation": missing_approval,
        "requested_route": {"kind": "agent", "target_id": "unapproved-agent"},
    }
    request_validator.validate(misrouted_human_gate)
    blocked_human_gate = evaluate_guarded_adapter_request(
        misrouted_human_gate, today=date(2026, 9, 1),
    )
    response_validator.validate(blocked_human_gate)
    assert blocked_human_gate["evaluation_result"]["decision"] == "human_gate", blocked_human_gate
    assert blocked_human_gate["transition_result"]["control_action"] == "hold", blocked_human_gate
    assert "RPE-M3-HUMAN-GATE-INVALID-ROUTE-KIND" in blocked_human_gate["transition_result"]["reason_codes"], blocked_human_gate
    assert blocked_human_gate["authority_effect"] == "none", blocked_human_gate
    assert blocked_human_gate["execution_effect"] == "none", blocked_human_gate

    print("M3 guarded adapter 0.2.0-exp core/schema checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
