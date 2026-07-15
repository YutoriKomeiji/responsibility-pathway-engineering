#!/usr/bin/env python3
"""Resolve candidate RPE requirement packs before multi-pack evaluation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

APPLICABILITY_FIELDS = ("action", "jurisdiction", "organization", "data_class")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def request_value(request: dict[str, Any], field: str) -> Any:
    if field == "action":
        return request.get("action")
    context = request.get("applicability_context", {})
    return context.get(field) if isinstance(context, dict) else None


def resolve_pack(pack: dict[str, Any], request: dict[str, Any], path: Path) -> dict[str, Any]:
    pack_id = str(pack.get("pack_id", "unknown-pack"))
    conditions = pack.get("applies_when", {})
    if not isinstance(conditions, dict):
        conditions = {}

    missing_context: list[str] = []
    mismatches: list[dict[str, Any]] = []
    matched: list[str] = []

    for field in APPLICABILITY_FIELDS:
        if field not in conditions:
            continue
        expected = conditions[field]
        observed = request_value(request, field)
        if observed is None:
            missing_context.append(field)
        elif observed != expected:
            mismatches.append({"field": field, "expected": expected, "observed": observed})
        else:
            matched.append(field)

    if mismatches:
        status = "not_applicable"
        reason_codes = ["RPE-APPLICABILITY-CONDITION-MISMATCH"]
    elif missing_context:
        status = "unknown"
        reason_codes = [f"RPE-APPLICABILITY-MISSING-{field.replace('_', '-').upper()}" for field in missing_context]
    else:
        status = "applicable"
        reason_codes = ["RPE-APPLICABILITY-CONDITIONS-MATCHED"]

    return {
        "pack_id": pack_id,
        "pack_path": str(path),
        "status": status,
        "matched_fields": matched,
        "missing_context": missing_context,
        "mismatches": mismatches,
        "reason_codes": reason_codes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("packs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    request = load_json(args.request)
    resolutions = [resolve_pack(load_json(path), request, path) for path in args.packs]
    applicable = [item["pack_path"] for item in resolutions if item["status"] == "applicable"]
    unknown = [item["pack_path"] for item in resolutions if item["status"] == "unknown"]

    output = {
        "request_id": request.get("request_id"),
        "decision": "human_gate" if unknown else "allow_to_evaluate",
        "applicable_pack_paths": applicable,
        "unknown_pack_paths": unknown,
        "resolutions": resolutions,
        "human_return": {"role": "applicability_review_owner"} if unknown else None,
        "next_step": "review_unknown_applicability" if unknown else "run_multi_pack_evaluator",
    }
    rendered = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
