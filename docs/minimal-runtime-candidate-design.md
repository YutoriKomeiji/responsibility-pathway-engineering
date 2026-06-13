# Minimal Runtime Candidate Design

This note records the narrowest acceptable shape for an early runtime candidate in Phase 3.1.

It is a design note only. It does not implement a runtime, connector, checker, workflow, adapter, production integration, approval system, execution system, certification system, legal decision system, safety certification system, compliance engine, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Purpose

The purpose is to decide what kind of minimal runtime artifact may be considered before service-specific connectors or production runtime integration.

The runtime candidate exists to create a small observable bridge between a synthetic runtime event and a draft Responsibility Pathway record.

It should help evaluate whether the repository can describe runtime observations without claiming production readiness, connector correctness, adapter correctness, schema correctness, JSON semantic correctness, legal validity, safety, compliance, fairness, moral resolution, or AI final-responsibility transfer.

## Allowed candidate shapes

Only one of the following should be considered first:

1. a minimal synthetic runtime fixture
2. a bounded runtime-checking stub

Do not create both in the same first implementation step.

The first candidate should be the smallest artifact that improves the ability to review the runtime boundary.

## Candidate A: minimal synthetic runtime fixture

A minimal synthetic runtime fixture may be considered if it remains:

- synthetic
- local to the repository
- vendor-neutral
- non-production
- review-required
- non-certifying
- disconnected from service-specific connectors
- disconnected from automatic approval
- disconnected from automatic execution
- explicit about missing context
- explicit about missing approval evidence
- explicit about missing execution evidence
- explicit about excluded claims

This candidate may be useful when the next question is whether the runtime observation shape is readable before any checker code exists.

It should not be described as a runtime implementation.

It should not claim that the runtime event schema is complete or correct.

## Candidate B: bounded runtime-checking stub

A bounded runtime-checking stub may be considered only after the runtime-event checking plan preconditions are satisfied.

The first stub should validate only one synthetic JSON fixture.

It should be structural and local.

It may check only simple shape-level requirements such as:

- JSON can be read
- expected top-level fields are present
- review requirement is explicit
- missing context is preserved
- approval evidence is not silently assumed
- execution evidence is not silently assumed
- excluded claims are present

It must not check:

- service connector behavior
- adapter mapping correctness
- production runtime behavior
- legal validity
- safety
- compliance
- fairness
- moral resolution
- production readiness
- responsibility assignment correctness
- completeness of the generated pathway record
- AI final-responsibility transfer

## Preferred first candidate

Prefer Candidate A before Candidate B if the repository still needs a clearer runtime reading example.

Prefer Candidate B only if the JSON fixture, runtime-event schema, event-to-pathway example, checker boundary, and repository operation path are stable enough that adding code will not blur the non-certifying boundary.

At the current roadmap point, Candidate A is usually lower risk than Candidate B.

## Preconditions before any runtime candidate

Before adding either candidate, confirm:

1. `spec/runtime-event.schema.yaml` remains small and readable.
2. `examples/adapter-input-event-minimal.json` remains synthetic, vendor-neutral, and review-required.
3. `examples/runtime-event-to-pathway-minimal.yaml` remains a readable draft generated record requiring human or institutional review.
4. The relation between the JSON fixture and the pathway example is explainable without service-specific connector assumptions.
5. Missing context, missing approval evidence, missing execution evidence, and excluded claims remain explicit.
6. Any future checker output can be described as a bounded repository-maintenance signal only.
7. Any future checker can fail safely without implying that passing examples are certified.
8. Documentation updates can be kept small and traceable through the operation model, operation index, current snapshot, checker coverage, roadmap notes, sync logs, or changelog milestones where appropriate.

## Stop conditions

Stop before adding a runtime candidate if it would require:

- service-specific connector assumptions
- production runtime integration
- production conversion code
- automatic approval
- automatic execution
- hidden human approval assumptions
- hidden execution evidence assumptions
- adapter mapping correctness claims
- schema correctness claims
- JSON semantic correctness claims
- service connector correctness claims
- legal validation claims
- safety certification claims
- compliance certification claims
- fairness certification claims
- moral-resolution claims
- production-readiness claims
- AI final-responsibility transfer claims

## Suggested first implementation path

If the candidate remains necessary after review, use this order:

1. update `docs/phase-3-1-roadmap-note.md` to name the selected candidate
2. add a minimal synthetic runtime fixture or design fixture, not production code
3. update `docs/example-index.md` only if the fixture changes how examples should be read
4. update `docs/checker-coverage.md` only if checker behavior changes or a planned checker boundary needs to be clarified
5. update `docs/phase-3-1-current-snapshot.md` after the artifact exists
6. defer checker code until the runtime-event checking plan preconditions remain satisfied after the fixture is added
7. defer workflow until local checker behavior exists and has been observed

## Current decision

A minimal runtime candidate is allowed only as a planning target.

No production runtime integration is allowed.

No service-specific connector is allowed.

No runtime-event checker is implemented by this note.

No runtime workflow is implemented by this note.

The current preferred next artifact, if the runtime path is opened, is a minimal synthetic runtime fixture rather than a checker stub.
