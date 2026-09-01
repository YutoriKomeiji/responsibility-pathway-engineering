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

## Implemented protocol surface

The reference adapter handles:

- `initialize`;
- `notifications/*` without a response;
- `ping`;
- `tools/list`;
- `tools/call`.

It exposes no autonomous execution capability.

## Boundary

This adapter evaluates proposed actions only. It does not execute the requested action, merge code, publish releases, approve policy or legal applicability, verify external effects, grant repair/resume authority, or transfer responsibility to an AI system.

The stdio launcher is a local reference integration. Production hosts must separately review executable-path trust, environment isolation, client permissions, logging, dependency provenance, transport security, authentication/authorization, and operational ownership.
