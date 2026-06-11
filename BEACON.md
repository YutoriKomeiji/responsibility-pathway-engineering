# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

## Current Position

Phase 0 foundation is complete.

Phase 1 concept model is substantially established.

Phase 1.5 specification binding is established.

Phase 1.6 lightweight validation and lifecycle-example coverage is substantially established.

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
- Prepare small Lean invariants
- Preserve the boundary that AI may participate as a pathway node but does not assume final responsibility
- Grow only when responsibility can still return from claims to definitions, examples, schemas, checker boundaries, excluded claims, and assumptions

## Read First

1. README.md or README.ja.md
2. LUMINALIA.md
3. ROADMAP.md
4. CHANGELOG.md
5. docs/minimal-core-rationale.md
6. docs/definition.md
7. docs/eight-elements.md
8. docs/phase-1-6-plan.md
9. docs/validator-boundary.md
10. docs/checker-coverage.md
11. docs/example-index.md
12. docs/example-review-notes.md
13. spec/responsibility-pathway-core.yaml
14. spec/pathway.schema.yaml

## Restart Point

The next low-risk action is to begin Phase 2 with a very small Lean invariant, such as:

- an AI node cannot be final responsibility holder
- an AI-assisted pathway must preserve a human or institutional return point
- a repaired pathway must reference a repair record

Do not begin larger reference implementations until definitions, examples, checker boundaries, and formalization assumptions remain aligned.

## Purpose

The objective is continuity, not memory.

The objective is to preserve a pathway through which responsibility, meaning, and understanding can return.

Read this file first when reconnecting to the project.
