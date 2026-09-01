#!/usr/bin/env python3
"""Bounded consistency checks for the external-kernel contract version manifest."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rpe_kernel.contract_versions import (  # noqa: E402
    CONTRACTS as RUNTIME_CONTRACTS,
    MANIFEST_VERSION as RUNTIME_MANIFEST_VERSION,
    REASON_CODE_POLICY as RUNTIME_REASON_CODE_POLICY,
)

MANIFEST = ROOT / "schemas/external-kernel/contract-versions.json"
POLICY = ROOT / "docs/contract-compatibility-policy.md"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
REQUIRED_CONTRACTS = {
    "action_request",
    "gate_decision",
    "runtime_evaluation_result",
    "requirement_pack",
    "requirement_pack_governance",
    "governed_pack_binding",
    "governed_evaluation_request",
    "governed_evaluation_result",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    manifest_version = data.get("manifest_version")
    if not isinstance(manifest_version, str) or not SEMVER.fullmatch(manifest_version):
        fail("manifest_version must use MAJOR.MINOR.PATCH")

    contracts = data.get("contracts")
    if not isinstance(contracts, dict) or set(contracts) != REQUIRED_CONTRACTS:
        expected = ", ".join(sorted(REQUIRED_CONTRACTS))
        fail(f"contracts must contain exactly the current external-kernel contract families: {expected}")

    for name, entry in contracts.items():
        if not isinstance(entry, dict):
            fail(f"{name} entry must be an object")
        version = entry.get("version")
        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            fail(f"{name}.version must use MAJOR.MINOR.PATCH")
        schema_path = entry.get("schema_path")
        if not isinstance(schema_path, str) or not schema_path:
            fail(f"{name}.schema_path is required")
        if not (ROOT / schema_path).is_file():
            fail(f"{name}.schema_path does not exist: {schema_path}")
        if entry.get("unknown_major_behavior") not in {"reject", "human_gate"}:
            fail(f"{name}.unknown_major_behavior must fail closed")

    reason_policy = data.get("reason_code_policy")
    if not isinstance(reason_policy, dict):
        fail("reason_code_policy is required")
    if not SEMVER.fullmatch(str(reason_policy.get("version", ""))):
        fail("reason_code_policy.version must use MAJOR.MINOR.PATCH")
    if reason_policy.get("unknown_code_behavior") != "preserve":
        fail("unknown reason codes must be preserved")
    if reason_policy.get("reuse_forbidden") is not True:
        fail("reason-code reuse must be forbidden")

    runtime_contracts = {
        name: {
            "version": entry["version"],
            "unknown_major_behavior": entry["unknown_major_behavior"],
        }
        for name, entry in contracts.items()
    }
    if RUNTIME_MANIFEST_VERSION != manifest_version:
        fail(f"installed runtime manifest version drift: {RUNTIME_MANIFEST_VERSION!r} != {manifest_version!r}")
    if RUNTIME_CONTRACTS != runtime_contracts:
        fail("installed runtime contract snapshot drifted from contract-versions.json")
    if RUNTIME_REASON_CODE_POLICY != reason_policy:
        fail("installed runtime reason-code policy drifted from contract-versions.json")

    policy_text = POLICY.read_text(encoding="utf-8")
    required_phrases = [
        "Unknown MAJOR version",
        "Reason-code stability",
        "Requirement-pack governance interaction",
        "migration note",
    ]
    for phrase in required_phrases:
        if phrase not in policy_text:
            fail(f"compatibility policy is missing required phrase: {phrase}")

    print("contract compatibility manifest and runtime snapshot: OK")


if __name__ == "__main__":
    main()
