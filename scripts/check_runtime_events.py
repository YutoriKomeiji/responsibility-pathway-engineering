#!/usr/bin/env python3
"""
Bounded runtime-event checker for Responsibility Pathway Engineering.

This script performs local structural checks on the first synthetic runtime-event
JSON fixture only. It is not schema validation, certification, compliance
review, legal review, safety review, fairness review, production-readiness
assessment, connector-correctness proof, adapter-correctness proof, or an
AI final-responsibility transfer mechanism.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_FIXTURE = Path("examples/adapter-input-event-minimal.json")

REQUIRED_TOP_LEVEL_KEYS = [
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

NON_CERTIFYING_NOTE = (
    "NOTE: This checker is bounded. PASS means only that the selected synthetic "
    "runtime-event JSON fixture satisfied local structural checks. PASS does not "
    "mean certified, safe, compliant, fair, legally valid, morally resolved, "
    "production ready, connector-correct, adapter-correct, or AI-responsibility-transferring."
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


def check_runtime_event(path: Path) -> CheckResult:
    result = CheckResult(path)

    try:
        data = load_json(path)
    except Exception as exc:  # noqa: BLE001 - bounded checker failure reporting
        result.fail(f"could not parse JSON: {exc}")
        return result

    if not isinstance(data, dict):
        result.fail("top-level JSON value must be a mapping")
        return result

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key in data:
            result.pass_(f"required key present: {key}")
        else:
            result.fail(f"required key missing: {key}")

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
    if excluded_claims is not None:
        missing = [claim for claim in EXPECTED_EXCLUDED_CLAIMS if claim not in excluded_claims]
        if missing:
            result.fail("excluded_claims missing expected boundaries: " + ", ".join(missing))
        else:
            result.pass_("excluded_claims include expected non-certifying boundaries")

    return result


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
        paths = [repo_root / DEFAULT_FIXTURE]

    print(NON_CERTIFYING_NOTE)

    results = [check_runtime_event(path) for path in paths]
    for result in results:
        print_result(result)

    if all(result.ok for result in results):
        print("\nPASS: bounded runtime-event checks completed without failures")
        print(NON_CERTIFYING_NOTE)
        return 0

    print("\nFAIL: bounded runtime-event checks found failures")
    print(NON_CERTIFYING_NOTE)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
