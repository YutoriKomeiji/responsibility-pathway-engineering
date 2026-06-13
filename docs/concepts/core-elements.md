# Core Elements of Responsibility Pathways

This document describes the current source-aligned minimal element set for Responsibility Pathway Engineering.

It does not replace the historical eight-element model in this repository. Instead, it records the current minimal operational set that emerged from the Zenn source-alignment pass.

## Scope

These elements describe responsibility-flow structure for AI-involved judgment and action.

They do not determine legal liability, safety, compliance, fairness, moral accountability, certification, or production readiness.

## Minimal element set

The current minimal pathway elements are:

1. Decision Owner
2. Approval Gate
3. Execution Actor
4. Stop Authority
5. Evidence Log
6. Repair Owner
7. Human Return Point

Together, these elements ask:

> Who owns the judgment, who approves, who executes, who can stop, what evidence remains, who repairs, and where can the case return to human responsibility capacity?

## Element summary

| Element | Short role | Primary question |
|---|---|---|
| Decision Owner | Owns judgment responsibility. | Who owns the decision or judgment unit? |
| Approval Gate | Defines required approval before action. | Where must approval occur before execution? |
| Execution Actor | Performs or triggers action. | Who or what executes the approved action? |
| Stop Authority | Can stop, suspend, or downgrade the path. | Who can stop or hold the process? |
| Evidence Log | Supports pathway reconstruction. | What remains to reconstruct what happened? |
| Repair Owner | Owns repair, rollback, or reconnection. | Who repairs after failure or ambiguity? |
| Human Return Point | Returns AI-mediated judgment to human capacity. | Where can the case return to human understanding and authority? |

## 1. Decision Owner

The Decision Owner is the human, role, team, or organization unit that owns the judgment responsibility.

A Decision Owner is not merely a name attached after an incident. It is the responsibility unit that can accept, reject, revise, or delegate a judgment.

Useful questions:

- Who owns the judgment before AI output is adopted?
- Who can decide whether the AI proposal is acceptable?
- Is the decision owner an individual, role, team, or organization unit?
- Does the decision owner have enough information, authority, and time?

Boundary:

- AI may suggest or classify.
- AI is not treated as the final Decision Owner under current minimal assumptions.

## 2. Approval Gate

The Approval Gate defines where approval is required before action can proceed.

Approval is not merely the existence of a button or policy field. It should indicate where responsibility is accepted before execution.

Useful questions:

- Is approval required for this action class?
- Who approves?
- Is approval explicit or implicit?
- Was approval planned?
- Was approval actually performed?
- Was approval skipped? Why?

Boundary:

- A planned approval gate is not the same as actual review.
- A human-in-the-loop step can degrade into rubber-stamping or skipped review.

## 3. Execution Actor

The Execution Actor performs or triggers the action.

In AI-agent settings, execution can involve a human, an AI tool call, a workflow system, an API, a script, or another operational actor.

Useful questions:

- Who or what executes the action?
- Was the execution internal or externally visible?
- Was the execution reversible?
- Was execution delegated to a tool or workflow?
- Did the execution match the approved action?

Boundary:

- Execution capability is not responsibility ownership.
- Stable execution is not responsibility readiness.

## 4. Stop Authority

Stop Authority defines who can stop, suspend, downgrade, or hold the pathway.

Stop Authority is not merely a technical abort. It is a responsibility-pathway role.

Useful questions:

- Who can stop before execution?
- Who can stop during execution?
- Who can stop after unexpected output or context change?
- Is stop authority separated from execution authority?
- What happens to pending responsibility after stop?

Boundary:

- A guardrail block is not enough by itself.
- The pathway must still answer who owns the stopped case and what happens next.

## 5. Evidence Log

Evidence Log records enough structure to reconstruct the responsibility pathway.

It is not merely a generic event log and not a legal proof engine.

Useful evidence can include:

- request
- context
- AI proposal
- proposal adopter
- planned approval
- actual approval
- review depth
- skipped review and reason
- execution actor
- stop condition
- stop actor
- rollback decision
- restart approval
- repair owner

Useful questions:

- Can the pathway be reconstructed after the fact?
- Can we distinguish AI proposal from human adoption?
- Can we distinguish planned review from actual review?
- Can we find where the pathway broke?

Boundary:

- Evidence Log supports reconstructability.
- It does not certify legal, safety, compliance, fairness, or production validity.

## 6. Repair Owner

Repair Owner owns post-failure repair, rollback, correction, explanation, incident response, or process reconnection.

Repair is not the same as blame. It is how the pathway reconnects after ambiguity, harm, error, skipped review, failed stop, or incomplete evidence.

Useful questions:

- Who decides rollback?
- Who corrects the output or action?
- Who owns incident response?
- Who reconnects the case to organizational responsibility?
- Who approves restart after repair?

Boundary:

- Explanation alone is not repair.
- Logging alone is not repair.
- Blame assignment is not the primary purpose of repair ownership.

## 7. Human Return Point

Human Return Point defines where AI-mediated judgment can return to human understanding, authority, time, information, and responsibility capacity.

It is not merely a human present in the loop.

Useful questions:

- Can the human understand what AI proposed?
- Can the human see what changed?
- Can the human see risk and uncertainty?
- Does the human have authority to approve, stop, or redirect?
- Does the human have time and information to meaningfully review?
- Who repairs if the human refuses or the action fails?

Boundary:

- HITL is not automatically HRP.
- Approval UI is not automatically HRP.
- HRP requires practical returnability, not only nominal human involvement.

## Relationship to Action Class Matrix

The required strength of each element depends on action class.

For example:

- Observe-Only may need low approval strength but still needs boundary clarity.
- Suggest-Only must distinguish AI proposal from human adoption.
- Approval-Required must have an explicit Approval Gate and Evidence Log.
- Reversible External Action should have rollback and stop paths.
- Irreversible or High-Impact Action should require stronger human return, stop, evidence, and repair design.
- Emergency Stop is itself a stop-oriented action class.

See `docs/concepts/action-class-matrix.md` when available.

## Relationship to try/catch/finally analogy

A developer-facing analogy maps the elements roughly as follows:

- `try`: Decision Owner, Approval Gate, Execution Actor
- `catch`: Stop Authority, Human Return Point, Action Class Matrix
- `finally`: Evidence Log, Repair Owner, rollback, restart, explanation, organizational rebundling

This analogy is explanatory only and not formal semantics.

See [docs/explanations/try-catch-finally-responsibility-pathway.md](../explanations/try-catch-finally-responsibility-pathway.md).

## Boundary and non-claims

This document does not claim:

- legal liability resolution
- moral accountability resolution
- safety assurance
- compliance certification
- fairness validation
- production readiness
- AI final-responsibility transfer
- complete formal semantics

It only records the current source-aligned minimal element set for repository design work.
