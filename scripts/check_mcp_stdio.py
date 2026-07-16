#!/usr/bin/env python3
"""Exercise the bounded MCP stdio message handler."""

from __future__ import annotations

from rpe_kernel.mcp_server import TOOL_NAME, handle_message


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    initialized = handle_message({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {"protocolVersion": "2025-11-25"},
    })
    require(initialized is not None, "initialize returned no response")
    require(initialized["result"]["capabilities"]["tools"] == {"listChanged": False}, "tool capability mismatch")

    listed = handle_message({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    require(listed is not None, "tools/list returned no response")
    require(listed["result"]["tools"][0]["name"] == TOOL_NAME, "tool name mismatch")

    request = {
        "request_id": "mcp-check-001",
        "action": "publish_release",
        "context": {},
    }
    pack = {
        "pack_id": "mcp-check-pack",
        "applies_when": {"action": "publish_release"},
        "requirements": ["human_review_completed"],
        "decision_on_missing_requirement": "human_gate",
        "reason_code_prefix": "RPE-MCP-CHECK",
        "human_return": {"role": "release_owner"},
    }
    called = handle_message({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {"name": TOOL_NAME, "arguments": {"request": request, "packs": [pack]}},
    })
    require(called is not None, "tools/call returned no response")
    structured = called["result"]["structuredContent"]
    require(structured["decision"] == "human_gate", "unexpected kernel decision")
    require(structured["request_id"] == "mcp-check-001", "request id not preserved")
    require(
        structured["reason_codes"] == ["RPE-MCP-CHECK-MISSING-HUMAN-REVIEW-COMPLETED"],
        "reason code mismatch",
    )

    invalid = handle_message({
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {"name": TOOL_NAME, "arguments": {"request": {}, "packs": "bad"}},
    })
    require(invalid is not None and invalid["error"]["code"] == -32602, "invalid params were not rejected")
    print("PASS: MCP stdio adapter checks completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
