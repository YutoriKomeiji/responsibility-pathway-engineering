"""Minimal JSON-RPC stdio adapter exposing RPE evaluation tools."""

from __future__ import annotations

import json
import sys
from typing import Any, TextIO

from .gateway import evaluate_gateway_request
from .guarded_adapter import evaluate_guarded_adapter_request
from .pipeline import evaluate_action, evaluate_governed_action

JsonObject = dict[str, Any]
TOOL_NAME = "rpe_evaluate_action"
GOVERNED_TOOL_NAME = "rpe_evaluate_governed_action"
TRANSITION_TOOL_NAME = "rpe_evaluate_responsibility_transition"
GUARDED_TRANSITION_TOOL_NAME = "rpe_evaluate_guarded_responsibility_transition"
PROTOCOL_VERSION = "2025-11-25"

TOOL: JsonObject = {
    "name": TOOL_NAME,
    "description": "Evaluate a proposed action through the legacy/M1-compatible RPE path without executing it.",
    "inputSchema": {"type": "object", "required": ["request", "packs"], "properties": {"request": {"type": "object"}, "packs": {"type": "array", "items": {"type": "object"}}}, "additionalProperties": False},
}
GOVERNED_TOOL: JsonObject = {
    "name": GOVERNED_TOOL_NAME,
    "description": "Evaluate a strict governed RPE envelope without executing it or granting operational authority.",
    "inputSchema": {"type": "object", "required": ["contract_version", "request", "governed_packs"], "properties": {"contract_version": {"type": "string"}, "request": {"type": "object"}, "governed_packs": {"type": "array", "items": {"type": "object"}}}, "additionalProperties": False},
}
TRANSITION_TOOL: JsonObject = {
    "name": TRANSITION_TOOL_NAME,
    "description": "Evaluate an experimental M3 responsibility transition through the strict governed M2 baseline without dispatch, authority creation, external-effect verification, or runtime recovery ownership.",
    "inputSchema": {"type": "object", "required": ["contract_version", "governed_evaluation"], "properties": {"contract_version": {"const": "0.1.0-exp"}, "governed_evaluation": {"type": "object"}, "risk_graph": {"type": ["object", "null"]}, "requested_route": {"type": ["object", "null"]}, "constraints": {"type": "array", "items": {"type": "string"}}}, "additionalProperties": False},
}
GUARDED_TRANSITION_TOOL: JsonObject = {
    "name": GUARDED_TRANSITION_TOOL_NAME,
    "description": "Evaluate the experimental 0.2 guarded responsibility transition with caller-observed integrity and Human Return readiness evidence. It does not authenticate identities, certify humans, create authority, or execute actions.",
    "inputSchema": {
        "type": "object",
        "required": ["contract_version", "governed_evaluation"],
        "properties": {
            "contract_version": {"const": "0.2.0-exp"},
            "governed_evaluation": {"type": "object"},
            "risk_graph": {"type": ["object", "null"]},
            "integrity_checks": {"type": "array", "items": {"type": "object"}},
            "human_return_checks": {"type": "array", "items": {"type": "object"}},
            "requested_route": {"type": ["object", "null"]},
            "constraints": {"type": "array", "items": {"type": "string"}},
        },
        "additionalProperties": False,
    },
}


def rpc_result(request_id: Any, value: JsonObject) -> JsonObject:
    return {"jsonrpc": "2.0", "id": request_id, "result": value}


def rpc_error(request_id: Any, code: int, message: str) -> JsonObject:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def _tool_result(decision: JsonObject) -> JsonObject:
    return {"content": [{"type": "text", "text": json.dumps(decision, ensure_ascii=False, sort_keys=True)}], "structuredContent": decision, "isError": False}


def handle_message(message: JsonObject) -> JsonObject | None:
    request_id = message.get("id")
    method = message.get("method")
    params = message.get("params", {})
    if message.get("jsonrpc") != "2.0" or not isinstance(method, str):
        return rpc_error(request_id, -32600, "Invalid Request")
    if method.startswith("notifications/"):
        return None
    if method == "ping":
        return rpc_result(request_id, {})
    if method == "initialize":
        requested = params.get("protocolVersion") if isinstance(params, dict) else None
        return rpc_result(request_id, {"protocolVersion": requested or PROTOCOL_VERSION, "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "rpe-kernel", "version": "0.1.0"}, "instructions": "This server evaluates proposals and responsibility transitions only; callers retain approval, routing, execution, external-effect verification, repair, resume, and final responsibility."})
    if method == "tools/list":
        return rpc_result(request_id, {"tools": [TOOL, GOVERNED_TOOL, TRANSITION_TOOL, GUARDED_TRANSITION_TOOL]})
    if method == "tools/call":
        if not isinstance(params, dict):
            return rpc_error(request_id, -32602, "Unknown tool or invalid params")
        tool_name = params.get("name")
        arguments = params.get("arguments")
        if not isinstance(arguments, dict):
            return rpc_error(request_id, -32602, "Tool arguments must be an object")
        if tool_name == GOVERNED_TOOL_NAME:
            return rpc_result(request_id, _tool_result(evaluate_governed_action(arguments)))
        if tool_name == TRANSITION_TOOL_NAME:
            return rpc_result(request_id, _tool_result(evaluate_gateway_request(arguments)))
        if tool_name == GUARDED_TRANSITION_TOOL_NAME:
            return rpc_result(request_id, _tool_result(evaluate_guarded_adapter_request(arguments)))
        if tool_name != TOOL_NAME:
            return rpc_error(request_id, -32602, "Unknown tool or invalid params")
        request = arguments.get("request")
        packs = arguments.get("packs")
        if not isinstance(request, dict) or not isinstance(packs, list) or not all(isinstance(pack, dict) for pack in packs):
            return rpc_error(request_id, -32602, "request must be an object and packs must be an array of objects")
        return rpc_result(request_id, _tool_result(evaluate_action(request, packs)))
    return rpc_error(request_id, -32601, "Method not found")


def serve(stdin: TextIO = sys.stdin, stdout: TextIO = sys.stdout) -> None:
    for line in stdin:
        if not line.strip():
            continue
        try:
            payload = json.loads(line)
            response = handle_message(payload) if isinstance(payload, dict) else rpc_error(None, -32600, "Invalid Request")
        except json.JSONDecodeError:
            response = rpc_error(None, -32700, "Parse error")
        if response is not None:
            stdout.write(json.dumps(response, ensure_ascii=False, sort_keys=True) + "\n")
            stdout.flush()


def main() -> None:
    serve()


if __name__ == "__main__":
    main()
