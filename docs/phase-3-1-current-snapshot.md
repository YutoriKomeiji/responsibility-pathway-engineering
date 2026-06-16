# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary, runtime event bridge, runtime-event checking plan, first bounded runtime-event checker stub, first minimal runtime-event workflow, observed runtime-event workflow successes, minimal runtime candidate planning, minimal synthetic runtime fixture, minimal runtime fixture checker coverage, minimal runtime fixture review, event-to-pathway relation checker planning, progress map, responsibility pathway availability, current task inventory, and repository operation layer.

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
- `docs/minimal-runtime-fixture-checker-workflow-observation.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`
- `docs/runtime-event-checking-plan.md`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/event-to-pathway-relation-checker-plan.md`
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
- `docs/external-review-readiness-checklist.md`

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

## Event-to-pathway relation checker planning

`docs/event-to-pathway-relation-checker-plan.md` records a possible future bounded checker plan for comparing selected runtime-event JSON fixtures with pathway YAML examples.

The plan currently treats the relation checker as future work only.

It identifies structurally checkable relation signals such as:

- source-reference preservation
- review requirement preservation
- evidence and missing-context preservation
- actor and responsibility-boundary preservation
- excluded-claim preservation
- lifecycle compatibility

The plan does not implement a checker, authorize implementation by itself, validate semantic correctness, prove responsibility assignment correctness, validate adapter mapping correctness, validate schema correctness, validate JSON semantic correctness, validate runtime correctness, establish conformance evidence, approve production use, or transfer final responsibility to AI.

Any future implementation should remain local, structural, selected-fixture-only, and non-certifying until the documented preconditions are deliberately reviewed.

## Runtime-event checking plan

`docs/runtime-event-checking-plan.md` defines the path for adding bounded runtime-event and JSON-fixture checks.

A first bounded runtime-event checker stub now exists at `scripts/check_runtime_events.py`.

A first minimal runtime-event workflow now exists at `.github/workflows/check-runtime-events.yml`.

The plan records:

- what the first bounded runtime-event checker stub currently checks
- what future runtime-event checker work may inspect
- what the first checker layer must not inspect
- preconditions before adding a runtime-event workflow expansion, schema checker, further minimal-runtime-fixture checker, service connector check, or broader runtime-event checker
- suggested next implementation order
- the boundary for passing checks
- the current decision that schema checking, further runtime-fixture checking, connectors, production runtime, semantic checking, workflow expansion, and AI final-responsibility transfer remain deferred or out of scope

The plan does not certify schema correctness, JSON fixture semantic correctness, adapter mapping correctness, service-specific connector behavior, production runtime behavior, workflow stability, legal validity, safety, compliance, fairness, moral resolution, production readiness, or AI final-responsibility transfer.

## Bounded runtime-event checker stub

`scripts/check_runtime_events.py` is the first bounded runtime-event checker stub.

It checks the following fixtures by default:

```text
examples/adapter-input-event-minimal.json
examples/minimal-synthetic-runtime-fixture.json
```

It performs only bounded structural checks on selected synthetic runtime-event and minimal synthetic runtime observation JSON fixtures.

For `examples/adapter-input-event-minimal.json`, the checker currently inspects only whether:

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

For `examples/minimal-synthetic-runtime-fixture.json`, the checker currently inspects only bounded runtime-boundary signals such as:

- explicit non-production scope
- synthetic fixture status
- vendor-neutral status
- review-required status
- no certification claim
- no production runtime
- no service-specific connector
- no automatic approval
- no automatic execution
- no external side effects
- AI final-responsibility non-claim
- missing approval evidence
- missing execution evidence
- human review requirement
- source event reference
- expected boundary-preservation flags
- excluded claims

## Local and workflow observation status

`docs/runtime-event-checker-local-observation.md` records the first local observation of `scripts/check_runtime_events.py` against `examples/adapter-input-event-minimal.json`.

The local observation recorded:

```text
exit code: 0
PASS: bounded runtime-event checks completed without failures
```

`docs/runtime-event-workflow-current-status.md` records observed runtime-event workflow successes.

First observed workflow run:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/runs/27501847137
```

First observed job:

```text
job id: 81286034329
job name: Bounded runtime-event checks
job status: completed
job conclusion: success
step: Run bounded runtime-event checker: completed / success
```

