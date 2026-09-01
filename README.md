# Responsibility Pathway Engineering

[![Value Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml)
[![Security Hygiene](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml)
[![Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml)

**Keep “the model proposed it” separate from “the system may do it.”**

Responsibility Pathway Engineering (RPE) is an open-source Python responsibility-evaluation layer for AI agents and automation. It evaluates scoped requirements, approval and evidence conditions, machine-readable reasons, and the next responsibility owner before an external action continues.

## Why use RPE?

Agent systems can accidentally collapse a proposal into permission. RPE inserts a small, inspectable decision boundary between those two steps.

RPE can:

- stop unsupported continuation with explicit outcomes such as `human_gate`;
- return stable reason codes and the next responsibility owner;
- keep evaluation evidence separate from verified external effect;
- sit in front of an existing execution stack without becoming the executor;
- preserve a legacy path where strict governance is not required.

Run the shortest before/after demo:

```bash
python scripts/value_demo.py
```

See [`docs/why-rpe.md`](docs/why-rpe.md) for the adoption-value boundary and the claims the demo does not make.

```text
AI proposes an action
        ↓
RPE evaluates requirements, approvals, evidence, and governance state
        ↓
allow / hold / human_gate / deny
        ↓
reason codes, missing conditions, responsibility handoff
        ↓
existing runtime, human, institution, or downstream system
```

## What you can use today

The current public implementation includes:

- deterministic applicability resolution and multi-pack evaluation;
- legacy-compatible Python entry `evaluate_action()`;
- strict governed Python entry `evaluate_governed_action()`;
- exact Requirement Pack / governance identity and version binding;
- governed REST reference routes;
- governed MCP stdio tools;
- OpenAPI 3.1 contracts;
- bounded caller-content and local-file loading;
- responsibility handoff metadata with `authority_effect = none` and `decision_scope = evaluation_only`;
- schemas, synthetic fixtures, regression tests, and CI guards.

Current implementation status: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md).

## Install

The current reference implementation targets Python 3.11+ and has no external runtime dependencies.

```bash
python -m pip install .
```

### Legacy-compatible API

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

### Strict governed API

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

The strict governed path evaluates:

```text
input admission
    ↓
contract compatibility
    ↓
Requirement Pack ↔ governance binding
    ↓
governance eligibility
    ↓
applicability
    ↓
requirement evaluation
    ↓
combined decision
    ↓
responsibility handoff metadata
```

## Interfaces

| Interface | Legacy-compatible entry | Strict governed entry | Documentation |
|---|---|---|---|
| Python | `evaluate_action()` | `evaluate_governed_action()` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| REST | `POST /v1/evaluate` | `POST /v1/evaluate/governed` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| MCP stdio | `rpe_evaluate_action` | `rpe_evaluate_governed_action` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |
| OpenAPI 3.1 | both documented | both documented | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |

These adapters evaluate proposed actions. They do not execute actions, approve deployment, verify external effects, publish releases, or transfer final responsibility.

## Critical authority boundary

An RPE `allow` result is an **evaluation result**, not an execution authorization token.

RPE does not by itself:

- dispatch or execute an external action;
- approve deployment;
- verify that an external effect occurred;
- treat a transport response or receipt as verified effect evidence;
- grant repair authority because repair is possible;
- grant resume authority because a path is ready to continue;
- transfer final responsibility to AI.

Evaluation evidence is not effect evidence. Repair readiness is not repair authority. Resume readiness is not resume authority.

## Bounded loading

The current loader accepts only:

- caller-provided UTF-8 JSON content; or
- an explicitly supplied local file.

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

It does not fetch URLs, discover remote registries, install packages, or establish source trust.

Readable bytes do not prove source authority, semantic correctness, governance eligibility, legal validity, or current applicability.

## Demo and public site

Shortest value demo:

```bash
python scripts/value_demo.py
```

Broader bounded walkthrough:

```bash
python scripts/demo.py
```

Browser entry: [`site/index.html`](site/index.html).

A passing demo or CI job is evidence that its named checks passed under the tested conditions. It is not security certification, legal or compliance approval, production approval, proof of real-world risk reduction, or proof that an external effect occurred.

## Support status and known limits

RPE is under active development, but documented surfaces can be tried and integrated within their stated boundaries. The repository is not treated as uniformly unusable because some areas are still under development.

RPE currently does not provide:

- a production authentication or authorization platform;
- remote source-trust establishment;
- external dispatch, retry, reconciliation, repair, or resume execution;
- security guarantees for arbitrary deployments;
- automated legal interpretation, compliance certification, or organizational authority.

Report bugs, adversarial cases, integration friction, counterexamples, or patches:

- [Support](SUPPORT.md)
- [Security](SECURITY.md)
- [Contributing](CONTRIBUTING.md)

## Long-term direction

RPE aims to support human-reviewed, bounded machine-readable controls derived from laws, public guidance, standards, organizational policies, professional duties, and affected-party commitments.

The kernel is not intended to become an automated legal authority, self-updating regulatory database, certification body, or source of organizational authority.

## Verification and assurance

RPE favors scoped, inspectable claims over blanket statements such as “safe” or “production ready.” Formal proofs may establish properties of explicitly modeled pathways under stated assumptions, but they do not automatically prove the complete Python implementation, source interpretation, legal validity, deployment behavior, or production safety.

See:

- [`docs/verification-assurance-and-open-governance.md`](docs/verification-assurance-and-open-governance.md)
- [`docs/claim-boundary-promotion.md`](docs/claim-boundary-promotion.md)

## Main links

- [Why use RPE?](docs/why-rpe.md)
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
