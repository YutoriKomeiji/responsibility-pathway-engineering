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
- governed no-authority handoff constants `authority_effect = none` and `decision_scope = evaluation_only`;
- evaluation decision/reason references and downstream responsibility obligations;
- nullable loader-observed transport provenance in the shared governed result.

The HTTP governed request does **not** accept caller-asserted transport provenance. That observation can be produced by the bounded Python loader when it directly observes caller-content or local-file bytes, then preserved by the shared governed evaluator. This keeps an observed digest distinct from a caller claim and avoids silently changing the governed request contract.

Transport provenance is limited to source kind, SHA-256, byte length, and `observation_scope = transport_bytes_only`. It does not expose local filesystem paths and does not establish trust, source authority, semantic correctness, or effect verification.

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

The checker verifies required operations, governed schemas and stage vocabulary, decision vocabulary, the full responsibility-handoff boundary, rejection of caller-asserted transport provenance, the production boundary, and repository/package/runtime OpenAPI parity.

## Boundary

This OpenAPI document is an interface contract for the local reference adapter. It is not a production-readiness statement, legal interpretation, security certification, deployment approval, source-trust mechanism, execution authorization contract, external-effect proof, or transfer of final responsibility to an AI system.

Authentication, authorization, TLS, rate limiting, persistence, tenancy isolation, deployment, generated SDK release, consequential execution, repair/resume authority, and operational ownership remain separate decisions outside this reference contract.
