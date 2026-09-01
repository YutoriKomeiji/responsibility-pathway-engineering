#!/usr/bin/env python3
"""Deterministic regression matrix for the explicit M2 governed Python entry."""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from rpe_kernel import evaluate_governed_action

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def main() -> int:
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))
    today = date(2026, 9, 1)

    allowed = evaluate_governed_action(base, today=today)
    assert allowed["decision"] == "allow", allowed
    assert allowed["stage"] == "evaluation", allowed
    assert allowed["responsibility_handoff"]["authority_effect"] == "none", allowed
    assert allowed["responsibility_handoff"]["decision_scope"] == "evaluation_only", allowed
    assert allowed["responsibility_handoff"]["selected_pack_refs"][0]["pack_id"] == "demo-pack", allowed

    wrong_pack_version = copy.deepcopy(base)
    wrong_pack_version["governed_packs"][0]["governance"]["pack_version"] = "9.9.9"
    held = evaluate_governed_action(wrong_pack_version, today=today)
    assert held["stage"] == "admission", held
    assert "RPE-GOVERNED-BINDING-PACK-VERSION-MISMATCH" in held["reason_codes"], held

    ambiguity = copy.deepcopy(base)
    ambiguity["governed_packs"][0]["governance"]["unresolved_ambiguity"] = ["scope conflict"]
    held = evaluate_governed_action(ambiguity, today=today)
    assert held["stage"] == "governance", held
    assert "RPE-PACK-GOV-UNRESOLVED-AMBIGUITY" in held["reason_codes"], held

    future_effective = copy.deepcopy(base)
    future_effective["governed_packs"][0]["governance"]["effective_date"] = "2026-10-01"
    held = evaluate_governed_action(future_effective, today=today)
    assert held["stage"] == "governance", held
    assert "RPE-PACK-GOV-NOT-YET-EFFECTIVE" in held["reason_codes"], held

    future_review = copy.deepcopy(base)
    future_review["governed_packs"][0]["governance"]["last_reviewed"] = "2026-10-01"
    held = evaluate_governed_action(future_review, today=today)
    assert held["stage"] == "governance", held
    assert "RPE-PACK-GOV-REVIEW-DATE-IN-FUTURE" in held["reason_codes"], held

    newer_minor = copy.deepcopy(base)
    newer_minor["contract_version"] = "1.1.0"
    held = evaluate_governed_action(newer_minor, today=today)
    assert held["stage"] == "compatibility", held
    assert "RPE-CONTRACT-UNSUPPORTED-GOVERNED-EVALUATION-REQUEST-MINOR" in held["reason_codes"], held

    missing_governance_version = copy.deepcopy(base)
    del missing_governance_version["governed_packs"][0]["governance"]["contract_version"]
    held = evaluate_governed_action(missing_governance_version, today=today)
    assert held["stage"] == "compatibility", held
    assert "RPE-CONTRACT-MISSING-REQUIREMENT-PACK-GOVERNANCE-VERSION" in held["reason_codes"], held

    duplicate = copy.deepcopy(base)
    duplicate["governed_packs"].append(copy.deepcopy(duplicate["governed_packs"][0]))
    duplicate["governed_packs"][1]["binding_id"] = "demo-pack@1.0.0-copy"
    held = evaluate_governed_action(duplicate, today=today)
    assert held["stage"] == "admission", held
    assert "RPE-GOVERNED-ADMISSION-DUPLICATE-PACK" in held["reason_codes"], held

    print("M2 governed admission checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
