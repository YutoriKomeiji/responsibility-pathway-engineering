# Repository Construction Status Labels

This note defines lightweight construction-status labels for Responsibility Pathway Engineering documents and implementation-adjacent artifacts.

It is a labeling policy only. It does not certify maturity, approve publication, authorize implementation, change schemas, change checkers, change workflows, change runtime behavior, change connectors, create conformance claims, prove legal validity, prove safety, prove compliance, prove fairness, prove social acceptance, or transfer final responsibility to AI.

## Purpose

The repository may contain many active notes, design parts, implementation candidates, and review paths at the same time.

That is acceptable if readers can tell whether an artifact is stable, experimental, draft, under construction, historical, or deferred.

Construction labels allow the project to keep building without pretending that every file is complete.

## Suggested labels

Use these labels in documents or indexes when helpful:

- `stable-reader-path` - safe as a current reader entrance or navigation route
- `active-focused-note` - current focused note for a bounded topic
- `under-construction` - useful but not stable enough to rely on alone
- `experimental-part` - implementation-adjacent or model-adjacent candidate, not production behavior
- `planning-only` - design or sequencing note only
- `review-required` - needs human or external review before stronger claims
- `historical-reference` - preserved for cause tracing or past synchronization
- `deferred` - known future work, not current capability
- `deprecated-route` - kept only to redirect readers or preserve history

## Default rule

If a file introduces a new implementation part, public-facing route, formalization candidate, checker idea, connector idea, or review process, mark or describe its maturity before readers can confuse it for a finished capability.

A file may be useful while still being `under-construction` or `planning-only`.

## Fork and modification posture

Forks and modifications may occur.

Therefore, labels should help downstream readers understand what the original repository considered stable, draft, experimental, deferred, or non-certifying at the time.

A fork may change the artifact, but it should not erase the need to preserve responsibility boundaries, non-claims, and human or institutional accountability.

## Non-claim boundary

A construction label must not be used to smuggle stronger claims.

For example:

- `experimental-part` does not mean usable implementation
- `stable-reader-path` does not mean certified content
- `review-required` does not mean reviewed
- `planning-only` does not mean approved future work
- `deferred` does not mean obsolete
- `historical-reference` does not mean current guidance

## Level 2 publication relation

Level 2 repository walkthrough may proceed while some files are marked `under-construction`, `planning-only`, `experimental-part`, or `deferred`.

The Level 2 requirement is that the reader can distinguish current reader paths, non-claims, construction zones, and deferred capabilities.

## Cleanup relation

Use `docs/repository-file-organization-audit.md` when labels reveal overlap, sprawl, merge candidates, deprecated routes, or delete candidates.

Do not delete solely because a file is under construction.

Classify first, preserve restart paths, and keep alternate routes visible.
