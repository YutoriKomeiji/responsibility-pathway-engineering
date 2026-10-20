#!/usr/bin/env python3
"""Deterministic checks for experimental M3 Human Return readiness."""

from __future__ import annotations

from rpe_kernel.human_return import (
    evaluate_human_return_readiness,
    human_return_result_to_risk_condition,
)
from rpe_kernel.risk_conditions import evaluate_risk_conditions


def main() -> int:
    ready = evaluate_human_return_readiness(
        {
            "return_id": "review-1",
            "owner_role": "review_owner",
            "authority_reference": "authority-record-1",
            "capability_status": "available",
            "response_window_status": "available",
            "next_decision_scope": "approve_or_deny_current_request",
            "evidence_scope": {
                "available": ["request", "evaluation", "approval-context"],
                "missing": [],
            },
        }
    )
    assert ready["readiness"] == "ready_for_review", ready
    assert ready["authority_validity_claim"] is False, ready
    assert ready["capability_validity_claim"] is False, ready
    assert ready["evidence_truth_claim"] is False, ready
    assert ready["authority_effect"] == "none", ready
    assert ready["human_decision_effect"] == "none", ready

    missing_authority = evaluate_human_return_readiness(
        {
            "return_id": "review-2",
            "owner_role": "review_owner",
            "authority_reference": None,
            "capability_status": "available",
            "response_window_status": "available",
            "next_decision_scope": "approve_or_deny_current_request",
            "evidence_scope": {"available": ["request"], "missing": []},
        }
    )
    assert missing_authority["readiness"] == "unresolved", missing_authority
    assert "RPE-M3-HUMAN-RETURN-AUTHORITY-REFERENCE-UNKNOWN" in missing_authority["reason_codes"], missing_authority

    incomplete = evaluate_human_return_readiness(
        {
            "return_id": "review-3",
            "owner_role": "review_owner",
            "authority_reference": "authority-record-3",
            "capability_status": "limited",
            "response_window_status": "limited",
            "next_decision_scope": "bounded_exception_review",
            "evidence_scope": {"available": ["request"], "missing": ["readback"]},
        }
    )
    assert incomplete["readiness"] == "unresolved", incomplete
    assert "RPE-M3-HUMAN-RETURN-EVIDENCE-INCOMPLETE" in incomplete["reason_codes"], incomplete
    assert "RPE-M3-HUMAN-RETURN-CAPABILITY-LIMITED" in incomplete["reason_codes"], incomplete
    assert "RPE-M3-HUMAN-RETURN-WINDOW-LIMITED" in incomplete["reason_codes"], incomplete

    conditional = evaluate_human_return_readiness(
        {
            "return_id": "review-4",
            "owner_role": "review_owner",
            "authority_reference": "authority-record-4",
            "capability_status": "limited",
            "response_window_status": "available",
            "next_decision_scope": "bounded_exception_review",
            "evidence_scope": {"available": ["request", "readback"], "missing": []},
        }
    )
    assert conditional["readiness"] == "conditional", conditional

    expired = evaluate_human_return_readiness(
        {
            "return_id": "review-5",
            "owner_role": "review_owner",
            "authority_reference": "authority-record-5",
            "capability_status": "available",
            "response_window_status": "expired",
            "next_decision_scope": "approve_or_deny_current_request",
            "evidence_scope": {"available": ["request"], "missing": []},
        }
    )
    assert expired["readiness"] == "unresolved", expired
    assert "RPE-M3-HUMAN-RETURN-WINDOW-EXPIRED" in expired["reason_codes"], expired

    risk_node = human_return_result_to_risk_condition(
        conditional,
        required_controls=["downgrade_autonomy"],
    )
    risk = evaluate_risk_conditions({"conditions": [risk_node]})
    assert risk["graph_status"] == "triggered", risk
    assert risk["required_controls"] == ["downgrade_autonomy"], risk

    unresolved_node = human_return_result_to_risk_condition(
        missing_authority,
        required_controls=["hold"],
    )
    unresolved_risk = evaluate_risk_conditions({"conditions": [unresolved_node]})
    assert unresolved_risk["graph_status"] == "unresolved", unresolved_risk

    invalid = evaluate_human_return_readiness(
        {
            "return_id": "review-6",
            "owner_role": "review_owner",
            "authority_reference": "authority-record-6",
            "capability_status": "magical",
            "response_window_status": "available",
            "next_decision_scope": "review",
            "evidence_scope": {"available": [], "missing": []},
        }
    )
    assert invalid["readiness"] == "invalid", invalid
    assert "RPE-M3-HUMAN-RETURN-INVALID-CAPABILITY-STATUS" in invalid["reason_codes"], invalid

    print("M3 Human Return readiness checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
