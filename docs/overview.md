# Responsibility Pathway Engineering Overview

This overview is the current entry map for the repository after the Zenn source-alignment pass and the Phase 3.1 reader-path synchronization work.

It explains what Responsibility Pathway Engineering currently means in this repository, what it does not claim, and where to go next.

## One-line definition

Responsibility Pathway Engineering is a bounded design approach for making AI-involved judgment and action returnable, stoppable, reconstructable, and repairable through human, organizational, and operational responsibility structures.

## Central question

RPE asks:

> When AI participates in judgment or action, where does responsibility arise, where does it move, where can it stop, where can it return to humans, what evidence remains, and who repairs?

This is different from asking only:

- whether the model was accurate
- whether a human approval button existed
- whether a role was named in a RACI table
- whether a guardrail blocked an action
- whether a log entry exists

Those may all matter, but none of them alone establishes a responsibility pathway.

## Current source-aligned interpretation

The reviewed source material supports the following interpretation:

- RPE does not make AI responsible.
- RPE does not replace RACI, HITL, Guardrails, ISO/IEC 42001, or human oversight.
- RPE designs how responsibility flows around AI-mediated judgment and action.
- RPE is operation-oriented, but not itself a production runtime.
- RPE requires explicit boundaries for what examples, schemas, checkers, and Lean files do not claim.

## Current repository status

The repository is currently in Phase 3.1: Adapter Boundary and Runtime Event Bridge.

The current public specification contains:

- definitions and design notes
- minimal examples
- bounded structural checkers
- review-result schema and fixtures
- minimal Lean formalization of scoped invariants
- source-alignment notes and synthesis
- adapter-boundary and runtime-event bridge notes
- a draft vendor-neutral runtime-event schema
- selected synthetic runtime-event JSON fixtures
- a bounded runtime-event checker for selected synthetic JSON fixtures
- observed bounded runtime-event workflow results
- external-review readiness and package notes
- rough planning-only progress and gate mapping

The repository does not yet contain:

- production runtime
- production verifier
- production connector
- legal responsibility engine
- compliance tool
- safety certification tool
- fairness certification tool
- complete action-class checker
- event-to-pathway semantic checker
- production runtime-event schema validation
- formal try/catch/finally semantics
- conformance model
- finished standardization claim

## Public and external-review path

For external readers, reviewers, or readers arriving from public articles, start from:

1. [../README.md](../README.md)
2. [../BEACON.md](../BEACON.md)
3. [operation-index.md](operation-index.md)
4. [external-review-package-note.md](external-review-package-note.md)
5. [external-review-readiness-checklist.md](external-review-readiness-checklist.md)
6. [progress-map.md](progress-map.md)
7. [phase-3-1-current-snapshot.md](phase-3-1-current-snapshot.md)
8. [current-task-inventory.md](current-task-inventory.md)

These documents help readers separate current claims from deferred work.

They are not external review findings, certification results, conformance evidence, standardization approval, production approval, legal review, safety review, compliance review, fairness review, or AI final-responsibility transfer.

## Two-layer model

The repository currently uses two related layers.

| Layer | Purpose | Where to read |
|---|---|---|
| Eight-element model | Structural dimensions that preserve responsibility returnability. | [eight-elements.md](eight-elements.md) |
| Operational roles and controls | Concrete workflow roles/checkpoints for AI-involved operations. | [concepts/core-elements.md](concepts/core-elements.md) |

The eight-element model is the broader structural layer:

- Meaning
- Authority
- Time
- Quality
- Trust
- Reversibility
- Value
- Cost

The operational role/control set is the current source-aligned implementation-facing layer:

- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Evidence Log
- Repair Owner
- Human Return Point

These are not competing lists. The seven operational roles/controls are practical pathway checkpoints that help preserve or inspect the eight structural dimensions in AI-involved workflows.

## Operational roles and controls

| Role / control | Role |
|---|---|
| Decision Owner | Owns the judgment or decision responsibility. |
| Approval Gate | Defines where approval is required before action. |
| Execution Actor | Performs or triggers the action. |
| Stop Authority | Can stop, suspend, or downgrade the action path. |
| Evidence Log | Supports reconstruction of the pathway. |
| Repair Owner | Owns rollback, repair, correction, or reconnection. |
| Human Return Point | Allows AI-mediated judgment to return to human understanding, authority, time, and responsibility capacity. |

## AI participation boundary

AI may participate as:

- classifier
- summarizer
- draft proposer
- recommendation generator
- tool-using actor under configured authority
- trace producer
- monitoring assistant
- local judgment node inside a bounded pathway, when evaluator separation and human or institutional return gates remain visible

But under the current minimal assumptions, AI is not treated as a final responsibility holder.

Examples and schemas should preserve this boundary explicitly.

## Neighboring concepts

RPE is close to several existing concepts, but it asks a different question.

