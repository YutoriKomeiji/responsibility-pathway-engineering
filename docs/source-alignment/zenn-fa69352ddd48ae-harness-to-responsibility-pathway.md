# Source Alignment: fa69352ddd48ae.md

This note records a source-alignment review for a legacy/hash-named Zenn article positioning Responsibility Pathway Design after Harness Engineering.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/fa69352ddd48ae.md`
- Title: `ハーネスエンジニアリングの次に必要な設計対象――責任経路設計とは何か`
- Published flag in frontmatter: `true`
- Published at: `2026-04-09 19:15`
- Review status: reviewed
- Review purpose: align a positioning article that separates Harness Engineering from Responsibility Pathway Design.

## Article-level role

The article positions Responsibility Pathway Design as the next design object after Harness Engineering. Harness Engineering stabilizes AI execution, while Responsibility Pathway Design handles where responsibility flows, stops, returns to humans, and shifts into repair responsibility.

Current repository alignment:

- strongly aligned with reference-implementation boundary
- strongly aligned with non-runtime / non-agent-framework positioning
- strongly aligned with the repository's responsibility-flow framing
- supports explaining why RPE is needed even if agent harnesses work correctly

Repository change decision:

- no immediate schema change required
- high-value source for positioning documentation above agent runtime / harness layers

## Harness Engineering boundary

The article says Harness Engineering is important and handles prompts, context retention, external tool calls, validation order, retry on failure, external state retention, and runtime control. In short, it stabilizes execution.

However, the article states that what is stabilized is execution, not responsibility flow.

Current repository alignment:

- strongly aligned with the repository boundary that RPE is not an agent runtime
- supports positioning RPE above harness/runtime/tool layers
- supports avoiding implementation claims about stable execution

Repository change decision:

- no runtime implementation claim should be added
- possible future positioning doc may reuse this harness/RPE distinction

## Accident despite correct execution

The article says accidents can happen even when AI operates correctly. The issue may be that it was not designed whose responsibility the judgment flowed through, where it could stop, where it returned to humans, and where repair responsibility began.

Current repository alignment:

- strongly aligned with RPL and RACI/HITL/Guardrails comparison source notes
- supports the idea that model correctness and runtime stability are not responsibility-pathway sufficiency
- supports Phase 3 examples that demonstrate responsibility flow rather than model capability

Repository change decision:

- no immediate example addition
- useful motivation source for future README / docs positioning

## Responsibility flow vs responsibility location

The article states that what is needed is not merely a list of responsible people. It is not only responsibility location, but responsibility flow.

It further states that AI-era incidents often occur not because responsibility did not exist, but because responsibility flow was cut off midway.

Current repository alignment:

- strongly aligned with the repository's responsibility-as-pathway concept
- supports fixed-responsibility-to-pathway source alignment
- supports avoiding a single final-accountability-only model

Repository change decision:

- no immediate definition change required
- useful source for explaining why fixed responsibility alone is insufficient

## Responsibility Pathway Design definition

The article defines Responsibility Pathway Design as pre-designing, for AI-involved judgments:

- the order in which responsibility flows
- where it returns to humans
- where it can stop
- where repair responsibility begins
- where organizational responsibility starts

It emphasizes that the target is not fixed responsibility, but movement, fragmentation, rebinding, stopping, and return of responsibility.

Current repository alignment:

- directly aligned with core Responsibility Pathway definition
- strongly aligned with Human Return Point, Stop Authority, Repair Owner, and organizational responsibility concepts
- supports Try-catch/finally analogy as explanation of normal flow, stop/return, and repair closure

Repository change decision:

- no immediate definition change required
- high-value source for concise responsibility-pathway positioning

## Guardrails boundary

The article says Guardrails are necessary, but they mainly handle boundary control: suppressing prohibited output, restricting dangerous actions, and narrowing allowed behavior.

Responsibility Pathway Design handles what comes after: who takes over judgment, where Stop Authority fires, who catches the issue if it did not stop, and where responsibility returns after recovery.

Current repository alignment:

- strongly aligned with Stop Authority and RACI/HITL/Guardrails comparison notes
- supports treating guardrails as necessary but insufficient
- supports post-stop responsibility flow design

Repository change decision:

- no guardrail certification claim should be added
- future guardrail examples should include post-stop responsibility flow

## HITL boundary

The article says HITL can collapse through formal approval, rubber-stamping AI recommendations, review overload, or normalized skipping of human confirmation during emergencies.

It states that the issue is not whether a human existed, but whether responsibility flow remains visible and whether stop/repair pathways remain after HITL collapses.

Current repository alignment:

- strongly aligned with Human Return Point source note
- supports the distinction between human-in-the-loop and human-returnable
- supports negative fixtures for formal approval or rubber-stamp HITL

Repository change decision:

- no immediate checker change
- useful source for future approval/HITL degradation examples

## Design points alignment

The article identifies design points where Responsibility Pathway Design should be embedded:

- judgment point
- delegation point
- stop point
- return point
- repair point

Current repository alignment:

- maps to Decision Owner, Approval Gate, Execution Actor, Stop Authority, Human Return Point, and Repair Owner
- supports a simplified teaching model before the full seven-element minimal set
- supports the Try-catch analogy: normal judgment/delegation, stop/return, and repair closure

Repository change decision:

- do not reduce the core element set
- possible future teaching section can use the five-point model

## Harness vs Responsibility Pathway scenario

The article uses an AI-assisted application-processing scenario: AI classifies an application, AI recommends approval candidates, a human approves, an external system executes, and failure triggers rollback.

Harness Engineering handles which information is passed to AI, which tools are called, and in what order validation occurs. Responsibility Pathway Design handles who accepts responsibility when the AI recommendation is adopted, who catches formalized human approval, who has Stop Authority after execution failure, who decides rollback, and where re-execution responsibility returns.

Current repository alignment:

- strongly aligned with Phase 3 workflow examples
- supports separating runtime control from responsibility-flow control
- supports incident/rollback/re-execution responsibility questions

Repository change decision:

- no immediate example addition
- possible future comparative scenario after legacy review completes

## Relationship to neighboring concepts

The article compares:

- Prompt / Context Engineering: instructions and context; how to make AI think
- Harness Engineering: execution environment and control; how to run stably
- Guardrails: boundary control; what not to allow
- HITL: human intervention; where humans check
- RACI: role assignment; who has responsibility
- Responsibility Pathway Design: responsibility flow; where responsibility passes, stops, and returns

It says Responsibility Pathway Design is not a replacement for these concepts, but a higher-level perspective for governing responsibility flow above them.

Current repository alignment:

- strongly aligned with non-replacement posture
- supports positioning RPE above prompt/context/harness/guardrail/HITL/RACI layers
- supports source-backed explanation for nearby-concept boundaries

Repository change decision:

- no replacement claim should be added
- useful future source for `docs/terminology-and-nearby-concepts.md`-style documentation

## Minimal design principle alignment

The article says a minimal version of Responsibility Pathway Design should answer:

- where the judgment arises
- which responsibility unit accepts it
- where it can stop
- where it can return to humans
- who takes repair responsibility on failure
- whether the flow can be reconstructed afterward

Current repository alignment:

- maps directly to Decision Owner, Stop Authority, Human Return Point, Repair Owner, and Evidence Log
- supports a minimal question set for examples and checklists
- supports reconstructability as a core Evidence Log purpose

Repository change decision:

- no immediate schema change
- useful source for future minimal-checklist phrasing

## Try-catch analogy alignment

The article strengthens the Try-catch/finally analogy:

- Harness Engineering stabilizes execution inside the try path
- Responsibility Pathway Design asks how the path stops, catches responsibility, returns to humans, rolls back, repairs, and reconstructs evidence after the try path fails or succeeds with later defects
- The finally-like part appears in reconstruction, repair, rollback, and post-incident responsibility rebundling

Current repository alignment:

- strengthens prior RPL / ACM / RACI-HITL-Guardrails try-catch notes
- should remain explanatory and non-formal unless formal semantics are defined later

Repository change decision:

- no immediate formalization
- possible future developer-facing explanation after all source review is complete

## Claim-strength assessment

Compatible claims:

- Harness Engineering stabilizes execution, not responsibility flow
- accidents can occur despite correct AI execution if responsibility flow is not designed
- Responsibility Pathway Design handles flow rather than fixed responsibility location
- Guardrails and HITL remain necessary but insufficient
- Responsibility Pathway Design can be positioned above Prompt / Context Engineering, Harness Engineering, Guardrails, HITL, and RACI
- minimal pathway design should answer judgment, responsibility unit, stop, human return, repair, and reconstructability questions

Claims to keep bounded:

- RPE replacing Harness Engineering, Prompt Engineering, Context Engineering, Guardrails, HITL, or RACI
- formal runtime semantics
- production readiness
- legal / compliance / safety / audit certification
- universal applicability without action-class and context sensitivity

Repository interpretation:

This hash-named article is important early positioning source material. It explains why the repository should remain above harness/runtime layers while still being implementation-oriented at the responsibility-flow level.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-guidance rule:

> RPE documentation should distinguish execution-stability design from responsibility-flow design: a correct or stable AI/harness execution does not by itself establish where responsibility stops, returns, is repaired, or can be reconstructed.

## Next action

Proceed to the next hash / legacy filename candidate:

- `articles/ef12f2db314a58.md`
