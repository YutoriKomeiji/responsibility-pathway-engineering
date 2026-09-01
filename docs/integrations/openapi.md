# OpenAPI contract

The reference REST adapter publishes an OpenAPI 3.1 document at:

```text
GET /openapi.json
```

The repository-owned source is:

```text
spec/openapi/rpe-kernel.openapi.json
```

A packaged snapshot is included with the Python distribution so `/openapi.json` remains available after `pip install .`. CI rejects drift between the repository source, packaged snapshot, and runtime document.

The contract currently describes:

- `GET /health`;
- `GET /openapi.json`;
- legacy `POST /v1/evaluate`;
- strict governed `POST /v1/evaluate/governed`;
- legacy and governed request/response schemas;
- governed stages `admission`, `compatibility`, `governance`, `applicability`, and `evaluation`;
- the decision vocabulary `allow`, `hold`, `human_gate`, and `deny`;
- governed no-authority handoff constants `authority_effect = none` and `decision_scope = evaluation_only`.

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

The checker verifies required operations, governed schemas and stage vocabulary, decision vocabulary, the production boundary, and repository/package/runtime OpenAPI parity.

## Boundary

This OpenAPI document is an interface contract for the local reference adapter. It is not a production-readiness statement, legal interpretation, security certification, deployment approval, source-trust mechanism, execution authorization contract, external-effect proof, or transfer of final responsibility to an AI system.

Authentication, authorization, TLS, rate limiting, persistence, tenancy isolation, deployment, generated SDK release, consequential execution, repair/resume authority, and operational ownership remain separate decisions outside this reference contract.
