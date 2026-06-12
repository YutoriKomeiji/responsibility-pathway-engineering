# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

## Current Position

Phase 0 foundation is complete.

Phase 1 concept model is substantially established.

Phase 1.5 specification binding is established.

Phase 1.6 lightweight validation and lifecycle-example coverage is substantially established.

Phase 2 formalization has started, the first minimal Lean lifecycle-invariant set has been introduced, the Lean core has been split into small modules, and a minimal Lean build path has been added.

Core definitions, the eight-element model, runtime model, responsibility node model, return point model, repair model, value/cost flow, stop authority, evidence log, action class matrix, approval gate, and decision owner model have been added.

The core YAML specification has been expanded to version 0.2.0.

A minimal schema split has been established under `spec/`:

- `spec/node.schema.yaml`
- `spec/action-class.schema.yaml`
- `spec/return-point.schema.yaml`
- `spec/evidence-log.schema.yaml`
- `spec/repair.schema.yaml`
- `spec/pathway.schema.yaml`

Minimal lifecycle examples now cover:

- `originating`
- `repaired`
- `suspended`
- `returning`
- `closed`

A bounded lightweight checker exists at `scripts/check_examples.py`.

The checker is lifecycle-aware, but it remains non-certifying. It checks structural signals only and does not claim legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

Lean formalization currently uses `formal/lean/ResponsibilityPathway/Core.lean` as a stable import entry point.

The Lean spine is split into:

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

Minimal Lean build files now exist:

- `lean-toolchain`
- `lakefile.lean`
- `.github/workflows/check-lean.yml`

The current minimal Lean lifecycle-invariant set covers:

1. AI final-responsibility boundary under current minimal assumptions
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

A Phase 2 Lean theorem-role index exists at `docs/phase-2-lean-theorem-index.md`.

The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates.

The AI final-responsibility boundary is assumption-scoped. In the current minimal model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

## Development Timeline

Observation
→ Definition
→ Specification
→ Lightweight structural checking
→ Formalization
→ Claim
→ Application

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.

## Current Focus

- Preserve the minimal, specification-first core
- Keep lifecycle examples readable
- Keep checker output bounded and non-certifying
- Keep Lean invariants small, explicit, and assumption-scoped
- Preserve the split Lean spine before adding more theorem families
- Use the theorem-role index before adding or renaming Lean theorem candidates
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility under the current minimal model
- Keep future artificial legal-personhood or institutional-personhood layers explicit if modeled later
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, Lean definitions, theorem roles, and assumptions

## Read First

1. README.md or README.ja.md
2. LUMINALIA.md
3. ROADMAP.md
4. CHANGELOG.md
5. docs/minimal-core-rationale.md
6. docs/phase-1-6-plan.md
7. formal/lean/README.md
8. docs/phase-2-lean-split-plan.md
9. docs/phase-2-lean-theorem-index.md
10. docs/definition.md
11. docs/eight-elements.md
12. docs/validator-boundary.md
13. docs/checker-coverage.md
14. docs/example-index.md
15. docs/example-review-notes.md
16. spec/responsibility-pathway-core.yaml
17. spec/pathway.schema.yaml

## Restart Point

The next low-risk action is not to expand into larger reference implementations yet.

Continue Phase 2 by either:

- observing the next Lean workflow result and adjusting only if the minimal build path fails
- adding only very small theorem candidates after the current assumptions, theorem roles, and split modules remain stable
- maintaining documentation synchronization across README, README.ja, ROADMAP, BEACON, CHANGELOG, `formal/lean/README.md`, and the theorem-role index

Do not begin larger reference implementations until definitions, examples, checker boundaries, Lean assumptions, theorem roles, and excluded claims remain aligned.

## Purpose

The objective is continuity.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
