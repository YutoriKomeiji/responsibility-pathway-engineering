# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary, runtime event bridge, runtime-event checking plan, first bounded runtime-event checker stub, first minimal runtime-event workflow, observed runtime-event workflow success, minimal runtime candidate planning, minimal synthetic runtime fixture, minimal runtime fixture review, progress map, responsibility pathway availability, current task inventory, and repository operation layer.

Phase 3.1 is the bridge from external logs, API events, workflow results, and runtime observations into draft Responsibility Pathway records.

It is not a production connector, production runtime, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, progress certification, or AI final-responsibility transfer mechanism.

## Current artifacts

Current Phase 3.1 artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`
- `scripts/check_runtime_events.py`
- `.github/workflows/check-runtime-events.yml`
- `docs/runtime-event-checker-local-observation.md`
- `docs/runtime-event-workflow-current-status.md`
- `docs/runtime-event-checking-plan.md`
- `docs/minimal-runtime-candidate-design.md`
- `docs/minimal-runtime-fixture-review.md`
- `docs/minimal-runtime-fixture-review-connection.md`
- `docs/progress-map.md`
- `docs/responsibility-pathway-availability.md`
- `docs/current-task-inventory.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/phase-3-1-roadmap-note.md`
- `docs/repository-operation-model.md`
- `docs/operation-index.md`

Repository-wide reader-path and operation records now also include:

- `README.md`
- `README.ja.md`
- `BEACON.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `docs/checker-coverage.md`
- `docs/example-index.md`
- `docs/standardization-strategy.md`

## Adapter boundary

`docs/adapter-boundary.md` defines the planned adapter layer as a support layer that may extract, normalize, summarize, classify, and transform external event data into draft Responsibility Pathway records.

An adapter may support:

- source event extraction
- event-field normalization
- source reference preservation
- candidate action-class suggestion
- candidate role detection
- uncertainty and missing-context recording
- draft record generation for human or institutional review

An adapter must not decide responsibility, approve actions, certify records, prove safety, prove compliance, resolve legal or moral responsibility, or transfer final responsibility to AI.

## Runtime event schema

`spec/runtime-event.schema.yaml` defines a minimal vendor-neutral input event shape.

The first runtime event schema is intentionally small. It preserves:

- event identity
- schema version
- source system
- observation timestamp
- observed actor
- observed action
- observed target
- evidence and missing-context notes
- review requirement
- excluded claims

The schema is draft-only and does not assume a vendor-specific connector.

## Minimal input fixture

`examples/adapter-input-event-minimal.json` is the first synthetic runtime event input fixture.

The fixture models an AI support agent drafting an internal document update proposal.

The fixture explicitly records that:

- the source system is synthetic and vendor-neutral
- the observed actor is an AI agent
- the AI agent does not claim final responsibility
- the event is a draft proposal only
- human approval evidence is missing
- execution evidence is missing
- human or institutional review is required
- the proposed action class is an adapter suggestion, not certification

## Event-to-pathway example

`examples/runtime-event-to-pathway-minimal.yaml` is the first runtime-event-to-pathway draft example.

It maps the synthetic runtime event into a Responsibility Pathway record with:

- lifecycle state `originating`
- AI support agent node
- human decision owner node
- internal document system node
- return-to-authority edge
- possible future execution edge after human approval
- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Repair Owner
- Evidence Log
- Human Return Point
- review requirement
- adapter boundary fields
- excluded claims

The generated pathway record remains a draft requiring human review.

## Runtime-event checking plan

`docs/runtime-event-checking-plan.md` defines the path for adding bounded runtime-event and JSON-fixture checks.

A first bounded runtime-event checker stub now exists at `scripts/check_runtime_events.py`.

A first minimal runtime-event workflow now exists at `.github/workflows/check-runtime-events.yml`.

The plan records:

- what the first bounded runtime-event checker stub currently checks
- what future runtime-event checker work may inspect
- what the first checker layer must not inspect
- preconditions before adding a runtime-event workflow expansion, schema checker, minimal-runtime-fixture checker, service connector check, or broader runtime-event checker
- suggested next implementation order
- the boundary for passing checks
- the current decision that schema checking, minimal-runtime-fixture checking, connectors, production runtime, semantic checking, workflow expansion, and AI final-responsibility transfer remain deferred or out of scope

The plan does not certify schema correctness, JSON fixture semantic correctness, adapter mapping correctness, service-specific connector behavior, production runtime behavior, workflow stability, legal validity, safety, compliance, fairness, moral resolution, production readiness, or AI final-responsibility transfer.

