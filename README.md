# Responsibility Pathway Engineering

**Executable Responsible AI controls for AI systems.**

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for turning explicitly scoped Responsible AI requirement mappings into runtime controls.

```text
Responsible AI requirements
        ↓
human-scoped machine-readable requirement packs
        ↓
AI action request
        ↓
RPE external kernel
        ↓
allow / hold / human_gate / deny
        ↓
reason codes, applicability, missing evidence, and human return
```

RPE helps an AI application determine which stated requirements apply, whether a proposed action may continue, what is missing, and when responsibility must return to a human or institution.

## M1 current position — Governed Reference Kernel

RPE has reached the **M1 Governed Reference Kernel** checkpoint.

Implemented at this checkpoint:

- one deterministic Python decision kernel;
- applicability resolution and multi-pack evaluation;
- Python, local REST, OpenAPI 3.1, and MCP stdio reference interfaces;
- requirement-pack lifecycle and maintenance governance;
- expiry, ambiguity, ownership, review, suspension, supersession, and retirement boundaries;
- independent semantic-version baselines for action requests, gate decisions, requirement packs, governance records, and reason-code policy;
- compatibility, unknown-version, deprecation, and migration rules;
- schemas, synthetic fixtures, checkers, and CI guards.

M1 does **not** include external pack loading, governance enforcement inside `evaluate_action()`, production authentication or deployment, automatic legal interpretation, or formal verification of the Python runtime.

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
| Local REST reference adapter | `rpe-rest` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| OpenAPI 3.1 contract | `GET /openapi.json` | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |
| MCP stdio reference adapter | `rpe-mcp` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |

The adapters evaluate proposed actions only. They do not execute actions, approve deployment, publish releases, merge code, or transfer responsibility.

## Run the executable examples

```bash
python scripts/run_external_kernel.py \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-action-request.json
```

```bash
python scripts/run_external_kernel_multi.py \
  examples/external-kernel/minimal-action-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-data-handling-pack.json
```

## Canonical runtime path

```text
Python / REST / MCP
        ↓
rpe_kernel.evaluate_action()
        ↓
applicability resolution
        ↓
pack evaluation and decision combination
```

Reference adapters must not independently redefine kernel semantics. See [`docs/single-source-kernel.md`](docs/single-source-kernel.md).

## Governance and compatibility artifacts

| Component | Start here |
|---|---|
| Requirement-pack governance | [`docs/requirement-pack-governance.md`](docs/requirement-pack-governance.md) |
| Governance schema | [`schemas/external-kernel/requirement-pack-governance.schema.json`](schemas/external-kernel/requirement-pack-governance.schema.json) |
| Compatibility policy | [`docs/contract-compatibility-policy.md`](docs/contract-compatibility-policy.md) |
| Version manifest | [`schemas/external-kernel/contract-versions.json`](schemas/external-kernel/contract-versions.json) |
| Requirement-pack schema | [`schemas/external-kernel/requirement-pack.schema.json`](schemas/external-kernel/requirement-pack.schema.json) |
| Action-request schema | [`schemas/external-kernel/action-request.schema.json`](schemas/external-kernel/action-request.schema.json) |
| Gate-decision schema | [`schemas/external-kernel/gate-decision.schema.json`](schemas/external-kernel/gate-decision.schema.json) |

A pack is an operational mapping maintained by identified humans. Schema validity does not establish that its source interpretation is correct, current, complete, or suitable for a deployment.

## Core implementation artifacts

| Component | Start here |
|---|---|
| Kernel package | [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py) |
| Applicability resolver | [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py) |
| Pack evaluator | [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py) |
| REST adapter | [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py) |
| MCP adapter | [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py) |
| OpenAPI contract | [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json) |
| Static artifact catalog | [`site/index.html`](site/index.html) |
| Architecture | [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md) |
| Product roadmap | [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md) |
| Project roadmap | [`ROADMAP.md`](ROADMAP.md) |
| AI/search-reader entrance | [`READMEforAI.md`](READMEforAI.md) |
| Japanese entrance | [`README.ja.md`](README.ja.md) |

## Next milestone

M2 is **Governed Pack Integration**. The next bounded work is:

1. make runtime payload version handling explicit;
2. define and implement governance eligibility at the runtime boundary;
3. add bounded external requirement-pack loading;
4. preserve visible failure for stale, ownerless, ambiguous, suspended, or incompatible packs;
5. continue toward trace, evidence, repair, and resume structures.

## Scope boundary

RPE is an enforcement and orchestration reference kernel for approved machine-readable controls. It is not a general legal reasoning engine, self-maintaining regulatory knowledge base, certification system, production governance service, or proof that an AI system is lawful, safe, compliant, fair, or socially adequate.

A schema-valid or passing result means only that the stated machine-readable checks passed. Source interpretation, real-world applicability, evidence sufficiency, deployment approval, execution authority, and final responsibility remain with the relevant human or institution.

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
