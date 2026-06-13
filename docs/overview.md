# Responsibility Pathway Engineering Overview

This overview is the current entry map for the repository after the Zenn source-alignment pass.

It explains what Responsibility Pathway Engineering currently means in this repository, what it does not claim, and where to go next.

## One-line definition

Responsibility Pathway Engineering is a bounded design approach for making AI-involved judgment and action returnable, stoppable, reconstructable, and repairable through human, organizational, and operational responsibility structures.

## Central question

RPE asks:

> When AI participates in judgment or action, where does responsibility arise, where does it move, where can it stop, where can it return to humans, what evidence remains, and who repairs?

This is different from asking only:

- whether the model was accurate
- whether a human approval button existed
- whether a role was named in a RACI table
- whether a guardrail blocked an action
- whether a log entry exists

Those may all matter, but none of them alone establishes a responsibility pathway.

## Current source-aligned interpretation

The reviewed source material supports the following interpretation:

- RPE does not make AI responsible.
- RPE does not replace RACI, HITL, Guardrails, ISO/IEC 42001, or human oversight.
- RPE designs how responsibility flows around AI-mediated judgment and action.
- RPE is operation-oriented, but not itself a production runtime.
- RPE requires explicit boundaries for what examples, schemas, checkers, and Lean files do not claim.

## Two-layer model

The repository currently uses two related layers.

| Layer | Purpose | Where to read |
|---|---|---|
| Eight-element model | Structural dimensions that preserve responsibility returnability. | [docs/eight-elements.md](eight-elements.md) |
| Operational roles and controls | Concrete workflow roles/checkpoints for AI-involved operations. | [docs/concepts/core-elements.md](concepts/core-elements.md) |

The eight-element model is the broader structural layer:

- Meaning
- Authority
- Time
- Quality
- Trust
- Reversibility
- Value
- Cost

The operational role/control set is the current source-aligned implementation-facing layer:

- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Evidence Log
- Repair Owner
- Human Return Point

These are not competing lists. The seven operational roles/controls are practical pathway checkpoints that help preserve or inspect the eight structural dimensions in AI-involved workflows.

## Operational roles and controls

| Role / control | Role |
|---|---|
| Decision Owner | Owns the judgment or decision responsibility. |
| Approval Gate | Defines where approval is required before action. |
| Execution Actor | Performs or triggers the action. |
| Stop Authority | Can stop, suspend, or downgrade the action path. |
| Evidence Log | Supports reconstruction of the pathway. |
| Repair Owner | Owns rollback, repair, correction, or reconnection. |
| Human Return Point | Allows AI-mediated judgment to return to human understanding, authority, time, and responsibility capacity. |

## AI participation boundary

AI may participate as:

- classifier
- summarizer
- draft proposer
- recommendation generator
- tool-using actor under configured authority
- trace producer
- monitoring assistant

But under the current minimal assumptions, AI is not treated as a final responsibility holder.

Examples and schemas should preserve this boundary explicitly.

## Neighboring concepts

RPE is close to several existing concepts, but it asks a different question.

| Neighboring concept | Main question | RPE distinction |
|---|---|---|
| RACI | Who has which role? | How does responsibility move, stop, return, and repair? |
| HITL | Where does a human check? | What if human review becomes formal, skipped, overloaded, or ineffective? |
| Guardrails | What should not be allowed? | Who owns pending responsibility after a stop or failure? |
| Harness Engineering | How does the agent run stably? | Stable execution is not responsibility readiness. |
| Meaningful Human Control | Is human control meaningful? | Can responsibility still be traced and returned if control degrades? |
| Accountability gap | Where does responsibility become unclear? | Design the pathway so gaps are less likely to arise. |
| Human oversight | Can humans supervise or intervene? | What happens after intervention, non-intervention, stop, or repair? |

## Action Class Matrix

The source-aligned Action Class Matrix is maintained in [docs/action-class-matrix.md](action-class-matrix.md).

It classifies AI-agent actions by:

- impact
- reversibility
- externality
- approval requirement

Current source-aligned classes:

1. Class A: Observe-Only
2. Class B: Suggest-Only
3. Class C: Approval-Required
4. Class D: Reversible External Action
5. Class E: Irreversible or High-Impact Action
6. Class F: Emergency Stop

Action class should influence:

- approval strength
- evidence requirement
- stop condition
- human-return condition
- repair ownership

A pathway should not claim sufficiency without considering action class.

## Evidence, stop, return, and repair

The source-alignment pass strongly reinforces four design concerns.

### Evidence

Evidence Log is not merely an event log. It supports reconstruction of the responsibility pathway.

Useful evidence can include:

- request
- context
- AI proposal
- proposal adopter
- planned review
- actual review
- skipped review and reason
- approval
- execution
- stop
- rollback
- restart approval
- repair

### Stop

Stop Authority is not merely a technical abort.

It asks:

- who can stop
- under what conditions
- whether stop authority is separated from execution authority
- who owns pending responsibility after stop

### Return

Human Return Point is not merely human presence.

It asks whether AI-mediated judgment can return to human understanding, authority, time, information, and responsibility capacity.

### Repair

Repair Owner is not simply blame assignment.

Repair may include:

- rollback
- correction
- explanation
- incident response
- permanent countermeasure connection
- organizational responsibility rebundling

## Try/catch/finally analogy

A developer-facing analogy is available in [docs/explanations/try-catch-finally-responsibility-pathway.md](explanations/try-catch-finally-responsibility-pathway.md).

Short version:

```text
try      = normal judgment / approval / execution path
catch    = stop / abnormal return / exception handling path
finally  = evidence / repair / explanation / closure path
```

This is only an explanatory analogy. It is not formal semantics.

## Current implementation status

The repository currently contains:

- definitions and design notes
- minimal examples
- bounded structural checkers
- review-result schema and fixtures
- minimal Lean formalization of scoped invariants
- source-alignment notes and synthesis

The repository does not yet contain:

- production runtime
- production verifier
- legal responsibility engine
- compliance tool
- safety certification tool
- complete action-class checker
- formal try/catch/finally semantics

## Recommended next work

The source-alignment pass suggests this implementation order:

1. Stabilize README and overview entry points.
2. Keep `docs/concepts/core-elements.md` aligned as operational roles/controls connected to the eight-element model.
3. Keep `docs/action-class-matrix.md` aligned as the Class A-F action-class design aid.
4. Add negative examples for HITL collapse and rubber-stamp approval.
5. Draft `docs/proposals/evidence-log-approval-state-extension.md`.
6. Extend checkers by action class.
7. Add small Lean invariants only after examples and schemas stabilize.

## Boundary

This overview does not claim:

- legal validity
- safety assurance
- compliance
- certification
- production readiness
- fairness validation
- moral accountability resolution
- AI final-responsibility transfer

It is an orientation map for the repository's current public specification work.
