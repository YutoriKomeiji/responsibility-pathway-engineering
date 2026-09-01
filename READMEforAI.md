# README for AI / Search Readers

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for evaluating explicitly scoped machine-readable Responsible AI controls.

Human repository entrance:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering
```

## Grounded current summary

RPE has moved beyond the M1-only implementation boundary. It is currently in **M2 implementation with the governed-integration baseline reached**. Full M2 closure is not yet claimed.

Current public status: `docs/m2-governed-integration-current.md`.

Implemented now:

- deterministic applicability resolution and single-/multi-pack evaluation;
- legacy/M1-compatible Python entry `rpe_kernel.evaluate_action()`;
- explicit strict governed entry `rpe_kernel.evaluate_governed_action()`;
- explicit governed contract families and contract-version handling;
- exact Requirement Pack/governance identity and version binding;
- strict runtime governance eligibility with visible fail-closed outcomes;
- structured `allow`, `hold`, `human_gate`, and `deny` decisions;
- explicit governed responsibility handoff with `authority_effect = none` and `decision_scope = evaluation_only`;
- legacy and governed REST reference routes;
- legacy and governed MCP stdio tools;
- OpenAPI 3.1 coverage for admission, compatibility, governance, applicability, and evaluation stages;
- packaged OpenAPI with repository/package/runtime drift checks;
- bounded caller-content and local-file governed-envelope loading;
- explicit rejection of network/registry loading in the first loader;
- schemas, synthetic fixtures, deterministic checkers, and CI guards.

The strict governed path is:

```text
governed envelope admission
        ↓
contract compatibility
        ↓
pack ↔ governance binding
        ↓
governance eligibility
        ↓
applicability resolution
        ↓
requirement evaluation
        ↓
decision combination
        ↓
