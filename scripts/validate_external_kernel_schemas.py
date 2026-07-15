#!/usr/bin/env python3
"""Validate the minimal external-kernel fixtures against JSON Schema.

This validator checks document shape only. It does not determine legal validity,
policy correctness, safety, compliance, fairness, production readiness, or final
responsibility.
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

CASES = [
    (
        Path("schemas/external-kernel/requirement-pack.schema.json"),
        Path("examples/external-kernel/minimal-requirement-pack.json"),
    ),
    (
        Path("schemas/external-kernel/action-request.schema.json"),
        Path("examples/external-kernel/minimal-action-request.json"),
    ),
    (
        Path("schemas/external-kernel/gate-decision.schema.json"),
        Path("examples/external-kernel/expected-human-gate-decision.json"),
    ),
]


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    failed = False
    for schema_path, instance_path in CASES:
        schema = load_json(schema_path)
        instance = load_json(instance_path)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))

        print(f"\n== {instance_path} ==")
        if not errors:
            print(f"PASS: matches {schema_path}")
            continue

        failed = True
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"FAIL: {location}: {error.message}")

    print(
        "\nNOTE: PASS means JSON Schema shape validation only. "
        "It is not policy approval, legal review, safety review, compliance review, "
        "fairness review, semantic responsibility validation, or production approval."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
