# Try-catch-finally Analogy for Responsibility Pathways

This note explains a developer-facing analogy between Responsibility Pathway Engineering and `try / catch / finally` control flow.

This is an analogy only. It is not formal semantics, not a runtime specification, not a legal model, and not a compliance claim.

## Purpose

Responsibility Pathway Engineering often looks abstract when described in governance language.

For developers, a useful analogy is:

```text
try      = normal judgment / approval / execution path
catch    = stop / abnormal return / exception handling path
finally  = evidence / repair / explanation / closure path
```

This analogy is useful because Responsibility Pathways are not only about assigning responsibility. They are also about what happens when normal execution fails, degrades, skips review, creates external impact, or needs repair.

## Mapping overview

| Programming analogy | Responsibility Pathway meaning | Typical RPE elements |
|---|---|---|
| `try` | normal judgment, approval, and execution path | Decision Owner, Approval Gate, Execution Actor |
| `catch` | abnormal, uncertain, unsafe, skipped, stopped, or return-required path | Stop Authority, Human Return Point, Action Class Matrix, contamination handling |
| `finally` | evidence preservation, repair, rollback, explanation, restart, and closure | Evidence Log, Repair Owner, rollback decision, restart approval, organizational rebundling |

## Try path

The `try` path corresponds to the ordinary expected route of an AI-involved action.

Typical questions:

- Who requested the action?
- Who owns the judgment?
- Is AI proposing, classifying, drafting, or executing?
- Who adopts the AI proposal?
- Which approval gate is required?
- Who executes the action?
- What action class is this?

Typical elements:

- Decision Owner
- Approval Gate
- Execution Actor
- AI Support Node / AI Responsibility Node
- Action Class Matrix

The `try` path is not automatically safe. It is simply the normal planned path.

## Catch path

The `catch` path corresponds to what happens when the normal path becomes unsafe, unclear, skipped, degraded, contaminated, high-impact, or externally risky.

Typical catch triggers:

- human approval is skipped
- HITL becomes rubber-stamping
- action class is higher than expected
- input is contaminated or manipulative
- external effect appears
- tool behavior differs from expectation
- evidence is missing
- stop condition is reached
- human understanding or authority is insufficient
- rollback or repair responsibility is unclear

Typical questions:

- Who can stop?
- Under what condition must the process stop?
- Is stop authority separated from execution authority?
- Where does the case return to a human?
- Who catches responsibility if a stop did not occur?
- Who owns pending responsibility after stop?

Typical elements:

- Stop Authority
- Human Return Point
- Action Class Matrix
- Stop-and-Await
- Emergency Stop
- Input Contamination Handling
- Graceful Degradation

In this analogy, `catch` is not merely an error message. It is a responsibility return path.

## Finally path

The `finally` path corresponds to what must remain true whether the action succeeds, fails, is stopped, is rolled back, or later turns out to be defective.

Typical questions:

- What was proposed?
- Who adopted the proposal?
- Was human confirmation planned?
- Did actual confirmation happen?
- Was confirmation skipped? Why?
- Who executed?
- Who stopped or failed to stop?
- Who decided rollback?
- Who approves restart?
- Who repairs?
- Can the responsibility path be reconstructed afterward?

Typical elements:

- Evidence Log
- Repair Owner
- rollback decision
- restart approval
- incident explanation
- organizational rebundling
- policy update / reevaluation where relevant

In this analogy, `finally` is not only logging. It is evidence, repair, and closure.

## Why this analogy helps

The analogy helps developers avoid three mistakes.

### Mistake 1: treating approval as the whole responsibility path

A human approval step can exist inside `try`, but if the approval collapses into rubber-stamping, the pathway still needs `catch` and `finally`.

Approval alone does not answer:

- who stops
- who catches skipped review
- who rolls back
- who repairs
- who explains
- what evidence remains

### Mistake 2: treating guardrails as the whole responsibility path

Guardrails can block behavior, but a block is not the same as a full responsibility path.

A guardrail does not automatically answer:

- who owns pending responsibility after stop
- who decides whether to resume
- who repairs after failure
- who explains the incident
- how the case is reconstructed

### Mistake 3: treating logs as the whole responsibility path

Logs are finally-like, but logs alone do not define responsibility.

Evidence Log must connect to:

- decision
- adoption
- approval
- execution
- stop
- rollback
- repair
- return point

Otherwise the log is only an event trace, not a responsibility-path reconstruction layer.

## Relationship to Action Class Matrix

Action Class Matrix can be understood as pre-try routing.

Before an action enters the normal path, classify it:

- Observe-Only
- Suggest-Only
- Approval-Required
- Reversible External Action
- Irreversible or High-Impact Action
- Emergency Stop

The action class determines the strength of:

- approval requirement
- stop condition
- evidence requirement
- human-return condition
- repair ownership

## Relationship to HITL collapse

HITL is often part of the `try` path.

But source material shows that HITL can degrade through:

- formal approval
- rubber-stamping
- volume pressure
- emergency skip
- responsibility dilution

When that happens, the responsibility pathway needs catch/finally structure:

- catch: identify where review degraded, who should stop, where to return
- finally: preserve evidence, decide rollback/restart, connect repair

This is why RPE should distinguish planned review, actual review, degraded review, and skipped review.

## Relationship to Human Return Point

Human Return Point is not just a button or a generic approval screen.

In this analogy, HRP is a catch-like return target: the point where AI-mediated judgment returns to human understanding, authority, time, information, and responsibility capacity.

A valid return point should make it possible for a human to answer:

- what was proposed
- what changed
- what the risk is
- what evidence exists
- what happens if they approve
- what happens if they refuse
- who repairs if it fails

## Relationship to Repair Owner

Repair Owner is part of the finally-like closure.

Repair is not the same as blame. It includes:

- rollback
- correction
- explanation
- incident response
- permanent countermeasure connection
- organizational rebundling

The source material repeatedly frames repair and visibility as improvement-oriented, not punishment-oriented.

## Non-formal boundary

This analogy must remain bounded.

It does not mean:

- RPE is literally exception handling
- every pathway can be compiled into code
- responsibility is a program variable
- legal responsibility follows programming control flow
- `catch` or `finally` semantics are formally defined in the repository
- the repository currently proves runtime behavior

It only means:

- normal action paths need stop/return paths
- stop/return paths need evidence/repair closure
- successful execution still needs reconstructability
- failed execution needs responsibility recovery

## Recommended wording

Safe wording:

> Responsibility Pathways can be explained by a try/catch/finally analogy: normal judgment and execution occur in the try path; stop, abnormal return, and HITL collapse are catch-like paths; evidence, repair, rollback, restart, and organizational rebundling are finally-like closure. This is an explanatory analogy, not formal semantics.

Unsafe wording:

> Responsibility Pathways are formally equivalent to try/catch/finally.

> RPE proves exception-safe responsibility handling.

> Evidence Log is equivalent to finally.

> Stop Authority is equivalent to catch.

## Repository alignment decision

Status: explanatory note added.

No schema, checker, Lean, or runtime semantics change is introduced by this note.

Future formalization may introduce a state-machine or transition-system model, but this note does not claim one.
