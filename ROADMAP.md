# ROADMAP

This roadmap is the compact current planning map for Responsibility Pathway Engineering.

It is intentionally short. Historical milestones, detailed workflow observations, phase synchronization details, and long current-state records belong in focused notes, snapshots, sync logs, `CHANGELOG.md`, and git history.

This roadmap is a planning aid only. It is not a certification record, conformance claim, external review finding, legal review, safety review, compliance review, fairness review, production approval, standardization claim, runtime correctness proof, connector correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.

## Current position

RPE is currently in **Phase 3.1: Adapter Boundary and Runtime Event Bridge**.

Current repository position:

- core definitions and initial examples exist
- bounded structural checkers exist for selected examples and fixtures
- a minimal Lean spine exists with assumption-scoped invariants
- adapter-boundary and runtime-event bridge documents exist
- published GitHub Pages reader paths exist as browser-friendly orientation aids
- external-review readiness and Zenn Level 2 repository-walkthrough readiness are connected
- the first browser-facing reader-aid pair now exists:
  - Example browser page
  - Template helper page
- the next likely transition is from static site reader aids toward a small program-design step

Published reader path:

- [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)

The published reader path helps first readers orient. It does not replace repository Markdown files, source artifacts, human review, external review, approval, validation, certification, or maintainer responsibility.

## Active gates

Use gates rather than excitement as the planning measure.

### Gate 1: keep the reader path aligned

Active.

Keep these aligned when reader-facing files or Pages change:

- `README.md`
- `README.ja.md`
- `BEACON.md`
- `OPEN_CONSTRUCTION.md`
- `docs/operation-index.md`
- `docs/overview.md`
- `docs/progress-map.md`
- `docs/external-review-readiness-checklist.md`
- `docs/external-review-package-note.md`
- `docs/phase-3-1-roadmap-note.md`
- published Pages reader aids

### Gate 2: keep examples and checker coverage aligned

Active.

Before adding or changing examples, keep these aligned:

- `docs/example-index.md`
- `docs/checker-coverage.md`
- checker scripts
- selected fixtures
- workflow observations

Checker success remains a bounded repository-maintenance signal only.

### Gate 3: keep the runtime-event bridge non-production

Active.

Phase 3.1 may preserve reviewable draft pathways from runtime observations, but it must not become:

- a service-specific connector
- production runtime integration
- production conversion code
- schema validation
- semantic responsibility correctness checking
- adapter mapping correctness proof
- runtime correctness proof
- conformance evidence
- production approval

### Gate 4: prepare browser-facing reader aids cautiously

Initial pair reached.

The first browser-facing reader-aid pair has been added:

- Example browser page
- Template helper page

These remain inspection aids only. They point back to source files and must not imply implementation maturity, certification, validation, conformance, production readiness, or approval.

### Gate 5: prepare first small program step

Candidate.

The next program step should start with a design note or a very small local helper. It must not become service-specific connector work, production runtime integration, automatic approval, automatic execution, semantic correctness checking, or conformance evidence.

## Next safe work

Recommended order:

1. Keep the newly added Example browser and Template helper reader paths aligned in the small set of documents that actually need the update.
2. Confirm site links after Pages deployment when the maintainer chooses to check them.
3. Create a short first-program design note before writing code.
4. Implement at most one small local helper at a time.
5. Keep `docs/example-index.md` and `docs/checker-coverage.md` aligned if example presentation or checker interpretation changes.
6. Keep `docs/phase-3-1-roadmap-note.md` as the detailed Phase 3.1 roadmap companion.
7. Use `docs/roadmap-history.md` and git history for older long-roadmap detail.

## Deferred work

The following remain deferred unless deliberately reopened with a scoped design note and human maintainer approval:

- service-specific connectors
- production runtime integration
- production conversion code
- full runtime-event schema validation
- full JSON schema-fixture validation
- event-to-pathway semantic correctness checking
- adapter mapping correctness checker
- responsibility assignment correctness checker
- action-class-specific checker enforcement beyond documented future work
- Class E positive examples
- conformance-model drafting
- public standardization claims
- Lean expansion around adapter, runtime-event, support-call, missed-support, evidence-completeness, approval-transfer, or later-return concepts

## Stop conditions

Stop and preserve state if a proposed change:

- makes RPE sound like a finished standard
- implies certification
- implies conformance evidence
- implies legal validity
- implies safety proof
- implies compliance proof
- implies fairness proof
- implies production readiness
- implies connector correctness
- implies adapter correctness
- implies runtime correctness
- implies schema correctness
- implies JSON semantic correctness
- implies semantic responsibility correctness
- implies social acceptance proof
- implies AI final-responsibility transfer
- replaces repository source files with Pages summaries
- hides uncertainty behind formal, mathematical, standardization, or publication language

## Detailed current-state sources

Use these for detail instead of expanding this roadmap:

- `docs/phase-3-1-roadmap-note.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/current-task-inventory.md`
- `docs/progress-map.md`
- `docs/repository-pathway-gap-inventory.md`
- `docs/operation-index.md`
- `docs/roadmap-history.md`
- `CHANGELOG.md`

## Maintenance rule

If this roadmap becomes too long to update safely or review clearly, replace it with a compact current version and move detail into a focused note, snapshot, sync log, changelog entry, or git history.

Do not let the active roadmap become a second changelog or sync log.

## Guiding principle

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.