After `examples/minimal-synthetic-runtime-fixture.json` was added to the default checker coverage and workflow watch path, the following workflow success was observed and recorded:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/runs/27607798655
```

Observed job:

```text
job id: 81624113270
job name: Bounded runtime-event checks
job status: completed
job conclusion: success
step: Run bounded runtime-event checker: completed / success
```

The focused observation note is `docs/minimal-runtime-fixture-checker-workflow-observation.md`.

The focused reader-path connection note is `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`.

A local or workflow pass may mean only that the selected synthetic runtime-event or minimal synthetic runtime observation JSON fixtures satisfy the bounded structural requirements implemented by the local checker or that the bounded checker completed successfully in GitHub Actions for that workflow run. It is not schema validation, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, runtime correctness proof, production readiness, certification, legal review, safety review, compliance review, fairness review, moral-resolution evidence, or AI final-responsibility transfer.

## Minimal runtime candidate design

`docs/minimal-runtime-candidate-design.md` defines the narrowest acceptable shape for an early runtime candidate.

The design note exists before any service connector, production runtime implementation, production conversion code, automatic approval system, or automatic execution system.

It allowed the first bounded candidates:

- a minimal synthetic runtime fixture
- a bounded runtime-checking stub

The first minimal synthetic runtime fixture, first bounded runtime-event checker stub, first minimal workflow, and observed bounded workflow successes are now separate bounded artifacts. They do not together create a production runtime or connector.

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

The fixture is now checked by `scripts/check_runtime_events.py` for bounded structural runtime-boundary signals only. That check does not validate runtime correctness, schema correctness, JSON semantic correctness, adapter mapping correctness, service connector correctness, production readiness, certification, or AI final-responsibility transfer.

## Minimal runtime fixture review

`docs/minimal-runtime-fixture-review.md` records the first review of `examples/minimal-synthetic-runtime-fixture.json` as a minimal synthetic runtime observation fixture for reading and review.

The first review found that the fixture is acceptable as a first minimal synthetic runtime observation fixture.

No change to `examples/minimal-synthetic-runtime-fixture.json` was required by that review.

`docs/minimal-runtime-fixture-review-connection.md` records the reader path connecting the review note to the current Phase 3.1 operation documents.

The review note and connection note do not unlock production runtime integration, service-specific connectors, production conversion code, schema correctness claims, JSON semantic correctness claims, adapter mapping correctness claims, connector correctness claims, responsibility assignment correctness claims, Class E positive examples, or Lean expansion around runtime events.

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

For Phase 3.1, the inventory currently treats the first bounded runtime-event checker stub as implemented bounded structural checker work, records observed runtime-event workflow successes as bounded workflow observations, keeps runtime fixture review as bounded artifact preparation, keeps event-to-pathway relation checker planning as a future local structural checker plan only, keeps `docs/progress-map.md` rough and planning-only, keeps `docs/responsibility-pathway-availability.md` reachable for degraded-pathway handling, and keeps runtime-event workflow expansion, service-specific connectors, production conversion code, production runtime integration, Class E positive examples, support-call schema fields, missed-support schema fields, support-call semantic checking, missed-support correctness checking, conformance-model drafting, and Lean expansion around runtime events, support-call policy, or missed-support signals deferred or conditional.

The task inventory is a planning and prioritization note only. It is not certification, production approval, legal review, safety review, compliance review, fairness review, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer.

## Runtime-event checking synchronization

The runtime-event checking plan, first bounded checker stub, local observation, first minimal workflow, observed workflow successes, minimal runtime fixture checker coverage, event-to-pathway relation checker planning, and focused observation notes have been synchronized across the repository-maintenance reader path.

Current synchronization status:

- `scripts/check_runtime_events.py` implements bounded structural checks for `examples/adapter-input-event-minimal.json` and `examples/minimal-synthetic-runtime-fixture.json`
- `.github/workflows/check-runtime-events.yml` runs the bounded runtime-event checker on push for the selected fixture and checker files
- `docs/runtime-event-checker-local-observation.md` records the first local pass observation
- `docs/runtime-event-workflow-current-status.md` records the first observed runtime-event workflow success on run `27501847137` and the observed minimal runtime fixture checker workflow success on run `27607798655`
- `docs/minimal-runtime-fixture-checker-workflow-observation.md` records the focused workflow observation for run `27607798655`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md` records the focused reader path for the minimal runtime fixture checker expansion and workflow observation
- `docs/runtime-event-checking-plan.md` records current bounded runtime-event checks, future checks, out-of-scope checks, and next implementation order
- `docs/runtime-event-schema-fixture-alignment.md` records current alignment between the draft runtime-event schema, selected JSON fixtures, and bounded runtime-event checker without treating it as validation
- `docs/event-to-pathway-relation-checker-plan.md` records planned future local structural relation-checker boundaries before any implementation
- `docs/checker-coverage.md` records the current runtime-event checker coverage and remaining boundaries
- `docs/operation-index.md` points runtime-event schema checking, JSON fixture checking, event-to-pathway relation checker planning, future runtime-event checker work, workflow observation, runtime candidate planning, degraded-pathway handling, progress review, and task selection to the relevant operation documents
- `BEACON.md` points readers to `docs/progress-map.md` for rough progress, gates, next gates, and stop conditions
- `BEACON.md` points readers to `docs/responsibility-pathway-availability.md` when the responsibility pathway is narrowed, incomplete, noisy, or temporarily broken
- `docs/current-task-inventory.md` keeps `docs/progress-map.md` visible before progress percentages, next gates, or maturity are discussed
- `docs/current-task-inventory.md` keeps `docs/responsibility-pathway-availability.md` visible when degraded-pathway handling matters
- `docs/current-task-inventory.md` keeps `docs/event-to-pathway-relation-checker-plan.md` visible before any future relation checker implementation
- `docs/phase-3-1-sync-log.md` records runtime-event checker stub synchronization and runtime-event workflow observation synchronization as responsibility units split across multiple small commits
- `docs/phase-3-1-roadmap-note.md` remains a planning companion and does not convert Phase 3.1 into a production runtime phase
- `docs/example-index.md` records the minimal synthetic runtime fixture as a runtime candidate fixture for reading and review only
- `docs/checker-coverage.md` records that `scripts/check_runtime_events.py` checks the selected synthetic runtime-event and minimal synthetic runtime observation JSON fixtures by default, while current checkers do not validate `spec/runtime-event.schema.yaml`
- `ROADMAP.md` records the runtime-event checking rule before broader implementation
- `CHANGELOG.md` records the runtime-event checking plan as a conceptual milestone before checker implementation

