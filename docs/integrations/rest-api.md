# Minimal REST API boundary

Status: reference implementation

The REST boundary exposes the framework-neutral `rpe_kernel.evaluate_action` API without adding third-party runtime dependencies.

## Run

```bash
python -m pip install .
rpe-rest --host 127.0.0.1 --port 8080
```

## Health

```http
GET /health
```

## Evaluate

```http
POST /v1/evaluate
Content-Type: application/json
```

```json
{
  "request": {
    "request_id": "example-1",
    "action": "publish"
  },
  "packs": [
    {
      "pack_id": "publication-pack",
      "applicability": {
        "action": ["publish"]
      },
      "requirements": []
    }
  ]
}
```

The response preserves the kernel decision contract, including `stage`, `decision`, `reason_codes`, applicability results, pack decisions, human return, and next step.

## Boundary

This is a local reference server, not a production deployment. It does not provide authentication, authorization, TLS termination, rate limiting, persistent storage, tenancy isolation, or legal/compliance validation. Production adapters must add those controls around the same kernel API.
