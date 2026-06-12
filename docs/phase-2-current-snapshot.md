# Phase 2 Current Snapshot

This snapshot records the current stable position of Phase 2 Lean formalization.

It is intended for future readers, maintainers, and AI-assisted continuation.

It adds no new formal claims. It does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness.

## Current position

Phase 2 formalization has reached a minimal, build-checked spine.

Current status:

- the Lean core has been split into small modules
- `Core.lean` remains the stable import entry point
- a minimal Lean build path exists
- Basic constructor sanity theorems have been added
- Example lifecycle sanity theorems have been added
- current invariant theorem candidates remain assumption-scoped and non-certifying
- the theorem-role index is available before further theorem expansion

## Lean module layout

Current modules:

```text
formal/lean/ResponsibilityPathway/Basic.lean
formal/lean/ResponsibilityPathway/Lifecycle.lean
formal/lean/ResponsibilityPathway/Examples.lean
formal/lean/ResponsibilityPathway/Invariants.lean
formal/lean/ResponsibilityPathway/Core.lean
```

`Core.lean` imports the split modules and serves as the stable entry point.

## Supporting documents

Read these documents before extending Phase 2:

- `formal/lean/README.md`
- `docs/phase-2-lean-split-plan.md`
- `docs/phase-2-lean-theorem-index.md`
- `README.md` or `README.ja.md`
- `ROADMAP.md`
- `BEACON.md`
- `CHANGELOG.md`

## Build path

Current build files:

```text
lean-toolchain
lakefile.lean
.github/workflows/check-lean.yml
```

The workflow installs Elan, runs `lake update`, and then runs `lake build`.

A passing build means only that the Lean package builds successfully.

It does not mean the formalization is legally valid, safe, compliant, fair, morally resolved, certified, or production ready.

## Current theorem categories

The current theorem roles are indexed in:

```text
docs/phase-2-lean-theorem-index.md
```

Current categories:

1. Basic constructor sanity theorems
2. Example lifecycle sanity theorems
3. Boundary predicates
4. Positive invariant theorem candidates
5. Vacuity / non-trigger theorem candidates

## Current invariant candidates

The current positive invariant theorem candidates cover:

1. AI final-responsibility boundary under current minimal assumptions
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

These are scoped to the explicitly modeled assumptions and constructor-level examples.

## AI final-responsibility boundary

The current AI final-responsibility boundary is assumption-scoped.

In the current minimal RPE model, no artificial legal-personhood layer is assumed. Therefore, an AI node is not treated as a final responsibility holder in this model.

This is not a universal claim about all possible future legal, institutional, national, international, or user/provider-agreement regimes.

If such a layer is introduced later, it must be modeled explicitly, and the current boundary must be revisited.

## Non-certifying boundary

The current Phase 2 Lean work does not claim:

- real-world legal validity
- real-world safety
- compliance
- fairness
- moral accountability resolution
- institutional certification
- production readiness
- operational completeness
- complete responsibility ontology
- artificial legal-personhood modeling

All current proofs and theorem candidates are structural and assumption-bound.

## Next allowed work

Low-risk next steps:

1. Observe the next Lean workflow result after Lean-file changes.
2. Keep theorem names stable unless there is a clear reason to rename.
3. Use `docs/phase-2-lean-theorem-index.md` before adding or renaming theorem candidates.
4. Add only small theorem candidates that preserve current assumptions.
5. Prefer constructor-level or implication-shape checks before generalized theory.
6. Keep documentation synchronized after each conceptual milestone.

## Stop conditions

Stop before expanding Phase 2 if:

- the minimal Lean build fails
- a theorem candidate requires new assumptions that are not documented
- a change blurs the non-certifying boundary
- theorem roles become unclear
- claims start implying legal validity, safety, compliance, fairness, certification, moral resolution, or production readiness
- a larger reference implementation would outrun current definitions, examples, checker boundaries, Lean assumptions, and excluded claims

## Current restart point

The next safe continuation point is:

- check the latest Lean workflow if a Lean file was changed
- then, if green, add only a small theorem or documentation refinement aligned with the theorem-role index

Do not jump directly to larger reference implementations yet.
