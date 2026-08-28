# Claim Boundary Promotion

RPE treats public claims as evidence-governed states. A current non-claim is not automatically a permanent disclaimer.

RPE distinguishes:

1. **evidence-limited milestone boundaries** that can move when declared engineering and field evidence is obtained and reviewed; and
2. **permanent responsibility boundaries** that an engineering kernel should not cross by itself.

## Current evidence boundary

RPE is currently at **M1 Governed Reference Kernel**. M1 evidence supports the deterministic reference kernel, applicability resolution, multi-pack evaluation, reference interfaces, lifecycle/maintenance governance, compatibility rules, schemas, fixtures, checkers, and CI guards described in the repository.

M1 does not yet include external pack loading, governance enforcement inside `evaluate_action()`, production deployment controls, reviewed real-world requirement mappings, or implementation-wide formal conformance.

## Promotion criteria

| Current boundary | Evidence that can move it |
|---|---|
| M1 only / no governed external pack integration | M2 implementation and tests for bounded external pack loading, runtime governance eligibility, visible stale/ownerless/ambiguous/suspended/incompatible handling, trace/evidence/repair/resume behavior |
| No production deployment claim | deployment architecture, authentication/authorization boundaries, operational monitoring, fault-injection, upgrade/rollback and supported-environment evidence |
| No reviewed real-world normative mapping claim | source/version control, named human owners, applicability/interpretation records, conflict handling, review/approval state, expiry/supersession controls, and qualified independent review for each claimed mapping |
| No implementation-wide formal conformance | explicit formalization target, model-to-runtime correspondence/refinement relation, and reproducible evidence for the claimed implementation surface |
| No broader interoperability claim | independent implementation/client evidence against declared schemas, interfaces, compatibility policy and failure semantics |

Promotion is explicit. Completing a milestone does not automatically promote legal, compliance, certification, production, or operational-authority claims.

## Permanent responsibility boundaries

- RPE does not automatically interpret law, policy, ethics, standards, or affected-party mandates.
- RPE does not create deployment approval, execution authority, certification, or legal compliance by itself.
- A schema-valid Requirement Pack does not prove that its source interpretation is correct, current, complete, or applicable.
- A gate result does not make an external action, external system, or business decision correct.
- Final legal, policy, assurance, deployment, and operational decisions remain with the responsible human or institution.
- Formal proof of an abstract model does not automatically prove the complete Python runtime, pack interpretation, or deployed system.

These are responsibility boundaries, not missing milestones.

## Evidence owners and promotion states

RPE engineering owns kernel, schema, interface, compatibility, failure-semantics, and declared implementation evidence. Pack owners and qualified reviewers own source interpretation and mapping evidence. Integrators/operators own deployment and operational evidence. Legal, certification, and final authorization decisions remain with qualified human/institutional authorities.

Where practical, evidence-limited boundaries use `evidence_collecting`, `review_ready`, or `promoted`; permanent boundaries use `permanently_out_of_scope`.
