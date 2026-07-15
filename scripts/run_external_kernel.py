#!/usr/bin/env python3
"""Minimal dependency-free RPE external-kernel reference evaluator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def evaluate(pack: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    applies_when = pack.get("applies_when", {})
    expected_action = applies_when.get("action")
    actual_action = request.get("action")

    if expected_action != actual_action:
        return {
            "request_id": request.get("request_id"),
            "pack_id": pack.get("pack_id"),
            "decision": "not_applicable",
            "reason_codes": ["RPE-PACK-NOT-APPLICABLE"],
            "missing_requirements": [],
            "human_return": None,
        }

    context = request.get("context", {})
    if not isinstance(context, dict):
        raise ValueError("request.context must be a JSON object")

    requirements = pack.get("requirements", [])
    if not isinstance(requirements, list) or not all(
        isinstance(item, str) for item in requirements
    ):
        raise ValueError("pack.requirements must be a list of strings")

    missing = [name for name in requirements if context.get(name) is not True]
    prefix = str(pack.get("reason_code_prefix", "RPE-GATE"))

    if missing:
        decision = str(pack.get("decision_on_missing_requirement", "human_gate"))
        reason_codes = [f"{prefix}-MISSING-{name.upper().replace('_', '-')}" for name in missing]
        human_return = pack.get("human_return")
    else:
        decision = "allow"
        reason_codes = [f"{prefix}-REQUIREMENTS-SATISFIED"]
        human_return = None

    return {
        "request_id": request.get("request_id"),
        "pack_id": pack.get("pack_id"),
        "decision": decision,
        "reason_codes": reason_codes,
        "missing_requirements": missing,
        "human_return": human_return,
        "evidence_scope": request.get("evidence_scope", {}),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate one synthetic AI action request against one RPE requirement pack."
    )
    parser.add_argument("pack", type=Path)
    parser.add_argument("request", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        decision = evaluate(load_json(args.pack), load_json(args.request))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"error: {exc}\n")

    rendered = json.dumps(decision, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
