# MCP stdio adapter

RPE includes a bounded reference adapter that exposes the kernel as Model Context Protocol tools over standard input and output.

## Start

```bash
python -m pip install .
rpe-mcp
```

Example client configuration:

```json
{
  "mcpServers": {
    "rpe-kernel": {
      "command": "rpe-mcp",
      "args": []
    }
  }
}
```

## Tools

### `rpe_evaluate_action`

Legacy/M1-compatible evaluation. Accepts:

- `request`: an RPE Action Request object;
- `packs`: an array of RPE Requirement Pack objects.

It delegates to `rpe_kernel.evaluate_action()`.

### `rpe_evaluate_governed_action`

Strict governed M2 evaluation. Accepts a governed evaluation envelope and delegates to `rpe_kernel.evaluate_governed_action()`.

Governed responses preserve the strict admission/compatibility/governance/applicability/evaluation stages plus the responsibility handoff with:

- `authority_effect = none`;
- `decision_scope = evaluation_only`.

The textual MCP content mirrors the structured result for clients that do not consume `structuredContent`.

## M3 guarded tool (experimental Draft only)

Draft PR #127 adds `rpe_evaluate_guarded_responsibility_transition` with `0.2.0-exp` guarded input in `tools/call.arguments`. It returns `structuredContent` and equivalent JSON text; the response is evaluation metadata, never an authorization token. For valid requests, adverse cases and host enforcement requirements see [M3 integration/operator guide](../m3-integration-operator-guide.md). This additional tool is not yet part of the merged M2 baseline.

## Implemented protocol surface

The reference adapter handles:

- `initialize`;
- `notifications/*` without a response;
- `ping`;
- `tools/list`;
- `tools/call`.

It exposes no autonomous execution capability.

## Transport/input security boundary

Each newline-delimited JSON-RPC message is limited to **1,048,576 bytes
(1 MiB)**, including framing whitespace. An oversized line is discarded
through its terminating newline; a subsequent valid request is processed.
Ambiguous duplicate JSON keys at any nesting level and non-finite JSON
constants are rejected. Invalid tool arguments and evaluator exceptions
produce bounded JSON-RPC errors rather than terminating the stdio server or
printing exception details to a model client.

The reference server is not a hardened sandbox: size limits are per message,
not a global concurrency or CPU quota; the caller remains responsible for
process isolation, request rate and tool-call budgets, trusted launch path,
secret separation, and verifying that its downstream executor enforces RPE's
machine-readable decisions. No authentication or identity proof is created by
the stdio transport.

## Boundary

This adapter evaluates proposed actions only. It does not execute the requested action, merge code, publish releases, approve policy or legal applicability, verify external effects, grant repair/resume authority, or transfer responsibility to an AI system.

The stdio launcher is a local reference integration. Production hosts must separately review executable-path trust, environment isolation, client permissions, logging, dependency provenance, transport security, authentication/authorization, and operational ownership.
