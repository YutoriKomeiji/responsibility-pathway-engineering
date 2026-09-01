#!/usr/bin/env python3
"""Cross-cutting adversarial closure checks for the bounded RPE M2 surface.

This checker intentionally targets gaps between the existing focused regression
scripts. It does not establish production, legal, compliance, deployment,
external-effect, or implementation-wide formal guarantees.
"""

from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from rpe_kernel import evaluate_governed_action

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "external-kernel"
FIXTURE = ROOT / "examples" / "external-kernel" / "minimal-governed-evaluation-request.json"
TODAY = date(2026, 9, 1)

SCHEMAS = [
    "action-request.schema.json",
    "requirement-pack.schema.json",
    "requirement-pack-governance.schema.json",
    "governed-pack-binding.schema.json",
    "governed-evaluation-request.schema.json",
    "governed-evaluation-result.schema.json",
]


def _base() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _result_validator() -> Draft202012Validator:
    registry = Registry()
    loaded: dict[str, dict] = {}
    for name in SCHEMAS:
        schema = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
        loaded[name] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    return Draft202012Validator(
        loaded["governed-evaluation-result.schema.json"],
        registry=registry,
        format_checker=FormatChecker(),
    )


def _assert_bounded_handoff(result: dict) -> None:
    handoff = result["responsibility_handoff"]
    obligations = handoff["downstream_obligations"]
    assert handoff["authority_effect"] == "none", result
    assert handoff["decision_scope"] == "evaluation_only", result
    assert obligations["dispatch_authority_required"] is True, result
    assert obligations["effect_verification_required_for_effect_claim"] is True, result
    assert obligations["receipt_sufficient_for_effect_claim"] is False, result
    assert obligations["reauthorization_required_for"] == ["retry", "repair", "resume"], result
    assert obligations["authority_owner"] == "downstream_runtime_or_institution", result


def _assert_case(
    validator: Draft202012Validator,
    envelope: dict,
    *,
    stage: str,
    reason_code: str,
) -> dict:
    result = evaluate_governed_action(envelope, today=TODAY)
    assert result["decision"] == "human_gate", result
    assert result["stage"] == stage, result
    assert reason_code in result["reason_codes"], result
    _assert_bounded_handoff(result)
    validator.validate(result)
    return result


def main() -> int:
    validator = _result_validator()

    # Positive baseline: runtime output must satisfy the public governed-result schema.
    allowed = evaluate_governed_action(_base(), today=TODAY)
    assert allowed["decision"] == "allow", allowed
    assert allowed["stage"] == "evaluation", allowed
    _assert_bounded_handoff(allowed)
    validator.validate(allowed)

    # Pack/governance relationship misbinding must fail before evaluation.
    source_authority = _base()
    source_authority["governed_packs"][0]["governance"]["source_authority"] = "Different Authority"
    _assert_case(
        validator,
        source_authority,
        stage="admission",
        reason_code="RPE-GOVERNED-BINDING-SOURCE-AUTHORITY-MISMATCH",
    )

    source_version = _base()
    source_version["governed_packs"][0]["governance"]["source_version"] = "different-version"
    _assert_case(
        validator,
        source_version,
        stage="admission",
        reason_code="RPE-GOVERNED-BINDING-SOURCE-VERSION-MISMATCH",
    )

    jurisdiction = _base()
    jurisdiction["governed_packs"][0]["governance"]["jurisdiction"] = "different-jurisdiction"
    _assert_case(
        validator,
        jurisdiction,
        stage="admission",
        reason_code="RPE-GOVERNED-BINDING-JURISDICTION-MISMATCH",
    )

    # Governance that is present but not eligible must not silently enter evaluation.
    inactive = _base()
    inactive["governed_packs"][0]["governance"]["lifecycle_state"] = "suspended"
    _assert_case(
        validator,
        inactive,
        stage="governance",
        reason_code="RPE-PACK-GOV-NOT-ACTIVE",
    )

    superseded = _base()
    superseded["governed_packs"][0]["governance"]["lifecycle_state"] = "superseded"
    superseded_result = _assert_case(
        validator,
        superseded,
        stage="governance",
        reason_code="RPE-PACK-GOV-NOT-ACTIVE",
    )
    assert "RPE-PACK-GOV-SUPERSEDED-WITHOUT-REPLACEMENT" in superseded_result["reason_codes"], superseded_result

    # Missing applicability context and explicit mismatch are distinct fail-closed paths.
    unknown_applicability = _base()
    del unknown_applicability["request"]["applicability_context"]["organization"]
    unknown_result = _assert_case(
        validator,
        unknown_applicability,
        stage="applicability",
        reason_code="RPE-APPLICABILITY-UNKNOWN",
    )
    assert unknown_result["responsibility_handoff"]["selected_pack_refs"] == [], unknown_result
    assert unknown_result["responsibility_handoff"]["rejected_pack_refs"], unknown_result

    no_applicable = _base()
    no_applicable["request"]["applicability_context"]["organization"] = "other"
    no_applicable_result = _assert_case(
        validator,
        no_applicable,
        stage="applicability",
        reason_code="RPE-APPLICABILITY-NO-APPLICABLE-PACKS",
    )
    assert no_applicable_result["responsibility_handoff"]["selected_pack_refs"] == [], no_applicable_result
    assert no_applicable_result["responsibility_handoff"]["rejected_pack_refs"], no_applicable_result

    # Compatibility-stage output is also schema-valid and authority-neutral.
    incompatible = _base()
    incompatible["contract_version"] = "2.0.0"
    _assert_case(
        validator,
        incompatible,
        stage="compatibility",
        reason_code="RPE-CONTRACT-UNSUPPORTED-GOVERNED-EVALUATION-REQUEST-MAJOR",
    )

    # Evaluation failure preserves evidence distinction and residual ownership.
    missing_approval = _base()
    missing_approval["request"]["context"]["human_approval_present"] = False
    missing_approval["request"]["evidence_scope"] = {
        "available": [],
        "missing": ["approval-record"],
    }
    evaluation_result = _assert_case(
        validator,
        missing_approval,
        stage="evaluation",
        reason_code="RPE-DEMO-MISSING-HUMAN-APPROVAL-PRESENT",
    )
    handoff = evaluation_result["responsibility_handoff"]
    assert handoff["evaluation_evidence_scope"] == {
        "available": [],
        "missing": ["approval-record"],
    }, evaluation_result
    assert handoff["downstream_obligations"]["residual_owner_role"] == "demo-owner", evaluation_result

    print("PASS: M2 adversarial closure matrix")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
