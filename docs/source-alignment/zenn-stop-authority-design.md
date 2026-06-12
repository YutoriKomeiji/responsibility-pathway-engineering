# Source Alignment: stop-authority-design.md

This note records a source-alignment review for the Zenn article on Stop Authority design.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/stop-authority-design.md`
- Title: `Stop Authority設計――AIエージェントの停止権限`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the public Stop Authority definition with the repository's bounded stop, suspension, return, evidence, and repair boundaries.

## Article-level role

The article frames Stop Authority as a responsibility-pathway design object for deciding who can stop AI-agent judgment, execution, tool use, or external effect, under what conditions, and where responsibility returns after stopping.

Current repository alignment:

- strongly aligned with Stop Authority vocabulary
- strongly aligned with Human Return Point
- strongly aligned with Evidence Log / Stop Log concepts
- strongly aligned with repair and lifecycle-state examples
- supports Phase 3 examples that distinguish execution, approval, stopping, return, and repair

Repository change decision:

- no immediate schema change required
- high-value source for future suspension, stop-and-await, and emergency-stop examples

## Stop Authority definition

The article defines Stop Authority as the design that specifies who can stop AI-agent judgment, execution, tool use, or external reflection, and under what conditions.

It also states that Stop Authority is not merely a stop button. It is both a brake for AI action and a branch point for returning responsibility to humans, organizations, or institutions.

Current repository alignment:

- directly aligned with Stop Authority concept
- supports distinguishing technical stop from responsibility-pathway stop
- supports the rule that stopping must connect to return and repair

Repository change decision:

- no immediate definition rewrite required
- future examples should show stopping as a pathway transition, not merely a boolean

## Agent infrastructure boundary

The article distinguishes Stop Authority from ordinary agent-runtime interrupt, human-in-the-loop, or execution-control mechanisms. Implementation interrupts are insufficient unless they show whose judgment the process returns to, what log remains, and what repair path follows.

Current repository alignment:

- supports Phase 3 reference-implementation boundary
- supports not turning the repository into an agent framework
- supports keeping examples small and structural

Repository change decision:

- no runtime implementation change
- agent-framework references should remain illustrative and non-production

## Human oversight / guardrails boundary

The article notes that guardrails, tripwires, and human oversight can stop inputs, outputs, or tool calls, but technical stopping and responsibility-pathway stopping are not the same.

Current repository alignment:

- strongly aligned with non-certifying guardrail boundary
- supports treating guardrails as necessary components, not final responsibility resolution
- supports evidence and return requirements after a guardrail stop

Repository change decision:

- no compliance or safety claim should be added
- future guardrail examples must show return point, stop log, and repair owner if claiming responsibility-pathway coverage

## Execution / approval / stop / repair authority separation

The article separates:

- Execution Authority
- Approval Authority
- Stop Authority
- Repair Authority

It warns that if the actor who wants to execute is also the only actor who can stop, stopping will be delayed by operational pressure.

Current repository alignment:

- strongly aligned with Decision Owner / Approval Gate / Execution Actor / Stop Authority / Repair Owner separation
- supports future examples where execution and stopping authority are deliberately distinct
- supports not treating approval as proof that stopping was unnecessary

Repository change decision:

- no immediate schema change required
- high-value source for future examples and negative fixtures

## Stop conditions alignment

The article lists stop conditions such as undefined approver, unclear execution target, unevaluated impact scope, external sending, irreversible operation, permission changes, personal/contract/invoice/hiring data, suspected input contamination, inability to show evidence, inability to preserve Evidence Log, major external oversight findings, policy-update risk shifts, missing Human Return Point, undefined Repair Owner, unexpected tool calls, and conflict between user instruction and organizational policy.

Current repository alignment:

- strongly supports Action Class Matrix and risk-level boundaries
- supports missing-Human-Return-Point and missing-Repair-Owner as stop conditions
- supports treating absence of Evidence Log as a stop or hold condition
- supports external oversight only as bounded context

Repository change decision:

- no immediate checker change
- possible future checker rule: high-impact or external-action examples must declare stop conditions and stop authority

## Action Class Matrix alignment

The article connects Stop Authority to Action Class Matrix. Observe-only, suggest-only, approval-required, reversible external action, irreversible/high-impact action, and emergency-stop classes require different stop strengths.

Current repository alignment:

- strongly aligned with action-class direction
- supports adding future examples one action class at a time
- supports heavily bounded irreversible or high-impact examples

Repository change decision:

- no immediate example addition
- future examples should define action class before defining stop conditions

## Emergency Stop alignment

The article treats Emergency Stop as a designed safe pathway, not ad-hoc exception handling. Emergency Stop can include tool-call stop, external-send stop, session isolation, permission downgrade, Safe-Only Mode, Stop-and-Await Mode, human review return, execution-queue pause, impact-scope freeze, and Evidence Log preservation.

Current repository alignment:

- supports future emergency-stop examples
- supports lifecycle-state vocabulary around suspension and return
- supports preserving evidence during stop rather than continuing execution silently

Repository change decision:

- no immediate schema change
- possible future bounded artifact: `examples/stop-and-await-minimal.yaml`

## Stop-and-Await Mode alignment

The article defines Stop-and-Await Mode as a state where AI detects danger or uncertainty and does not proceed, instead waiting for human judgment. AI may still explain what is uncertain, what should be checked, what choices exist, and what logs are needed, but it must not execute, send, update, delete, or call external APIs.

Current repository alignment:

- strongly aligned with AI support-node boundary
- strongly aligned with Phase 3 first example
- supports modeling AI assistance without execution authority
- supports future examples where AI can explain but not act while stopped

Repository change decision:

- no immediate schema change
- high-value source for a future bounded example after current source alignment stabilizes

## Responsibility after stop

The article states that stopping is not the endpoint. After stopping, someone must pick up, check, repair, and decide whether to restart. Stop Authority becomes a responsibility pathway only when connected to Repair Owner and return destinations.

Current repository alignment:

- strongly aligned with Repair Owner
- strongly aligned with Human Return Point
- supports repair and restart examples
- supports the user's note that Repair Owner may require cross-article treatment rather than standalone article treatment

Repository change decision:

- no immediate Repair Owner note yet
- after this Stop Authority review, a cross-article Repair Owner note becomes more justified

## Stop levels alignment

The article distinguishes stop levels:

- Level 1: Pause
- Level 2: Require Approval
- Level 3: Tool Freeze
- Level 4: Permission Downgrade
- Level 5: Emergency Stop

Current repository alignment:

- useful for future lifecycle-state and action-class examples
- should not be treated as a completed normative standard
- supports bounded example design

Repository change decision:

- no immediate schema change
- possible future concept note before encoding stop levels in examples

## Non-punitive stop culture

The article says Stop Authority does not work if people who stop are blamed. It requires organizational support: stopping under defined conditions is correct, people exercising Stop Authority are not disadvantaged, stop reasons are logged, post-stop reviewers and restart decision-makers are defined, and false stops are treated as improvement material.

Current repository alignment:

- supports organizational responsibility context
- supports not reducing Stop Authority to a UI button
- supports repair and learning boundaries

Repository change decision:

- no organizational-policy claim should be added to schemas
- keep as source context for future guidance

## Stop Log alignment

The article states that Stop Authority must connect to Evidence Log, especially Stop Log. Stop Log records when stopping occurred, what was stopped, who stopped it, which condition applied, whether AI suggested stopping, whether a human stopped it, whether automatic stop occurred, why stopping failed if it failed, where the process returned after stopping, and who made the restart decision.

Current repository alignment:

- strongly aligned with Evidence Log source alignment
- supports stop-record examples
- supports recording failed or unused stop opportunities

Repository change decision:

- no immediate schema change
- high-value source for future Stop Log fixture or example

## Bad stop design patterns

The article lists bad stop designs such as stopping only on errors, only executors being able to stop, approvers lacking stop authority, stop conditions existing only in policy documents, no return point after stop, missing Stop Log, punishing the stopper, missing repair owner after stop, and AI continuing to argue that execution should continue.

Current repository alignment:

- useful for future negative fixtures
- supports checker-boundary examples
- supports non-production guidance for stop weaknesses

Repository change decision:

- no immediate negative fixture required
- preserve as future test inspiration

## External-context boundary

The article references EU AI Act Article 14, NIST AI RMF, NIST AI 600-1, LangGraph, Model Context Protocol, and guardrail/tripwire concepts as background.

Current repository alignment:

- useful context for implementation and governance discussion
- must not become legal, compliance, safety, standards, or production certification

Repository change decision:

- no compliance or safety claim should be added
- keep external references contextual

## Claim-strength assessment

Compatible claims:

- Stop Authority is necessary for AI-agent actions that become operational effects
- technical stop and responsibility-pathway stop are different
- execution authority and stop authority should be separated in meaningful examples
- stop conditions should include missing approver, missing Human Return Point, missing Repair Owner, and missing Evidence Log
- action class affects stop strength
- stopping must connect to human return, repair, restart decision, and Stop Log
- Stop-and-Await Mode can allow explanation while forbidding execution

Claims to keep bounded:

- stop-level taxonomy as normative standard
- organizational policy prescriptions
- guardrail or tripwire certification
- legal human-oversight interpretation
- production safety approval

Repository interpretation:

Stop Authority is core source-aligned vocabulary. It should remain connected to Human Return Point, Evidence Log, Repair Owner, and Action Class Matrix rather than becoming a standalone stop button concept.

## Repository alignment decision

Status: aligned.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> A Stop Authority claim should show who can stop, under what condition, what level of stop applies, where the stopped process returns, what Stop Log is preserved, who can decide restart, and who owns repair after stop.

## Next action

Proceed to the next inventory target:

- `articles/enterprise-agent-checklist.md`

Before adding a larger Phase 3 reference example, consider whether a small `Stop-and-Await` or `Evidence Log` example should be created first.
