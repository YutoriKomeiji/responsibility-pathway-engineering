# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

## Current Position

Phase 0 foundation is complete.

Phase 1 concept model is substantially established.

Phase 1.5 specification binding is established.

Phase 1.6 lightweight validation and lifecycle-example coverage is substantially established.

Phase 2 formalization has started, the first minimal Lean lifecycle-invariant set has been introduced, and the Lean core has been split into small modules.

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

Lean CI or local Lean build verification is not yet established in this repository. The current GitHub Actions workflow covers only the bounded Python example checker.

The current minimal Lean lifecycle-invariant set covers:

1. AI final-responsibility boundary under current minimal assumptions
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

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
- Establish a minimal Lean check path before treating the split formalization as build-verified
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility under the current minimal model
- Keep future artificial legal-personhood or institutional-personhood layers explicit if modeled later
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, Lean definitions, and assumptions

## Read First

1. README.md or README.ja.md
2. LUMINALIA.md
3. ROADMAP.md
4. CHANGELOG.md
5. docs/minimal-core-rationale.md
6. docs/phase-1-6-plan.md
7. formal/lean/README.md
8. docs/phase-2-lean-split-plan.md
9. docs/definition.md
10. docs/eight-elements.md
11. docs/validator-boundary.md
12. docs/checker-coverage.md
13. docs/example-index.md
14. docs/example-review-notes.md
15. spec/responsibility-pathway-core.yaml
16. spec/pathway.schema.yaml

## Restart Point

The next low-risk action is not to expand into larger reference implementations yet.

Continue Phase 2 by either:

- establishing a minimal Lean toolchain and build/check path
- adding only very small additional invariant candidates after the current assumptions remain clear and the split modules remain stable
- maintaining documentation synchronization across README, README.ja, ROADMAP, BEACON, CHANGELOG, and `formal/lean/README.md`

Do not begin larger reference implementations until definitions, examples, checker boundaries, Lean assumptions, and excluded claims remain aligned.

## Purpose

The objective is continuity.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
