#!/usr/bin/env python3
"""Evaluate one AI action request against multiple RPE requirement packs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DECISION_ORDER = {"allow": 0, "hold": 1, "human_gate": 2, "deny": 3}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def applies(pack: dict[str, Any], request: dict[str, Any]) -> bool:
    conditions = pack.get("applies_when", {})
    return all(request.get(key) == expected for key, expected in conditions.items())


def evaluate_pack(pack: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    pack_id = str(pack.get("pack_id", "unknown-pack"))
    if not applies(pack, request):
        return {"pack_id": pack_id, "applicable": False, "decision": "allow", "reason_codes": [], "missing_requirements": []}

    context = request.get("context", {})
    requirements = pack.get("requirements", [])
    missing = [name for name in requirements if context.get(name) is not True]
    decision = str(pack.get("decision_on_missing_requirement", "human_gate")) if missing else "allow"
    prefix = str(pack.get("reason_code_prefix", "RPE"))
    reasons = [f"{prefix}-MISSING-{name.replace('_', '-').upper()}" for name in missing]
    result: dict[str, Any] = {
        "pack_id": pack_id,
        "applicable": True,
        "decision": decision,
        "reason_codes": reasons,
        "missing_requirements": missing,
    }
    if decision != "allow":
        result["human_return"] = pack.get("human_return", {})
    return result


def combine(results: list[dict[str, Any]]) -> str:
    return max((str(item["decision"]) for item in results), key=lambda value: DECISION_ORDER.get(value, 2), default="allow")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("packs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    request = load_json(args.request)
    results = [evaluate_pack(load_json(path), request) for path in args.packs]
    output = {
        "request_id": request.get("request_id"),
        "combined_decision": combine(results),
        "pack_decisions": results,
        "non_claims": [
            "The result is a reference evaluation, not legal or compliance approval.",
            "Pack applicability and requirement quality still require human or institutional review."
        ],
    }
    rendered = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
