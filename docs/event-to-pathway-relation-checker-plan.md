# Event-to-Pathway Relation Checker Plan

This document plans a possible future bounded checker for the relation between a runtime-event fixture and a draft Responsibility Pathway record.

It is a plan only. It does not implement a checker, validate semantic correctness, prove responsibility assignment correctness, validate adapter mapping correctness, validate schema correctness, validate JSON semantic correctness, validate runtime correctness, establish conformance evidence, approve production use, or transfer final responsibility to AI.

## Purpose

The purpose is to define which relation signals may be checked structurally before any event-to-pathway relation checker is implemented.

The checker, if later implemented, should help maintainers detect missing or broken traceability between:

- a selected synthetic runtime-event JSON fixture
- a selected draft pathway YAML example derived from or aligned with that event
- recorded evidence and missing-context signals
- review requirement signals
- excluded-claim boundaries

The purpose is not to decide whether the pathway record is semantically correct, legally valid, safe, compliant, fair, complete, production ready, or morally resolved.

## Current related artifacts

Current Phase 3.1 artifacts relevant to this plan:

- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`
- `scripts/check_runtime_events.py`
- `scripts/check_examples.py`
- `docs/adapter-boundary.md`
- `docs/runtime-event-checking-plan.md`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/checker-coverage.md`
- `docs/example-index.md`
- `docs/external-review-readiness-checklist.md`

## Current checker separation

The current checker separation must be preserved:

- `scripts/check_runtime_events.py` checks selected JSON fixtures for bounded structural runtime-event or runtime-boundary signals.
- `scripts/check_examples.py` checks pathway YAML examples for bounded structural pathway signals.
- Neither checker currently checks the relation between the runtime-event JSON fixture and the pathway YAML example.
- Neither checker validates semantic correctness, adapter correctness, runtime correctness, or responsibility assignment correctness.

A future relation checker must not blur this separation.

## Candidate relation inputs

A future relation checker may initially consider only explicitly selected local files, for example:

- source runtime-event fixture: `examples/adapter-input-event-minimal.json`
- target pathway example: `examples/runtime-event-to-pathway-minimal.yaml`

A later plan may consider whether `examples/minimal-synthetic-runtime-fixture.json` should be checked only as an indirect runtime-boundary observation source.

Do not infer production runtime behavior from these fixtures.

## Structurally checkable relation signals

A future checker may inspect structural signals such as:

### Source reference preservation

- The pathway example contains an explicit reference to the source runtime-event identity or source-event identifier.
- The source reference is present in a predictable field or metadata block.
- The source reference is not empty.

Boundary: this checks presence and rough traceability only. It does not prove that the mapping is correct.

### Review requirement preservation

- If the runtime-event fixture records human or institutional review as required, the pathway example preserves a human or institutional review requirement.
- The pathway example does not claim automatic final approval by AI.
- The pathway example preserves a return point to human or institutional judgment.

Boundary: this does not validate the quality, sufficiency, legality, fairness, or actual performance of review.

### Evidence and missing-context preservation

- Evidence references from the runtime-event fixture are represented in the pathway example.
- Missing fields or missing context from the runtime-event fixture are not silently erased.
- Uncertainty notes or review reasons remain visible where the pathway example has a place to preserve them.

Boundary: this does not decide whether evidence is true, complete, sufficient, admissible, or semantically interpreted correctly.

### Actor and responsibility-boundary preservation

- AI-related actor signals do not become AI final-responsibility claims in the pathway example.
- The pathway example preserves a non-final AI responsibility boundary where applicable.
- Human, institutional, or review roles remain explicit enough for a reviewer to inspect.

Boundary: this does not prove responsibility assignment correctness or legal responsibility.

### Excluded-claim preservation

- The pathway example includes excluded-claim boundaries compatible with the runtime-event fixture and repository policy.
- Expected non-certifying boundaries remain visible.

Boundary: this does not certify that every relevant excluded claim has been identified.

### Lifecycle compatibility

- The generated or aligned pathway example declares a lifecycle state compatible with being an initial draft record, such as `originating`, unless a future plan explicitly allows another lifecycle state.
- The lifecycle-specific structural signals required by `scripts/check_examples.py` remain present.

Boundary: this does not prove lifecycle correctness in a real process.

## Signals that must not be checked as correctness

A future relation checker must not claim to check:

- semantic correctness of event-to-pathway transformation
- responsibility assignment correctness
- adapter mapping correctness
- connector behavior correctness
- runtime behavior correctness
- production workflow correctness
- schema completeness
- JSON semantic correctness
- legal validity
- safety
- compliance
- fairness
- moral resolution
- institutional approval quality
- conformance
- certification
- production readiness
- AI final-responsibility transfer

If any future checker rule starts to imply one of these claims, stop and revise the plan before implementation.

## Allowed implementation shape

If implemented later, the first relation checker should remain small and explicit.

Allowed shape:

- local script only
- selected fixture/example pair only
- no network calls
- no connector calls
- no production runtime calls
- no service-specific behavior
- no schema-wide validation
- no semantic model
- no LLM judgment
- simple structural presence checks
- clear warning/error messages
- bounded interpretation documented in `docs/checker-coverage.md`

Possible name:

- `scripts/check_event_to_pathway_relation.py`

Possible default checked pair:

- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`

## Required preconditions before implementation

Before implementing a relation checker, confirm that:

1. `docs/runtime-event-schema-fixture-alignment.md` remains current.
2. `docs/example-index.md` still distinguishes JSON fixtures from pathway YAML examples.
3. `docs/checker-coverage.md` still distinguishes current checker behavior from planned checker behavior.
4. `docs/runtime-event-checking-plan.md` still supports the intended expansion boundary.
5. `examples/adapter-input-event-minimal.json` remains the selected synthetic runtime-event JSON fixture.
6. `examples/runtime-event-to-pathway-minimal.yaml` remains the selected pathway YAML example for this relation.
7. The desired relation fields are already visible and stable enough to check without inventing semantic rules.
8. The first implementation can remain local, structural, and non-certifying.

## Required documentation updates if implemented

If a relation checker is later implemented, update at minimum:

- `docs/checker-coverage.md`
- `docs/example-index.md`
- `docs/runtime-event-checking-plan.md`
- `docs/runtime-event-schema-fixture-alignment.md` if alignment interpretation changes
- `docs/current-task-inventory.md`
- `docs/operation-index.md` if the reader path changes
- `BEACON.md` only if restart guidance changes

Do not update public-facing claims unless the boundary remains clear and non-certifying.

## Stop conditions

Stop before implementation if:

- the desired rule requires semantic judgment
- the desired rule requires adapter correctness judgment
- the desired rule requires connector or runtime behavior
- the desired rule requires production data
- the desired rule requires LLM interpretation
- the desired rule would imply conformance evidence or certification
- the target fixture/example pair is unstable
- the intended checked fields are not explicitly present
- the checker would become broad enough to obscure its bounded purpose

## Current next step

Current safe next step is not implementation.

The next safe step is to connect this plan from operation and task navigation documents if it improves restartability and reviewability.

Implementation should remain deferred until the preconditions above are deliberately reviewed.
