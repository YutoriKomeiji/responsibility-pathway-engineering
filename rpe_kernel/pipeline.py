"""Composable Python API for applicability resolution and evaluation."""

from __future__ import annotations

from typing import Any, Sequence

from .applicability import resolve_pack
from .evaluation import combine_decisions, evaluate_pack


def evaluate_action(request: dict[str, Any], packs: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Resolve applicability, evaluate applicable packs, and return one structured result."""
    resolutions = [resolve_pack(pack, request, str(pack.get("pack_id", index))) for index, pack in enumerate(packs)]
    unknown_ids = [item["pack_id"] for item in resolutions if item["status"] == "unknown"]
    applicable_indexes = [index for index, item in enumerate(resolutions) if item["status"] == "applicable"]

    if unknown_ids:
        return {
            "request_id": request.get("request_id"),
            "decision": "human_gate",
            "stage": "applicability",
            "reason_codes": ["RPE-APPLICABILITY-UNKNOWN"],
            "applicability": resolutions,
            "pack_decisions": [],
            "human_return": {"role": "applicability_review_owner"},
            "next_step": "review_unknown_applicability",
        }

    if not applicable_indexes:
        return {
            "request_id": request.get("request_id"),
            "decision": "human_gate",
            "stage": "applicability",
            "reason_codes": ["RPE-APPLICABILITY-NO-APPLICABLE-PACKS"],
            "applicability": resolutions,
            "pack_decisions": [],
            "human_return": {"role": "applicability_review_owner"},
            "next_step": "select_or_review_requirement_packs",
        }

    decisions = [evaluate_pack(packs[index], request) for index in applicable_indexes]
    combined = combine_decisions(decisions)
    human_returns = [item.get("human_return") for item in decisions if item.get("human_return")]
    return {
        "request_id": request.get("request_id"),
        "decision": combined,
        "stage": "evaluation",
        "reason_codes": [code for item in decisions for code in item["reason_codes"]],
        "applicability": resolutions,
        "pack_decisions": decisions,
        "human_return": human_returns[0] if human_returns else None,
        "next_step": "continue_action" if combined == "allow" else "return_to_human",
    }
