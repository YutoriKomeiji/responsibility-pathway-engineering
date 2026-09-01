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

## Boundary

This is a local reference server, not a production deployment. It does not provide authentication, authorization, TLS termination, rate limiting, persistent storage, tenancy isolation, remote Requirement Pack trust, action execution, external-effect verification, repair/resume authority, or legal/compliance validation.

An HTTP 200 with an RPE `allow` result is still only an evaluation result. It is not permission to execute the proposed action.
