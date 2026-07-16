"""Minimal JSON-RPC stdio adapter exposing the RPE evaluator as one MCP tool."""

from __future__ import annotations

import json
import sys
from typing import Any, TextIO

from .pipeline import evaluate_action

JsonObject = dict[str, Any]
TOOL_NAME = "rpe_evaluate_action"
PROTOCOL_VERSION = "2025-11-25"

TOOL: JsonObject = {
    "name": TOOL_NAME,
    "description": "Evaluate a proposed action through RPE without executing it.",
    "inputSchema": {
        "type": "object",
        "required": ["request", "packs"],
        "properties": {
            "request": {"type": "object"},
            "packs": {"type": "array", "items": {"type": "object"}},
        },
        "additionalProperties": False,
    },
}


def rpc_result(request_id: Any, value: JsonObject) -> JsonObject:
    return {"jsonrpc": "2.0", "id": request_id, "result": value}


def rpc_error(request_id: Any, code: int, message: str) -> JsonObject:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


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
        return rpc_result(request_id, {
            "protocolVersion": requested or PROTOCOL_VERSION,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "rpe-kernel", "version": "0.1.0"},
            "instructions": "This server evaluates proposals only; callers retain approval and execution responsibility.",
        })
    if method == "tools/list":
        return rpc_result(request_id, {"tools": [TOOL]})
    if method == "tools/call":
        if not isinstance(params, dict) or params.get("name") != TOOL_NAME:
            return rpc_error(request_id, -32602, "Unknown tool or invalid params")
        arguments = params.get("arguments")
        if not isinstance(arguments, dict):
            return rpc_error(request_id, -32602, "Tool arguments must be an object")
        request = arguments.get("request")
        packs = arguments.get("packs")
        if not isinstance(request, dict) or not isinstance(packs, list) or not all(isinstance(pack, dict) for pack in packs):
            return rpc_error(request_id, -32602, "request must be an object and packs must be an array of objects")
        decision = evaluate_action(request, packs)
        return rpc_result(request_id, {
            "content": [{"type": "text", "text": json.dumps(decision, ensure_ascii=False, sort_keys=True)}],
            "structuredContent": decision,
            "isError": False,
        })
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