## Bounded runtime-event checker stub

`scripts/check_runtime_events.py` is the first bounded runtime-event checker stub.

It checks `examples/adapter-input-event-minimal.json` by default and performs only local structural checks on the selected synthetic runtime-event JSON fixture.

The checker currently inspects only whether:

- the selected file is parseable JSON
- the top-level JSON value is a mapping
- required top-level runtime-event fields are present
- `source_system.vendor_specific` is explicitly `false`
- the first minimal fixture remains synthetic or warns if it does not
- an AI-agent observed actor does not claim final responsibility
- `evidence.captured_fields` is a non-empty list
- `evidence.missing_fields` is present as a list
- `evidence.uncertainty_notes` is present as a list
- `evidence.raw_event_available` is explicitly `true`
- `review_requirement.human_or_institutional_review_required` is explicitly `true`
- `review_requirement.reason` is present
- `excluded_claims` includes the expected non-certifying boundary items

## Local and workflow observation status

`docs/runtime-event-checker-local-observation.md` records the first local observation of `scripts/check_runtime_events.py` against `examples/adapter-input-event-minimal.json`.

The local observation recorded:

```text
exit code: 0
PASS: bounded runtime-event checks completed without failures
```

`docs/runtime-event-workflow-current-status.md` records the first observed runtime-event workflow success.

