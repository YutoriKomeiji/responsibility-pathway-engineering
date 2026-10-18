#!/usr/bin/env python3
"""Show identical M3 guarded I/O across Python, loopback REST and MCP stdio.

No external action, authority grant, payment, or non-loopback connection occurs.
This is an executable interoperability contract, not a production deployment.
"""

from __future__ import annotations

import argparse
import copy
import io
import json
import threading
import urllib.request
from datetime import date, timedelta
from http.server import ThreadingHTTPServer
from pathlib import Path

from rpe_kernel.guarded_adapter import evaluate_guarded_adapter_request
from rpe_kernel.http_api import create_handler
from rpe_kernel.mcp_server import GUARDED_TRANSITION_TOOL_NAME, serve

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples/external-kernel/minimal-governed-evaluation-request.json"


def _cases() -> dict[str, dict]:
    approved = json.loads(FIXTURE.read_text(encoding="utf-8"))
    governance = approved["governed_packs"][0]["governance"]
    # The demo exercises admission without coupling its outcome to a stale
    # fixed review date. It makes no claim about production pack authority.
    governance["last_reviewed"] = (date.today() - timedelta(days=1)).isoformat()
    governance["next_review_due"] = (date.today() + timedelta(days=365)).isoformat()

    def guarded(governed: dict, graph: dict | None = None) -> dict:
        return {
            "contract_version": "0.2.0-exp",
            "governed_evaluation": governed,
            "risk_graph": graph if graph is not None else {"conditions": []},
        }

    missing = copy.deepcopy(approved)
    missing["request"]["context"]["human_approval_present"] = False
    missing["request"]["evidence_scope"] = {"available": [], "missing": ["approval-record"]}
    mismatch = {
        "conditions": [{
            "condition_id": "trusted_upstream_mismatch_observed",
            "status": "triggered",
            "required_controls": ["require_authority"],
            "evidence_refs": ["caller_supplied_comparison"],
        }]
    }
    return {
        "approved": guarded(copy.deepcopy(approved)),
        "missing_approval": guarded(missing),
        "caller_flagged_mismatch": guarded(copy.deepcopy(approved), mismatch),
        "invalid_graph_envelope": guarded(copy.deepcopy(approved), {"conditions": [], "dispatch_now": True}),
    }


def _mcp_stdio(payload: dict) -> dict:
    msg = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": GUARDED_TRANSITION_TOOL_NAME, "arguments": payload},
    }
    stdin = io.StringIO(json.dumps(msg, ensure_ascii=False) + "\n")
    stdout = io.StringIO()
    serve(stdin, stdout)
    records = [json.loads(line) for line in stdout.getvalue().splitlines()]
    assert len(records) == 1 and records[0].get("id") == 1, records
    rpc = records[0]
    assert "error" not in rpc, rpc
    value = rpc["result"]["structuredContent"]
    assert json.loads(rpc["result"]["content"][0]["text"]) == value
    return value


def _rest_loopback(url: str, payload: dict) -> dict:
    request = urllib.request.Request(
        url, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(request, timeout=5) as response:
        assert response.status == 200
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable cases and observed results")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", 0), create_handler())
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    records = {}
    try:
        url = f"http://127.0.0.1:{server.server_port}/v1/evaluate/transition/guarded"
        for name, payload in _cases().items():
            python_result = evaluate_guarded_adapter_request(payload)
            rest_result = _rest_loopback(url, payload)
            mcp_result = _mcp_stdio(payload)
            assert python_result == rest_result == mcp_result, name
            transition = python_result["transition_result"]
            observed = {
                "m2_decision": python_result["evaluation_result"]["decision"] if python_result["evaluation_result"] else None,
                "m3_control_action": transition["control_action"],
                "reason_codes": transition["reason_codes"],
                "unmet_conditions": transition["unmet_conditions"],
                "authority_effect": python_result["authority_effect"],
                "execution_effect": python_result["execution_effect"],
                "downstream_executor_required": transition["downstream_executor_required"],
            }
            assert observed["authority_effect"] == "none"
            assert observed["execution_effect"] == "none"
            assert observed["downstream_executor_required"] is True
            records[name] = {"request": payload, "observed": observed, "all_surfaces_equal": True}
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()

    assert records["approved"]["observed"]["m3_control_action"] == "allow", records["approved"]
    assert records["missing_approval"]["observed"]["m3_control_action"] != "allow", records["missing_approval"]
    assert records["caller_flagged_mismatch"]["observed"]["m3_control_action"] == "require_authority", records["caller_flagged_mismatch"]
    assert records["invalid_graph_envelope"]["observed"]["m3_control_action"] == "hold", records["invalid_graph_envelope"]

    if args.json:
        print(json.dumps({
            "contract": "0.2.0-exp",
            "surfaces": ["python", "rest_loopback", "mcp_stdio"],
            "cases": records,
            "external_action_executed": False,
            "evidence_scope": "synthetic_reference_adapters_only",
        }, ensure_ascii=False, sort_keys=True))
    else:
        for name, record in records.items():
            result = record["observed"]
            print(f"{name}: M2={result['m2_decision']} M3={result['m3_control_action']}; Python=REST=MCP")
        print("M3 cross-surface I/O parity passed; no external action executed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
