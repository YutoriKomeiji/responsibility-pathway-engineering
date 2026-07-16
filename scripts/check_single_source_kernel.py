#!/usr/bin/env python3
"""Guard the RPE decision kernel against adapter-level implementation drift."""

from __future__ import annotations

import ast
import json
from pathlib import Path

from rpe_kernel.mcp_server import TOOL_NAME, handle_message
from rpe_kernel.pipeline import evaluate_action

ROOT = Path(__file__).resolve().parents[1]
KERNEL_DIR = ROOT / "rpe_kernel"

CANONICAL_DEFINITIONS = {
    "evaluate_action": KERNEL_DIR / "pipeline.py",
    "evaluate_pack": KERNEL_DIR / "evaluation.py",
    "combine_decisions": KERNEL_DIR / "evaluation.py",
    "resolve_pack": KERNEL_DIR / "applicability.py",
}

ADAPTERS = [
    KERNEL_DIR / "http_api.py",
    KERNEL_DIR / "mcp_server.py",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def function_definitions(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def check_canonical_definitions() -> None:
    python_files = sorted(KERNEL_DIR.glob("*.py"))
    for function_name, canonical_path in CANONICAL_DEFINITIONS.items():
        defining_files = [path for path in python_files if function_name in function_definitions(path)]
        require(
            defining_files == [canonical_path],
            f"{function_name} must be defined only in {canonical_path.relative_to(ROOT)}; found "
            + ", ".join(str(path.relative_to(ROOT)) for path in defining_files),
        )


def check_adapters_delegate() -> None:
    for path in ADAPTERS:
        text = path.read_text(encoding="utf-8")
        require("from .pipeline import evaluate_action" in text, f"{path.relative_to(ROOT)} must import evaluate_action")
        require("evaluate_action(" in text, f"{path.relative_to(ROOT)} must delegate to evaluate_action")
        require("DECISION_ORDER" not in text, f"{path.relative_to(ROOT)} must not define decision precedence")
        require("resolve_pack(" not in text, f"{path.relative_to(ROOT)} must not resolve applicability directly")
        require("evaluate_pack(" not in text, f"{path.relative_to(ROOT)} must not evaluate packs directly")


def fixture() -> tuple[dict[str, object], list[dict[str, object]]]:
    request = {
        "request_id": "single-source-check-001",
        "action": "publish_release",
        "context": {},
    }
    packs = [{
        "pack_id": "single-source-pack",
        "applies_when": {"action": "publish_release"},
        "requirements": ["human_review_completed"],
        "decision_on_missing_requirement": "human_gate",
        "reason_code_prefix": "RPE-SINGLE-SOURCE",
        "human_return": {"role": "release_owner"},
    }]
    return request, packs


def check_mcp_parity() -> None:
    request, packs = fixture()
    direct = evaluate_action(request, packs)
    response = handle_message({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": TOOL_NAME,
            "arguments": {"request": request, "packs": packs},
        },
    })
    require(response is not None, "MCP adapter returned no response")
    via_mcp = response["result"]["structuredContent"]
    require(via_mcp == direct, "MCP result drifted from direct package API")
    require(json.loads(response["result"]["content"][0]["text"]) == direct, "MCP text result drifted")


def main() -> int:
    check_canonical_definitions()
    check_adapters_delegate()
    check_mcp_parity()
    print("PASS: all runtime adapters delegate to the single RPE kernel source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
