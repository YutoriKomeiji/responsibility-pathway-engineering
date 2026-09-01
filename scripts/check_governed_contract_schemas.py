#!/usr/bin/env python3
"""Validate strict governed M2 contract skeletons and migration boundaries."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas/external-kernel"
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"

SCHEMAS = [
    "action-request.schema.json",
    "requirement-pack.schema.json",
    "requirement-pack-governance.schema.json",
    "governed-pack-binding.schema.json",
    "governed-evaluation-request.schema.json",
    "governed-evaluation-result.schema.json",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = Registry()
    loaded: dict[str, dict] = {}
    for name in SCHEMAS:
        schema = load(SCHEMA_DIR / name)
        loaded[name] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))

    request_validator = Draft202012Validator(
        loaded["governed-evaluation-request.schema.json"],
        registry=registry,
        format_checker=FormatChecker(),
    )

    valid = load(FIXTURE)
    request_validator.validate(valid)

    missing_request_version = copy.deepcopy(valid)
    del missing_request_version["request"]["contract_version"]
    assert list(request_validator.iter_errors(missing_request_version)), (
        "strict governed request must require action request contract_version"
    )

    missing_governance_version = copy.deepcopy(valid)
    del missing_governance_version["governed_packs"][0]["governance"]["contract_version"]
    assert list(request_validator.iter_errors(missing_governance_version)), (
        "strict governed binding must require governance contract_version"
    )

    legacy_governance = copy.deepcopy(valid["governed_packs"][0]["governance"])
    legacy_governance.pop("contract_version")
    governance_validator = Draft202012Validator(
        loaded["requirement-pack-governance.schema.json"],
        format_checker=FormatChecker(),
    )
    governance_validator.validate(legacy_governance)

    print("governed contract schema skeleton: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
