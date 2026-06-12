# Source Alignment: fixed-responsibility-to-pathway.md

This note records the fifth source-alignment review for prior public Zenn writing.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/fixed-responsibility-to-pathway.md`
- Title: `責任固定から責任経路設計へ――AIガバナンスに必要な「固定後」の設計`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the responsibility-fixation boundary and post-fixation design argument with the current bounded repository specification.

## Article-level role

The article argues that responsibility fixation is necessary but insufficient. It treats fixation as an important snapshot or cross-section within a broader responsibility pathway rather than the end state of responsible AI.

Current repository alignment:

- strongly aligned with the repository's lifecycle examples
- strongly aligned with repair, suspension, returning, closure, and reopening boundaries
- strongly aligned with review-result outputs that preserve checked, not-checked, and not-claimed items
- strongly aligned with the rule that evidence and green checks do not complete responsibility

Repository change decision:

- no immediate schema change required
- high-value source for future premise-record, evidence-record, and repair-record examples

## Responsibility fixation definition

The article defines a responsibility-fixation approach as a design that predefines stop subjects, stop points, pass conditions, responsibility boundaries, approval boundaries, and evidence logs in a third-party-verifiable and hard-to-retrofit form, in order to prevent responsibility evaporation or gaps.

Current repository alignment:

- compatible with Stop Authority
- compatible with Approval Gate
- compatible with Evidence Log
- compatible with responsibility-boundary flags
- compatible with checker expectations that structural fields are visible

Repository change decision:

- no immediate new concept file required
- possible future glossary note: `responsibility fixation is a necessary cross-section inside a responsibility pathway, not the whole pathway`

## Fixed responsibility is not completion

The article states that responsibility fixation is necessary, but not the entire responsibility design. Fixed responsibility must be connected to premise, passage, stop, return, repair, and reevaluation.

Current repository alignment:

- supports lifecycle modeling beyond a single fixed state
- supports Phase 2 invariant candidates about suspension, returning, repair, and closure
- supports Phase 3 example boundaries that prevent treating approval or logging as final resolution

Repository change decision:

- no immediate example expansion required
- future examples should show what happens after approval, execution, stop, or failure

## Premise Pathway alignment

The article introduces `前提経路 / Premise Pathway` as a pathway for handling where a premise came from, who adopted it, under what conditions it was treated as valid, and where it returns if it collapses.

Current repository alignment:

- strongly aligned with Lean assumption-scope notes
- strongly aligned with the idea that future legal, institutional, national, international, or user/provider-agreement layers must be explicit if modeled
- supports future premise-record or assumption-record examples

Repository change decision:

- do not add premise pathway to schemas yet
- possible future bounded artifact after source alignment stabilizes: `docs/premise-pathway-boundary.md`
- possible future minimal example: `examples/premise-review-flow.yaml`

## Responsibility weight changes

The article argues that responsibility is not zero-or-one and may redistribute after later facts become visible. It gives a scenario where AI-generated sales mail, old internal documents, time pressure, UI design, permissions, review process, and repair response can all affect responsibility weight.

Current repository alignment:

- supports future examples involving post-fact review
- supports review-result boundaries that preserve not-checked items
- supports avoiding one-shot blame assignment

Repository change decision:

- do not model responsibility weights formally yet
- keep as source context for future review and repair examples

## Post-fixation design requirements

The article lists post-fixation design needs:

- reevaluation of fixed conditions
- premise pathway recording and reevaluation
- later-fact intake
- separation between formal approval and substantial approval
- organizational pressure and UI pressure records
- repair responsibility after stopping
- reinterpretation of evidence
- redistribution of responsibility weight
- return to Human Return Point
- connection to Repair Owner

Current repository alignment:

- strongly aligned with Human Return Point
- strongly aligned with Repair Owner
- strongly aligned with Evidence Log
- strongly aligned with Stop Authority
- strongly aligned with lifecycle-state examples

Repository change decision:

- high-value source for future evidence-record flow or repair-record flow
- no immediate schema addition before more alignment notes are reviewed

## Evidence Log alignment

The article states that Evidence Log must support reconstruction of the responsibility pathway, not merely record events. It asks who requested, what context was passed to AI, what AI proposed, what the approver saw, under what conditions execution occurred, where stopping was possible, why it was not stopped, and who repaired after failure.

Current repository alignment:

- directly supports the repository's Evidence Log concept
- supports review-result and checker boundary language
- supports the first Phase 3 example's evidence categories

Repository change decision:

- no immediate change required
- use this article as source support if future Evidence Log docs are expanded

## Stop Authority alignment

The article states that responsibility fixation only becomes operationally meaningful when connected to Stop Authority. It emphasizes that stop authority must include who can stop, under what conditions, and who picks up the process after stopping.

Current repository alignment:

- directly supports Stop Authority model
- supports separation between execution authority and stop authority
- supports future examples involving suspension or return after stop

Repository change decision:

- no immediate change required
- high-value source for future Stop Authority examples

## Concept hierarchy boundary

The article says Responsibility Pathway Engineering is not a subordinate concept under responsibility-fixation approaches. Instead, RPE is a broader framework that includes responsibility fixation as one important cross-section.

Current repository alignment:

- supports keeping RPE as pathway-wide structure rather than a single fixed-control method
- supports BEACON and ROADMAP language that avoids treating any one control as the full answer

Repository change decision:

- no immediate README change required
- possible future note in glossary or concept mapping

## External-context boundary

The article references standards and external sources such as ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF, EU AI Act Article 14, and OpenAI social responsibility principles as background context.

Current repository alignment:

- useful context for enterprise and standards-adjacent discussions
- must not become legal, compliance, safety, or standards certification inside the repository

Repository change decision:

- no compliance or standards claim should be added
- treat external references as context only unless a dedicated source-mapping note is later created

## Claim-strength assessment

Compatible claims:

- responsibility fixation is necessary but not sufficient
- fixed responsibility is a snapshot, not permanent closure
- post-fixation reevaluation matters
- premise collapse must be returnable
- responsibility may redistribute after later facts
- Human Return Point and Repair Owner are needed after fixation, stop, or failure
- Evidence Log must reconstruct responsibility pathway context, not only events

Claims to keep bounded:

- responsibility-weight redistribution as a formal model
- premise pathway as a new schema object
- standards alignment
- OpenAI social-responsibility principle interpretation
- organizational adoption claims

Repository interpretation:

The article strongly supports a core RPE rule: fixing responsibility is not the same as resolving responsibility.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> When an example includes a fixed responsibility boundary, it should also show how that boundary can be reevaluated, returned to a human or institution, connected to repair, and bounded by evidence.

## Next action

Proceed to the next inventory target:

- `articles/ai-responsibility-node.md`

Keep review incremental. Do not add premise-pathway schema or responsibility-weight formalization before more source-alignment notes are reviewed.
