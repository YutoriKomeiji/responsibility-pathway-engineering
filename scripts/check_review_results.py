#!/usr/bin/env python3
"""
Bounded review-result checker for Responsibility Pathway Engineering.

This script performs small structural checks on review-result YAML fixtures under
fixtures/review-results/ against spec/review-result.schema.yaml.

It is not legal validation, safety certification, compliance certification,
fairness certification, moral resolution, institutional certification,
production approval, or AI final-responsibility transfer.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - runtime guidance
    print("FAIL: PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)


NON_CERTIFYING_NOTE = (
    "NOTE: This checker is bounded. PASS does not mean legal validation, "
    "safety certification, compliance certification, fairness certification, "
    "moral resolution, institutional certification, production approval, "
    "or AI final-responsibility transfer."
)

EXPECTED_BOUNDARY_FLAGS = {
    "human_or_institutional_responsibility_required": True,
    "ai_final_responsibility_allowed": False,
    "review_result_is_certification": False,
    "review_result_is_legal_decision": False,
    "review_result_is_safety_decision": False,
    "review_result_is_compliance_decision": False,
    "review_result_is_fairness_decision": False,
    "review_result_is_moral_resolution": False,
    "review_result_is_production_approval": False,
}


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


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def require_mapping(result: CheckResult, value: Any, label: str) -> dict[str, Any] | None:
    if isinstance(value, dict):
        result.pass_(f"{label} is a mapping")
        return value
    result.fail(f"{label} must be a mapping")
    return None


def require_nonempty_list(result: CheckResult, value: Any, label: str) -> list[Any] | None:
    if isinstance(value, list) and value:
        result.pass_(f"{label} is a non-empty list")
        return value
    result.fail(f"{label} must be a non-empty list")
    return None


def load_schema(repo_root: Path) -> dict[str, Any]:
    schema_path = repo_root / "spec" / "review-result.schema.yaml"
    schema = load_yaml(schema_path)
    if not isinstance(schema, dict):
        raise ValueError("spec/review-result.schema.yaml must be a mapping")
    return schema


def schema_required_fields(schema: dict[str, Any]) -> list[str]:
    review_result = schema.get("review_result")
    if not isinstance(review_result, dict):
        raise ValueError("schema.review_result must be a mapping")
    required = review_result.get("required_fields")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValueError("schema.review_result.required_fields must be a list of strings")
    return required


def allowed_values(schema: dict[str, Any], field_name: str) -> list[str]:
    review_result = schema.get("review_result")
    if not isinstance(review_result, dict):
        raise ValueError("schema.review_result must be a mapping")
    fields = review_result.get("fields")
    if not isinstance(fields, dict):
        raise ValueError("schema.review_result.fields must be a mapping")
    field = fields.get(field_name)
    if not isinstance(field, dict):
        raise ValueError(f"schema.review_result.fields.{field_name} must be a mapping")
    values = field.get("allowed_values")
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"schema.review_result.fields.{field_name}.allowed_values must be a list of strings")
    return values


def schema_expected_list(schema: dict[str, Any], key: str) -> list[str]:
    values = schema.get(key)
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"schema.{key} must be a list of strings")
    return values


def missing_items(actual: list[Any], expected: list[str]) -> list[str]:
    actual_strings = {str(item) for item in actual}
    return [item for item in expected if item not in actual_strings]


def check_review_result_fixture(path: Path, schema: dict[str, Any]) -> CheckResult:
    result = CheckResult(path)

    try:
        data = load_yaml(path)
    except Exception as exc:  # noqa: BLE001 - report bounded checker failure
        result.fail(f"could not parse YAML: {exc}")
        return result

    data = require_mapping(result, data, "top-level YAML value")
    if data is None:
        return result

    for field in schema_required_fields(schema):
        if field in data:
            result.pass_(f"required field present: {field}")
        else:
            result.fail(f"required field missing: {field}")

    review_scope = data.get("review_scope")
    if review_scope in allowed_values(schema, "review_scope"):
        result.pass_("review_scope is allowed by schema")
    else:
        result.fail(f"review_scope is not allowed by schema: {review_scope!r}")

    review_status = data.get("review_status")
    if review_status in allowed_values(schema, "review_status"):
        result.pass_("review_status is allowed by schema")
    else:
        result.fail(f"review_status is not allowed by schema: {review_status!r}")

    checked_items = require_nonempty_list(result, data.get("checked_items"), "checked_items")
    if checked_items is not None:
        result.pass_("checked_items preserves at least one structural check")

    not_checked = require_nonempty_list(result, data.get("not_checked"), "not_checked")
    if not_checked is not None:
        missing = missing_items(not_checked, schema_expected_list(schema, "minimum_expected_not_checked"))
        if missing:
            result.fail("not_checked missing expected boundary items: " + ", ".join(missing))
        else:
            result.pass_("not_checked includes expected boundary items")

    not_claimed = require_nonempty_list(result, data.get("not_claimed"), "not_claimed")
    if not_claimed is not None:
        missing = missing_items(not_claimed, schema_expected_list(schema, "minimum_expected_not_claimed"))
        if missing:
            result.fail("not_claimed missing expected boundary items: " + ", ".join(missing))
        else:
            result.pass_("not_claimed includes expected boundary items")

    boundary = require_mapping(result, data.get("responsibility_boundary"), "responsibility_boundary")
    if boundary is not None:
        for key, expected in EXPECTED_BOUNDARY_FLAGS.items():
            actual = boundary.get(key)
            if actual is expected:
                result.pass_(f"responsibility_boundary.{key} is {expected}")
            else:
                result.fail(
                    f"responsibility_boundary.{key} must be {expected}; got {actual!r}"
                )

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
    fixtures_dir = repo_root / "fixtures" / "review-results"

    try:
        schema = load_schema(repo_root)
    except Exception as exc:  # noqa: BLE001 - report bounded checker failure
        print(f"FAIL: could not load review-result schema: {exc}")
        return 1

    if len(argv) > 1:
        paths = [Path(arg) for arg in argv[1:]]
    else:
        paths = sorted(fixtures_dir.glob("*.yaml"))

    print(NON_CERTIFYING_NOTE)

    if not paths:
        print("FAIL: no review-result YAML fixtures found")
        return 1

    results = [check_review_result_fixture(path, schema) for path in paths]
    for result in results:
        print_result(result)

    if all(result.ok for result in results):
        print("\nPASS: bounded review-result checks completed without failures")
        print(NON_CERTIFYING_NOTE)
        return 0

    print("\nFAIL: bounded review-result checks found failures")
    print(NON_CERTIFYING_NOTE)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
