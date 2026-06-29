# Document Redundancy Review Findings - Operation Rules

This note records the first low-risk findings for the operation-rules and operation-guards document group.

It follows `docs/document-redundancy-review-plan.md`.

## Review scope

Reviewed by repository search only at this stage.

Candidate search terms included:

- `operation rule guard checklist maintenance`
- `focused note reconnection recovery path tool selection`

Search results surfaced the following likely operation-rule or guard anchors:

- `docs/operation-index.md`
- `docs/operation-improvement-log.md`
- `docs/assistant-pathway-maintenance-checklist.md`
- `docs/phase-3-1-sync-log.md`
- `ROADMAP.md`
- `CHANGELOG.md`

Known additional operation-rule anchors from current work context include:

- `docs/repository-operation-model.md`
- `docs/operation-tool-selection-guard.md`
- `docs/focused-note-reconnection-rule.md`
- `docs/document-redundancy-review-plan.md`

## Initial classification

| Document | Initial role |
| --- | --- |
| `docs/repository-operation-model.md` | authoritative operation model |
| `docs/operation-index.md` | broad operation navigation surface |
| `docs/operation-tool-selection-guard.md` | focused tool-selection guard |
| `docs/focused-note-reconnection-rule.md` | focused recovery and reconnection rule |
| `docs/assistant-pathway-maintenance-checklist.md` | assistant-side maintenance checkpoint |
| `docs/operation-improvement-log.md` | durable improvement and recurrence log |
| `docs/document-redundancy-review-plan.md` | planned redundancy review method |
| `docs/phase-3-1-sync-log.md` | phase-specific historical synchronization record |
| `ROADMAP.md` | phase-level direction, not operation-rule authority |
| `CHANGELOG.md` | archival milestone record, not active operation-rule authority |

## Initial findings

1. The operation-rule group is not yet ready for merging or deletion.

2. The documents have overlapping boundary language, but much of it is local readability repetition rather than harmful duplication.

3. `docs/repository-operation-model.md` should remain the authoritative operation model.

4. `docs/operation-index.md` should remain the broad navigation surface, but it should not absorb detailed state from focused notes.

5. `docs/operation-tool-selection-guard.md`, `docs/focused-note-reconnection-rule.md`, and `docs/assistant-pathway-maintenance-checklist.md` should remain separate for now because they guard different failure modes:

   - tool surface selection,
   - focused-note recovery and reconnection,
   - assistant-side in-session maintenance checks.

6. `docs/operation-improvement-log.md` should remain a log, not a rule source. It may point to rule files, but it should not become the authoritative operation model.

7. `docs/document-redundancy-review-plan.md` should remain a planning note until at least one candidate group is reviewed more deeply.

8. `ROADMAP.md` and `CHANGELOG.md` should not be used as primary operation-rule lookup surfaces.

## Possible low-risk next steps

- Add a short pointer from `docs/operation-index.md` to `docs/document-redundancy-review-plan.md` only if a small safe update path is available.
- Add a short pointer from `docs/operation-index.md` to `docs/assistant-pathway-maintenance-checklist.md` only if the operation index becomes misleading without it.
- Avoid merging focused guard files until their priority relationship is clearer.
- If overlap becomes confusing, update `docs/operation-index.md` with a role table rather than copying detailed rule text.

## Boundary

This findings note does not merge, delete, rename, archive, or rewrite any document.

It does not change schemas, checkers, workflows, runtime behavior, connector behavior, Lean files, README files, BEACON, ROADMAP, or CHANGELOG.

It does not certify repository maturity, conformance, legal validity, safety, compliance, fairness, production readiness, or AI final-responsibility transfer.
