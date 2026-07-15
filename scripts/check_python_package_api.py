#!/usr/bin/env python3
"""Check the importable RPE Python package API."""

from __future__ import annotations

import json
from pathlib import Path

from rpe_kernel import evaluate_action

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "external-kernel"


def load(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def main() -> int:
    unresolved = evaluate_action(
        load("applicability-request.json"),
        [load("minimal-requirement-pack.json"), load("applicability-organization-pack.json")],
    )
    assert unresolved["stage"] == "applicability"
    assert unresolved["decision"] == "human_gate"

    resolved = evaluate_action(
        load("applicability-request-resolved.json"),
        [load("minimal-requirement-pack.json"), load("applicability-eu-pack.json"), load("applicability-organization-pack.json")],
    )
    assert resolved["stage"] == "evaluation"
    assert resolved["decision"] == "human_gate"
    assert len(resolved["pack_decisions"]) == 2
    print("Python package API checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
