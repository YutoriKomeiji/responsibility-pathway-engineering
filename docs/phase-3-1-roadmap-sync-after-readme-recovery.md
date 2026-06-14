# Phase 3.1 Roadmap Sync After README Recovery

This note records the current synchronization state after the README mobile-rendering recovery, support-call / missed-support concept work, and operation-index update.

It is a short companion note only. It does not replace `docs/phase-3-1-current-snapshot.md`, `docs/phase-3-1-sync-log.md`, `docs/phase-3-1-roadmap-note.md`, `ROADMAP.md`, or `CHANGELOG.md`.

## Why this note exists

The repository briefly encountered a practical reader-path issue: the root `README.md` was readable through the GitHub API but appeared blank in the GitHub mobile app.

The repair path was:

1. preserve the expanded root README content in `docs/readme-expanded.md`
2. shorten `README.md` into a mobile-renderer-friendly public entrance
3. strengthen the shortened README with a compact `Why this matters` section and a short provenance link
4. update `docs/operation-index.md` so future maintainers understand the root README role
5. update `ROADMAP.md` so Phase 1.6, Phase 3, and Phase 3.1 reflect the missed-support and README recovery work

## Current synchronized artifacts

Reader-path and operation synchronization currently involves:

- `README.md`
- `README.ja.md`
- `docs/readme-expanded.md`
- `docs/operation-index.md`
- `docs/operation-tool-selection-guard.md`
- `docs/concepts/index.md`
- `docs/concepts/support-call-policy.md`
- `docs/concepts/missed-support-review-signal.md`
- `docs/examples/missed-support-current-status.md`
- `docs/examples/missed-support-workflow-observation.md`
- `examples/missed-support-boundary-minimal.yaml`
- `docs/checker-coverage.md`
- `docs/example-index.md`
- `docs/current-task-inventory.md`
- `ROADMAP.md`

## Current interpretation

The missed-support boundary example is now a checked, boundary-only, repository-maintenance example with `lifecycle_state: returning`.

`Check examples #17` was observed failed because the first version declared `lifecycle_state: returning` without a top-level `returning` block.

`Check examples #18` was observed green after the top-level `returning` block was added.

This observed green status is only a bounded repository-maintenance signal. It does not validate support-call semantics, missed-support correctness, legal validity, safety, compliance, fairness, production readiness, runtime correctness, connector correctness, or AI final-responsibility transfer.

## Current boundaries

Do not yet add:

- support-call schema fields
- missed-support schema fields
- support-call semantic checking
- missed-support correctness checking
- runtime-event support-call fields
- service-specific connectors
- production conversion code
- production runtime integration
- Lean expansion around support-call policy or missed-support signals
- Class E positive examples

These remain deferred until examples, schema conventions, checker boundaries, and review-signal semantics are deliberately stabilized.

## Next low-risk work

The next low-risk work should remain documentation and reader-path synchronization unless a narrower artifact is explicitly selected.

Good candidates:

1. update `docs/phase-3-1-sync-log.md` with this synchronization unit
2. update `CHANGELOG.md` with a short non-certifying milestone
3. review `BEACON.md` only if the read-first path is stale
4. avoid runtime checker, connector, production runtime, or Lean expansion until restart conditions are satisfied

## Non-certifying boundary

This note is repository-maintenance documentation only.

It does not certify the repository, examples, schemas, checkers, workflows, adapter design, runtime-event bridge, runtime candidates, public claims, or future implementations.

The human author or maintainer remains responsible for deciding whether a change should be made, published, relied upon, reverted, repaired, or deferred.
