#!/usr/bin/env python3
"""Exercise the bounded MCP stdio message handler."""

from __future__ import annotations

import json
from pathlib import Path

from rpe_kernel.mcp_server import (
    GOVERNED_TOOL_NAME,
    GUARDED_TRANSITION_TOOL_NAME,
    TOOL_NAME,
    TRANSITION_TOOL_NAME,
    handle_message,
)

ROOT = Path(__file__).resolve().parents[1]
GOVERNED_FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    initialized = handle_message({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25"}})
    require(initialized is not None, "initialize returned no response")
    require(initialized["result"]["capabilities"]["tools"] == {"listChanged": False}, "tool capability mismatch")
    instructions = initialized["result"]["instructions"]
    require("execution" in instructions and "final responsibility" in instructions, "MCP responsibility boundary missing")

    listed = handle_message({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    require(listed is not None, "tools/list returned no response")
    names = [tool["name"] for tool in listed["result"]["tools"]]
    require(names == [TOOL_NAME, GOVERNED_TOOL_NAME, TRANSITION_TOOL_NAME, GUARDED_TRANSITION_TOOL_NAME], "tool list mismatch")

    request = {"request_id": "mcp-check-001", "action": "publish_release", "context": {}}
    pack = {"pack_id": "mcp-check-pack", "applies_when": {"action": ["publish_release"]}, "requirements": ["human_review_completed"], "decision_on_missing_requirement": "human_gate", "reason_code_prefix": "RPE-MCP-CHECK", "human_return": {"role": "release_owner"}}
    called = handle_message({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": TOOL_NAME, "arguments": {"request": request, "packs": [pack]}}})
    require(called is not None, "tools/call returned no response")
    structured = called["result"]["structuredContent"]
    require(structured["decision"] == "human_gate", "unexpected kernel decision")

    governed_payload = json.loads(GOVERNED_FIXTURE.read_text(encoding="utf-8"))
    governed_called = handle_message({"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": GOVERNED_TOOL_NAME, "arguments": governed_payload}})
    require(governed_called is not None, "governed tools/call returned no response")
    governed = governed_called["result"]["structuredContent"]
    require(governed["decision"] == "allow", "unexpected governed decision")
    require(governed["responsibility_handoff"]["authority_effect"] == "none", "authority effect mismatch")

    transition_payload = {"contract_version": "0.1.0-exp", "governed_evaluation": governed_payload, "risk_graph": {"conditions": [{"condition_id": "authority_scope_mismatch", "status": "triggered", "required_controls": ["require_authority"]}]}, "constraints": ["no_delegation"]}
    transitioned = handle_message({"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": TRANSITION_TOOL_NAME, "arguments": transition_payload}})
    require(transitioned is not None, "transition tools/call returned no response")
    transition = transitioned["result"]["structuredContent"]
    require(transition["transition_result"]["control_action"] == "require_authority", "unexpected transition control")
    require(transition["transition_result"]["authority_effect"] == "none", "transition created authority")
    require(transition["transition_result"]["execution_effect"] == "none", "transition claimed execution")

    guarded_payload = {
        "contract_version": "0.2.0-exp",
        "governed_evaluation": governed_payload,
        "integrity_checks": [{"check": {"check_id": "cfg", "kind": "configuration", "expected": {"configuration_id": "a"}, "observed": {"configuration_id": "b"}}, "required_controls": ["require_authority"]}],
        "human_return_checks": [{"check": {"return_id": "review", "owner_role": "review_owner", "authority_reference": "auth", "capability_status": "available", "response_window_status": "available", "next_decision_scope": "bounded_review", "evidence_scope": {"available": ["request"], "missing": []}}, "required_controls": ["require_authority"]}],
    }
    guarded_called = handle_message({"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": GUARDED_TRANSITION_TOOL_NAME, "arguments": guarded_payload}})
    require(guarded_called is not None, "guarded tools/call returned no response")
    guarded = guarded_called["result"]["structuredContent"]
    require(guarded["contract_version"] == "0.2.0-exp", "guarded contract version mismatch")
    require(guarded["guard_observations"]["integrity_results"][0]["status"] == "triggered", "guarded integrity observation missing")
    require(guarded["guard_observations"]["integrity_results"][0]["independent_authentication_claim"] is False, "guarded adapter inflated authentication")
    require(guarded["guard_observations"]["human_return_results"][0]["authority_validity_claim"] is False, "guarded adapter inflated authority validity")
    require(guarded["transition_result"]["control_action"] == "require_authority", "guarded control mismatch")
    require(guarded["authority_effect"] == "none" and guarded["execution_effect"] == "none", "guarded adapter created effect")

    invalid_guarded = handle_message({"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": GUARDED_TRANSITION_TOOL_NAME, "arguments": {"contract_version": "0.2.0-exp", "governed_evaluation": governed_payload, "dispatch_now": True}}})
    require(invalid_guarded is not None, "invalid guarded transition returned no response")
    held = invalid_guarded["result"]["structuredContent"]["transition_result"]
    require(held["control_action"] == "hold", "guarded unknown field was not fail-closed")

    invalid = handle_message({"jsonrpc": "2.0", "id": 8, "method": "tools/call", "params": {"name": TOOL_NAME, "arguments": {"request": {}, "packs": "bad"}}})
    require(invalid is not None and invalid["error"]["code"] == -32602, "invalid params were not rejected")
    print("PASS: MCP stdio adapter checks completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
