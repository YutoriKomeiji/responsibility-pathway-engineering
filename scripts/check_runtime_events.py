#!/usr/bin/env python3
"""
Bounded runtime-event checker for Responsibility Pathway Engineering.

This script performs local structural checks on selected synthetic runtime-event
and minimal synthetic runtime observation JSON fixtures. It is not schema
validation, certification, compliance review, legal review, safety review,
fairness review, production-readiness assessment, connector-correctness proof,
adapter-correctness proof, runtime-correctness proof, or an AI
final-responsibility transfer mechanism.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_FIXTURES = [
    Path("examples/adapter-input-event-minimal.json"),
    Path("examples/minimal-synthetic-runtime-fixture.json"),
]

RUNTIME_EVENT_REQUIRED_TOP_LEVEL_KEYS = [
    "event_id",
    "schema_version",
    "source_system",
    "observed_at",
    "observed_actor",
    "observed_action",
    "observed_target",
    "evidence",
    "review_requirement",
    "excluded_claims",
]

MINIMAL_RUNTIME_FIXTURE_REQUIRED_TOP_LEVEL_KEYS = [
    "fixture_id",
    "fixture_version",
    "fixture_type",
    "non_production",
    "synthetic",
    "vendor_neutral",
    "review_required",
    "certification_claimed",
    "runtime_scope",
    "runtime_observation",
    "expected_boundary_preservation",
    "candidate_status",
    "excluded_claims",
]

EXPECTED_EXCLUDED_CLAIMS = [
    "legal_validity",
    "safety_certification",
    "compliance_certification",
    "fairness_certification",
    "moral_resolution",
    "institutional_approval",
    "production_readiness",
    "ai_final_responsibility_transfer",
]

EXPECTED_MINIMAL_RUNTIME_FIXTURE_EXCLUDED_CLAIMS = [
    "legal_validity",
    "safety_certification",
    "compliance_certification",
    "fairness_certification",
    "moral_resolution",
    "institutional_approval",
    "production_readiness",
    "service_connector_correctness",
    "adapter_mapping_correctness",
    "schema_correctness",
    "json_semantic_correctness",
    "responsibility_assignment_correctness",
    "ai_final_responsibility_transfer",
]

NON_CERTIFYING_NOTE = (
    "NOTE: This checker is bounded. PASS means only that the selected synthetic "
    "runtime-event or minimal synthetic runtime observation JSON fixture satisfied "
    "local structural checks. PASS does not mean certified, safe, compliant, fair, "
    "legally valid, morally resolved, production ready, connector-correct, "
    "adapter-correct, runtime-correct, semantically correct, or "
    "AI-responsibility-transferring."
)


class CheckResult:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def pass_(self, message: str) -> None:
        self.passes.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def fail(self, message: str) -> None:
        self.failures.append(message)

    @property
    def ok(self) -> bool:
        return not self.failures


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require_mapping(result: CheckResult, value: Any, key: str) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        result.fail(f"{key} must be a mapping")
        return None
    result.pass_(f"{key} is a mapping")
    return value


def require_bool(result: CheckResult, mapping: dict[str, Any], key: str, expected: bool) -> None:
    value = mapping.get(key)
    if value is expected:
        result.pass_(f"{key} is explicitly {expected}")
    else:
        result.fail(f"{key} must be explicitly {expected}")


def require_top_level_bool(result: CheckResult, data: dict[str, Any], key: str, expected: bool) -> None:
    value = data.get(key)
    if value is expected:
        result.pass_(f"{key} is explicitly {expected}")
    else:
        result.fail(f"{key} must be explicitly {expected}")


def require_nonempty_list(result: CheckResult, mapping: dict[str, Any], key: str) -> list[Any] | None:
    value = mapping.get(key)
    if isinstance(value, list) and value:
        result.pass_(f"{key} is a non-empty list")
        return value
    result.fail(f"{key} must be a non-empty list")
    return None


def require_list(result: CheckResult, mapping: dict[str, Any], key: str) -> list[Any] | None:
    value = mapping.get(key)
    if isinstance(value, list):
        result.pass_(f"{key} is a list")
        return value
    result.fail(f"{key} must be a list")
    return None


def require_expected_claims(
    result: CheckResult,
    claims: list[Any] | None,
    expected_claims: list[str],
) -> None:
    if claims is None:
        return
    missing = [claim for claim in expected_claims if claim not in claims]
    if missing:
        result.fail("excluded_claims missing expected boundaries: " + ", ".join(missing))
    else:
        result.pass_("excluded_claims include expected non-certifying boundaries")


def load_top_level_mapping(path: Path, result: CheckResult) -> dict[str, Any] | None:
    try:
        data = load_json(path)
    except Exception as exc:  # noqa: BLE001 - bounded checker failure reporting
        result.fail(f"could not parse JSON: {exc}")
        return None

    if not isinstance(data, dict):
        result.fail("top-level JSON value must be a mapping")
        return None

    result.pass_("top-level JSON value is a mapping")
    return data


def check_required_top_level_keys(
    result: CheckResult,
    data: dict[str, Any],
    required_keys: list[str],
) -> None:
    for key in required_keys:
        if key in data:
            result.pass_(f"required key present: {key}")
        else:
            result.fail(f"required key missing: {key}")


def check_runtime_event(path: Path) -> CheckResult:
    result = CheckResult(path)
    data = load_top_level_mapping(path, result)
    if data is None:
        return result

    check_required_top_level_keys(result, data, RUNTIME_EVENT_REQUIRED_TOP_LEVEL_KEYS)

    source_system = require_mapping(result, data.get("source_system"), "source_system")
    if source_system is not None:
        require_bool(result, source_system, "vendor_specific", False)
        if source_system.get("type") == "synthetic":
            result.pass_("source_system.type is synthetic")
        else:
            result.warn("first minimal runtime-event fixture should remain synthetic")

    observed_actor = require_mapping(result, data.get("observed_actor"), "observed_actor")
    if observed_actor is not None:
        if observed_actor.get("type") == "ai_agent":
            result.pass_("observed_actor.type is ai_agent")
            require_bool(result, observed_actor, "final_responsibility_claimed", False)
        else:
            result.warn("first minimal runtime-event fixture is expected to model an ai_agent actor")

    evidence = require_mapping(result, data.get("evidence"), "evidence")
    if evidence is not None:
        require_nonempty_list(result, evidence, "captured_fields")
        require_list(result, evidence, "missing_fields")
        require_list(result, evidence, "uncertainty_notes")
        require_bool(result, evidence, "raw_event_available", True)

    review_requirement = require_mapping(result, data.get("review_requirement"), "review_requirement")
    if review_requirement is not None:
        require_bool(result, review_requirement, "human_or_institutional_review_required", True)
        if isinstance(review_requirement.get("reason"), str) and review_requirement.get("reason"):
            result.pass_("review_requirement.reason is present")
        else:
            result.fail("review_requirement.reason must be a non-empty string")

    excluded_claims = require_list(result, data, "excluded_claims")
    require_expected_claims(result, excluded_claims, EXPECTED_EXCLUDED_CLAIMS)

    return result


def check_minimal_runtime_fixture(path: Path) -> CheckResult:
    result = CheckResult(path)
    data = load_top_level_mapping(path, result)
    if data is None:
        return result

    check_required_top_level_keys(result, data, MINIMAL_RUNTIME_FIXTURE_REQUIRED_TOP_LEVEL_KEYS)

    if data.get("fixture_type") == "minimal_synthetic_runtime_observation":
        result.pass_("fixture_type is minimal_synthetic_runtime_observation")
    else:
        result.fail("fixture_type must be minimal_synthetic_runtime_observation")

    require_top_level_bool(result, data, "non_production", True)
    require_top_level_bool(result, data, "synthetic", True)
    require_top_level_bool(result, data, "vendor_neutral", True)
    require_top_level_bool(result, data, "review_required", True)
    require_top_level_bool(result, data, "certification_claimed", False)

    runtime_scope = require_mapping(result, data.get("runtime_scope"), "runtime_scope")
    if runtime_scope is not None:
        require_bool(result, runtime_scope, "production_runtime", False)
        require_bool(result, runtime_scope, "service_specific_connector", False)
        require_bool(result, runtime_scope, "automatic_approval", False)
        require_bool(result, runtime_scope, "automatic_execution", False)
        require_bool(result, runtime_scope, "external_side_effects", False)

    runtime_observation = require_mapping(result, data.get("runtime_observation"), "runtime_observation")
    if runtime_observation is not None:
        source_system = require_mapping(result, runtime_observation.get("source_system"), "runtime_observation.source_system")
        if source_system is not None:
            require_bool(result, source_system, "vendor_specific", False)
            require_bool(result, source_system, "production_system", False)
        observed_sequence = require_nonempty_list(result, runtime_observation, "observed_sequence")
        if observed_sequence is not None:
            for index, step in enumerate(observed_sequence):
                if not isinstance(step, dict):
                    result.fail(f"observed_sequence[{index}] must be a mapping")
                    continue
                result.pass_(f"observed_sequence[{index}] is a mapping")
                if step.get("actor_type") == "ai_agent":
                    result.pass_(f"observed_sequence[{index}].actor_type is ai_agent")
                    require_bool(result, step, "actor_final_responsibility_claimed", False)
                require_bool(result, step, "approval_evidence_present", False)
                require_bool(result, step, "execution_evidence_present", False)
                require_bool(result, step, "human_review_required", True)
                if isinstance(step.get("source_event_reference"), str) and step.get("source_event_reference"):
                    result.pass_(f"observed_sequence[{index}].source_event_reference is present")
                else:
                    result.fail(f"observed_sequence[{index}].source_event_reference must be present")

    expected_boundary_preservation = require_mapping(
        result,
        data.get("expected_boundary_preservation"),
        "expected_boundary_preservation",
    )
    if expected_boundary_preservation is not None:
        require_bool(result, expected_boundary_preservation, "missing_context_explicit", True)
        require_bool(result, expected_boundary_preservation, "missing_approval_evidence_explicit", True)
        require_bool(result, expected_boundary_preservation, "missing_execution_evidence_explicit", True)
        require_bool(result, expected_boundary_preservation, "excluded_claims_explicit", True)
        require_bool(result, expected_boundary_preservation, "human_or_institutional_review_required", True)
        require_bool(result, expected_boundary_preservation, "ai_final_responsibility_claimed", False)
        require_bool(result, expected_boundary_preservation, "adapter_mapping_correctness_claimed", False)
        require_bool(result, expected_boundary_preservation, "service_connector_correctness_claimed", False)
        require_bool(result, expected_boundary_preservation, "schema_correctness_claimed", False)
        require_bool(result, expected_boundary_preservation, "json_semantic_correctness_claimed", False)
        require_bool(result, expected_boundary_preservation, "production_readiness_claimed", False)

    candidate_status = require_mapping(result, data.get("candidate_status"), "candidate_status")
    if candidate_status is not None:
        if candidate_status.get("selected_candidate") == "minimal_synthetic_runtime_fixture":
            result.pass_("candidate_status.selected_candidate is minimal_synthetic_runtime_fixture")
        else:
            result.fail("candidate_status.selected_candidate must be minimal_synthetic_runtime_fixture")
        require_bool(result, candidate_status, "production_runtime_included", False)
        require_bool(result, candidate_status, "service_connector_included", False)
        require_bool(result, candidate_status, "automatic_approval_included", False)
        require_bool(result, candidate_status, "automatic_execution_included", False)

    excluded_claims = require_list(result, data, "excluded_claims")
    require_expected_claims(result, excluded_claims, EXPECTED_MINIMAL_RUNTIME_FIXTURE_EXCLUDED_CLAIMS)

    return result


def check_path(path: Path) -> CheckResult:
    if path.name == "minimal-synthetic-runtime-fixture.json":
        return check_minimal_runtime_fixture(path)
    return check_runtime_event(path)


def print_result(result: CheckResult) -> None:
    print(f"\n== {result.path} ==")
    for message in result.passes:
        print(f"PASS: {message}")
    for message in result.warnings:
        print(f"WARN: {message}")
    for message in result.failures:
        print(f"FAIL: {message}")


def main(argv: list[str]) -> int:
    repo_root = Path(__file__).resolve().parents[1]

    if len(argv) > 1:
        paths = [Path(arg) for arg in argv[1:]]
    else:
        paths = [repo_root / fixture for fixture in DEFAULT_FIXTURES]

    print(NON_CERTIFYING_NOTE)

    results = [check_path(path) for path in paths]
    for result in results:
        print_result(result)

    if all(result.ok for result in results):
        print("\nPASS: bounded runtime-event and minimal runtime fixture checks completed without failures")
        print(NON_CERTIFYING_NOTE)
        return 0

    print("\nFAIL: bounded runtime-event checks found failures")
    print(NON_CERTIFYING_NOTE)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
