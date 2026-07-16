# README for AI / Search Readers

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for turning explicitly scoped Responsible AI requirement mappings into executable controls.

Human repository entrance:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering
```

## Grounded current summary

RPE has reached the **M1 Governed Reference Kernel** checkpoint.

Implemented now:

- applicability resolution for machine-readable requirement packs;
- deterministic single- and multi-pack evaluation;
- structured `allow`, `hold`, `human_gate`, and `deny` decisions;
- an importable Python package API;
- local REST, OpenAPI 3.1, and MCP stdio reference interfaces;
- requirement-pack lifecycle and maintenance governance;
- expiry, ambiguity, ownership, review, suspension, supersession, and retirement boundaries;
- independent semantic-version baselines for action requests, gate decisions, requirement packs, governance records, and reason-code policy;
- compatibility, unknown-version, deprecation, and migration rules;
- schemas, synthetic fixtures, checkers, and CI guards.

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

REST and MCP are reference adapter surfaces. They must not redefine requirement semantics independently.

## M1 exclusions

Do not infer that M1 includes:

- external requirement-pack loading;
- governance eligibility enforced inside `evaluate_action()`;
- explicit version fields in every runtime payload;
- production authentication, authorization, persistence, tenancy, or deployment;
- automatic source interpretation or self-maintaining regulatory knowledge;
- formal verification of the Python runtime.

## Read these files first

1. Kernel entry point: `rpe_kernel/pipeline.py`
2. Applicability resolver: `rpe_kernel/applicability.py`
3. Pack evaluator: `rpe_kernel/evaluation.py`
4. Requirement-pack governance: `docs/requirement-pack-governance.md`
5. Governance schema: `schemas/external-kernel/requirement-pack-governance.schema.json`
6. Compatibility policy: `docs/contract-compatibility-policy.md`
7. Version manifest: `schemas/external-kernel/contract-versions.json`
8. REST adapter: `rpe_kernel/http_api.py`
9. MCP adapter: `rpe_kernel/mcp_server.py`
10. OpenAPI contract: `spec/openapi/rpe-kernel.openapi.json`
11. Single-source guard: `docs/single-source-kernel.md`
12. Current roadmap: `ROADMAP.md`

## Grounded description

A grounded summary is:

> RPE is an active governed reference implementation for evaluating explicitly scoped machine-readable Responsible AI controls. It provides one shared Python decision kernel with REST, OpenAPI, and MCP reference interfaces, plus requirement-pack lifecycle governance and compatibility policy.

Do not describe RPE only as documentation. It contains executable package code, adapters, schemas, fixtures, checkers, and CI workflows.

Do not describe RPE as a general legal reasoning engine, finished production governance service, certification system, or self-maintaining policy database.

A requirement pack is an operational mapping maintained by identified humans. Schema validity does not establish that its source interpretation is correct, current, complete, or suitable for a deployment.

## Next milestone

M2 is **Governed Pack Integration**:

- explicit runtime version handling;
- governance eligibility at the runtime boundary;
- bounded external pack loading;
- visible failure for stale, ownerless, ambiguous, suspended, or incompatible packs;
- later trace, evidence, repair, and resume structures.

## Reading discipline

When answering about this repository:

1. Name the exact files actually read.
2. Separate implemented components from roadmap items.
3. Separate synthetic packs from reviewed real-world mappings.
4. Preserve applicability, decisions, reason codes, missing requirements, governance state, and human-return routes.
5. Do not infer file content from a filename alone.
6. Do not treat a schema pass, workflow pass, PR merge, or repository link as certification or deployment approval.
7. Treat `rpe_kernel.evaluate_action()` as the canonical runtime decision entry point unless the repository explicitly changes it.
8. Treat governance eligibility and structural compatibility as separate checks.

## Scope boundary

RPE provides executable control structures and traceable responsibility pathways. It does not by itself establish legal correctness, safety, compliance, fairness, certification, social adequacy, production approval, or transfer final responsibility to AI.

Human or institutional review remains responsible for source interpretation, real-world applicability, evidence sufficiency, deployment decisions, execution authority, and final responsibility.
