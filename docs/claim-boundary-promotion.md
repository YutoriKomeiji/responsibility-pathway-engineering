# Claim Boundary Promotion

RPE treats public claims as evidence-governed states. A current non-claim is not automatically a permanent disclaimer.

RPE distinguishes:

1. **evidence-limited milestone boundaries** that can move when declared engineering and field evidence is obtained and reviewed; and
2. **permanent responsibility boundaries** that an engineering kernel should not cross by itself.

## Current evidence boundary

RPE has moved beyond the M1-only implementation boundary and is now in **M2 implementation with the governed-integration baseline reached**.

Current engineering evidence supports:

- explicit strict governed contracts;
- governed contract-version checks;
- pack/governance binding;
- runtime governance eligibility;
- visible failure for major stale/ambiguous/ineligible/incompatible classes;
- legacy and governed Python/REST/MCP surfaces;
- governed OpenAPI coverage;
- bounded caller-content/local-file loading;
- explicit evaluation-only/no-authority handoff semantics;
- deterministic regression and CI checks for these repository surfaces.

Full M2 closure is **not yet claimed**. Remaining engineering evidence includes uncertainty/effect/evidence handoff semantics, repair/resume responsibility boundaries, residual-owner/Human Return continuity, adversarial validation, and closure review.

The current public implementation detail is recorded in [`m2-governed-integration-current.md`](m2-governed-integration-current.md).

## Promotion criteria

| Current boundary | Evidence that can move it |
|---|---|
| M2 governed-integration baseline / full M2 not yet closed | adversarial evidence for authority/effect/evidence confusion, repair/resume boundary behavior, residual-owner/Human Return continuity, declared closure criteria, and synchronized public claim review |
| No production deployment claim | deployment architecture, authentication/authorization boundaries, operational monitoring, fault-injection, upgrade/rollback and supported-environment evidence |
| No reviewed real-world normative mapping claim | source/version control, named human owners, applicability/interpretation records, conflict handling, review/approval state, expiry/supersession controls, and qualified independent review for each claimed mapping |
| No implementation-wide formal conformance | explicit formalization target, model-to-runtime correspondence/refinement relation, and reproducible evidence for the claimed implementation surface |
| No broader interoperability claim | independent implementation/client evidence against declared schemas, interfaces, compatibility policy and failure semantics |

Promotion is explicit. Completing an engineering milestone does not automatically promote legal, compliance, certification, production, or operational-authority claims.

## Permanent responsibility boundaries

- RPE does not automatically interpret law, policy, ethics, standards, or affected-party mandates.
- RPE does not create deployment approval, execution authority, certification, or legal compliance by itself.
- A schema-valid or loadable Requirement Pack does not prove that its source interpretation is correct, current, complete, or applicable.
- An RPE `allow` result is an evaluation result, not an execution authorization token.
- Evaluation evidence does not prove an external effect occurred.
- A receipt does not by itself establish verified effect.
- Repair readiness does not create repair authority.
- Resume authority belongs to the runtime/institution that owns execution and requires a separate authority-bearing transition.
- A gate result does not make an external action, external system, or business decision correct.
- Final legal, policy, assurance, deployment, and operational decisions remain with the responsible human or institution.
- Formal proof of an abstract model does not automatically prove the complete Python runtime, pack interpretation, or deployed system.

These are responsibility boundaries, not missing milestones.

## Evidence owners and promotion states

RPE engineering owns kernel, schema, interface, compatibility, failure-semantics, loader-boundary, and declared implementation evidence. Pack owners and qualified reviewers own source interpretation and mapping evidence. Integrators/operators own deployment, execution authority, external-effect, repair/resume, and operational evidence. Legal, certification, and final authorization decisions remain with qualified human/institutional authorities.

Where practical, evidence-limited boundaries use `evidence_collecting`, `review_ready`, or `promoted`; permanent boundaries use `permanently_out_of_scope`.
