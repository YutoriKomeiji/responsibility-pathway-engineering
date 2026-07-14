# Open Construction

This repository is built in public as a reviewable construction site.

Some parts may be useful, runnable, copyable, or testable before the project is complete. That is intentional.

A runnable checker, template, fixture, script, workflow, or future library-like package does not mean:

- certified
- production ready
- legally valid
- safe for deployment
- compliance approved
- fairness approved
- externally reviewed
- conformance ready
- final responsibility transferred to AI

It means only that a bounded artifact is available for inspection, testing, review, and improvement under the limits stated in the relevant file.

Please test, inspect, fork, adapt, and point out problems. Feedback is welcome especially when it improves:

- maturity labels
- non-claim boundaries
- examples and fixtures
- checker clarity
- human or institutional return points
- evidence logging
- repair, dispute, reopening, or rollback paths

## Maturity labels for implementation-adjacent artifacts

The repository may include useful artifacts before they are complete. Use these labels when they help readers understand what a file, checker, template, workflow, or future package does and does not mean.

| Label | Meaning | Non-claim boundary |
|---|---|---|
| `runnable-prototype` | Can be run locally for bounded tests | Not production ready |
| `test-welcome` | Feedback and failure cases are welcome | Not validated by community yet |
| `feedback-welcome` | Conceptual, documentation, checker, fixture, and boundary critique invited | Not endorsement-seeking |
| `library-candidate` | May later become a reusable package or library | Not a stable API |
| `synthetic-first` | Uses synthetic fixtures before real integrations | Not a service connector |
| `review-required` | Needs human or external review before stronger claims | Not reviewed |

These labels extend the repository's existing construction-status language. They do not replace the existing boundary notes in README, BEACON, checker coverage, examples, templates, or formalization notes.

## Tool boundary

If a checker, CLI, package, workflow, or library-like component is introduced, include a boundary close to its usage instructions.

Suggested boundary block:

```md
This tool is an under-construction structural aid.

It may help detect missing fields, inconsistent boundaries, absent human return points, or incomplete evidence records.

It does not decide whether a workflow, organization, AI system, deployment, legal claim, safety claim, compliance claim, fairness claim, or responsibility assignment is correct.

A passing result means only that the checked artifact satisfied the bounded structural rules implemented by this version.
```

## Release posture

Open Construction allows public visibility before completion. It does not authorize overclaiming.

Before presenting any implementation-adjacent artifact as broadly reusable, confirm that it has:

1. current README / BEACON / checker-boundary alignment
2. visible maturity label
3. synthetic-first test fixture or clearly bounded example, when applicable
4. minimal local run or inspection instructions, when applicable
5. non-certifying result language
6. known limitations section
7. issue, discussion, or feedback route
8. human review before release announcements or stronger public claims

## Non-goals

Open Construction does not mean:

- the project is complete
- external review has occurred
- standardization has occurred
- conformance has been reached
- safety has been proved
- compliance has been proved
- legal validity has been established
- production readiness has been reached
- connector correctness has been proved
- runtime correctness has been proved
- AI has received final responsibility

## Current application

This document supports public inspection and careful experimentation while keeping the repository's core boundaries intact.

Published GitHub Pages reader paths provide a browser-friendly inspection route for the current catalog, Japanese catalog, reader path maps, boundary glossary pages, and reviewer checklist pages. They are reader and inspection aids only, not certification, validation, review completion, production approval, or AI final-responsibility transfer.

It should be read with:

- [README.md](README.md)
- [README.ja.md](README.ja.md)
- [BEACON.md](BEACON.md)
- [Published RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)
- [docs/checker-coverage.md](docs/checker-coverage.md)
- [docs/repository-construction-status-labels.md](docs/repository-construction-status-labels.md)
- [docs/public-adoption-and-fork-strategy.md](docs/public-adoption-and-fork-strategy.md)
