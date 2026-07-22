#!/usr/bin/env python3
"""Deterministic checks for the M2 runtime compatibility and governance gates."""

from __future__ import annotations

from datetime import date

from rpe_kernel import evaluate_action

REQUEST = {
    "contract_version": "1.0.0",
    "request_id": "m2-entry-check",
    "actor": {"type": "ai_agent", "id": "demo-agent"},
    "action": "external_send",
    "target": "synthetic-target",
    "applicability_context": {"organization": "demo"},
    "context": {"human_approval_present": True},
    "evidence_scope": {"available": ["approval-record"], "missing": []},
}

PACK = {
    "contract_version": "1.0.0",
    "pack_id": "demo-pack",
    "title": "Synthetic M2 Entry Pack",
    "version": "1.0.0",
    "source_type": "synthetic_demo",
    "source_metadata": {
        "authority_name": "Synthetic",
        "source_url": None,
        "jurisdiction": "synthetic",
        "source_version": "1",
        "effective_date": None,
        "review_owner": "demo-owner",
        "review_status": "synthetic",
        "interpretation_status": "not_applicable",
    },
    "applies_when": {"action": "external_send", "organization": "demo"},
    "requirements": ["human_approval_present"],
    "decision_on_missing_requirement": "human_gate",
    "human_return": {"role": "demo-owner"},
    "reason_code_prefix": "RPE-DEMO",
}

ACTIVE_GOVERNANCE = {
    "pack_id": "demo-pack",
    "pack_version": "1.0.0",
    "lifecycle_state": "active",
    "maintenance_owner": "demo-owner",
    "reviewer": "demo-reviewer",
    "approver": "demo-approver",
    "source_authority": "Synthetic",
    "source_version": "1",
    "jurisdiction": "synthetic",
    "effective_scope": "demo only",
    "interpretation_status": "reviewed",
    "unresolved_ambiguity": [],
    "last_reviewed": "2026-07-01",
    "next_review_due": "2026-12-31",
    "human_return": {"role": "demo-owner"},
}


def main() -> int:
    today = date(2026, 7, 23)

    allowed = evaluate_action(
        REQUEST,
        [PACK],
        governance_records={"demo-pack": ACTIVE_GOVERNANCE},
        today=today,
        enforce_contract_versions=True,
    )
    assert allowed["decision"] == "allow", allowed
    assert allowed["stage"] == "evaluation", allowed

    expired = dict(ACTIVE_GOVERNANCE, next_review_due="2026-07-01")
    held = evaluate_action(
        REQUEST,
        [PACK],
        governance_records={"demo-pack": expired},
        today=today,
        enforce_contract_versions=True,
    )
    assert held["decision"] == "human_gate", held
    assert "RPE-PACK-GOV-REVIEW-EXPIRED" in held["reason_codes"], held

    incompatible = evaluate_action(
        dict(REQUEST, contract_version="2.0.0"),
        [PACK],
        governance_records={"demo-pack": ACTIVE_GOVERNANCE},
        today=today,
        enforce_contract_versions=True,
    )
    assert incompatible["decision"] == "human_gate", incompatible
    assert incompatible["stage"] == "compatibility", incompatible

    missing_governance = evaluate_action(
        REQUEST,
        [PACK],
        governance_records={},
        today=today,
        enforce_contract_versions=True,
    )
    assert missing_governance["decision"] == "human_gate", missing_governance
    assert "RPE-PACK-GOV-MISSING-RECORD" in missing_governance["reason_codes"], missing_governance

    print("M2 entry pipeline checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
