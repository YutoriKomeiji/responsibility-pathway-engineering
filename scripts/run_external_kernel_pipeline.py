#!/usr/bin/env python3
"""Resolve requirement-pack applicability and evaluate applicable packs in one run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from resolve_pack_applicability import load_json, resolve_pack
from run_external_kernel_multi import combine, evaluate_pack


def run_pipeline(request_path: Path, pack_paths: list[Path]) -> dict[str, Any]:
    request = load_json(request_path)
    loaded_packs = [(path, load_json(path)) for path in pack_paths]
    resolutions = [resolve_pack(pack, request, path) for path, pack in loaded_packs]

    unknown = [item for item in resolutions if item["status"] == "unknown"]
    applicable_ids = {
        item["pack_id"] for item in resolutions if item["status"] == "applicable"
    }

    if unknown:
        return {
            "request_id": request.get("request_id"),
            "decision": "human_gate",
            "stage": "applicability",
            "reason_codes": sorted(
                {code for item in unknown for code in item["reason_codes"]}
            ),
            "applicability": resolutions,
            "pack_decisions": [],
            "human_return": {"role": "applicability_review_owner"},
            "next_step": "review_unknown_applicability",
        }

    applicable_packs = [
        pack for _, pack in loaded_packs if str(pack.get("pack_id")) in applicable_ids
    ]
    if not applicable_packs:
        return {
            "request_id": request.get("request_id"),
            "decision": "human_gate",
            "stage": "applicability",
            "reason_codes": ["RPE-APPLICABILITY-NO-APPLICABLE-PACKS"],
            "applicability": resolutions,
            "pack_decisions": [],
            "human_return": {"role": "applicability_review_owner"},
            "next_step": "confirm_requirement_pack_selection",
        }

    pack_decisions = [evaluate_pack(pack, request) for pack in applicable_packs]
    return {
        "request_id": request.get("request_id"),
        "decision": combine(pack_decisions),
        "stage": "evaluation",
        "reason_codes": sorted(
            {code for item in pack_decisions for code in item.get("reason_codes", [])}
        ),
        "applicability": resolutions,
        "pack_decisions": pack_decisions,
        "human_return": next(
            (item.get("human_return") for item in pack_decisions if item.get("human_return")),
            None,
        ),
        "next_step": "return_to_human" if combine(pack_decisions) != "allow" else "proceed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("packs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    output = run_pipeline(args.request, args.packs)
    rendered = json.dumps(output, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
