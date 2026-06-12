# Source Alignment: human-return-point.md

This note records a source-alignment review for the Zenn article on Human Return Point.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/human-return-point.md`
- Title: `Human Return Point――HITLと人間監督の再設計`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the public Human Return Point definition with the repository's bounded responsibility-return and AI participation boundaries.

## Article-level role

The article distinguishes Human-in-the-loop from Human Return Point. HITL shows that a human is in the loop. Human Return Point designs the state in which responsibility can actually return to human understanding, authority, time, information, and responsibility units.

Current repository alignment:

- strongly aligned with the Phase 3 human-AI review workflow example
- strongly aligned with AI final-responsibility exclusion
- strongly aligned with review-result boundaries that avoid treating formal approval as responsibility completion
- strongly aligned with the repository's responsibility-return vocabulary

Repository change decision:

- no immediate schema change required
- high-value source for future examples involving approval, stop, repair, and human review

## HITL boundary

The article states that humans being present, clicking approval, seeing a screen, being the formal final decision-maker, or leaving approval logs does not necessarily mean responsibility returned to humans.

Current repository alignment:

- supports not treating `human_review: true` as sufficient by itself
- supports requiring visible evidence, uncertainty, impact, refusal, stop, and repair paths in future examples
- supports `not_checked` and `not_claimed` fields when human review did not actually cover a point

Repository change decision:

- no immediate checker change required
- possible future checker idea: if an example claims Human Return Point, require information, authority, time, and repair/stop linkage fields

## Definition alignment

The article defines Human Return Point as the point where AI-agent judgments or actions can return to human understanding, authority, time, information, and responsibility units.

It is not merely a UI, not merely an approver, and not merely a human in the loop. It is a return path inside the responsibility pathway.

Current repository alignment:

- directly aligned with the first Phase 3 example
- directly aligned with AI support-node boundaries
- supports treating returnability as stronger than nominal approval

Repository change decision:

- no definition rewrite required
- future examples should distinguish formal approval from substantive return

## Minimum conditions

The article identifies minimum conditions for Human Return Point:

- information returns
- authority returns
- time returns
- responsibility can return to an organizational unit
- repair path is available

Current repository alignment:

- strongly aligned with Evidence Log
- strongly aligned with Stop Authority
- strongly aligned with Repair Owner
- strongly aligned with institutional and organizational responsibility return

Repository change decision:

- no immediate schema addition
- high-value source for future Human Return Point validation examples

## UI boundary

The article warns that UI can break Human Return Point when AI proposals dominate, evidence is hidden, changes are invisible, impacts are unclear, approval is emphasized over refusal, risks are collapsed, large approvals become assembly-line work, execution consequences are unclear, or rollback/repair is hidden.

Current repository alignment:

- supports future UI-facing examples without becoming a UI design system
- supports treating human approval as invalidly weak when key information or refusal authority is missing
- supports future review-result distinctions around missing context and unchecked risk

Repository change decision:

- no UI schema required now
- possible future example: `examples/human-return-point-ui-check.yaml` only if kept small and non-production

## Strong Human Return Point display

The article lists elements that strengthen Human Return Point:

- AI proposal
- AI evidence or references
- change diff
- impact scope
- uncertainty
- risk
- alternatives
- post-approval execution effect
- refusal / return / stop controls
- rollback availability
- repair owner
- external oversight or policy update changes
- Evidence Log content

Current repository alignment:

- strongly aligned with Evidence Log and review-result outputs
- supports future checkers that require display of evidence and missing context before claiming successful human return
- supports the boundary that evidence presentation helps returnability but does not itself certify correctness

Repository change decision:

- no immediate checker change
- high-value source for future example design

## Action Class Matrix alignment

The article connects Human Return Point to action classes. It states that return requirements differ by action class, and heavier actions require stronger Human Return Point design.

Examples include:

- Observe-Only: input source, quoted range, confidentiality check
- Suggest-Only: evidence and uncertainty at adoption
- Approval-Required: approver, diff, impact, refusal right
- Reversible External Action: rollback procedure and repair responsibility
- Irreversible or High-Impact Action: organizational owner, audit, legal return
- Emergency Stop: stop reason and restart conditions

Current repository alignment:

- strongly aligned with Action Class Matrix direction
- supports adding small future examples one action class at a time
- supports keeping high-impact and irreversible examples heavily bounded

Repository change decision:

- no immediate example addition
- future examples should select one action class and keep assumptions explicit

## Evidence Log connection

The article states that Human Return Point must connect to Evidence Log. It is not enough to say that a matter returned to a human. The log should record when it returned, to whom, what was displayed, what was approved, what was rejected, what information was missing, and what judgment led to repair.

Current repository alignment:

- strongly aligned with Evidence Log concept
- strongly aligned with review-result boundary
- supports the idea that human return must be reconstructable after the fact

Repository change decision:

- no immediate schema change
- possible future example: human-return evidence record

## Stop Authority connection

The article states that Human Return Point must connect to Stop Authority. If a human notices risk but cannot stop execution, responsibility has not meaningfully returned.

Current repository alignment:

- directly supports Stop Authority
- supports separating approval, refusal, stop, restart, and repair actions
- supports future examples involving suspension and return after stop

Repository change decision:

- no immediate schema change
- high-value source for future Stop Authority alignment note

## Repair Owner connection

The article states that responsibility returns not only at decision time but also after failure, and that Human Return Point must connect to Repair Owner. Without repair connection, the responsibility pathway does not close.

Current repository alignment:

- directly supports Repair Owner as a repeated cross-article concept
- supports the user's note that Repair Owner may not have its own standalone article
- supports later cross-article Repair Owner alignment note

Repository change decision:

- do not create a standalone Repair Owner source note yet
- after Evidence Log and Stop Authority reviews, create a cross-article note if useful

## External-context boundary

The article references EU AI Act Article 14, NIST AI RMF, OpenAI Agents SDK Human-in-the-loop, and human automation literature as background context.

Current repository alignment:

- useful for human oversight context
- should not become legal, compliance, safety, or certification claim
- should remain background unless a dedicated source-mapping note is created

Repository change decision:

- no compliance claim should be added
- keep external references contextual and bounded

## Claim-strength assessment

Compatible claims:

- HITL is necessary but not sufficient
- a human in the loop is not the same as responsibility returning to humans
- Human Return Point requires information, authority, time, organizational return, and repair connection
- UI can weaken or break responsibility return
- Action Class Matrix affects how strong the return point must be
- Evidence Log and Stop Authority are required connections
- Repair Owner is needed to close the pathway after failure

Claims to keep bounded:

- human oversight legal interpretation
- UI design prescriptions
- automation-bias claims beyond cited context
- compliance or safety certification
- production approval

Repository interpretation:

Human Return Point is one of the strongest source-aligned concepts for Phase 3. It should remain central, but always with explicit boundaries: human presence is not enough, and human approval is not completion.

## Repository alignment decision

Status: aligned.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> A Human Return Point claim should show what information returned, what authority returned, whether the human had time to judge, whether refusal or stop was possible, what evidence was recorded, and how repair ownership connects after failure.

## Next action

Proceed to the next inventory target:

- `articles/evidence-log-design.md`

Keep review incremental. Evidence Log should be reviewed before adding any new example that claims Human Return Point completeness.