| Neighboring concept | Main question | RPE distinction |
|---|---|---|
| RACI | Who has which role? | How does responsibility move, stop, return, and repair? |
| HITL | Where does a human check? | What if human review becomes formal, skipped, overloaded, or ineffective? |
| Guardrails | What should not be allowed? | Who owns pending responsibility after a stop or failure? |
| Harness Engineering | How does the agent run stably? | Stable execution is not responsibility readiness. |
| Meaningful Human Control | Is human control meaningful? | Can responsibility still be traced and returned if control degrades? |
| Accountability gap | Where does responsibility become unclear? | Design the pathway so gaps are less likely to arise. |
| Human oversight | Can humans supervise or intervene? | What happens after intervention, non-intervention, stop, or repair? |

## Action Class Matrix

The source-aligned Action Class Matrix is maintained in [action-class-matrix.md](action-class-matrix.md).

It classifies AI-agent actions by:

- impact
- reversibility
- externality
- approval requirement

Current source-aligned classes:

1. Class A: Observe-Only
2. Class B: Suggest-Only
3. Class C: Approval-Required
4. Class D: Reversible External Action
5. Class E: Irreversible or High-Impact Action
6. Class F: Emergency Stop

Action class should influence:

- approval strength
- evidence requirement
- stop condition
- human-return condition
- repair ownership

A pathway should not claim sufficiency without considering action class.

Class E positive examples remain deferred.

## Phase 3.1 runtime-event bridge

Phase 3.1 connects adapter-boundary and runtime-event concepts to draft Responsibility Pathway records.

Important Phase 3.1 documents include:

- [adapter-boundary.md](adapter-boundary.md)
- [phase-3-1-current-snapshot.md](phase-3-1-current-snapshot.md)
- [runtime-event-schema-fixture-alignment.md](runtime-event-schema-fixture-alignment.md)
- [event-to-pathway-relation-checker-plan.md](event-to-pathway-relation-checker-plan.md)
- [runtime-event-workflow-current-status.md](runtime-event-workflow-current-status.md)
- [phase-3-1-progress-map-connection.md](phase-3-1-progress-map-connection.md)

Current Phase 3.1 implementation artifacts include:

- [../spec/runtime-event.schema.yaml](../spec/runtime-event.schema.yaml)
- [../examples/adapter-input-event-minimal.json](../examples/adapter-input-event-minimal.json)
- [../examples/minimal-synthetic-runtime-fixture.json](../examples/minimal-synthetic-runtime-fixture.json)
- [../examples/runtime-event-to-pathway-minimal.yaml](../examples/runtime-event-to-pathway-minimal.yaml)
- [../scripts/check_runtime_events.py](../scripts/check_runtime_events.py)

Current runtime-event checking is bounded and structural for selected synthetic JSON fixtures only.

It is not schema validation, JSON semantic correctness proof, adapter mapping correctness proof, runtime correctness proof, production readiness, certification, or event-to-pathway semantic correctness proof.

## Evidence, stop, return, and repair

The source-alignment pass strongly reinforces four design concerns.

### Evidence

Evidence Log is not merely an event log. It supports reconstruction of the responsibility pathway.

Useful evidence can include:

- request
- context
- AI proposal
- proposal adopter
- planned review
- actual review
- skipped review and reason
- approval
- execution
- stop
- rollback
- restart approval
- repair

### Stop

Stop Authority is not merely a technical abort.

It asks:

- who can stop
- under what conditions
- whether stop authority is separated from execution authority
- who owns pending responsibility after stop

### Return

Human Return Point is not merely human presence.

It asks whether AI-mediated judgment can return to human understanding, authority, time, information, and responsibility capacity.

### Repair

Repair Owner is not simply blame assignment.

Repair may include:

- rollback
- correction
- explanation
- incident response
- permanent countermeasure connection
- organizational responsibility rebundling

## Try/catch/finally analogy

A developer-facing analogy is available in [explanations/try-catch-finally-responsibility-pathway.md](explanations/try-catch-finally-responsibility-pathway.md).

Short version:

```text
try      = normal judgment / approval / execution path
catch    = stop / abnormal return / exception handling path
finally  = evidence / repair / explanation / closure path
```

This is only an explanatory analogy. It is not formal semantics.

## Recommended next work

Recommended next work should be chosen from [current-task-inventory.md](current-task-inventory.md) and checked against [deferred-work-restart-conditions.md](deferred-work-restart-conditions.md).

At the current stage, low-risk work is preferred:

1. Keep README, README.ja, BEACON, operation-index, overview, current-task-inventory, progress-map, and Phase 3.1 notes aligned.
2. Keep external-review package and readiness checklist reachable without treating them as review results.
3. Keep checker coverage and example index aligned with actual checker behavior.
4. Keep event-to-pathway relation checker work as planning only until preconditions are deliberately reviewed.
5. Keep production connectors, production runtime integration, conformance claims, schema validation, semantic checking, Class E positive examples, and Lean expansion deferred unless explicitly reopened.

## Boundary

This overview does not claim:

- legal validity
- safety assurance
- compliance
- certification
- production readiness
- fairness validation
- moral accountability resolution
- conformance status
- finished standardization
- runtime correctness
- connector correctness
- schema semantic correctness
- event-to-pathway semantic correctness
- AI final-responsibility transfer

It is an orientation map for the repository's current public specification work.
