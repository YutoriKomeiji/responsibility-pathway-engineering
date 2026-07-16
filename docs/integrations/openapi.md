# OpenAPI contract

The reference REST adapter publishes a repository-owned OpenAPI 3.1 document at:

```text
GET /openapi.json
```

The canonical source is:

```text
spec/openapi/rpe-kernel.openapi.json
```

The contract currently describes:

- `GET /health`
- `GET /openapi.json`
- `POST /v1/evaluate`
- request, decision, health, and bounded error schemas
- the kernel decision vocabulary: `allow`, `hold`, `human_gate`, and `deny`

## Local use

```bash
python -m pip install .
rpe-rest --host 127.0.0.1 --port 8080
curl http://127.0.0.1:8080/openapi.json
```

## Verification

```bash
python scripts/check_openapi_contract.py
```

The checker confirms the required operations and component schemas, preserves the decision vocabulary and production boundary, and verifies that the runtime document is identical to the repository contract.

## Boundary

This OpenAPI document is an interface contract for the local reference adapter. It is not a production-readiness statement, legal interpretation, security certification, deployment approval, or transfer of final responsibility to an AI system. Authentication, authorization, TLS, rate limiting, persistence, tenancy isolation, deployment, and generated SDK release remain separate Human Gate decisions.