Observed workflow run:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/runs/27501847137
```

Observed job:

```text
job id: 81286034329
job name: Bounded runtime-event checks
job status: completed
job conclusion: success
step: Run bounded runtime-event checker: completed / success
```

A local or workflow pass may mean only that the selected synthetic runtime-event JSON fixture satisfies the bounded structural requirements implemented by the local checker or that the bounded checker completed successfully in GitHub Actions for that workflow run. It is not schema validation, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, runtime correctness proof, production readiness, certification, legal review, safety review, compliance review, fairness review, moral-resolution evidence, or AI final-responsibility transfer.

## Minimal runtime candidate design

`docs/minimal-runtime-candidate-design.md` defines the narrowest acceptable shape for an early runtime candidate.

The design note exists before any runtime fixture, runtime checker expansion, runtime workflow expansion, connector, or production runtime implementation.

It allows only one first candidate:

- a minimal synthetic runtime fixture
- or a bounded runtime-checking stub

The first minimal synthetic runtime fixture, first bounded runtime-event checker stub, and first minimal workflow are now separate bounded artifacts. They do not together create a production runtime or connector.

The candidate must remain non-production, synthetic, local to the repository, review-required, non-certifying, disconnected from service-specific connectors, disconnected from automatic approval or execution, and explicit about missing context, missing approval evidence, missing execution evidence, and excluded claims.

The design note does not implement a production runtime, connector, production integration, approval system, execution system, certification system, legal decision system, safety certification system, compliance engine, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Minimal synthetic runtime fixture

`examples/minimal-synthetic-runtime-fixture.json` is the first minimal synthetic runtime observation fixture.

It is a runtime-like observation point, not a runtime implementation.

The fixture is:

- non-production
- synthetic
- vendor-neutral
- local to the repository
- review-required
- non-certifying
- disconnected from service-specific connectors
- disconnected from automatic approval
- disconnected from automatic execution
- explicit about missing approval evidence
- explicit about missing execution evidence
- explicit about excluded claims

It references `examples/adapter-input-event-minimal.json` as the source event reference for the observed draft proposal.

The fixture is not currently checked by `scripts/check_examples.py` or `scripts/check_runtime_events.py` and does not unlock service-specific connector work, production conversion code, or production runtime integration.

## Minimal runtime fixture review

`docs/minimal-runtime-fixture-review.md` records the first review of `examples/minimal-synthetic-runtime-fixture.json` as a minimal synthetic runtime observation fixture for reading and review.

The first review found that the fixture is acceptable as a first minimal synthetic runtime observation fixture.

No change to `examples/minimal-synthetic-runtime-fixture.json` was required by that review.

`docs/minimal-runtime-fixture-review-connection.md` records the reader path connecting the review note to the current Phase 3.1 operation documents.

The review note and connection note do not unlock production runtime integration, service-specific connectors, production conversion code, runtime fixture checker implementation, schema correctness claims, JSON semantic correctness claims, adapter mapping correctness claims, connector correctness claims, responsibility assignment correctness claims, Class E positive examples, or Lean expansion around runtime events.

## Progress map

`docs/progress-map.md` records rough progress estimates, active gates, next gates, recommended order, and progress-related stop conditions for repository planning.

It exists because the repository has accumulated enough structure that progress needs a visible orientation map rather than an implicit feeling of movement.

The progress map is rough, planning-only, and non-certifying.

It does not certify progress, prove maturity, establish conformance, replace external review, prove standardization readiness, prove legal validity, prove safety, prove compliance, prove fairness, prove production readiness, prove connector correctness, prove runtime correctness, or transfer final responsibility to AI.

Use it before discussing progress percentage, next gates, maturity, world-standard candidate readiness, or progress-related stop conditions.

## Responsibility pathway availability

`docs/responsibility-pathway-availability.md` records how to handle narrowed, incomplete, noisy, or temporarily broken Responsibility Pathways during repository maintenance.

It distinguishes availability from completeness, reachability, recoverability, and continuity.

It records the minimum state to preserve when a pathway is degraded: intended operation, actual event, repository content change status, residual evidence, missing or unobserved evidence, continuation safety, and the judgment that should be returned to the human maintainer or explicit decision process.

The availability note is an operation note only. It does not turn degraded pathway states into certification, legal validity, safety, compliance, fairness, production readiness, connector correctness, runtime correctness, Lean completeness, public standardization claims, or AI final-responsibility transfer.

## Current task inventory

`docs/current-task-inventory.md` records the current P0-P4 task inventory across active and near-active phases.

Use it before selecting the next task, especially before checker work, workflow work, runtime work, Lean expansion, connector work, Class E examples, standardization claims, conformance-model drafting, or public-claim expansion.

For Phase 3.1, the inventory currently treats the first bounded runtime-event checker stub as implemented local structural checker work, records the first observed runtime-event workflow success as bounded workflow observation, keeps runtime fixture review as bounded artifact preparation, keeps `docs/progress-map.md` rough and planning-only, keeps `docs/responsibility-pathway-availability.md` reachable for degraded-pathway handling, and keeps runtime fixture checking, runtime-event workflow expansion, service-specific connectors, production conversion code, production runtime integration, Class E positive examples, support-call schema fields, missed-support schema fields, support-call semantic checking, missed-support correctness checking, conformance-model drafting, and Lean expansion around runtime events, support-call policy, or missed-support signals deferred or conditional.

The task inventory is a planning and prioritization note only. It is not certification, production approval, legal review, safety review, compliance review, fairness review, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer.

## Runtime-event checking synchronization

The runtime-event checking plan, first bounded checker stub, local observation, first minimal workflow, and first observed workflow success have been synchronized across the repository-maintenance reader path.

Current synchronization status:

- `scripts/check_runtime_events.py` implements the first bounded runtime-event checker stub for `examples/adapter-input-event-minimal.json`
- `.github/workflows/check-runtime-events.yml` runs the bounded runtime-event checker on push for the selected fixture and checker files
- `docs/runtime-event-checker-local-observation.md` records the first local pass observation
- `docs/runtime-event-workflow-current-status.md` records the first observed runtime-event workflow success on run `27501847137`
- `docs/runtime-event-checking-plan.md` records current bounded runtime-event checks, future checks, out-of-scope checks, and next implementation order
- `docs/checker-coverage.md` records the current runtime-event checker coverage and remaining boundaries
- `docs/operation-index.md` points runtime-event schema checking, JSON fixture checking, and future runtime-event checker work to `docs/runtime-event-checking-plan.md` first
- `docs/operation-index.md` points runtime candidate selection to `docs/minimal-runtime-candidate-design.md` before any runtime candidate is added
- `docs/operation-index.md` points minimal runtime fixture review to `docs/minimal-runtime-fixture-review.md` before changing the minimal runtime fixture or treating its first review as current
- `docs/operation-index.md` points progress review, rough progress estimates, gates, next gates, and progress-related stop conditions to `docs/progress-map.md`
- `docs/operation-index.md` points degraded-pathway handling, residual evidence, missing evidence, uncertainty, and judgment-return handling to `docs/responsibility-pathway-availability.md`
- `docs/operation-index.md` points task selection to `docs/current-task-inventory.md` before starting higher-risk work
- `BEACON.md` points readers to `docs/progress-map.md` for rough progress, gates, next gates, and stop conditions
- `BEACON.md` points readers to `docs/responsibility-pathway-availability.md` when the responsibility pathway is narrowed, incomplete, noisy, or temporarily broken
- `docs/current-task-inventory.md` keeps `docs/progress-map.md` visible before progress percentages, next gates, or maturity are discussed
- `docs/current-task-inventory.md` keeps `docs/responsibility-pathway-availability.md` visible when degraded-pathway handling matters
- `docs/phase-3-1-sync-log.md` records runtime-event checker stub synchronization and runtime-event workflow observation synchronization as responsibility units split across multiple small commits
- `docs/phase-3-1-roadmap-note.md` remains a planning companion and does not convert Phase 3.1 into a production runtime phase
- `docs/example-index.md` records the minimal synthetic runtime fixture as a runtime candidate fixture for reading and review only
- `docs/checker-coverage.md` records that `scripts/check_runtime_events.py` checks `examples/adapter-input-event-minimal.json` by default, while current checkers do not validate `spec/runtime-event.schema.yaml` or `examples/minimal-synthetic-runtime-fixture.json`
- `ROADMAP.md` records the runtime-event checking rule before broader implementation
- `CHANGELOG.md` records the runtime-event checking plan as a conceptual milestone before checker implementation

This synchronization does not unlock service-specific connectors, production runtime integration, conformance-model drafting, public standardization claims, semantic responsibility correctness checking, progress certification, schema correctness claims, JSON semantic correctness claims, runtime correctness claims, or AI final-responsibility transfer.

## Open-source review intent

The repository is prepared so that future open-source review can inspect boundaries, responsibility paths, examples, schemas, checker limits, runtime fixture limits, first bounded runtime-event checker stub, first minimal runtime-event workflow, first observed workflow success, progress estimates, active gates, next gates, degraded-pathway handling, judgment-return rules, and deferred implementation choices.

Open-source review is intended to help others examine whether the repository preserves return paths from claims to definitions, examples, schemas, checker boundaries, excluded claims, operation documents, runtime candidate boundaries, progress-map boundaries, responsibility-pathway availability boundaries, and deferred work.

Opening the repository for review does not itself certify the repository, approve production use, prove connector correctness, prove adapter correctness, prove schema correctness, prove runtime correctness, certify progress, certify degraded-pathway handling, certify checker completeness, certify workflow completeness, or transfer final responsibility to reviewers, users, or AI systems.

## Repository operation layer

Phase 3.1 now has an explicit repository-operation layer.

`docs/repository-operation-model.md` records:

- document purpose and usage phase policy
- staged update operation
- synchronization unit operation
- session load and handoff policy
- sync-log and roadmap-note separation policy
- document roles
- snapshot roles
- sync-log roles
- roadmap-note roles
- commit granularity policy
- periodic operation review policy
- workflow observation policy
- checker interpretation policy
- long-file update policy
- log organization policy
- non-certifying operation boundaries
- restart rules

`docs/operation-index.md` records which operation-related document to read for each maintenance situation.

The operation index is now connected from:

- `docs/repository-operation-model.md`
- `README.md`
- `README.ja.md`
- `BEACON.md`

`docs/runtime-event-checking-plan.md` is now connected from `docs/operation-index.md` as the plan to read before considering runtime-event schema checking, JSON fixture checking, future runtime-event checker work, runtime-event workflow work, or broader checker expansion.

`docs/minimal-runtime-candidate-design.md` is now connected from `docs/operation-index.md` as the design note to read before considering a minimal synthetic runtime fixture or bounded runtime-checking stub.

`docs/progress-map.md` is now connected from `docs/operation-index.md`, `BEACON.md`, `docs/current-task-inventory.md`, and `docs/phase-3-1-sync-log.md` as the rough planning and gate-tracking map for progress review.

`docs/responsibility-pathway-availability.md` is now connected from `docs/operation-index.md`, `BEACON.md`, `docs/current-task-inventory.md`, `docs/phase-3-1-current-snapshot.md`, and `docs/phase-3-1-sync-log.md` as the operation note for degraded-pathway handling, minimum preservation, and judgment-return handling.

`scripts/check_runtime_events.py` is now the first bounded local runtime-event checker stub. It is connected through `docs/runtime-event-checking-plan.md`, `docs/checker-coverage.md`, this snapshot, and the Phase 3.1 sync log. It does not create a production runtime, service connector, schema certification, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, or AI final-responsibility transfer.

`.github/workflows/check-runtime-events.yml` is now the first minimal runtime-event workflow. Its first observed success is recorded in `docs/runtime-event-workflow-current-status.md` and `docs/phase-3-1-sync-log.md`. This workflow success does not create schema validation, JSON semantic correctness proof, runtime correctness proof, production readiness, certification, or AI final-responsibility transfer.
