# Source Alignment: 1982703147789e.md

This note records a source-alignment review for a legacy/hash-named Zenn article on HITL collapse and responsibility-visibility design.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/1982703147789e.md`
- Title: `HITL崩壊を前提にした責任経路設計――AIエージェント運用で最後に残る問題`
- Published flag in frontmatter: `true`
- Published at: `2026-04-10 19:28`
- Review status: reviewed
- Review purpose: align a source article on HITL degradation, responsibility visibility, stop/return/repair traceability, and improvement-oriented evidence.

## Article-level role

The article argues that Human-in-the-loop is important but does not maintain itself in production-like operation. Therefore responsibility-pathway design must assume that HITL can degrade and must preserve responsibility visibility even after degradation.

Current repository alignment:

- strongly aligned with Human Return Point and RACI/HITL/Guardrails comparison notes
- strongly aligned with Evidence Log and Stop Authority source notes
- supports negative fixtures where human review exists formally but collapses operationally

Repository change decision:

- no immediate schema change required
- high-value source for future HITL-collapse and responsibility-visibility examples

## HITL importance and limitation

The article states that HITL remains important for high-risk handling, final human approval, pre-automation review, exception absorption, explainability, and risk acceptance. However, the article also states that merely introducing HITL does not preserve it.

Current repository alignment:

- supports non-rejection of HITL
- supports treating HITL as necessary but insufficient
- supports distinguishing human review presence from responsibility-pathway sufficiency

Repository change decision:

- no anti-HITL claim should be added
- future docs should say HITL is useful but needs pathway support

## HITL collapse patterns

The article lists several HITL degradation patterns:

- formal approval
- rubber-stamping AI recommendations
- volume pressure
- emergency skip
- responsibility dilution

Current repository alignment:

- directly aligned with prior RACI/HITL/Guardrails comparison review
- supports negative fixtures for formal approval, rubber-stamping, and skipped review
- supports action-class-sensitive review depth rather than universal manual review

Repository change decision:

- no immediate checker change
- useful source for future scenario tests around approval quality

## Problem is not whether a human existed

The article states that the real question is not whether a human existed, whether an approval column existed, or whether HITL was defined in policy. The real question is where responsibility flow is cut when HITL collapses, where it can be picked up, and where it can return.

Current repository alignment:

- strongly aligned with Human Return Point and responsibility-flow framing
- supports distinguishing human-in-loop from human-returnable
- supports Evidence Log fields for actual review state, not only nominal approval

Repository change decision:

- no immediate schema change
- future checkers may distinguish planned review from actual performed review

## Responsibility visibility definition

The article defines responsibility-visibility design as design that prevents responsibility flow from becoming invisible in AI operation.

It says at least the following should be visible:

- where judgment arose
- which responsibility unit accepted it
- who adopted the AI recommendation
- where human confirmation was supposed to occur
- whether confirmation actually occurred
- where stopping was possible
- who catches the responsibility if it was not stopped
- where responsibility returns after failure

Current repository alignment:

- strongly aligned with Evidence Log and traceability
- supports differentiating planned approval, actual approval, skipped approval, and failure return
- supports future fields for adoption, review performance, stop possibility, and return target

Repository change decision:

- no immediate schema change
- high-value source for future Evidence Log / approval-state extension

## Responsibility visibility vs HITL

The article distinguishes:

- HITL: inserting humans, creating confirmation points, reducing runaway automation
- responsibility visibility: making visible whether intervention actually occurred, preserving responsibility flow when intervention collapses, and tracing stop/return/repair responsibility pathways

Current repository alignment:

- strongly aligned with HRP and Evidence Log distinction
- supports saying that human confirmation is not the same as responsibility visibility
- supports catch/finally analogy for collapsed review

Repository change decision:

- no immediate definition change required
- useful future teaching distinction

## Visibility points alignment

The article identifies five visibility points:

- judgment occurrence point
- adoption confirmation point
- intervention execution point
- stop activation point
- repair connection point

Current repository alignment:

- maps to Decision Owner, Approval Gate, Human Return Point, Stop Authority, Repair Owner, and Evidence Log
- supports a compact diagnostic model for examples
- supports tracing where a responsibility path broke

Repository change decision:

- no core element reduction
- possible future checklist or diagnostic view

## Example alignment: internal approval support

The article uses an internal approval-support scenario: AI classifies an application, AI recommends approval/denial, a staff member checks and approves, API execution follows, and issues trigger stop or rollback.

It shows how apparent HITL can degrade through AI-recommendation-only approval, no-look approval, emergency execution without confirmation, and unclear stop responsibility.

Current repository alignment:

- strongly aligned with Phase 3 human-AI review workflow
- supports future negative examples for rubber-stamp approval and missing stop authority
- supports not claiming safety merely from the presence of an approver

Repository change decision:

- no immediate example addition
- useful source for future negative fixture

## Post-incident failures without visibility

The article states that if responsibility flow is not visible, post-incident analysis can fail:

- only the formal responsible person remains
- operational staff absorb responsibility for design defects
- AI recommendation influence disappears from discussion
- permanent countermeasures are misdirected toward training or warnings instead of stop/delegation design flaws

Current repository alignment:

- strongly aligned with source notes about repair, explanation, and organizational rebundling
- supports distinguishing design defect from operator blame
- supports improvement-oriented Evidence Log rather than punishment-oriented logging

Repository change decision:

- no blame-oriented claim should be added
- future docs may emphasize improvement and reconstruction over punishment

## Minimum implementation / operation items

The article says responsibility-visibility design need not begin with heavy governance documents. It can start by logging:

- AI recommendation content
- recommendation adopter
- whether human confirmation occurred
- confirmation skip reason
- execution instruction giver
- stop instruction giver
- rollback decision maker
- restart approver

It also says design should decide where responsibility moves, where it returns to humans, where it stops, who catches it if it does not stop, and where repair responsibility connects.

Current repository alignment:

- strongly aligned with Evidence Log and Approval Log needs
- supports minimal operational checklist design
- supports future structured log fields

Repository change decision:

- no immediate schema change
- possible future example fields: recommendation_adopter, confirmation_performed, confirmation_skip_reason, rollback_decider, restart_approver

## Improvement-oriented boundary

The article explicitly says responsibility-visibility design is not for making punishment easier. Its purpose is to find responsibility breakpoints, un-stoppable points, undelegatable points, unrepairable points, and the next design target.

Current repository alignment:

- strongly aligned with non-punitive stop and repair culture
- supports source-alignment self-application boundary
- supports using Evidence Log for learning and improvement, not blame assignment alone

Repository change decision:

- no punitive framing should be added
- future docs should preserve improvement-oriented purpose

## Explanation vs repair direction

The article points toward future separation of explanation responsibility and repair responsibility.

Current repository alignment:

- strongly aligned with the MHC/accountability/oversight article's repair-and-return emphasis
- supports future distinction between explaining an incident and repairing harm or process defects

Repository change decision:

- no immediate schema addition
- likely worth revisiting after final legacy article review

## Try-catch analogy alignment

The article strongly reinforces the Try-catch/finally analogy:

- HITL can degrade inside the normal try path
- catch-like responsibility begins where collapsed approval, skipped review, failed stop, or abnormal execution is detected
- finally-like closure includes Evidence Log, rollback decision, restart approval, repair responsibility, and permanent-countermeasure connection

Current repository alignment:

- strongly aligned with prior RPL / ACM / RACI-HITL / harness / MHC notes
- supports future developer-facing explanation
- should remain analogy, not formal semantics

Repository change decision:

- no immediate formalization
- possible future explanatory doc after source alignment completes

## Claim-strength assessment

Compatible claims:

- HITL is important but does not maintain itself automatically
- HITL can degrade through formal approval, rubber-stamping, volume pressure, emergency skip, and responsibility dilution
- responsibility visibility is different from inserting humans into the loop
- planned human confirmation and actual performed confirmation should be distinguished
- visibility should include AI recommendation, adopter, actual confirmation, skip reason, stop possibility, stop actor, rollback decider, restart approver, and repair connection
- responsibility visibility supports improvement, not punishment
- lack of visibility can misdirect post-incident learning

Claims to keep bounded:

- HITL is useless
- responsibility visibility as legal proof
- audit/compliance/safety/production readiness
- punitive accountability framing
- immediate schema or checker formalization

Repository interpretation:

This hash-named article is important operational source material for HITL degradation and responsibility visibility. It supports future negative examples and possible Evidence Log extensions, but does not require immediate schema changes.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-guidance rule:

> RPE documentation should not treat the presence of a human approval step as sufficient. It should distinguish planned human review, actual review, degraded review, skipped review, stop possibility, rollback decision, restart approval, and repair connection.

## Next action

Proceed to the final hash / legacy filename candidate:

- `articles/3235e5affbb7c9.md`
