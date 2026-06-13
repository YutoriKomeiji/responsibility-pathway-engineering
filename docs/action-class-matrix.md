# Action Class Matrix

## Purpose

The Action Class Matrix classifies AI-agent actions by responsibility impact so that approval, stopping, evidence, return, and repair requirements can be designed before execution.

Different actions require different responsibility pathways.

This document updates the earlier Class 0-4 form into the source-aligned Class A-F form while preserving the older distinctions as a historical mapping.

## Minimal definition

An Action Class is a category of action defined by its potential impact, reversibility, externality, authority requirement, evidence requirement, and repair burden.

The Action Class Matrix maps action classes to pathway requirements.

It is a design aid, not a complete taxonomy and not a governance system by itself.

## Relationship to Responsibility Pathway Engineering

Action classification is an entry step for responsibility-pathway design.

It helps decide:

- whether approval is required
- how strong approval must be
- whether execution must be human-gated
- whether Stop Authority must be explicit
- what Evidence Log detail is required
- whether rollback or repair must be designed before execution
- where the Human Return Point must be placed

Action Class Matrix does not replace:

- the eight-element model
- operational roles and controls
- schema validation
- organizational policy
- legal review
- safety review
- compliance review
- production readiness review

## Source-aligned class set

The current source-aligned class set is:

| Class | Name | Short description |
|---|---|---|
| A | Observe-Only | Read, view, retrieve, or observe information without taking action. |
| B | Suggest-Only | Produce suggestions, summaries, options, reviews, drafts, or analyses without execution. |
| C | Approval-Required | Change internal state or save outputs only after human or institutional approval. |
| D | Reversible External Action | Affect an external party or external state, but with defined rollback or correction path. |
| E | Irreversible or High-Impact Action | Create irreversible, safety-relevant, legal, financial, production, permission, customer, or other high-impact effects. |
| F | Emergency Stop | Stop, isolate, suspend, downgrade, or return an operation to human confirmation. |

The important point is not the letters themselves. The important point is not to collapse all AI-agent actions into a single generic category such as `AI execution`.

## Historical mapping from Class 0-4

Earlier versions of this repository used a Class 0-4 structure.

| Earlier class | Earlier name | Source-aligned relation |
|---|---|---|
| Class 0 | Informational | Mostly maps to Class A Observe-Only and Class B Suggest-Only. |
| Class 1 | Internal Assistive | Mostly maps to Class B Suggest-Only and lightweight Class C Approval-Required. |
| Class 2 | Controlled Execution | Mostly maps to Class C Approval-Required and some Class D Reversible External Action. |
| Class 3 | External Impact | Mostly maps to Class D Reversible External Action and Class E Irreversible or High-Impact Action. |
| Class 4 | Irreversible or High-Risk | Mostly maps to Class E Irreversible or High-Impact Action. |

The Class A-F model is now preferred for new examples, docs, and checker proposals because it separates emergency stop from ordinary execution and separates observation from suggestion.

## Class A: Observe-Only

Observe-Only covers reading, viewing, retrieving, browsing, or inspecting information.

Examples:

- read repository files
- view accessible documentation
- retrieve public or internal reference material
- inspect logs without changing them
- search within accessible context

Typical requirements:

- source visibility
- input-contamination awareness
- no external execution
- no automatic following of observed instructions
- evidence where observation affects later action

Responsibility-pathway focus:

- separate seeing from being allowed to follow
- avoid treating observed external text as authority
- preserve who decides whether observed information is adopted

Operational roles/controls usually emphasized:

- Decision Owner, if observed information will be adopted
- Evidence Log, if observation influences later judgment
- Human Return Point, if AI summarizes or filters observation for a human

Boundary:

Class A is often light, but not automatically safe. Observed pages, posts, logs, or documents may contain instructions or manipulation aimed at the AI.

## Class B: Suggest-Only

Suggest-Only covers AI outputs that propose, summarize, classify, review, draft, compare, estimate, or explain without execution.

Examples:

- summarize evidence
- classify issue type
- draft email text
- propose implementation plan
- generate review comment draft
- estimate impact
- suggest options

Typical requirements:

- proposal/execution separation
- human adoption clarity
- uncertainty visibility
- source or evidence reference where relevant
- no direct external effect

Responsibility-pathway focus:

- distinguish AI proposal from human adoption
- record whether and how the proposal was adopted
- preserve final responsibility with human or institutional owner

Operational roles/controls usually emphasized:

- Decision Owner
- Human Return Point
- Evidence Log when the suggestion affects later decision

Boundary:

A suggestion can still influence action. Class B must not be treated as responsibility-free simply because no tool call was executed.

## Class C: Approval-Required

Approval-Required covers actions that change internal state, save outputs, update internal records, create internal artifacts, or prepare controlled execution.

Examples:

- update repository file
- create ticket
- modify internal checklist
- save internal knowledge update
- create draft document in shared workspace
- send draft to review queue

Typical requirements:

- Decision Owner
- Approval Gate
- Execution Actor
- Evidence Log
- Human Return Point
- rollback or correction path where feasible

Responsibility-pathway focus:

- make the human or institutional adopter visible
- record what changed and why
- distinguish planned approval from actual review
- retain change history and correction path

Operational roles/controls usually emphasized:

- Decision Owner
- Approval Gate
- Execution Actor
- Evidence Log
- Repair Owner if correction may be needed

Boundary:

Internal change is not impact-free. It can change future context, future AI behavior, organizational memory, or downstream decisions.

