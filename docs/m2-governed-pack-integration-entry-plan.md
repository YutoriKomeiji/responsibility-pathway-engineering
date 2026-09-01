# RPE M2 Governed Pack Integration — Entry Plan

Status: **Historical entry baseline.**

This document records the original M2 entry plan. It is retained as design history, not as the current implementation-status source.

Current public status: [`m2-governed-integration-current.md`](m2-governed-integration-current.md).

## Original purpose

Define how RPE should move from the M1 Governed Reference Kernel into governed pack integration without collapsing governance eligibility, compatibility, applicability, requirement evaluation, execution authority, or final responsibility.

## What changed after implementation experience

The original plan assumed that M2 would largely be a linear E1–E7 implementation sequence. Subsequent RPE implementation and downstream runtime work showed that the boundary needed revision.

The current design now separates:

- the legacy/M1-compatible `evaluate_action()` entry;
- the explicit strict `evaluate_governed_action()` entry;
- evaluation authority from execution authority;
- evaluation evidence from external-effect evidence;
- repair readiness from repair authority;
- responsibility-preserving handoff from downstream execution-state ownership.

RPE therefore does **not** import an entire post-execution state machine into M2.

## Original objective retained

Governed, versioned Requirement Packs must fail visibly when incompatible, incorrectly bound, stale, ambiguous, suspended, superseded, ownerless, or otherwise ineligible. Such failures must not silently produce `allow`.

M2 still does not create:

- automatic legal or policy interpretation;
- self-updating regulation;
- production authorization;
- action execution authority;
- certification or compliance proof;
- transfer of final responsibility from the responsible human or institution.

## Original E1–E7 mapping to the current implementation

| Original slice | Current status |
|---|---|
| E1 runtime contract versioning | Implemented through explicit governed contract families and packaged version coherence |
| E2 canonical governance eligibility | Implemented for the strict governed path with normalized fail-closed checks |
| E3 compatibility gate | Implemented before governed evaluation |
| E4 governed evaluation pipeline | Implemented as `evaluate_governed_action()` |
| E5 deterministic negative fixtures | Implemented for major admission/governance/binding/version failure classes and retained as ongoing adversarial work |
| E6 bounded external loading | Implemented for caller content and explicit local files only; network/registry trust remains out of scope |
| E7 trace/repair/resume references | Revised: RPE preserves responsibility handoff requirements but does not own the complete post-execution repair/resume state machine |

## Current governed pipeline

```text
governed envelope admission
→ compatibility
→ pack/governance binding
→ governance eligibility
→ applicability
→ requirement evaluation
→ decision combination
→ responsibility-preserving handoff
```

Every governed result remains evaluation-only. `allow` is not an execution authorization token.

## Loader boundary

The first loader accepts:

- caller-provided UTF-8 JSON content;
- explicitly supplied local files.

It intentionally rejects network/remote registry loading. Loading bytes is not trust establishment. Source interpretation and governance correctness remain separately reviewable human/institutional responsibilities.

## Current completion decision

The original entry phase has been surpassed, but **full M2 closure is not yet claimed**.

The remaining M2 work is defined by the current roadmap and current-status document, with emphasis on:

1. uncertainty/effect/evidence handoff semantics;
2. repair/resume responsibility boundaries;
3. residual-owner and Human Return continuity;
4. adversarial validation;
5. claim-boundary and closure evidence.

Production or consequential live integration remains a separate Human Gate outside this document.
