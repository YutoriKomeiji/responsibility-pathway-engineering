# Responsibility Pathway Engineering

**Executable Responsible AI controls for AI systems.**

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for turning Responsible AI requirements into runtime controls.

```text
Responsible AI requirements
        ↓
machine-readable requirement packs
        ↓
AI action request
        ↓
RPE external kernel
        ↓
allow / hold / human_gate / deny
        ↓
reason codes, applicability, missing evidence, and human return
```

RPE helps an AI application determine which requirements apply, whether an action may continue, what is missing, and when responsibility must return to a human or institution.

## Install and call the kernel

The current reference implementation is dependency-free Python 3.11+.

```bash
python -m pip install .
```

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

All supported runtime interfaces delegate to this same package API.

| Interface | Entry point | Documentation |
|---|---|---|
| Python package | `from rpe_kernel import evaluate_action` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| Local REST adapter | `rpe-rest` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| OpenAPI 3.1 contract | `GET /openapi.json` | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |
| MCP stdio adapter | `rpe-mcp` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |

The REST adapter exposes:

```text
GET  /health
GET  /openapi.json
POST /v1/evaluate
```

The MCP adapter exposes one bounded tool:

```text
rpe_evaluate_action
```

Both adapters evaluate proposed actions only. They do not execute the action, approve deployment, publish releases, merge code, or transfer responsibility.

## Run the executable examples

Single pack:

```bash
python scripts/run_external_kernel.py \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-action-request.json
```

Multiple packs:

```bash
python scripts/run_external_kernel_multi.py \
  examples/external-kernel/minimal-action-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-data-handling-pack.json
```

Original responsibility-path demo:

```bash
python scripts/demo.py
```

## What is implemented

- applicability resolution for requirement packs
- deterministic multi-pack evaluation
- structured `allow`, `hold`, `human_gate`, and `deny` decisions
- Python package API
- local REST adapter
- OpenAPI 3.1 contract served by the REST adapter
- bounded MCP stdio adapter
- source metadata and human-return routes
- schemas, synthetic fixtures, checkers, and GitHub Actions
- a single-source guard that prevents REST and MCP from reimplementing kernel semantics

The canonical runtime path is:

```text
Python / REST / MCP
        ↓
rpe_kernel.evaluate_action()
        ↓
applicability resolution
        ↓
pack evaluation and decision combination
```

See [`docs/single-source-kernel.md`](docs/single-source-kernel.md) for the implementation-drift guard.

## Core artifacts

| Component | Start here |
|---|---|
| Kernel package | [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py) |
| Applicability resolver | [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py) |
| Pack evaluator | [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py) |
| REST adapter | [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py) |
| MCP adapter | [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py) |
| OpenAPI contract | [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json) |
| Requirement-pack schema | [`schemas/external-kernel/requirement-pack.schema.json`](schemas/external-kernel/requirement-pack.schema.json) |
| Action-request schema | [`schemas/external-kernel/action-request.schema.json`](schemas/external-kernel/action-request.schema.json) |
| Gate-decision schema | [`schemas/external-kernel/gate-decision.schema.json`](schemas/external-kernel/gate-decision.schema.json) |
| Static artifact catalog | [`site/index.html`](site/index.html) |
| Architecture | [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md) |
| Product roadmap | [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md) |
| Project roadmap | [`ROADMAP.md`](ROADMAP.md) |
| AI/search-reader entrance | [`READMEforAI.md`](READMEforAI.md) |
| Japanese entrance | [`README.ja.md`](README.ja.md) |

## Requirement packs

A requirement pack converts a law mapping, standard, guideline, organizational policy, or synthetic test requirement into an executable control. A pack can carry applicability conditions, required context, decision behavior, reason-code namespace, human-return role, source authority, jurisdiction, version, effective date, review owner, and interpretation status.

The included packs are synthetic examples. A real law-, standard-, or policy-derived pack requires source-specific human review and maintenance.

## Current direction

The kernel package and first portable interfaces are implemented. Near-term work now focuses on:

1. stabilizing request and result contracts, including explicit schema-version policy;
2. loading and validating external requirement packs through a bounded interface;
3. adding integration examples without duplicating kernel semantics;
4. improving traces, repair, resume, and evidence handling;
5. researching production boundaries such as authentication, authorization, tenancy, persistence, and deployment controls before any production claim.

## Scope boundary

RPE provides executable control structures and traceable responsibility pathways. It does not by itself establish that a system is lawful, safe, compliant, fair, certified, socially adequate, or production-approved.

A schema-valid or passing result means only that the stated machine-readable checks passed. Real-world applicability, source interpretation, evidence sufficiency, deployment approval, and final responsibility remain with the relevant human or institution.

## Author and construction

Author: **Akihisa Ono (小野昭久)**  
Repository affiliation: Independent

RPE is developed through Open Construction with assistance from [Luminalia AI](docs/ai-assisted-construction-note.md). Human maintainer judgment remains responsible for direction, merge, publication, external claims, and final decisions.

- [Provenance](docs/provenance.md)
- [Authorship](AUTHORSHIP.md)
- [Open Construction](OPEN_CONSTRUCTION.md)
- [Citation metadata](CITATION.cff)

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 Akihisa Ono (小野昭久). See [NOTICE.md](NOTICE.md) for attribution and AI-assistance notes.