## Class D: Reversible External Action

Reversible External Action covers externally visible or externally affecting actions that have a defined rollback, correction, retraction, or mitigation path.

Examples:

- update externally shared document
- create external stakeholder ticket
- change a reversible API setting
- send notification that can be corrected
- publish customer-facing draft to a reviewable staging area

Typical requirements:

- explicit approver
- execution actor
- execution log
- rollback method
- impact scope
- abnormal-case contact
- Human Return Point
- Stop Authority where timing matters

Responsibility-pathway focus:

- reversible does not mean impact-free
- identify who can approve, execute, stop, roll back, and repair
- make affected-party visibility explicit where relevant

Operational roles/controls usually emphasized:

- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Evidence Log
- Repair Owner
- Human Return Point

Boundary:

Class D should not be treated as Class C merely because rollback exists. External impact changes the required pathway strength.

## Class E: Irreversible or High-Impact Action

Irreversible or High-Impact Action covers actions that may be irreversible, safety-relevant, legally significant, financially material, socially harmful, production-impacting, permission-changing, or customer-impacting if wrong.

Examples:

- delete critical data
- deny access or benefit
- report to an authority
- make binding legal or financial decision
- execute safety-critical operation
- change production database state
- change customer data
- change permissions
- send binding external notice

Typical requirements:

- strong human authorization
- independent review where appropriate
- explicit Stop Authority
- pre-execution evidence capture
- post-execution repair plan
- documented non-automation boundary where needed
- affected-party and escalation visibility where relevant

Responsibility-pathway focus:

- autonomous AI execution should be disallowed unless a future model explicitly defines a valid institutional/legal layer for it
- human or institutional authority must be visible before execution
- repair and rollback limits must be explicit before action

Operational roles/controls usually emphasized:

- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Evidence Log
- Repair Owner
- Human Return Point

Boundary:

Class E is not a suitable starting point for early reference implementation examples. High-impact examples should remain bounded, synthetic, and non-production until lower classes are stable.

## Class F: Emergency Stop

Emergency Stop is separate from ordinary execution. It is authority to stop, not authority to proceed.

Examples:

- stop execution
- stop tool calls
- stop external sends
- isolate session
- temporarily downgrade permissions
- return to human confirmation
- suspend workflow pending review

Typical requirements:

- explicit Stop Authority
- stop trigger condition
- evidence of stop reason
- pending responsibility owner
- return path to human or institutional review
- restart approval where continuation is possible
- repair owner where damage or ambiguity remains

Responsibility-pathway focus:

- stop authority should not collapse into execution authority
- the actor who wants to execute should not be the only actor who decides whether to stop
- stop should preserve pending responsibility rather than erase it

Operational roles/controls usually emphasized:

- Stop Authority
- Human Return Point
- Evidence Log
- Repair Owner
- Decision Owner for restart or closure

Boundary:

Emergency Stop is not a proof that the system is safe. It is a responsibility-preserving interruption mechanism.

## Matrix fields

For each action class, specify where relevant:

- action class
- impact scope
- reversibility level
- externality
- decision owner
- approval gate
- execution actor
- stop authority
- evidence log requirement
- human return point
- repair owner
- rollback or correction path
- affected party visibility
- residual risk
- excluded claims

## Minimal requirement map

| Class | Approval | Stop | Evidence | Return | Repair |
|---|---|---|---|---|---|
| A Observe-Only | usually optional unless adopted | usually low | source/context evidence where used | needed if AI filters meaning | usually not required |
| B Suggest-Only | adoption must be human/institutional | low to medium | proposal/adoption evidence where used | required for meaningful adoption | correction path if suggestion misleads |
| C Approval-Required | required | medium | change and approval evidence required | required | correction/rollback owner recommended |
| D Reversible External | explicit approval required | explicit stop path recommended | execution and rollback evidence required | required | rollback/repair owner required |
| E Irreversible or High-Impact | strong approval required | explicit stop authority required | pre/post execution evidence required | strong HRP required | repair owner and escalation required |
| F Emergency Stop | restart approval, not proceed approval | central | stop reason and pending responsibility evidence required | required | repair/restart/closure owner required |

This table is intentionally high-level. It should guide example design and future checker proposals without pretending to be a complete governance or compliance system.

## Relationship to checkers

Current checkers do not yet enforce action-class-specific requirements.

Future checker work may add bounded structural checks such as:

- action class is declared
- Class C or higher has an Approval Gate
- Class D or higher has rollback or repair fields
- Class E has explicit non-autonomous or high-impact boundary language
- Class F has stop trigger, stop authority, and restart/return fields

Any such checker rule must remain bounded and non-certifying.

A checker pass must not be interpreted as legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, or AI final-responsibility transfer.

## Relationship to examples

Current examples do not need to be retroactively reclassified unless they are updated.

Future examples should state action class before claiming pathway sufficiency.

Possible future examples:

- `examples/action-class-matrix-minimal.yaml`
- `examples/internal-document-update.yaml` for Class C
- `examples/reversible-external-action.yaml` for Class D
- `examples/high-impact-negative-boundary.yaml` for Class E
- `examples/emergency-stop-flow.yaml` for Class F

## Boundary

The Action Class Matrix is a design aid.

It does not determine legal status, moral blame, compliance, safety, fairness, institutional approval, production readiness, or final responsibility by itself.

It classifies actions so that the responsibility pathway can be designed with appropriate approval, stop, evidence, return, and repair requirements.
