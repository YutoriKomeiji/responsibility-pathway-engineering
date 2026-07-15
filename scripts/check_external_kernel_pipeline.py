#!/usr/bin/env python3
"""Check the one-shot external-kernel applicability and evaluation pipeline."""

from pathlib import Path

from run_external_kernel_pipeline import run_pipeline

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "external-kernel"
PACKS = [
    EXAMPLES / "minimal-requirement-pack.json",
    EXAMPLES / "applicability-eu-pack.json",
    EXAMPLES / "applicability-organization-pack.json",
]


def main() -> int:
    unresolved = run_pipeline(EXAMPLES / "applicability-request.json", PACKS)
    assert unresolved["decision"] == "human_gate"
    assert unresolved["stage"] == "applicability"
    assert unresolved["pack_decisions"] == []
    assert unresolved["next_step"] == "review_unknown_applicability"

    resolved = run_pipeline(EXAMPLES / "applicability-request-resolved.json", PACKS)
    assert resolved["decision"] == "human_gate"
    assert resolved["stage"] == "evaluation"
    assert len(resolved["pack_decisions"]) == 2
    assert resolved["next_step"] == "return_to_human"

    print("external kernel pipeline checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
