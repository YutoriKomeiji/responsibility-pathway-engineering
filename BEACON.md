# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

## Current Position

Phase 0 foundation is complete.

Phase 1 concept model is substantially established.

Phase 1.5 specification binding is established.

Phase 1.6 lightweight validation and lifecycle-example coverage is substantially established.

Phase 2 formalization has started, the first minimal Lean lifecycle-invariant set has been introduced, the Lean core has been split into small modules, and a minimal Lean build path has been added.

Phase 2.5 enterprise implementation guidance has started. `docs/enterprise-implementation-profile.md` connects the minimal formal core to workflow, evidence, checker, and governance layers. `docs/responsibility-pathway-record-review.md` describes a plain-language review and recheck process for Responsibility Pathway records. `docs/phase-2-5-current-snapshot.md` records the current Phase 2.5 restart point.

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

The checker is lifecycle-aware and now includes optional `review_metadata` checks when that block is present, but it remains non-certifying. It checks structural signals only and does not claim legal validity, safety, compliance, fairness, moral resolution, production readiness, or real-world responsibility resolution.

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

A Phase 2 Lean current snapshot exists at `docs/phase-2-current-snapshot.md`.

A Phase 2 Lean theorem-role index exists at `docs/phase-2-lean-theorem-index.md`.

A Phase 2.5 enterprise and record-review current snapshot exists at `docs/phase-2-5-current-snapshot.md`.

The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates.

The AI final-responsibility boundary is assumption-scoped. In the current minimal model, no artificial legal-personhood layer is assumed, so an AI node is not treated as a final responsibility holder. Future legal, institutional, national, international, or user/provider-agreement layers must be modeled explicitly if introduced.

Enterprise guidance and record review guidance remain non-certifying. They help organizations preserve readable responsibility pathways, evidence records, review conditions, and excluded claims. They do not claim legal validity, safety, compliance, fairness, moral resolution, institutional certification, production readiness, or replacement of accountable humans and institutions.

## Development Timeline

Observation
→ Definition
→ Specification
→ Lightweight structural checking
→ Formalization
→ Enterprise guidance
→ Record review
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
- Use the current snapshot and theorem-role index before adding or renaming Lean theorem candidates
- Keep enterprise guidance readable and non-certifying
- Keep Responsibility Pathway record review plain, recheckable, and bounded to structure
- Use the Phase 2.5 current snapshot before expanding record-review examples or checker coverage
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility under the current minimal model
- Keep future artificial legal-personhood or institutional-personhood layers explicit if modeled later
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, Lean definitions, theorem roles, snapshots, assumptions, enterprise guidance, and record review boundaries

## Read First

1. README.md or README.ja.md
2. LUMINALIA.md
3. ROADMAP.md
4. CHANGELOG.md
5. docs/minimal-core-rationale.md
6. docs/enterprise-implementation-profile.md
7. docs/responsibility-pathway-record-review.md
8. docs/phase-2-5-current-snapshot.md
9. docs/phase-1-6-plan.md
10. formal/lean/README.md
11. docs/phase-2-current-snapshot.md
12. docs/phase-2-lean-split-plan.md
13. docs/phase-2-lean-theorem-index.md
14. docs/definition.md
15. docs/eight-elements.md
16. docs/validator-boundary.md
17. docs/checker-coverage.md
18. docs/example-index.md
19. docs/example-review-notes.md
20. spec/responsibility-pathway-core.yaml
21. spec/pathway.schema.yaml

## Restart Point

The next low-risk action is not to expand into larger reference implementations yet.

Continue by either:

- observing the next Lean workflow result and adjusting only if the minimal build path fails after Lean-file changes
- adding only very small theorem candidates after the current assumptions, theorem roles, split modules, and current snapshot remain stable
- checking schema and checker alignment with the enterprise implementation profile, Responsibility Pathway record review guide, and Phase 2.5 current snapshot
- adding only narrowly scoped record-review fixtures or checker checks while keeping them optional unless existing examples are deliberately migrated
- maintaining documentation synchronization across README, README.ja, ROADMAP, BEACON, CHANGELOG, `formal/lean/README.md`, the current snapshot, theorem-role index, enterprise implementation profile, record review guide, and Phase 2.5 snapshot

Do not begin larger reference implementations until definitions, examples, checker boundaries, Lean assumptions, theorem roles, current snapshot, enterprise guidance, record review boundaries, Phase 2.5 snapshot, and excluded claims remain aligned.

## Purpose

The objective is continuity.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
