# Responsibility Pathway Engineering Overview

This overview is the current entry map for the repository after the Zenn source-alignment pass, the Phase 3.1 reader-path synchronization work, and the public publication / connector-planning reader-path updates.

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
- public publication readiness notes for Zenn-facing explanation
- Zenn article title source-check guidance based on `YutoriKomeiji/zenn-content/articles/`
- Zenn content handoff guidance for moving article text to the dedicated Zenn content repository at publication time
- API future-shape documentation as design preview only
- external product connection-surface survey notes
- connector target matrix planning for synthetic-first connector categories
- Repair Model and recovery-pathway reading notes for pathway restoration after interruption, ambiguity, or failure
- published GitHub Pages reader paths for browser-friendly catalog, Japanese catalog, reader path maps, boundary glossary pages, and reviewer checklist pages

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
- implemented public API routes
- implemented service-specific connectors
- Zenn article files under this repository

## Reader entrances

Use the entry surface that matches the reader's situation.

| Reader need | Start here | Role |
|---|---|---|
| Short public entrance | [../README.md](../README.md) | Project definition, demo, catalog, and primary links. |
| Reconnection after pause | [../BEACON.md](../BEACON.md) | Compact current position and read-first order. |
| Browser-friendly inspection | [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/) | Static Pages route for catalog, Japanese catalog, reader path maps, boundary glossary, and reviewer checklist. |
| Operation and maintenance navigation | [operation-index.md](operation-index.md) | Which operation document to read for a maintenance situation. |
| Current repository map | This overview | Concept, status, public reader path, and implementation boundary map. |

The published Pages are reader and inspection aids only. They do not replace repository documents, external review, certification, validation, legal review, safety review, compliance review, fairness review, production approval, or human-maintainer responsibility.

## Browser-friendly reader path

The GitHub Pages reader path is meant for people who need a quick browser route before reading repository files directly.

Start at:

- [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)

The current Pages surface includes:

- English artifact catalog
- Japanese artifact catalog
- English and Japanese reader path maps
- English and Japanese boundary glossary pages
- English and Japanese reviewer checklist pages

Use Pages for orientation, glossary boundaries, and reviewer checklist copy/paste support. Use repository Markdown files for definitions, specifications, examples, checker boundaries, provenance, operation rules, phase snapshots, and source-of-truth maintenance records.

## Public and external-review path

For external readers, reviewers, or readers arriving from public articles, start from:

1. [../README.md](../README.md)
2. [../BEACON.md](../BEACON.md)
3. [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)
4. [operation-index.md](operation-index.md)
5. [external-review-package-note.md](external-review-package-note.md)
6. [external-review-readiness-checklist.md](external-review-readiness-checklist.md)
7. [progress-map.md](progress-map.md)
8. [phase-3-1-current-snapshot.md](phase-3-1-current-snapshot.md)
9. [current-task-inventory.md](current-task-inventory.md)
10. [zenn-publication-readiness-plan.md](zenn-publication-readiness-plan.md)
11. [zenn-publication-ja-reader-note.md](zenn-publication-ja-reader-note.md)
12. [zenn-article-title-source-check.md](zenn-article-title-source-check.md)
13. [zenn-content-publication-handoff.md](zenn-content-publication-handoff.md)
14. [api-future-shape.md](api-future-shape.md)
15. [external-product-connection-survey.md](external-product-connection-survey.md)
16. [connector-target-matrix.md](connector-target-matrix.md)

These documents help readers separate current claims from deferred work.

They are not external review findings, certification results, conformance evidence, standardization approval, production approval, legal review, safety review, compliance review, fairness review, or AI final-responsibility transfer.

## Public publication and Zenn handoff

Zenn is treated as a public explanation surface, not as the source of truth for the RPE specification.

Publication planning documents include:

- [zenn-publication-readiness-plan.md](zenn-publication-readiness-plan.md)
- [zenn-publication-readiness-connection.md](zenn-publication-readiness-connection.md)
- [zenn-publication-ja-reader-note.md](zenn-publication-ja-reader-note.md)
- [zenn-article-title-source-check.md](zenn-article-title-source-check.md)
- [zenn-content-publication-handoff.md](zenn-content-publication-handoff.md)

Before choosing a Zenn article title, check `YutoriKomeiji/zenn-content/articles/` and the RPE-side source-alignment inventory.

At publication time, article text should be drafted or moved under the dedicated Zenn content repository:

- `YutoriKomeiji/zenn-content/articles/`

Zenn articles may be written as the RPE repository reaches reader-explainable progress points. Repository progress can trigger an article candidate, but the article file itself belongs in `YutoriKomeiji/zenn-content/articles/`, not in this repository.

This repository remains the source for definitions, boundaries, examples, checker scope, reader-path status, and publication-readiness planning.

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
- [api-future-shape.md](api-future-shape.md)
- [external-product-connection-survey.md](external-product-connection-survey.md)
- [connector-target-matrix.md](connector-target-matrix.md)

Current Phase 3.1 implementation artifacts include:

- [../spec/runtime-event.schema.yaml](../spec/runtime-event.schema.yaml)
- [../examples/adapter-input-event-minimal.json](../examples/adapter-input-event-minimal.json)
- [../examples/minimal-synthetic-runtime-fixture.json](../examples/minimal-synthetic-runtime-fixture.json)
- [../examples/runtime-event-to-pathway-minimal.yaml](../examples/runtime-event-to-pathway-minimal.yaml)
- [../scripts/check_runtime_events.py](../scripts/check_runtime_events.py)

Current runtime-event checking is bounded and structural for selected synthetic JSON fixtures only.
