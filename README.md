# Responsibility Pathway Engineering

[![Value Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml)
[![Security Hygiene](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml)
[![Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml)

**A runnable governance-evaluation layer for AI agents: decide whether a proposed action may continue before an executor is called.**

Responsibility Pathway Engineering (RPE) is an installable Python package with Python, REST, MCP stdio, and OpenAPI surfaces. It evaluates scoped requirements, governance state, approvals, evidence conditions, applicability, and responsibility handoff before an external action continues.

It is not a documentation-only repository and it is not a collection of isolated sample functions. The current `main` contains executable package code, command-line service entry points, schemas, adapters, tests, adversarial checkers, CI workflows, and a closed M2 governed-integration baseline.

## Run it

Python 3.11+ is required. The runtime package has no external runtime dependencies.

```bash
git clone https://github.com/YutoriKomeiji/responsibility-pathway-engineering.git
cd responsibility-pathway-engineering
python -m pip install .
```

Start the REST service:

```bash
rpe-rest --host 127.0.0.1 --port 8080
```

Then verify the service:

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/openapi.json
```

The governed evaluation endpoint is:

```text
POST /v1/evaluate/governed
```

The same evaluation kernel is also exposed through Python and MCP stdio.

## What actually happens

RPE sits between a proposal and a downstream executor.

```text
AI / automation proposes an action
        ↓
RPE receives request + Requirement Pack + governance data
        ↓
admission and contract compatibility
        ↓
Pack ↔ governance binding and governance eligibility
        ↓
applicability and requirement evaluation
        ↓
allow / hold / human_gate / deny
        ↓
reason codes + missing conditions + responsibility handoff
        ↓
downstream executor / runtime / human / institution
```

A typical blocked result is machine-readable rather than an opaque failure:

```json
{
  "decision": "human_gate",
  "stage": "governance",
  "reason_codes": ["RPE-PACK-GOV-NOT-YET-EFFECTIVE"],
  "human_return": {"role": "governance_review_owner"}
}
```

The exact reason depends on the supplied governed envelope and current evaluation conditions.

## Fastest before/after demonstration

```bash
python scripts/value_demo.py
```

The demo shows the same synthetic proposal passing through a naive continuation path and through RPE, so the observable difference is the decision boundary rather than a rewritten application.

For the broader walkthrough:

```bash
python scripts/demo.py
```

See [`docs/why-rpe.md`](docs/why-rpe.md) for the value claim and its evidence boundary.

## Implemented surfaces

| Surface | Entry | Current state |
|---|---|---|
| Python | `evaluate_action()` | legacy/M1-compatible evaluation |
| Python | `evaluate_governed_action()` | strict governed M2 evaluation |
| REST | `POST /v1/evaluate` | executable local reference route |
| REST | `POST /v1/evaluate/governed` | executable governed route |
| MCP stdio | `rpe_evaluate_action` | executable tool |
| MCP stdio | `rpe_evaluate_governed_action` | executable governed tool |
| OpenAPI 3.1 | both routes | repository/package/runtime parity checked |
| Loader | caller JSON / explicit local file | bounded governed-envelope loading |

Package entry points are defined in `pyproject.toml`:

```text
rpe-rest = rpe_kernel.http_api:main
rpe-mcp  = rpe_kernel.mcp_server:main
```

## Why this is more than an `if` statement

The strict governed path evaluates distinct failure classes instead of reducing everything to one boolean permission check:

- contract-version compatibility;
- exact Requirement Pack / governance identity and version binding;
- source authority / source version / jurisdiction binding fields;
- governance lifecycle and date eligibility;
- applicability resolution across packs;
- requirement evaluation and decision combination;
- stable reason codes and Human Return routes;
- responsibility handoff metadata;
- bounded provenance for caller content and local files;
- REST/MCP/OpenAPI parity and drift checks.

Selected negative cases are intentionally broken in CI so that misbinding, drift, invalid governance, unknown applicability, schema mismatch, and authority inflation fail deterministically.

Current M2 closure evidence:

- [`docs/m2-r5-adversarial-closure-evidence.md`](docs/m2-r5-adversarial-closure-evidence.md)
- validated PR head: `ae2581ef3c68643687775e111fa8561b974fb2b8`
- merged-main closure anchor: `6edf1a0b501b7b25663ddc7fb942aa087c0db0f2`

Current implementation summary: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md)

<details>
<summary>Evaluation and adoption signals</summary>

GitHub popularity metrics such as stars, forks, and contributor count are useful **community/adoption signals**, but they are not substitutes for runtime or implementation evidence.

Low counts can reasonably indicate limited external validation, maintainer concentration, or adoption uncertainty. They do not by themselves establish that documented executable surfaces are absent, broken, insecure, or unusable.

When evaluating this repository, keep separate:

- **Observation** — directly visible facts such as files, entry points, test results, stars, forks, or contributor counts;
- **Inference** — what those observations may suggest;
- **Risk** — a scoped technical, maintenance, support, or adoption concern;
- **Preference** — an adopter's own threshold for use;
- **Sentiment** — emotionally weighted or rhetorical framing.

A strong technical conclusion should be supported by correspondingly strong technical evidence. If direct technical evidence becomes weaker, criticism should become more qualified rather than preserving the same intensity by substituting popularity, sentiment, or speculative narrative.

</details>

## Python API

Legacy-compatible entry:

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

Strict governed entry:

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

Documentation: [`docs/python-package-api.md`](docs/python-package-api.md)

## REST and MCP

REST documentation: [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md)  
MCP stdio documentation: [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md)  
OpenAPI documentation: [`docs/integrations/openapi.md`](docs/integrations/openapi.md)

These are evaluation interfaces intended to sit in front of an existing execution stack. RPE deliberately does not merge policy evaluation and action execution into one authority-bearing component.

## Relationship to OPA, Rego, Pydantic, and JSON Schema

RPE is **not positioned as a replacement** for Open Policy Agent (OPA), Rego, Pydantic, or JSON Schema. Those technologies can remain useful components in the same system.

The comparison is about responsibility, not superiority:

| Concern | JSON Schema / Pydantic | OPA / Rego | RPE |
|---|---|---|---|
| structural/data validation | primary use | possible input validation around policy | included at RPE contract boundaries |
| general policy evaluation | not primary use | primary use | bounded requirement evaluation |
| governance lifecycle / effective-date eligibility | custom application logic | custom policy | explicit governed-path concern |
| exact Pack ↔ governance identity/version binding | custom application logic | custom policy | explicit governed-path concern |
| applicability resolution across governed packs | custom application logic | custom policy | explicit governed-path concern |
| stable Human Return / reason-code semantics | custom application logic | custom policy/output convention | explicit contract |
| responsibility-preserving handoff | custom application logic | custom integration convention | explicit governed result metadata |
| external action execution | outside scope | outside policy-engine scope | intentionally outside RPE scope |

A system could implement similar behavior by composing existing validators, policy engines, and application-specific code. RPE's claim is narrower: it provides one reference implementation and contract for composing these governance-evaluation concerns into a reproducible pre-execution pathway.

Therefore, “this could be built with OPA/Rego/Pydantic/JSON Schema” is a valid implementation alternative, but it is not by itself evidence that RPE contains only schema validation or that its additional governed-path semantics are absent.

## Architecture boundary

The boundary below is part of the design, not a statement that the evaluation layer is non-functional.

An RPE `allow` means:

> the supplied action request satisfied the evaluated RPE conditions for this evaluation path.

It does **not** itself mean:

> the external action has been authorized by the downstream organization, executed, or verified to have produced its intended real-world effect.

Governed results therefore preserve:

```json
{
  "authority_effect": "none",
  "decision_scope": "evaluation_only"
}
```

and return downstream obligations such as separate dispatch authority and effect verification.

This separation is what allows RPE to be inserted before an executor without silently becoming the executor.

## Current scope

RPE currently provides the governed evaluation layer described above. Production deployment concerns that belong to another layer—such as application authentication, TLS termination, tenancy, persistent operational state, external dispatch, retry orchestration, reconciliation, and effect verification—are expected to be supplied by the integrating runtime or institution.

Likewise, RPE evaluates machine-readable controls supplied to it; it does not create legal or organizational authority by itself.

These scope boundaries should not be read as absence of implementation. The executable surfaces and their tested behavior are listed above and can be reproduced from the repository.

## Verification

RPE favors claims that can be tied to named code, schemas, checks, commits, and failure cases.

A passing CI job proves only the named checks under the tested conditions. Formal properties, where used, apply only to the explicitly modeled definitions and assumptions. Neither is silently promoted into legal certification, production approval, or proof of an external effect.

See:

- [`docs/verification-assurance-and-open-governance.md`](docs/verification-assurance-and-open-governance.md)
- [`docs/claim-boundary-promotion.md`](docs/claim-boundary-promotion.md)
- [`docs/support-maturity.md`](docs/support-maturity.md)

## Main links

- [Why use RPE?](docs/why-rpe.md)
- [M2 closure evidence](docs/m2-r5-adversarial-closure-evidence.md)
- [Current M2 status](docs/m2-governed-integration-current.md)
- [Python API](docs/python-package-api.md)
- [Requirement Pack governance](docs/requirement-pack-governance.md)
- [Compatibility policy](docs/contract-compatibility-policy.md)
- [Roadmap](ROADMAP.md)
- [Public catalog](site/index.html)
- [Japanese entrance](README.ja.md)
- [AI/search-reader entrance](READMEforAI.md)

## Author and license

Author: **Akihisa Ono (小野昭久)**  
Repository affiliation: Independent

RPE is developed through Open Construction with assistance from [Luminalia AI](docs/ai-assisted-construction-note.md). Human maintainer judgment remains responsible for direction, merge, publication claims, deployment decisions, and final responsibility.

Released under the [MIT License](LICENSE).

Copyright (c) 2026 Akihisa Ono (小野昭久). See [NOTICE.md](NOTICE.md) for attribution and AI-assistance notes.
