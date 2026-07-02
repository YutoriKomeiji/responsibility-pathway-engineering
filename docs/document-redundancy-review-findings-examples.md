# Document Redundancy Review Findings - Example Indexes and Example Notes

This note records low-risk findings for example indexes, example notes, fixtures, and example-adjacent checker interpretation documents.

It follows `docs/document-redundancy-review-plan.md`.

## Review scope

Reviewed by repository search only at this stage.

Candidate search terms included:

- `example index examples fixture minimal checker coverage example note`
- `repair recovery pathway reading repair-flow recovery-pathway-reading`

Search results surfaced likely example, fixture, or example-adjacent anchors, including:

- `docs/example-review-notes.md`
- `docs/minimal-runtime-candidate-design.md`
- `docs/minimal-runtime-fixture-review-connection.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/event-to-pathway-relation-checker-plan.md`
- `docs/runtime-event-checking-plan.md`
- `docs/checker-coverage.md`
- `docs/example-index.md`

Known additional example and fixture anchors from current work context include:

- `examples/*.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`
- `fixtures/review-results/*.yaml`
- `scripts/check_examples.py`
- `scripts/check_runtime_events.py`
- `scripts/check_review_results.py`

## Initial classification

| Document or artifact type | Initial role |
| --- | --- |
| `docs/example-index.md` | broad navigation surface for examples |
| `examples/*.yaml` | pathway example records used for reading and bounded structural checks |
| JSON runtime fixtures | synthetic runtime-event or runtime-observation fixtures |
| review-result fixtures | bounded review-result output fixtures |
| example review notes | human-readable interpretation and review notes for examples |
| schema-fixture alignment notes | alignment notes between schemas, fixtures, and bounded checker behavior |
| checker coverage | authoritative map for current checker interpretation of examples and fixtures |
| checker plans | future checking routes, not current example behavior |
| `docs/repair-model.md` | authoritative repair definition and recovery-pathway pointer |
| `docs/recovery-pathway-reading.md` | focused reading boundary for repair-as-recovery; not a separate model, certification layer, or example index |
| `examples/repair-flow.yaml` | minimal example showing repair and recovery-pathway reading |

## Initial findings

1. The example index and example-note group is not ready for merging or deletion.

2. `docs/example-index.md` should remain the broad example navigation surface, but it should not absorb detailed review notes, fixture design notes, or checker-plan reasoning.

3. Example and fixture files should remain small readable artifacts, not documentation indexes.

4. `docs/checker-coverage.md` should remain the authority for how current checkers interpret examples and fixtures.

5. Schema-fixture alignment notes should remain separate when they explain why a selected fixture is structurally aligned without claiming validation.

6. Example review notes are useful when they preserve human-readable interpretation that would make example files too large if embedded directly.

7. Future checker plans should remain separate from example indexes so readers do not confuse planned checking with current checker behavior.

8. Repetition is acceptable when it preserves local readability, but any repeated boundary must not imply certification, conformance, production readiness, runtime correctness, connector correctness, or AI final-responsibility transfer.

9. `docs/recovery-pathway-reading.md` is acceptable as a focused boundary note only if it stays narrow and does not duplicate the full Repair Model.

10. If future updates make `docs/recovery-pathway-reading.md` and `docs/repair-model.md` carry the same definition body, prefer keeping `docs/repair-model.md` authoritative and either shorten, merge, or delete the focused reading note after a replacement path is clear.

11. `examples/repair-flow.yaml` may carry a short recovery-pathway explanation for local readability, but detailed recovery-pathway language should remain in `docs/recovery-pathway-reading.md` or `docs/repair-model.md` rather than expanding the example file.

12. No deletion is recommended in this pass. The current safe action is to keep boundaries short, keep pointers explicit, and recheck after reader-path use.

## Possible low-risk next steps

- Add this findings note to the `Findings notes` section of `docs/document-redundancy-review-plan.md`.
- Add a short pointer from `docs/operation-index.md` if example-related redundancy review needs a stable navigation entry.
- Avoid moving detailed review text into `docs/example-index.md` unless the index becomes misleading without it.
- If example and fixture interpretation becomes confusing, add a role table rather than merging example notes into checker coverage.
- Recheck `docs/recovery-pathway-reading.md` after the next reader-path pass; keep it only while it provides a distinct focused reading boundary.
- Do not delete `docs/recovery-pathway-reading.md` unless `docs/repair-model.md` or another authoritative document clearly replaces its reader-path role.

## Boundary

This findings note does not merge, delete, rename, archive, or rewrite any document, example, fixture, schema, or checker.

It does not change checker implementations, workflows, schemas, runtime behavior, connector behavior, Lean files, README files, BEACON, ROADMAP, or CHANGELOG.

It does not certify repository maturity, conformance, legal validity, safety, compliance, fairness, production readiness, fixture correctness, example correctness, runtime correctness, connector correctness, or AI final-responsibility transfer.
