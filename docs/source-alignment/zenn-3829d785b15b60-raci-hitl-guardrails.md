# Source Alignment: 3829d785b15b60.md

This note records a source-alignment review for a legacy/hash-named Zenn article comparing RACI, HITL, Guardrails, and Responsibility Pathway Design.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/3829d785b15b60.md`
- Title: `RACI / HITL / Guardrails / 責任経路設計 の違い`
- Published flag in frontmatter: `true`
- Published at: `2026-04-09 20:25`
- Review status: reviewed
- Review purpose: align a comparison article with the repository's neighboring-concept boundary, responsibility-flow framing, and non-replacement posture.

## Article-level role

The article distinguishes RACI, Human-in-the-loop, Guardrails, and Responsibility Pathway Design by the design object each primarily handles.

Current repository alignment:

- strongly aligned with prior RPL / Action Class Matrix source notes
- strongly aligned with the repository's non-rejection boundary toward neighboring concepts
- supports explaining why RPE is needed after role assignment, human review, and guardrail design

Repository change decision:

- no immediate schema change required
- high-value source for comparison / positioning documentation

## Core comparison alignment

The article summarizes:

- RACI handles responsibility placement / role assignment
- HITL handles human intervention points
- Guardrails handle behavioral boundaries
- Responsibility Pathway Design handles responsibility flow

Current repository alignment:

- directly aligned with current positioning of RPE
- supports explaining RPE as flow design rather than a replacement for RACI/HITL/Guardrails
- supports bounded use of neighboring concepts as components

Repository change decision:

- no replacement claim should be added
- future docs can reuse this comparison as source-backed framing

## RACI boundary

The article says RACI is useful for role assignment but weak for dynamic responsibility movement in AI-agent operations. AI recommends, humans approve, systems execute, operations recover, and management explains afterward. Responsibility does not stay in one place.

Current repository alignment:

- strongly aligned with Decision Owner / Approval Gate / Execution Actor separation
- supports treating RACI as useful but insufficient for responsibility flow
- supports not collapsing a pathway into a single final accountable role

Repository change decision:

- no RACI replacement claim should be made
- future role-mapping guidance may reference RACI as a neighboring component

## HITL boundary

The article says HITL is important but can degrade: approvals become formalized, AI recommendations become rubber-stamped, volume makes review hollow, or emergency situations skip human review.

It says the real question is whether responsibility flow, stop, return, and repair pathways remain even after human review collapses.

Current repository alignment:

- strongly aligned with Human Return Point source note
- supports distinction between human-in-the-loop and human-returnable
- supports the Try-catch analogy: HITL can be part of try, but catch/return/repair must remain if HITL degrades

Repository change decision:

- no immediate checker change
- useful source for future negative fixtures about formal approval / rubber-stamp HITL

## Guardrails boundary

The article says Guardrails are important behavioral boundary controls, but they do not automatically design post-stop responsibility transfer, pending responsibility after stop, rollback decision authority, or post-incident explanation paths.

Current repository alignment:

- strongly aligned with Stop Authority and Evidence Log source notes
- supports treating guardrails as boundary controls, not responsibility-pathway completion
- supports requiring post-stop return and repair design

Repository change decision:

- no guardrail certification claim should be added
- future guardrail examples should include return, evidence, and repair responsibilities

## Responsibility Pathway Design definition

The article says Responsibility Pathway Design handles where judgment arises, which responsibility unit accepts it, where it is delegated, where it can stop, where it returns to humans, where it shifts into repair responsibility, and where it is re-bundled into organizational responsibility.

It explicitly says this is not merely deciding the final responsible person, but pre-designing how responsibility passes through judgment, delegation, approval, execution, stop, return, and repair.

Current repository alignment:

- directly aligned with Responsibility Pathway definition
- strongly aligned with core RPE element set
- supports flow-based framing across multiple prior source notes

Repository change decision:

- no immediate definition change required
- high-value source for a concise comparison section

## Same-case comparison alignment

The article compares the four concepts in an internal-application workflow:

- AI classifies an application
- AI recommends approval candidates
- human approves
- API executes
- failure triggers stop or rollback

In this case, RACI identifies responsible roles, HITL identifies human-review points, Guardrails block risky auto-execution, and Responsibility Pathway Design asks how responsibility moves when AI recommendation is adopted, what happens if approval is formalized, who has stop authority after API execution, who decides rollback, where responsibility returns on re-execution, and which unit owns explanation.

Current repository alignment:

- strongly aligned with Action Class Matrix and Phase 3 examples
- supports examples that show multiple concepts together rather than choosing only one
- supports incident/restart/rollback responsibility questions

Repository change decision:

- no immediate example addition
- possible future comparative scenario after more source alignment

## Why AI makes this stronger

The article identifies four reasons AI agents strengthen the problem:

- recommendations mix invisibly into judgment
- execution actors are distributed across layers and roles
- stop and return are often treated as operational effort rather than design
- responsibility is hard to recover after incidents

Current repository alignment:

- strongly aligned with AI support-node boundary
- supports RPL and ACM as necessary design layers
- supports explicit stop/return/repair rather than post-hoc operational recovery

Repository change decision:

- no immediate schema change
- useful source for motivation text

## Minimum design points alignment

The article suggests five practical points for Responsibility Pathway Design:

- judgment point
- delegation point
- stop point
- return point
- repair point

Current repository alignment:

- maps cleanly to Decision Owner / Approval Gate / Execution Actor / Stop Authority / Human Return Point / Repair Owner
- supports reduced teaching model before seven-element minimal set
- supports Try-catch framing: normal judgment/delegation, stop/return, repair closure

Repository change decision:

- no core element reduction required
- useful explanatory simplification for future docs

## Try-catch analogy alignment

The article gives strong support to the user's Try-catch observation:

- RACI and HITL are insufficient when normal review/execution degrades
- Guardrails can stop, but post-stop responsibility flow is separate
- Responsibility Pathway Design preserves stop, return, rollback, repair, and explanation paths

Current repository alignment:

- strengthens the try/catch/finally analogy from RPL and ACM reviews
- catch is not just stopping; it includes who catches the failed or stopped responsibility
- finally-like closure appears in repair, rollback, explanation, and organizational rebundling

Repository change decision:

- no formal semantics yet
- useful source for future developer-facing explanation

## Claim-strength assessment

Compatible claims:

- RACI, HITL, and Guardrails are necessary but insufficient by themselves
- RACI assigns roles but does not fully model dynamic responsibility movement
- HITL can collapse into formal approval or rubber-stamping
- Guardrails stop behavior but do not define post-stop responsibility flow
- Responsibility Pathway Design handles responsibility flow across judgment, delegation, approval, execution, stop, return, repair, and organizational rebundling
- AI agents strengthen responsibility-pathway needs because recommendation, execution, stop, and recovery spread across layers

Claims to keep bounded:

- RPE replacing RACI, HITL, or Guardrails
- proof of safety, compliance, or production readiness
- formal runtime semantics
- universal applicability without action-class/context sensitivity
- legal conclusion about responsibility assignment

Repository interpretation:

This hash-named article is important comparison source material. It should be treated as a primary explanation of how RPE differs from and composes with RACI, HITL, and Guardrails.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-guidance rule:

> RPE documentation should present RACI, HITL, and Guardrails as useful neighboring mechanisms, while explaining that Responsibility Pathway Design covers the flow through judgment, delegation, approval, execution, stop, return, repair, and organizational rebundling.

## Next action

Proceed to the next hash / legacy filename candidate:

- `articles/fa69352ddd48ae.md`