responsibility-preserving handoff
```

The legacy path remains available for compatibility. Do not conflate it with the strict governed path.

## Critical authority boundary

An RPE `allow` is an **evaluation result**, not an execution authorization token.

Do not infer that RPE:

- dispatches or executes an external action;
- approves deployment;
- verifies that an external effect occurred;
- turns a receipt into verified effect evidence;
- grants repair authority because repair is possible;
- grants resume authority because a blocked path is ready to continue;
- transfers final responsibility to AI.

Evaluation evidence is not effect evidence. Repair readiness is not repair authority. Resume authority belongs to the runtime/institution that owns execution and requires a separate authority-bearing transition.

## Loader boundary

The first governed loader accepts only:

- caller-provided UTF-8 JSON content;
- explicitly supplied local files.

It does not fetch URLs, discover registries, install packages, or establish source trust.

A readable local file proves only that bytes were available at that path. It does not prove source authority, interpretation correctness, governance eligibility, legal validity, or current applicability.

## Current M2 non-closure items

Do not describe M2 as fully closed yet. Remaining work includes:

- uncertainty/effect/evidence handoff semantics;
- repair/resume responsibility boundaries;
- residual-owner and Human Return continuity;
- adversarial tests for authority confusion, evidence confusion, governance/binding failures, adapter drift, and loader-boundary violations;
- final claim-boundary and closure evidence review.

## Production and normative exclusions

Do not infer that the current repository includes:

- production authentication, authorization, persistence, tenancy, secrets, rate limiting, or deployment controls;
- automatic source interpretation or self-maintaining regulatory knowledge;
- reviewed real-world law or guideline mappings by default;
- certification, conformity assessment, official-standard status, or legal/compliance proof;
- formal verification of the complete Python runtime or external system.

## Verification and assurance scope

RPE uses **verifiable AI** in a bounded sense. It aims to make assumptions, requirement mappings, applicability, decisions, stop conditions, reason codes, governance state, compatibility state, missing evidence, and Human Return routes inspectable and re-checkable.

Planned or partial formalization may prove properties of explicitly modeled responsibility pathways under stated assumptions. Do not extend such proof into claims about the complete Python runtime, external services, input data, human conduct, Requirement Pack interpretation, legal validity, social adequacy, production safety, or the full AI system without separate correspondence evidence.

RPE treats AI assurance as accumulation of scoped requirements, decision records, evidence, verification results, governance ownership, and explicit proof boundaries—not as a blanket declaration that an AI system is safe.

## Public-guidance boundary

Official public guidance may inform future human-reviewed Requirement Packs.

Do not claim that RPE currently:

- officially implements a public guideline or law;
- conforms or complies with it;
- automatically interprets it;
- provides reviewed real-world Requirement Packs derived from it by default;
- has government adoption or endorsement.

Use language such as “references,” “may inform a human-reviewed mapping,” “makes related responsibility pathways more explicit,” or “is a complementary engineering framework” unless stronger evidence exists.

## Open-governance position

RPE is MIT-licensed. It aims for open specifications, interoperability, independent verification, and multiple-implementation potential. It is not currently an official standard.

## Read these files first

1. Current M2 status: `docs/m2-governed-integration-current.md`
2. Kernel entry points: `rpe_kernel/pipeline.py`
3. Bounded loader: `rpe_kernel/loader.py`
4. Applicability resolver: `rpe_kernel/applicability.py`
5. Pack evaluator: `rpe_kernel/evaluation.py`
6. Requirement-pack governance: `docs/requirement-pack-governance.md`
7. Compatibility policy: `docs/contract-compatibility-policy.md`
8. Version manifest: `schemas/external-kernel/contract-versions.json`
9. REST adapter: `rpe_kernel/http_api.py`
10. MCP adapter: `rpe_kernel/mcp_server.py`
11. OpenAPI contract: `spec/openapi/rpe-kernel.openapi.json`
12. Claim boundary: `docs/claim-boundary-promotion.md`
13. Current roadmap: `ROADMAP.md`
14. Historical M2 entry plan: `docs/m2-governed-pack-integration-entry-plan.md`

## Grounded description

A grounded current summary is:

> RPE is an active governed reference implementation for evaluating explicitly scoped machine-readable Responsible AI controls. It provides legacy and strict governed evaluation paths, runtime compatibility/governance checks, responsibility-preserving no-authority handoff, bounded local/caller-content loading, and REST/OpenAPI/MCP reference interfaces. M2 is still in progress and production/legal/execution-authority claims remain outside the current evidence boundary.

Do not describe RPE only as documentation. It contains executable package code, adapters, schemas, fixtures, checkers, CI workflows, and synthetic demonstrations.

Do not describe RPE as a general legal reasoning engine, finished production governance service, certification system, official standard, self-maintaining policy database, or execution controller.

A Requirement Pack is an operational mapping maintained by identified humans. Schema validity or loader success does not establish that its source interpretation is correct, current, complete, or suitable for a deployment.

## Reading discipline

When answering about this repository:

1. Name the exact files actually read.
2. Separate implemented components from roadmap items.
3. Separate M1 compatibility behavior from strict M2 governed behavior.
4. Separate synthetic packs from reviewed real-world mappings.
5. Preserve compatibility, governance, applicability, decisions, reason codes, missing requirements, and Human Return routes.
6. Do not infer file content from a filename alone.
7. Do not treat a schema pass, loader success, workflow pass, demo pass, PR merge, or repository link as certification or deployment approval.
8. Treat `evaluate_governed_action()` as the strict governed evaluation entry and `evaluate_action()` as the retained legacy/M1-compatible entry.
9. Treat governance eligibility, structural compatibility, source trust, and real-world interpretation correctness as separate questions.
10. Keep formal proof claims within explicitly modeled definitions, assumptions, and correspondence evidence.
11. Keep public-guidance claims at “reference,” “mapping,” or “complementary framework” unless reviewed conformity evidence is added.
12. Never turn an RPE `allow` into execution authority without a separate authority-bearing system decision.

## Construction boundary

RPE is developed through Open Construction with Luminalia AI assistance. Human maintainer judgment remains responsible for direction, merge, publication, external claims, deployment decisions, and final responsibility.
