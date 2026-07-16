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

## Executable demo

`scripts/demo.py` calls the canonical kernel with three synthetic scenarios:

- missing approval -> `human_gate`;
- complete stated evidence -> `allow`;
- missing applicability context -> visible `human_gate` at the applicability stage.

The demo supports `--scenario human_gate|allow|unknown` and `--json`. It does not execute an external action and is not certification, legal review, compliance determination, safety approval, fairness assessment, or deployment approval.

## M1 exclusions

Do not infer that M1 includes:

- external requirement-pack loading;
- governance eligibility enforced inside `evaluate_action()`;
- explicit version fields in every runtime payload;
- production authentication, authorization, persistence, tenancy, or deployment;
- automatic source interpretation or self-maintaining regulatory knowledge;
- reviewed real-world law or guideline mappings;
- formal verification of the Python runtime;
- certification, conformity assessment, or official-standard status.

## Verification and assurance scope

RPE uses **verifiable AI** in a bounded sense. It aims to make assumptions, requirement mappings, applicability, decisions, stop conditions, reason codes, missing evidence, and human-return routes inspectable and re-checkable.

Planned Lean 4 formalization may prove properties of explicitly modeled responsibility pathways, including deterministic decisions, absence of `allow` under modeled missing mandatory evidence, preservation of stronger stop outcomes, existence of required human-return routes, rejection of forbidden transitions, and preservation of stated invariants.

A correct description is:

> Lean 4 may prove that a formalized responsibility path follows formalized rules under stated assumptions.

Do not extend that statement into a proof of the complete Python runtime, external services, input data, human conduct, Requirement Pack interpretation, legal validity, social adequacy, production safety, or the full AI system. Those claims require additional model-to-runtime correspondence and real-world evidence.

RPE treats AI assurance as accumulation of scoped requirements, decision records, evidence, verification results, governance ownership, and explicit proof boundaries—not as a blanket declaration that an AI system is safe.

RPE does not claim to solve model-internal value alignment or the complete AI alignment problem. It addresses external operational alignment between proposed actions, stated requirements, stop conditions, and human responsibility routes.

## Public-guidance boundary

The Japanese MIC/METI **AI Guidelines for Business Ver. 1.2** dated 31 March 2026 is an official non-binding governance reference that may inform future human-reviewed mappings.

Do not claim that RPE currently:

- officially implements the guideline;
- conforms or complies with it;
- automatically interprets it;
- provides reviewed real-world Requirement Packs derived from it;
- has government adoption or endorsement.

Use language such as “references,” “may inform a human-reviewed mapping,” “makes related responsibility pathways more explicit,” or “is a complementary design framework.”

## Open-governance position

RPE is MIT-licensed. It aims for open specifications, interoperability, independent verification, and multiple-implementation potential. It is not currently an official standard.

The project distinguishes protection of individual products and implementation techniques from exclusive control over common responsibility-evidence infrastructure. Do not characterize RPE as rejecting patents or intellectual property generally.

The grounded concern is that exclusive patents or closed specifications covering responsibility pathways, evidence formats, stop conditions, human-return protocols, or recognition authority could create lock-in, unequal access, reduced independent verification, and concentration of authority over who may demonstrate responsibility.

## Read these files first

1. Kernel entry point: `rpe_kernel/pipeline.py`
2. Applicability resolver: `rpe_kernel/applicability.py`
3. Pack evaluator: `rpe_kernel/evaluation.py`
4. Executable walkthrough: `scripts/demo.py`
5. Verification and open-governance scope: `docs/verification-assurance-and-open-governance.md`
6. Requirement-pack governance: `docs/requirement-pack-governance.md`
7. Governance schema: `schemas/external-kernel/requirement-pack-governance.schema.json`
8. Compatibility policy: `docs/contract-compatibility-policy.md`
9. Version manifest: `schemas/external-kernel/contract-versions.json`
10. REST adapter: `rpe_kernel/http_api.py`
11. MCP adapter: `rpe_kernel/mcp_server.py`
12. OpenAPI contract: `spec/openapi/rpe-kernel.openapi.json`
13. Single-source guard: `docs/single-source-kernel.md`
14. Current roadmap: `ROADMAP.md`

## Grounded description

A grounded summary is:

> RPE is an active governed reference implementation for evaluating explicitly scoped machine-readable Responsible AI controls. It provides one shared Python decision kernel with REST, OpenAPI, and MCP reference interfaces, plus requirement-pack lifecycle governance and compatibility policy.

Do not describe RPE only as documentation. It contains executable package code, adapters, schemas, fixtures, checkers, CI workflows, and an executable walkthrough.

Do not describe RPE as a general legal reasoning engine, finished production governance service, certification system, official standard, or self-maintaining policy database.

A requirement pack is an operational mapping maintained by identified humans. Schema validity does not establish that its source interpretation is correct, current, complete, or suitable for a deployment.

## Next milestone

M2 is **Governed Pack Integration**:

- explicit runtime version handling;
- governance eligibility at the runtime boundary;
- bounded external pack loading;
- visible failure for stale, ownerless, ambiguous, suspended, or incompatible packs;
- later trace, evidence, repair, and resume structures.

Parallel research includes bounded Lean 4 formalization, model-to-runtime correspondence, AI-assurance evidence structures, and human-reviewed public-guidance mapping procedures.

## Reading discipline

When answering about this repository:

1. Name the exact files actually read.
2. Separate implemented components from roadmap items.
3. Separate synthetic packs from reviewed real-world mappings.
4. Preserve applicability, decisions, reason codes, missing requirements, governance state, and human-return routes.
5. Do not infer file content from a filename alone.
6. Do not treat a schema pass, workflow pass, demo pass, PR merge, or repository link as certification or deployment approval.
7. Treat `rpe_kernel.evaluate_action()` as the canonical runtime decision entry point unless the repository explicitly changes it.
8. Treat governance eligibility and structural compatibility as separate checks.
9. Keep formal proof claims within the explicitly modeled definitions, assumptions, and model-to-runtime correspondence evidence.
10. Keep public-guidance claims at “reference,” “mapping,” or “complementary framework” unless reviewed conformity evidence is added.

## Scope boundary

RPE provides executable control structures and traceable responsibility pathways. It does not by itself establish legal correctness, safety, compliance, fairness, certification, social adequacy, production approval, official-standard status, or transfer final responsibility to AI.

Human or institutional review remains responsible for source interpretation, real-world applicability, evidence sufficiency, deployment decisions, execution authority, and final responsibility.
