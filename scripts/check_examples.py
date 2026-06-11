#!/usr/bin/env python3
"""
Lightweight example checker for Responsibility Pathway Engineering.

This script performs bounded structural checks on YAML example files.
It is not schema validation, certification, compliance review, legal review,
safety review, fairness review, moral accountability judgment, or a
production-readiness assessment.

It checks only declared structure, lifecycle-specific structural signals,
and explicit responsibility-boundary fields.
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


REQUIRED_TOP_LEVEL_KEYS = [
    "id",
    "version",
    "lifecycle_state",
    "nodes",
    "edges",
    "roles",
    "evidence_logs",
    "return_points",
    "responsibility_boundary",
    "formalization_scope",
]

EXCLUDED_CLAIM_KEYWORDS = [
    "legal",
    "moral",
    "compliance",
    "safety",
    "fairness",
    "production",
]

LIFECYCLE_REQUIRED_BLOCKS = {
    "suspended": "suspension",
    "returning": "returning",
    "closed": "closure",
}

LIFECYCLE_DISALLOWED_INTERPRETATION_KEYWORDS = {
    "suspended": [
        "closure",
        "repair_completion",
        "certification",
        "ai_decision",
    ],
    "returning": [
        "automatic_continuation",
        "repair_completion",
        "closure",
        "certification",
        "ai_decision",
    ],
    "closed": [
        "erasure",
        "immunity",
        "repair_completion",
        "certification",
    ],
}

NON_CERTIFYING_NOTE = (
    "NOTE: This checker is bounded. PASS does not mean certified, safe, "
    "compliant, fair, legally valid, morally resolved, or production ready."
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


def find_ai_final_responsibility_flags(value: Any) -> list[tuple[str, Any]]:
    """Find keys that look like AI final responsibility declarations."""
    found: list[tuple[str, Any]] = []

    def walk(node: Any, trail: str) -> None:
        if isinstance(node, dict):
            for key, child in node.items():
                child_trail = f"{trail}.{key}" if trail else str(key)
                normalized = str(key).lower()
                if normalized in {
                    "assumes_final_responsibility",
                    "ai_final_responsibility_allowed",
                }:
                    found.append((child_trail, child))
                walk(child, child_trail)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{trail}[{index}]")

    walk(value, "")
    return found


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


def has_human_return_point(data: dict[str, Any]) -> bool:
    return_points = data.get("return_points")
    if not isinstance(return_points, list):
        return False

    for item in return_points:
        if not isinstance(item, dict):
            continue
        values = " ".join(str(value).lower() for value in item.values())
        if "human" in values:
            return True
    return False


def has_nonempty_list(value: Any, key: str) -> bool:
    if not isinstance(value, dict):
        return False
    item = value.get(key)
    return isinstance(item, list) and bool(item)


def contains_all_keywords(value: Any, keywords: list[str]) -> list[str]:
    joined = joined_strings(value)
    return [keyword for keyword in keywords if keyword not in joined]


def check_suspension_block(result: CheckResult, data: dict[str, Any]) -> None:
    suspension = data.get("suspension")
    if not isinstance(suspension, dict):
        result.fail("lifecycle_state suspended requires suspension mapping")
        return

    result.pass_("suspended lifecycle block present: suspension")

    if suspension.get("continuation_allowed") is False:
        result.pass_("suspension.continuation_allowed is explicitly false")
    else:
        result.warn("suspension.continuation_allowed should be false while suspended")

    if suspension.get("closure_allowed") is False:
        result.pass_("suspension.closure_allowed is explicitly false")
    else:
        result.warn("suspension.closure_allowed should be false while suspended")

    if has_nonempty_list(suspension, "required_before_continuation"):
        result.pass_("suspension.required_before_continuation is present")
    else:
        result.warn("suspension.required_before_continuation should be a non-empty list")

    missing = contains_all_keywords(
        suspension.get("disallowed_interpretations"),
        LIFECYCLE_DISALLOWED_INTERPRETATION_KEYWORDS["suspended"],
    )
    if missing:
        result.warn(
            "suspension.disallowed_interpretations may be missing signals: "
            + ", ".join(missing)
        )
    else:
        result.pass_("suspension disallowed-interpretation signals present")


def check_returning_block(result: CheckResult, data: dict[str, Any]) -> None:
    returning = data.get("returning")
    if not isinstance(returning, dict):
        result.fail("lifecycle_state returning requires returning mapping")
        return

    result.pass_("returning lifecycle block present: returning")

    if returning.get("previous_lifecycle_state") == "suspended":
        result.pass_("returning.previous_lifecycle_state is suspended")
    else:
        result.warn("returning.previous_lifecycle_state should usually be suspended")

    for key in [
        "automatic_continuation_allowed",
        "automatic_closure_allowed",
        "automatic_repair_completion_allowed",
    ]:
        if returning.get(key) is False:
            result.pass_(f"returning.{key} is explicitly false")
        else:
            result.warn(f"returning.{key} should be false")

    if has_nonempty_list(returning, "required_before_next_state"):
        result.pass_("returning.required_before_next_state is present")
    else:
        result.warn("returning.required_before_next_state should be a non-empty list")

    missing = contains_all_keywords(
        returning.get("disallowed_interpretations"),
        LIFECYCLE_DISALLOWED_INTERPRETATION_KEYWORDS["returning"],
    )
    if missing:
        result.warn(
            "returning.disallowed_interpretations may be missing signals: "
            + ", ".join(missing)
        )
    else:
        result.pass_("returning disallowed-interpretation signals present")


def check_closure_block(result: CheckResult, data: dict[str, Any]) -> None:
    closure = data.get("closure")
    if not isinstance(closure, dict):
        result.fail("lifecycle_state closed requires closure mapping")
        return

    result.pass_("closed lifecycle block present: closure")

    for key in ["closure_basis", "residual_obligations", "reopening_conditions"]:
        if has_nonempty_list(closure, key):
            result.pass_(f"closure.{key} is present")
        else:
            result.warn(f"closure.{key} should be a non-empty list")

    for key in [
        "automatic_reopening_allowed",
        "automatic_closure_allowed",
        "AI_closure_authority_allowed",
    ]:
        if closure.get(key) is False:
            result.pass_(f"closure.{key} is explicitly false")
        else:
            result.warn(f"closure.{key} should be false")

    missing = contains_all_keywords(
        closure.get("closure_does_not_mean"),
        LIFECYCLE_DISALLOWED_INTERPRETATION_KEYWORDS["closed"],
    )
    if missing:
        result.warn("closure.closure_does_not_mean may be missing signals: " + ", ".join(missing))
    else:
        result.pass_("closure does-not-mean signals present")

    formalization_scope = data.get("formalization_scope")
    closure_exclusion_missing = contains_all_keywords(
        formalization_scope,
        ["closure_as_erasure", "closure_as_immunity", "closure_as_repair_completion"],
    )
    if closure_exclusion_missing:
        result.warn(
            "closed formalization_scope may be missing closure exclusions: "
            + ", ".join(closure_exclusion_missing)
        )
    else:
        result.pass_("closed formalization_scope includes closure-specific exclusions")


def check_lifecycle_specific_fields(result: CheckResult, data: dict[str, Any]) -> None:
    lifecycle_state = data.get("lifecycle_state")
    if not isinstance(lifecycle_state, str):
        result.fail("lifecycle_state must be a string")
        return

    result.pass_(f"lifecycle_state is declared: {lifecycle_state}")

    required_block = LIFECYCLE_REQUIRED_BLOCKS.get(lifecycle_state)
    if required_block is None:
        result.warn(
            "no lifecycle-specific structural rule for lifecycle_state: "
            + lifecycle_state
        )
        return

    if required_block not in data:
        result.fail(f"lifecycle_state {lifecycle_state} requires top-level key: {required_block}")
        return

    if lifecycle_state == "suspended":
        check_suspension_block(result, data)
    elif lifecycle_state == "returning":
        check_returning_block(result, data)
    elif lifecycle_state == "closed":
        check_closure_block(result, data)


def check_example(path: Path) -> CheckResult:
    result = CheckResult(path)

    try:
        data = load_yaml(path)
    except Exception as exc:  # noqa: BLE001 - report bounded checker failure
        result.fail(f"could not parse YAML: {exc}")
        return result

    if not isinstance(data, dict):
        result.fail("top-level YAML value must be a mapping")
        return result

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key in data:
            result.pass_(f"required key present: {key}")
        else:
            result.fail(f"required key missing: {key}")

    nodes = data.get("nodes")
    if isinstance(nodes, list) and nodes:
        result.pass_("nodes list is present and non-empty")
    else:
        result.fail("nodes must be a non-empty list")

    edges = data.get("edges")
    if isinstance(edges, list):
        result.pass_("edges list is present")
    else:
        result.fail("edges must be a list")

    if has_human_return_point(data):
        result.pass_("human return point signal present")
    else:
        result.warn("no human return point signal detected")

    boundary = data.get("responsibility_boundary")
    if isinstance(boundary, dict):
        if boundary.get("ai_final_responsibility_allowed") is False:
            result.pass_("AI final responsibility is explicitly disallowed")
        else:
            result.fail("responsibility_boundary.ai_final_responsibility_allowed must be false")
    else:
        result.fail("responsibility_boundary must be a mapping")

    flags = find_ai_final_responsibility_flags(data)
    for trail, value in flags:
        if trail.endswith("assumes_final_responsibility") and value is not False:
            result.fail(f"{trail} must be false")
        elif trail.endswith("ai_final_responsibility_allowed") and value is not False:
            result.fail(f"{trail} must be false")

    formalization_scope = data.get("formalization_scope")
    joined = joined_strings(formalization_scope)
    missing_keywords = [word for word in EXCLUDED_CLAIM_KEYWORDS if word not in joined]
    if missing_keywords:
        result.warn(
            "formalization_scope may be missing excluded-claim signals: "
            + ", ".join(missing_keywords)
        )
    else:
        result.pass_("formalization_scope includes expected excluded-claim signals")

    check_lifecycle_specific_fields(result, data)

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
    examples_dir = repo_root / "examples"

    if len(argv) > 1:
        paths = [Path(arg) for arg in argv[1:]]
    else:
        paths = sorted(examples_dir.glob("*.yaml"))

    print(NON_CERTIFYING_NOTE)

    if not paths:
        print("FAIL: no example YAML files found")
        return 1

    results = [check_example(path) for path in paths]
    for result in results:
        print_result(result)

    if all(result.ok for result in results):
        print("\nPASS: bounded structural checks completed without failures")
        print(NON_CERTIFYING_NOTE)
        return 0

    print("\nFAIL: bounded structural checks found failures")
    print(NON_CERTIFYING_NOTE)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
