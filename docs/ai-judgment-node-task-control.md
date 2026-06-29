# AI Judgment Node and Task Control Boundary

This note records a bounded concept for AI-assisted task control inside a Responsibility Pathway.

It exists because modern AI tooling can already place AI systems in local judgment roles, such as deciding whether a task should continue, stop, retry, escalate, or re-observe a changing state.

This note is a concept and operation boundary note only. It does not introduce schema changes, checker changes, workflow changes, runtime connectors, production runtime, legal decision logic, safety certification, compliance certification, fairness certification, Lean formalization, conformance model, or AI final-responsibility transfer.

## Core distinction

Responsibility Pathway Engineering must distinguish:

- final responsibility
- intermediate operational judgment
- evidence visibility
- execution authority
- review or override authority

A human or institution may remain the final responsible party while an AI system performs local operational judgment within the pathway.

Treating every AI-assisted operation as if the human made every intermediate decision can hide real judgment points.

Treating an AI local judgment as final responsibility can also overstate what the system does.

Both errors are out of scope for this repository.

## AI Judgment Node

An AI Judgment Node is a non-human system component that performs a local decision function within a Responsibility Pathway.

Examples of local decision functions include:

- stop or continue judgment
- retry judgment
- re-observation timing judgment
- escalation judgment
- prioritization judgment
- evidence-selection judgment
- action-selection judgment
- boundary-return judgment

An AI Judgment Node does not necessarily bear final responsibility.

However, its judgment should be treated as a pathway-relevant event when it affects continuation, stopping, evidence selection, escalation, or downstream action.

## Loop and goal style task control

Loop-style and goal-style AI task control can be useful as bounded task-control mechanisms.

In this repository vocabulary:

- a loop-like mechanism may be modeled as a re-observation or continuation-control signal
- a goal-like mechanism may be modeled as a stop-condition or return-condition signal
- an evaluator model may be modeled as a local AI Judgment Node

This does not make evaluator separation the same as verification.

Evaluator separation may reduce self-completion or self-grading failure modes, but it does not by itself establish factual correctness, semantic responsibility correctness, safety, legality, compliance, fairness, connector correctness, runtime correctness, conformance, or production readiness.

## Evidence visibility boundary

An AI Judgment Node may only judge from the information visible to it.

If the judging system sees only summarized conversation content, selected tool output, selected evidence, or another AI system's report, then the judgment is bounded by that visibility.

This matters because an AI worker may also act as an evidence-selection node by deciding which evidence to present to an evaluator or human reviewer.

A pathway record should therefore distinguish:

- who or what selected the evidence
- what evidence was visible to the judging node
- what evidence was missing or unobserved
- whether the judgment was based on tool output, file diff, logs, tests, citations, reviewer comments, or only an AI-generated summary

## Judgment versus execution

AI judgment and AI execution are separate pathway events.

A system may judge that an action should be taken without executing it.

A system may execute an action because another node judged it allowable.

A bounded pathway record should preserve this separation when it matters for review, repair, or accountability.

## Approval-skip and responsibility transfer boundary

A pathway may allow a human approval step to be skipped for bounded AI judgment or execution.

Approval skip is not responsibility skip.

If approval is skipped, the pathway should preserve:

- the rule or policy that allowed the skip
- the risk or reversibility class
- the AI Judgment Node involved
- the responsible human, role, or institutional owner that accepted the skip condition
- the escalation or return point if the skipped approval later becomes disputed
- the evidence needed to reconstruct why the skip was allowed

High-volume processing should not hide responsibility inside individual omitted approvals.

When repeated AI-assisted decisions are allowed without per-case human approval, responsibility should move to the higher-level owner that authorized the design, policy, contract, deployment condition, or operating rule.

This transfer may be internal to an organization, based on contract or policy, or may later be interpreted through legal or regulatory layers.

It does not transfer final responsibility to the AI system.

## Layered responsibility return

A responsibility pathway may return through multiple layers, depending on the matter and governance context:

1. individual actor or operator
2. team, manager, or designated owner
3. organization under internal rule, policy, or contract
4. state or legal framework
5. cross-border or international governance body where applicable

This list is a conceptual pathway map only.

It does not decide legal liability, jurisdiction, or institutional authority.

## Minimum record for AI local judgment

When an AI Judgment Node matters to a task, a minimum record should preserve:

- input context or triggering event
- visible evidence
- missing or unobserved evidence
- available options when known
- selected option
- stop, continue, retry, escalation, or action-selection result
- risk or reversibility class when known
- whether execution was allowed, blocked, or returned
- whether human or institutional review was required
- whether approval was performed, skipped, or transferred under a policy
- downstream action or no-action status
- audit or repair path

This minimum record is a documentation target, not a schema requirement in the current repository state.

## Task-control boundary

A bounded task-control layer may include:

1. Entry Condition
2. AI Judgment Node
3. Evidence Gate
4. Risk or Reversibility Classifier
5. Authority Gate
6. Execution Node
7. Observation Loop
8. Stop Condition
9. Human or Institutional Return Gate
10. Record Handoff

This list is a conceptual planning aid only.

It does not authorize implementation of autonomous task control, runtime connectors, automatic approval, automatic execution, production conversion code, workflow expansion, schema expansion, checker expansion, conformance checks, or Lean expansion.

## Required non-claims

This note does not claim that:

- AI can hold final responsibility
- AI local judgment is legally responsible judgment
- evaluator separation proves correctness
- loop or goal mechanisms prove safety
- AI task control is production-ready
- runtime correctness is established
- connector correctness is established
- semantic responsibility correctness is established
- human review can be omitted without a defined policy, record, and responsibility-transfer path
- responsibility can be laundered through post-hoc human approval

## Current repository use

For now, this note should be used only to name and bound a concept that may affect future runtime-event, adapter-boundary, repository-maintenance, and external-review discussions.

It can help reviewers ask whether an AI system was only a support node, or whether it also acted as a local judgment node inside the responsibility pathway.

Any future schema, checker, workflow, connector, runtime, or Lean work based on this concept requires a separate design note and restart-condition review.
