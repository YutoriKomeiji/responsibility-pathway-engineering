# Minimal REST API boundary

Status: reference implementation

The dependency-free REST adapter exposes both the retained legacy/M1-compatible evaluation surface and the explicit strict governed M2 surface.

## Run

```bash
python -m pip install .
rpe-rest --host 127.0.0.1 --port 8080
```

## Health

```http
GET /health
```

## OpenAPI

```http
GET /openapi.json
```

The runtime document is loaded from the packaged OpenAPI snapshot. CI checks it against the repository-owned OpenAPI source.

## Legacy / M1-compatible evaluation

```http
POST /v1/evaluate
Content-Type: application/json
```

Body:

```json
{
  "request": {"request_id": "example-1", "action": "publish"},
  "packs": [{"pack_id": "publication-pack", "requirements": []}]
}
```

This route delegates to `rpe_kernel.evaluate_action()`.

## Strict governed evaluation

```http
POST /v1/evaluate/governed
Content-Type: application/json
```

The request is a governed evaluation envelope and delegates to `rpe_kernel.evaluate_governed_action()`.

The governed path can return stages including:

- `admission`;
- `compatibility`;
- `governance`;
- `applicability`;
- `evaluation`.

Governed results preserve `authority_effect = none` and `decision_scope = evaluation_only`.

## Input boundary and safe exposure

The built-in reference server binds to `127.0.0.1` by default. All POST
evaluation routes now require exactly one decimal `Content-Length`, a
`Content-Type: application/json` media type, and a request body of at most
**1,048,576 bytes (1 MiB)**. The server rejects chunked/transfer-encoded
requests, duplicate JSON object members (including nested policy/authority
fields), and non-finite JSON values rather than accepting ambiguous inputs.
It bounds request-body reads with a 10-second socket timeout. Invalid framing,
unsupported media types, and over-limit bodies return HTTP 400, 415, and 413
respectively; an incomplete body returns 400 and a read timeout returns 408.

These are **minimum reference-adapter controls**, not a complete hostile-network
perimeter: the built-in threaded server has no authentication, connection-count
or per-source rate limits, TLS, request-context attestation, or trusted reverse
proxy configuration. Do **not** bind it to a public interface without an
independently managed enterprise security boundary. MCP stdio has a separate
transport boundary. The 1 MiB cap is an initial compatibility limit, not a
performance/SLO claim.

## Boundary

This is a local reference server, not a production deployment. It does not provide authentication, authorization, TLS termination, rate limiting, persistent storage, tenancy isolation, remote Requirement Pack trust, action execution, external-effect verification, repair/resume authority, or legal/compliance validation.

An HTTP 200 with an RPE `allow` result is still only an evaluation result. It is not permission to execute the proposed action.
