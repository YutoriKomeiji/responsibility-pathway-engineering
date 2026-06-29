#!/usr/bin/env python3
"""
Bounded Issue Form checker for Responsibility Pathway Engineering.

This script checks whether the AI-assisted work GitHub Issue Form preserves
RPE-specific structural fields.

It is not issue-content validation, legal review, safety review, compliance
review, fairness review, production approval, certification, conformance
evidence, social acceptance proof, or AI final-responsibility transfer.
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


ISSUE_FORM_PATH = Path(".github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml")

REQUIRED_TOP_LEVEL_KEYS = [
    "name",
    "description",
    "title",
    "body",
]

REQUIRED_FIELD_IDS = [
    "source-reference",
    "work-context",
    "ai-role",
    "ai-boundary",
    "human-review",
    "evidence-log",
    "responsibility-return-point",
    "repair-reopening",
    "non-claims",
]

RPE_ANCHOR_FIELD_IDS = [
    "ai-boundary",
    "evidence-log",
    "missing-context",
    "responsibility-return-point",
    "repair-reopening",
    "non-claims",
]

NON_CLAIM_KEYWORDS = [
    "legal",
    "safety",
    "compliance",
    "fairness",
    "production",
    "certify",
    "responsibility",
]

NON_FINAL_AI_TEXT = "final responsibility holder"

NON_CERTIFYING_NOTE = (
    "NOTE: This checker is bounded. PASS means only that the issue form "
    "contains selected RPE structural fields. It does not validate issue "
    "content, certify correctness, prove legal validity, prove safety, prove "
    "compliance, prove fairness, prove production readiness, prove conformance, "
    "or transfer final responsibility to AI."
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


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def flatten_strings(value: Any) -> list[str]:
    strings: list[str] = []

    def walk(node: Any) -> None:
        if isinstance(node, str):
            strings.append(node)
        elif isinstance(node, dict):
            for child in node.values():
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(value)
    return strings


def joined_strings(value: Any) -> str:
    return " ".join(text.lower() for text in flatten_strings(value))


def form_fields(data: dict[str, Any]) -> list[dict[str, Any]]:
    body = data.get("body")
    if not isinstance(body, list):
        return []
    return [item for item in body if isinstance(item, dict)]


def field_ids(data: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for field in form_fields(data):
        field_id = field.get("id")
        if isinstance(field_id, str):
            ids.add(field_id)
    return ids


def get_field(data: dict[str, Any], field_id: str) -> dict[str, Any] | None:
    for field in form_fields(data):
        if field.get("id") == field_id:
            return field
    return None


def field_required(field: dict[str, Any]) -> bool:
    validations = field.get("validations")
    return isinstance(validations, dict) and validations.get("required") is True


def check_issue_form(path: Path) -> CheckResult:
    result = CheckResult(path)

    if not path.exists():
        result.fail(f"missing issue form: {path}")
        return result

    data = load_yaml(path)
    if not isinstance(data, dict):
        result.fail("issue form must be a YAML mapping")
        return result

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in data:
            result.fail(f"missing top-level key: {key}")
        else:
            result.pass_(f"top-level key present: {key}")

    ids = field_ids(data)
    for field_id in REQUIRED_FIELD_IDS:
        if field_id not in ids:
            result.fail(f"missing required RPE field id: {field_id}")
        else:
            result.pass_(f"RPE field present: {field_id}")

    for field_id in RPE_ANCHOR_FIELD_IDS:
        field = get_field(data, field_id)
        if field is None:
            continue
        if field_id in {"repair-reopening", "missing-context"}:
            result.pass_(f"RPE anchor field present as optional repair/uncertainty signal: {field_id}")
        elif field_required(field):
            result.pass_(f"RPE anchor field required: {field_id}")
        else:
            result.warn(f"RPE anchor field is present but not required: {field_id}")

    all_text = joined_strings(data)
    for keyword in NON_CLAIM_KEYWORDS:
        if keyword not in all_text:
            result.fail(f"non-claim boundary missing keyword: {keyword}")
        else:
            result.pass_(f"non-claim keyword present: {keyword}")

    if NON_FINAL_AI_TEXT not in all_text:
        result.fail("AI non-final-responsibility boundary text is missing")
    else:
        result.pass_("AI non-final-responsibility boundary text present")

    non_claims = get_field(data, "non-claims")
    if non_claims is None:
        result.fail("non-claims checkbox field missing")
    elif non_claims.get("type") != "checkboxes":
        result.fail("non-claims field must use checkboxes")
    else:
        result.pass_("non-claims field uses checkboxes")
        attributes = non_claims.get("attributes")
        options = attributes.get("options") if isinstance(attributes, dict) else None
        if not isinstance(options, list) or not options:
            result.fail("non-claims checkboxes must contain required options")
        else:
            for index, option in enumerate(options):
                if not isinstance(option, dict):
                    result.fail(f"non-claims option {index} is not a mapping")
                elif option.get("required") is not True:
                    result.fail(f"non-claims option {index} must be required")
            if all(isinstance(option, dict) and option.get("required") is True for option in options):
                result.pass_("all non-claims checkbox options are required")

    return result


def print_result(result: CheckResult) -> None:
    print(f"Checking {result.path}")
    for message in result.passes:
        print(f"PASS: {message}")
    for message in result.warnings:
        print(f"WARN: {message}")
    for message in result.failures:
        print(f"FAIL: {message}")
    print(NON_CERTIFYING_NOTE)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ISSUE_FORM_PATH
    result = check_issue_form(path)
    print_result(result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
