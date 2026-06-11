#!/usr/bin/env python3
"""
Lightweight example checker for Responsibility Pathway Engineering.

This script performs bounded structural checks on YAML example files.
It is not schema validation, certification, compliance review, legal review,
safety review, fairness review, moral accountability judgment, or a
production-readiness assessment.

It checks only declared structure and explicit responsibility-boundary fields.
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
    strings = [text.lower() for text in flatten_strings(formalization_scope)]
    joined = " ".join(strings)
    missing_keywords = [word for word in EXCLUDED_CLAIM_KEYWORDS if word not in joined]
    if missing_keywords:
        result.warn(
            "formalization_scope may be missing excluded-claim signals: "
            + ", ".join(missing_keywords)
        )
    else:
        result.pass_("formalization_scope includes expected excluded-claim signals")

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