This synchronization does not unlock service-specific connectors, production runtime integration, relation-checker implementation, conformance-model drafting, public standardization claims, semantic responsibility correctness checking, progress certification, schema correctness claims, JSON semantic correctness claims, runtime correctness claims, or AI final-responsibility transfer.

## Open-source review intent

The repository is prepared so that future open-source review can inspect boundaries, responsibility paths, examples, schemas, checker limits, runtime fixture limits, first bounded runtime-event checker stub, first minimal runtime-event workflow, observed workflow successes, minimal runtime fixture checker coverage, event-to-pathway relation checker planning, progress estimates, active gates, next gates, degraded-pathway handling, judgment-return rules, and deferred implementation choices.

Open-source review is intended to help others examine whether the repository preserves return paths from claims to definitions, examples, schemas, checker boundaries, excluded claims, operation documents, runtime candidate boundaries, relation-checker planning boundaries, progress-map boundaries, responsibility-pathway availability boundaries, and deferred work.

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

`docs/event-to-pathway-relation-checker-plan.md` is now connected from `docs/operation-index.md` as the plan to read before considering a future local structural relation checker between selected runtime-event JSON fixtures and pathway YAML examples.

`docs/minimal-runtime-candidate-design.md` is now connected from `docs/operation-index.md` as the design note to read before considering a minimal synthetic runtime fixture or bounded runtime-checking stub.

`docs/progress-map.md` is now connected from `docs/operation-index.md`, `BEACON.md`, `docs/current-task-inventory.md`, and `docs/phase-3-1-sync-log.md` as the rough planning and gate-tracking map for progress review.

`docs/responsibility-pathway-availability.md` is now connected from `docs/operation-index.md`, `BEACON.md`, `docs/current-task-inventory.md`, `docs/phase-3-1-current-snapshot.md`, and `docs/phase-3-1-sync-log.md` as the operation note for degraded-pathway handling, minimum preservation, and judgment-return handling.

`scripts/check_runtime_events.py` is the first bounded runtime-event checker stub. It is connected through `docs/runtime-event-checking-plan.md`, `docs/checker-coverage.md`, this snapshot, and the Phase 3.1 sync log. It does not create a production runtime, service connector, schema certification, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, runtime correctness proof, or AI final-responsibility transfer.

`.github/workflows/check-runtime-events.yml` is the first minimal runtime-event workflow. Its observed successes are recorded in `docs/runtime-event-workflow-current-status.md`, `docs/minimal-runtime-fixture-checker-workflow-observation.md`, `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`, and `docs/phase-3-1-sync-log.md`. These workflow successes do not create schema validation, JSON semantic correctness proof, runtime correctness proof, production readiness, certification, or AI final-responsibility transfer.
