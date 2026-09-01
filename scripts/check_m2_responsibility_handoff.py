#!/usr/bin/env python3
"""Deterministic checks for M2 evaluation-to-runtime responsibility handoff."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from rpe_kernel import evaluate_governed_action

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


def assert_handoff(result: dict) -> None:
    assert result["contract_version"] == "1.1.0", result
    handoff = result["responsibility_handoff"]
    assert handoff["authority_effect"] == "none", handoff
    assert handoff["decision_scope"] == "evaluation_only", handoff
    assert handoff["evaluation_decision"] == result["decision"], handoff
    assert handoff["evaluation_reason_codes"] == result["reason_codes"], handoff

    obligations = handoff["downstream_obligations"]
    assert obligations == {
        "dispatch_authority_required": True,
        "effect_verification_required_for_effect_claim": True,
        "receipt_sufficient_for_effect_claim": False,
        "reauthorization_required_for": ["retry", "repair", "resume"],
        "authority_owner": "downstream_runtime_or_institution",
        "residual_owner_role": obligations["residual_owner_role"],
    }, obligations
    assert obligations["residual_owner_role"], obligations

    assert not (FORBIDDEN_OPERATIONAL_KEYS & set(handoff)), handoff
    assert not (FORBIDDEN_OPERATIONAL_KEYS & set(result)), result


def main() -> int:
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))

    allowed = evaluate_governed_action(base, today=date(2026, 9, 1))
    assert allowed["decision"] == "allow", allowed
    assert allowed["responsibility_handoff"]["selected_pack_refs"][0]["pack_id"] == "demo-pack", allowed
    assert allowed["responsibility_handoff"]["evaluation_evidence_scope"] == {
        "available": ["approval-record"],
        "missing": [],
    }, allowed
    assert allowed["responsibility_handoff"]["downstream_obligations"]["residual_owner_role"] == "downstream_execution_owner", allowed
    assert_handoff(allowed)

    blocked = copy.deepcopy(base)
    blocked["request"]["context"]["human_approval_present"] = False
    blocked["request"]["evidence_scope"] = {"available": [], "missing": ["approval-record"]}
    held = evaluate_governed_action(blocked, today=date(2026, 9, 1))
    assert held["decision"] == "human_gate", held
    assert held["responsibility_handoff"]["human_return"]["role"] == "demo-owner", held
    assert held["responsibility_handoff"]["downstream_obligations"]["residual_owner_role"] == "demo-owner", held
    assert held["responsibility_handoff"]["evaluation_evidence_scope"]["missing"] == ["approval-record"], held
    assert_handoff(held)

    incompatible = copy.deepcopy(base)
    incompatible["contract_version"] = "2.0.0"
    stopped = evaluate_governed_action(incompatible, today=date(2026, 9, 1))
    assert stopped["decision"] == "human_gate", stopped
    assert stopped["stage"] == "compatibility", stopped
    assert stopped["responsibility_handoff"]["downstream_obligations"]["residual_owner_role"] == "contract_compatibility_owner", stopped
    assert_handoff(stopped)

    print("M2 responsibility handoff checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
