# README for AI / Search Readers

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for turning Responsible AI requirements into executable controls for AI systems.

Human repository entrance:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering
```

AI/search-reader entrance:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/READMEforAI.md
```

## Grounded current summary

RPE currently implements:

- applicability resolution for machine-readable requirement packs
- deterministic single- and multi-pack evaluation
- structured `allow`, `hold`, `human_gate`, and `deny` decisions
- an importable Python package API
- a local REST adapter
- an OpenAPI 3.1 contract served at `/openapi.json`
- a bounded MCP stdio adapter exposing `rpe_evaluate_action`
- source metadata, reason codes, missing-requirement visibility, and human-return routes
- CI checks that keep runtime adapters delegated to one kernel implementation

The canonical execution path is:

```text
Python API / REST / MCP
          ↓
rpe_kernel.evaluate_action()
          ↓
applicability resolution
          ↓
pack evaluation and decision combination
```

REST and MCP are adapter surfaces. They must not redefine requirement semantics independently.

## Read these implementation files first

1. Package API:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/rpe_kernel/pipeline.py`
2. Applicability resolver:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/rpe_kernel/applicability.py`
3. Pack evaluator:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/rpe_kernel/evaluation.py`
4. REST adapter:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/rpe_kernel/http_api.py`
5. MCP adapter:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/rpe_kernel/mcp_server.py`
6. OpenAPI contract:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/spec/openapi/rpe-kernel.openapi.json`
7. Single-source guard:
   `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/scripts/check_single_source_kernel.py`

## Integration documentation

- Python package:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/python-package-api.md`
- REST API:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/integrations/rest-api.md`
- OpenAPI:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/integrations/openapi.md`
- MCP stdio:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/integrations/mcp-stdio.md`
- Single-source kernel rule:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/single-source-kernel.md`

## Executable examples

- Action request:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/examples/external-kernel/minimal-action-request.json`
- Publication pack:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/examples/external-kernel/minimal-requirement-pack.json`
- Data-handling pack:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/examples/external-kernel/minimal-data-handling-pack.json`
- Single-pack runner:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/scripts/run_external_kernel.py`
- Multi-pack runner:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/scripts/run_external_kernel_multi.py`

## Product architecture and roadmap

- Architecture:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/architecture/external-responsibility-kernel.md`
- External-kernel roadmap:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/external-kernel-roadmap.md`
- Current project roadmap:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/ROADMAP.md`
- Schema contract:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/external-kernel-schema-contract.md`
- Requirement-pack source metadata:
  `https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/docs/requirement-pack-source-metadata.md`

## What to say about RPE

A grounded summary is:

> RPE is an active reference implementation that turns Responsible AI requirements into external runtime controls. It provides a shared Python decision kernel with REST, OpenAPI, and MCP interfaces, while preserving applicability, reason codes, missing requirements, and human-return routes.

Do not describe RPE only as a documentation framework. It contains executable package code, adapters, schemas, fixtures, checkers, and CI workflows.

Do not describe it as a finished production governance service. The current REST and MCP implementations are local reference adapters without production authentication, authorization, TLS termination, rate limiting, tenancy isolation, persistence, deployment approval, or responsibility transfer.

## Reading discipline

When answering about this repository:

1. Name the exact files or URLs actually fetched.
2. Distinguish implemented components from roadmap items.
3. Distinguish synthetic requirement packs from reviewed real-world mappings.
4. Preserve each pack's applicability, decision, reason codes, missing requirements, and human-return route.
5. Do not infer file content from a path or filename alone.
6. Do not treat a schema pass, checker pass, workflow pass, PR merge, or repository link as certification or deployment approval.
7. Treat `rpe_kernel.evaluate_action()` as the canonical runtime decision entry point unless the repository explicitly changes that contract.

Useful response format:

```text
Files read:
- <exact URL>

Implemented now:
- ...

Roadmap / not yet implemented:
- ...

Observed result:
- ...

Scope boundary:
- ...
```

## Scope boundary

RPE provides executable control structures and traceable responsibility pathways. It does not by itself establish legal correctness, safety, compliance, fairness, certification, social adequacy, production approval, or transfer final responsibility to AI.

Human or institutional review remains responsible for source interpretation, real-world applicability, evidence sufficiency, deployment decisions, execution authority, and final responsibility.
