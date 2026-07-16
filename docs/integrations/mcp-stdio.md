# MCP stdio adapter

RPE includes a bounded reference adapter that exposes the kernel as one Model Context Protocol tool over standard input and output.

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

## Tool

`rpe_evaluate_action` accepts:

- `request`: an RPE Action Request object
- `packs`: an array of RPE Requirement Pack objects

It returns the same structured decision produced by `rpe_kernel.evaluate_action()`:

- `allow`
- `hold`
- `human_gate`
- `deny`

The textual MCP content mirrors the structured result for clients that do not consume `structuredContent`.

## Implemented protocol surface

The reference adapter handles:

- `initialize`
- `notifications/*` without a response
- `ping`
- `tools/list`
- `tools/call`

It exposes no resources, prompts, sampling, roots, or autonomous execution capability.

## Boundary

This adapter evaluates proposed actions only. It does not execute the requested action, merge code, publish releases, approve policy or legal applicability, or transfer responsibility to an AI system.

The stdio launcher is a local reference integration. Production hosts must separately review executable-path trust, environment isolation, client permissions, logging, dependency provenance, and transport security.
