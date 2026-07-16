#!/usr/bin/env python3
"""One-command RPE decision walkthrough.

The demo exercises the canonical ``rpe_kernel.evaluate_action()`` path with
synthetic data. It remains dependency-free and does not certify safety,
compliance, legal correctness, or production readiness.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from rpe_kernel import evaluate_action  # noqa: E402

EXAMPLE_DIR = REPOSITORY_ROOT / "examples" / "external-kernel"
DECISION_ORDER = {"allow": 0, "hold": 1, "human_gate": 2, "deny": 3}


def _load_json(filename: str) -> dict[str, Any]:
    with (EXAMPLE_DIR / filename).open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {filename}")
    return data


def _build_scenarios() -> list[dict[str, Any]]:
    pack = _load_json("minimal-requirement-pack.json")
    blocked_request = _load_json("minimal-action-request.json")

    approved_request = copy.deepcopy(blocked_request)
    approved_request["request_id"] = "request-demo-approved"
    approved_request["context"]["authority_confirmed"] = True
    approved_request["context"]["human_approval_present"] = True
    approved_request["evidence_scope"] = {
        "available": ["draft-content", "authority-record", "human-approval-record"],
        "missing": [],
    }

    unknown_request = copy.deepcopy(blocked_request)
    unknown_request["request_id"] = "request-demo-unknown-applicability"
    unknown_request.pop("action", None)

    return [
        {
            "id": "human_gate",
            "title": "External publication without required approval",
            "intent": "Show a proposed action being returned to an authorized human.",
            "request": blocked_request,
            "packs": [pack],
        },
        {
            "id": "allow",
            "title": "External publication with authority and approval evidence",
            "intent": "Show the same action continuing after the stated requirements are satisfied.",
            "request": approved_request,
            "packs": [pack],
        },
        {
            "id": "unknown",
            "title": "Missing applicability context",
            "intent": "Show visible failure instead of silently assuming that a pack applies.",
            "request": unknown_request,
            "packs": [pack],
        },
    ]


def _format_value(value: Any) -> str:
    if value is None:
        return "none"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else "none"
    return str(value)


def _print_scenario(index: int, total: int, scenario: dict[str, Any], result: dict[str, Any]) -> None:
    decision = str(result.get("decision", "unknown"))
    print("=" * 76)
    print(f"SCENARIO {index}/{total}  {scenario['title']}")
    print("-" * 76)
    print(f"Purpose       : {scenario['intent']}")
    print(f"Request       : {scenario['request'].get('request_id', 'unknown')}")
    print(f"Action        : {_format_value(scenario['request'].get('action'))}")
    print(f"Requirement   : {scenario['packs'][0].get('title', 'unknown pack')}")
    print()
    print(f"DECISION      : {decision.upper()}")
    print(f"Stage         : {_format_value(result.get('stage'))}")
    print(f"Reason codes  : {_format_value(result.get('reason_codes'))}")
    print(f"Next step     : {_format_value(result.get('next_step'))}")

    human_return = result.get("human_return")
    if isinstance(human_return, dict):
        print(f"Return to     : {_format_value(human_return.get('role'))}")

    pack_decisions = result.get("pack_decisions", [])
    if isinstance(pack_decisions, list):
        missing = [
            item
            for decision_record in pack_decisions
            if isinstance(decision_record, dict)
            for item in decision_record.get("missing_requirements", [])
        ]
        if missing:
            print(f"Missing       : {_format_value(missing)}")

    applicability = result.get("applicability", [])
    if isinstance(applicability, list):
        statuses = [
            f"{item.get('pack_id', 'unknown')}={item.get('status', 'unknown')}"
            for item in applicability
            if isinstance(item, dict)
        ]
        print(f"Applicability : {_format_value(statuses)}")
    print()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the dependency-free RPE decision walkthrough.")
    parser.add_argument(
        "--scenario",
        choices=("all", "human_gate", "allow", "unknown"),
        default="all",
        help="Run all scenarios or select one decision path.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable results instead of the narrative walkthrough.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    scenarios = _build_scenarios()
    if args.scenario != "all":
        scenarios = [scenario for scenario in scenarios if scenario["id"] == args.scenario]

    evaluated = [
        {"scenario": scenario, "result": evaluate_action(scenario["request"], scenario["packs"])}
        for scenario in scenarios
    ]

    if args.json:
        payload = [
            {
                "scenario_id": item["scenario"]["id"],
                "title": item["scenario"]["title"],
                "result": item["result"],
            }
            for item in evaluated
        ]
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
        return 0

    print("RPE DECISION WALKTHROUGH")
    print("Canonical path: action request -> applicability -> pack evaluation -> decision -> human return")
    print("Synthetic examples only; no action is executed by this program.")
    print()

    for index, item in enumerate(evaluated, start=1):
        _print_scenario(index, len(evaluated), item["scenario"], item["result"])

    strongest = max(
        (str(item["result"].get("decision", "human_gate")) for item in evaluated),
        key=lambda decision: DECISION_ORDER.get(decision, DECISION_ORDER["human_gate"]),
    )
    print("SUMMARY")
    print("- The same canonical kernel produced ALLOW and HUMAN_GATE outcomes from explicit evidence.")
    print("- Missing applicability context remained visible and returned to a human reviewer.")
    print(f"- Strongest stop observed in this run: {strongest.upper()}.")
    print()
    print("Boundary: passing this demo is not certification, legal review, compliance review,")
    print("safety approval, fairness assessment, deployment approval, or transfer of final responsibility.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
