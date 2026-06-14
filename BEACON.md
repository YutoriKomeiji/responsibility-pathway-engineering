# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

BEACON is the short reconnection entrance. It is not the full current-state record, changelog, roadmap, proof, certification, legal review, safety review, compliance review, production approval, connector correctness proof, runtime correctness proof, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer mechanism.

## Current position

The repository is currently in Phase 3.1: Adapter Boundary and Runtime Event Bridge.

The current stable construction path includes:

- a specification-first core
- source-aligned Action Class Matrix examples
- bounded structural example checks
- bounded review-result checks
- Lean formalization with assumption-scoped invariants
- enterprise and record-review guidance
- reference implementation boundaries
- adapter-boundary and runtime-event bridge notes
- a minimal synthetic runtime fixture for reading and review only
- support-call and missed-support concept notes
- a boundary-only missed-support example
- explicit repository operation documents
- a grounded standardization strategy for future open-specification review
- a progress map for rough planning estimates and gate tracking

Recent synchronization restored and recorded the reader path after a README mobile-rendering issue. The root `README.md` was shortened and strengthened, while the previous expanded README content was preserved at `docs/readme-expanded.md`.

The support-call / missed-support path is currently concept-level and boundary-example-level only. It does not yet unlock schema fields, semantic checking, runtime-event support-call fields, Lean expansion, service-specific connectors, production conversion code, production runtime integration, or Class E positive examples.

## Read first

1. `README.md` or `README.ja.md`
2. `docs/operation-index.md`
3. `docs/phase-3-1-current-snapshot.md`
4. `docs/phase-3-1-sync-log.md`
5. `docs/phase-3-1-roadmap-note.md`
6. `docs/phase-3-1-roadmap-sync-after-readme-recovery.md`
7. `docs/current-task-inventory.md`
8. `docs/progress-map.md` for rough progress, gates, next gates, and stop conditions
9. `docs/concepts/index.md`
10. `docs/standardization-strategy.md` before expanding world-standard or conformance language
11. `docs/example-index.md`
12. `docs/checker-coverage.md`
13. `ROADMAP.md`
14. `CHANGELOG.md` only when historical cause tracing or milestone review is needed

Use `docs/repository-operation-model.md` before broad reader-path synchronization, long-file updates, session handoff, or periodic operation review.

## Current focus

- Keep the root README short and mobile-renderer friendly.
- Keep detailed README content in `docs/readme-expanded.md`.
- Keep examples small, readable, and non-certifying.
- Keep progress estimates rough, planning-only, and non-certifying.
- Keep standardization strategy grounded, complementary to existing frameworks, and non-certifying.
- Keep support-call and missed-support semantics concept-level until deliberately stabilized.
- Keep runtime-event schema checking, JSON fixture checking, and runtime fixture checking deferred.
- Keep service-specific connectors and production runtime integration deferred.
- Keep Lean expansion around adapter, runtime-event, support-call, or missed-support concepts deferred.
- Keep Class E positive examples deferred.
- Preserve restartability through operation-index, current snapshots, sync logs, roadmap notes, progress map, and short changelog milestones.

## Recent bounded check observations

- `Check review-result fixtures #1` observed green on commit `aaaece3`.
- `Check examples #14` observed green on commit `caf285b` for the Class D reversible external action fixture.
- `Check examples #16` observed green on commit `d377be2` for the runtime-event-to-pathway draft example after structural repair.
- `Check examples #17` observed failed on commit `57445b1` because the missed-support example declared `lifecycle_state: returning` without a top-level `returning` block.
- `Check examples #18` observed green on commit `f63678c` after the top-level `returning` block was added.

All observed green statuses are bounded repository-maintenance signals only. They are not certification, legal validation, safety validation, compliance validation, fairness validation, moral resolution, production approval, connector correctness proof, runtime correctness proof, support-call semantic validation, missed-support correctness validation, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer.

## Do not start yet

Do not start the following without satisfying the relevant restart conditions and reading the current plans first:

- service-specific connectors
- production conversion code
- production runtime integration
- runtime-event schema checker
- JSON fixture checker
- runtime fixture checker
- `scripts/check_runtime_events.py`
- runtime-event workflow
- action-class-specific checker enforcement
- support-call schema fields
- missed-support schema fields
- support-call semantic checker
- missed-support correctness checker
- runtime-event support-call fields
- Class E positive examples
- Lean expansion around adapter, runtime-event, support-call, or missed-support concepts
- conformance-model drafting or public standardization claims before `docs/standardization-strategy.md` conditions are satisfied

## Operating rule

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.

The human author or maintainer remains responsible for deciding whether a change should be made, published, relied upon, reverted, repaired, or deferred.
