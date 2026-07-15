#!/usr/bin/env python3
"""Check the pack applicability resolver against deterministic fixtures."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    command = [
        sys.executable,
        str(ROOT / "scripts/resolve_pack_applicability.py"),
        str(ROOT / "examples/external-kernel/applicability-request.json"),
        str(ROOT / "examples/external-kernel/minimal-requirement-pack.json"),
        str(ROOT / "examples/external-kernel/applicability-eu-pack.json"),
        str(ROOT / "examples/external-kernel/applicability-organization-pack.json"),
    ]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    result = json.loads(completed.stdout)

    statuses = {item["pack_id"]: item["status"] for item in result["resolutions"]}
    expected = {
        "rpe.synthetic.publication-gate.v0": "applicable",
        "rpe.synthetic.eu-publication.v0": "not_applicable",
        "rpe.synthetic.organization-publication.v0": "unknown",
    }
    if statuses != expected:
        raise AssertionError(f"unexpected statuses: {statuses!r}")
    if result["decision"] != "human_gate":
        raise AssertionError(f"unexpected decision: {result['decision']!r}")
    if result["next_step"] != "review_unknown_applicability":
        raise AssertionError(f"unexpected next step: {result['next_step']!r}")

    print("Pack applicability resolver check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
