# Source Alignment: 7ee72995004c90.md

This note records a source-alignment review for a legacy/hash-named Zenn article on Action Class Matrix.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/7ee72995004c90.md`
- Title: `AIエージェントの行為分類――責任経路を壊さないための Action Class Matrix`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align an Action Class Matrix source article with the repository's action-class, approval, stop, evidence, and human-return boundaries.

## Article-level role

The article defines Action Class Matrix as a lower-level component beneath Responsibility Pathway Layer for classifying AI-agent actions.

Although the file name is a hash, the article is core source material for action classification.

Current repository alignment:

- strongly aligned with Action Class Matrix vocabulary
- strongly aligned with Phase 3 staged example expansion
- strongly aligned with differentiated approval, stop, evidence, and repair requirements

Repository change decision:

- no immediate schema change required
- high-value source for future action-class examples and checker fixtures

## Action Class Matrix definition

The article defines Action Class Matrix as a design for classifying AI-agent actions according to impact scope, reversibility, externality, and approval requirement.

Its purpose is not to stop AI itself, but to change required responsibility pathways by action type.

Current repository alignment:

- directly aligned with action-class source direction
- supports action-class-sensitive governance rather than universal heavy controls
- supports avoiding both over-control of light actions and under-control of dangerous actions

Repository change decision:

- no immediate schema change
- future examples should state action class before claiming pathway sufficiency

## Why classification is needed

The article says AI-agent actions must not all be treated as a single `AI execution`. Reading, proposing, internal modification, external effects, reversible actions, irreversible actions, and emergency stops have different responsibility weight.

Current repository alignment:

- strongly aligned with RPL article and ISO action-granularity note
- supports not collapsing AI proposal, human adoption, execution, and external effect into one event
- supports future checker logic for action-class-specific required fields

Repository change decision:

- no immediate checker change
- useful source for future validation rules

## Six-class structure

The article defines six action classes:

- Class A: Observe-Only
- Class B: Suggest-Only
- Class C: Approval-Required
- Class D: Reversible External Action
- Class E: Irreversible or High-Impact Action
- Class F: Emergency Stop

It states that this is not a perfect classification table; the important point is not to treat all AI-agent actions as the same.

Current repository alignment:

- directly aligned with current action-class vocabulary
- supports incremental example design
- supports caution that the matrix is a design aid, not complete taxonomy

Repository change decision:

- no formal taxonomy claim should be added
- future examples may use these six classes as source-backed labels

## Class A: Observe-Only

The article says Observe-Only covers reading, viewing, and retrieving actions. It is generally light, but not automatically safe because external pages or user posts may include instructions or manipulation aimed at the AI.

The article emphasizes separating `seeing` from `being allowed to follow`.

Current repository alignment:

- strongly aligned with input-contamination and manipulation-pressure concerns from the RPL article
- supports lightweight personal/research/development contexts while still recognizing external-input risk
- supports future prompt-injection or contamination notes

Repository change decision:

- no immediate core-element addition
- possible future Input Contamination Handling note if repeated again

## Class B: Suggest-Only

The article says Suggest-Only covers summary, analysis, options, impact estimation, review comments, and email drafts. The key point is to separate proposal from execution.

Current repository alignment:

- strongly aligned with AI support-node boundary
- supports the existing human-AI review workflow example
- supports requiring separate human adoption for AI proposals

Repository change decision:

- no immediate example change required
- useful source for low-risk example expansions

## Class C: Approval-Required

The article says Approval-Required covers internal-state changes such as document updates, ticket-status changes, repository commits, internal knowledge updates, and draft saves. These require at least clarity about what changes, why, whose judgment, rollback, and change history.

Current repository alignment:

- strongly aligned with internal file-update examples
- supports Approval Gate and Evidence Log requirements
- supports internal-state-change examples without external-action claims

Repository change decision:

- no immediate example addition
- useful source for future internal-state example fixtures

## Class D: Reversible External Action

The article says Reversible External Action covers actions that affect the outside world but are relatively reversible, such as external shared-document updates, customer-facing drafts, external stakeholder tickets, some API setting changes, and notifications.

It requires approver, executor, execution log, rollback method, impact scope, and abnormal-case contact.

Current repository alignment:

- strongly aligned with enterprise checklist and external-action boundaries
- supports requiring stronger evidence and repair planning than internal-state changes
- supports reminding that reversible does not mean impact-free

Repository change decision:

- no immediate example addition
- possible future reversible external-action fixture

## Class E: Irreversible or High-Impact Action

The article says Irreversible or High-Impact Action includes external mail sending, contract/hiring/billing/customer notices, production DB updates, customer-data changes, permission changes, and production-system reflection.

It says this is not an area for autonomous AI execution and requires strong human approval, double-checking, execution logs, rollback possibility, and repair owner.

Current repository alignment:

- strongly aligned with high-impact and enterprise/SAP boundaries
- supports keeping DB/API/production examples parked until generic examples are stable
- supports explicit non-production and non-autonomous boundaries

Repository change decision:

- no immediate high-impact example addition
- useful source for future negative fixtures

## Class F: Emergency Stop

The article says Emergency Stop should be defined separately from ordinary execution. It is authority to stop, not authority to proceed. It includes stopping execution, tool calls, external sends, session isolation, temporary permission downgrade, and return to human confirmation.

It also states that Stop Authority should not be placed in the same location as execution authority, because if the actor who wants to execute also decides whether to stop, stopping may be delayed.

Current repository alignment:

- strongly aligned with Stop Authority source note
- supports catch-like exception path in the Try-catch analogy
- supports separated stop authority in high-impact examples

Repository change decision:

- no immediate schema change
- possible future Stop-and-Await or Emergency Stop example after source-alignment phase

## Connection to Responsibility Pathway Layer

The article states that Action Class Matrix is not complete by itself. Its purpose is to connect to Responsibility Pathway Layer and determine which responsibility path should be used.

It maps action classes to Decision Owner, Approval Gate, Execution Actor, Evidence Log, and Human Return Point.

Current repository alignment:

- directly aligned with RPL and source-alignment architecture
- supports treating Action Class Matrix as preprocessing for pathway design
- supports future checker rules that require different fields by action class

Repository change decision:

- no immediate checker change
- possible future rule: action class determines required evidence / approval / stop fields

## Implementation checklist alignment

The article provides a checklist for each tool or action:

- Which class is this action?
- Does it have external impact?
- Is it reversible or irreversible?
- Does it change internal state?
- Whose approval is required?
- Where does execution log remain?
- Whom does it return to in abnormal cases?
- Where is Stop Authority?

Current repository alignment:

- strongly aligned with enterprise checklist and RPL pre-execution checklist
- supports future tool/action manifest examples
- supports lightweight classification before full responsibility-pathway modeling

Repository change decision:

- no immediate schema change
- possible future `examples/action-class-matrix-minimal.yaml`

## Remaining design boundary

The article says Action Class Matrix alone is not final operational design. Real operations also require tool permission models, approval UI/UX, execution-log schema, rollback design, Human Return Point implementation conditions, Stop Authority firing conditions, and organization-role mapping.

Current repository alignment:

- strongly aligned with reference-implementation boundary
- supports not treating ACM as complete governance
- supports no production-readiness claim

Repository change decision:

- no immediate production claim
- keep ACM as entry point, not complete system

## Try-catch analogy alignment

The article strengthens the Try-catch/finally explanatory analogy:

- action classification is pre-try routing
- normal action path uses Decision Owner / Approval Gate / Execution Actor
- Emergency Stop and abnormal return are catch-like paths
- Evidence Log and repair requirements preserve finally-like closure

Current repository alignment:

- supports the analogy added during RPL legacy review
- should remain explanatory and non-formal unless formal semantics are added later

Repository change decision:

- no immediate formalization
- useful developer-facing explanatory bridge

## Claim-strength assessment

Compatible claims:

- Action Class Matrix classifies AI-agent actions by impact, reversibility, externality, and approval requirement
- not all AI actions should use the same responsibility-pathway weight
- proposal and execution must be separated
- internal-state changes require approval and evidence
- reversible external actions still require approval, logs, rollback, impact-scope, and abnormal contact
- irreversible/high-impact actions are not candidates for autonomous AI execution
- Emergency Stop is a separate stop authority, not execution authority
- Action Class Matrix is preprocessing for Responsibility Pathway Layer
- ACM is useful but incomplete without permissions, approval UI, logs, rollback, HRP, Stop Authority conditions, and organization-role mapping

Claims to keep bounded:

- perfect taxonomy
- complete operational design
- safety, compliance, legal, audit, or production readiness
- universal heavy controls for all AI actions
- immediate formal checker semantics

Repository interpretation:

This hash-named article is core Action Class Matrix source material. It should be treated as a primary source for future action-class examples, especially after Phase 3 examples move beyond the first minimal human-AI review workflow.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-guidance rule:

> Before claiming an AI-agent action has a responsibility pathway, classify the action by impact, reversibility, externality, and approval requirement; then decide approval, evidence, stop, human-return, and repair requirements from that class.

## Next action

Proceed to the next hash / legacy filename candidate:

- `articles/3829d785b15b60.md`
