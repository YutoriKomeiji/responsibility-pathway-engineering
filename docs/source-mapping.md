# Source Mapping

This document maps public explanatory articles to canonical repository definitions.

Public articles are treated as origin records and explanatory context.
The repository is treated as the canonical specification and formalization workspace.

## Mapping Principles

1. Articles preserve how the concept was first explained to readers.
2. Repository documents normalize the concept into definitions, specifications, and models.
3. Article language should not be copied directly into specifications without review.
4. Differences between article wording and repository wording are treated as concept maturation, not necessarily contradiction.
5. Formalization must refer to repository definitions, not informal article phrasing.

## Source Articles

| Source article | Extracted concept | Canonical repository document | Future spec / formalization target |
|---|---|---|---|
| `zenn-content/articles/what-is-responsibility-pathway.md` | Responsibility Pathway is not responsibility itself, but a pathway through which judgment, grounds, approval, execution, stopping, explanation, and repair can be made visible and returnable. | `docs/definition.md`, `docs/runtime-model.md`, `docs/responsibility-node.md` | lifecycle states, node capabilities, pathway invariants |
| `zenn-content/articles/why-responsibility-pathway-engineering.md` | Responsibility cannot be closed by evidence fixation alone; assumptions, observation boundaries, evaluation, communication, supervision, and improvement must remain connected. | `docs/eight-elements.md`, `docs/runtime-model.md`, `lessons/2026-06-formalization-scope-boundary.md` | premise pathways, evidence scope, assumption invalidation |
| `zenn-content/articles/responsible-ai-to-responsibility-pathway.md` | Responsible AI remains important, but AI-agent operation needs a pathway vocabulary for responsibility to originate, stop, return, and be repaired across humans, organizations, systems, and AI agents. | `docs/definition.md`, `docs/responsibility-node.md`, `spec/responsibility-pathway-core.yaml` | AI-as-pathway-participant model, state transition model |
| `zenn-content/articles/human-return-point.md` | Human-in-the-loop is not enough; responsibility must return to human understanding, authority, time, information, and organizational responsibility units. | pending: `docs/return-point.md` | Human Return Point conditions, returnability invariant |

## Canonicalization Notes

### Responsibility Pathway

Article-origin phrasing emphasizes explanatory clarity: responsibility becomes hard to trace when AI participates in judgment, approval, execution, stopping, explanation, and repair.

Repository phrasing should keep the same core idea while using implementation-neutral language:

- originate
- propagate
- suspend
- return
- repair
- close

### Responsibility Node

Article-origin parts such as Decision Owner, Approval Gate, Execution Actor, Stop Authority, Evidence Log, Repair Owner, and Human Return Point are treated as possible node roles.

The repository generalizes these into Responsibility Nodes with capabilities such as receive, preserve, transform, explain, escalate, suspend, return, repair, and close.

### Human Return Point

The Human Return Point article is the origin record for the distinction between a human merely being present and responsibility actually returning to a human-capable state.

The repository should formalize this as a return point model rather than as a simple HITL synonym.

## Boundary

This document does not make priority, ownership, legal, or novelty claims.

It exists to preserve a responsibility pathway between public explanatory writing and canonical technical specification.
