# RPE Tool Discovery and Citation Plan

This note defines how Responsibility Pathway Engineering tooling can be made discoverable without pretending that the tools prove, certify, validate, assure, conform, or solve the broader responsibility-related domain.

The goal is not to build tools at random.

The goal is to publish small, bounded, searchable tool proposals that connect:

- a responsibility-related domain term,
- a public problem or research concern,
- a cited source or reference link,
- an RPE interpretation,
- a small implementation artifact,
- clear non-claims,
- and a feedback request.

## Core idea

RPE tooling may use a public posture like:

> I found a recurring responsibility-path problem in this area. I tried turning one bounded part of it into an inspectable RPE artifact. I used a small tool in YAML, Python, JavaScript, or Lean4. It may or may not be useful. If this touches a real pain point, feedback is welcome.

This is different from saying:

> This tool proves that the AI system is responsible, safe, explainable, verified, assured, compliant, or conformant.

The discovery layer should make the experiment findable while preserving the non-claims.

## Discovery fields

Each public tool proposal should include a small discovery block.

Suggested fields:

```yaml
discovery:
  area_terms: []
  related_keywords: []
  source_links: []
  source_types: []
  rpe_problem_statement: ""
  rpe_tool_angle: ""
  implementation_surface: ""
  tool_status: "prototype"
  feedback_requested: true
  non_claims: []
```

The discovery block is metadata for readers.

It is not evidence that the tool satisfies the domain term or source.

## Area terms

Area terms are broad discovery anchors.

Examples:

- Responsible AI
- Explainable AI
- Safe AI
- Verified AI
- AI verification
- TEVV
- AI assurance
- conformity assessment
- provenance
- traceability
- record-keeping
- cryptographic verifiability

Area terms help a reader understand the conceptual neighborhood.

They must not be used as proof that the tool satisfies that field.

## Related keywords

Related keywords should be more specific than area terms.

Examples:

- responsibility holder
- human oversight
- review gate
- approval status
- evidence route
- missing context
- source provenance
- traceable decision path
- accountable workflow
- audit trail
- tamper-evident record
- signed manifest
- model output review
- AI-assisted work record
- disputed output return path
- post-deployment incident record

Keywords should reflect the actual contents of the tool.

Do not add popular keywords merely to attract search traffic if the tool does not address them.

## Source links

A source link may be:

- a paper URL
- an arXiv URL
- a standards-page URL
- a regulator or government guidance URL
- a public technical report URL
- a public incident write-up URL
- a project documentation URL
- a public benchmark or assurance framework URL

A source link should be used as context, not as endorsement.

A tool proposal should state:

- what the source appears to discuss,
- which responsibility-path angle RPE extracts,
- what the tool tries to make inspectable,
- what the tool does not solve,
- whether the source author has not reviewed or endorsed the tool.

## Source-type labels

Possible source-type labels:

- `paper`
- `preprint`
- `standard`
- `guidance`
- `regulatory_material`
- `technical_report`
- `incident_report`
- `project_documentation`
- `benchmark`
- `framework`
- `news_context`

The label is descriptive only.

It should not imply authority beyond what the source actually provides.

## RPE problem statement

The problem statement should translate the source or domain into a responsibility-path concern.

Good examples:

- "The output may be reviewed, reused, or published without a visible human responsibility holder."
- "The evidence route behind an AI-assisted decision is difficult to inspect."
- "The approval status may collapse into a vague statement that the tool checked it."
- "A reader cannot easily see where a disputed result should return."
- "A generated artifact may cite sources without making unchecked sources visible."

Avoid:

- "This solves Responsible AI."
- "This proves the model is explainable."
- "This verifies safety."
- "This provides conformity assessment."

## RPE tool angle

The tool angle should name the bounded artifact being proposed.

Examples:

- YAML responsibility-path record
- Python required-field checker
- Python source-reference checker
- JavaScript first-use helper
- JavaScript non-claim reminder panel
- Lean4 responsibility-holder distinction
- hash manifest design note
- paper-to-RPE proposal template

The tool angle should be small enough for one PR or one visible prototype.

## Implementation surfaces

### YAML

Use YAML when discovery metadata, source links, and responsibility-path records need to be copyable.

Useful artifacts:

- tool proposal metadata
- paper-to-RPE intake records
- evidence manifests
- source-reference records
- review status records
- non-claim flags

### Python

Use Python when the tool can inspect local files without claiming external correctness.

Useful artifacts:

- missing-field checker
- local reference checker
- source-link presence checker
- discovery metadata linter
- report generator
- hash manifest checker

### JavaScript

Use JavaScript when the tool should help readers navigate or understand a record.

Useful artifacts:

- static page for tool proposals
- keyword browser
- source-link viewer
- copyable template helper
- non-claim reminder UI
- feedback prompt UI

### Lean4

Use Lean4 when a structural distinction can be stated under explicit assumptions.

Useful artifacts:

- AI assistance is not final responsibility
- approval status is distinct from validation
- review gate existence is distinct from approval
- a return path is a structural requirement
- non-claim flags are not proof objects

Lean4 should not be used to claim real-world correctness.

## Searchable public page pattern

A public page for each tool proposal should include:

1. title
2. short summary
3. area terms
4. related keywords
5. source links
6. source relationship note
7. RPE problem statement
8. tool made
9. how to try it
10. what it may help with
11. what it does not prove
12. feedback request

Example title pattern:

```text
RPE Tool Proposal: Traceability helper for AI-assisted review records
```

Example summary pattern:

```text
This prototype explores whether a small RPE record and checker can make the responsibility path of an AI-assisted review easier to inspect. It is not certification, validation, assurance, or conformity assessment.
```

## Paper-to-RPE discovery pattern

A paper-inspired tool proposal should include:

```text
Source:
- title
- URL
- source type
- date checked

Observed concern:
- short description of the responsibility-path issue noticed from the source

RPE translation:
- responsibility holder
- AI assistance boundary
- evidence route
- missing context
- review gate
- approval status
- return path
- non-claims

Tool made:
- artifact path
- language or format
- bounded function

Non-claims:
- does not solve the paper's problem
- does not represent the paper author's intent
- does not validate the source
- does not prove real-world correctness
- does not provide certification, assurance, conformity, legal, safety, compliance, fairness, or production approval

Feedback request:
- ask whether this tool shape matches a real pain point
```

## Repository placement

Possible future locations:

- `docs/tool-discovery/`
- `docs/tool-proposals/`
- `kits/paper-to-rpe/`
- `tools/discovery/`
- `site/tool-proposals/`

The first step should be a design note only.

The second step may add one prototype discovery metadata template.

The third step may add one filled example based on a public source.

## Link discipline

Source links should be stable enough for readers to inspect.

For papers and technical reports, prefer:

- DOI page when available
- arXiv abstract page when relevant
- official publisher page when accessible
- official project page
- official standards or guidance page

Do not cite a source as if it endorses the tool.

Do not imply that the repository has performed a literature review unless it has.

Do not imply that one source represents the whole field.

## Keyword discipline

Keywords should be accurate, not maximal.

A tool proposal may use a term if:

- the source uses the term, or
- the tool directly maps to a responsibility-path concern commonly associated with the term, and
- the proposal clearly states that it is not satisfying the full discipline.

A tool proposal should avoid a term if:

- it is only included for search traffic,
- the tool does not address it,
- the term would imply certification or assurance beyond the tool boundary,
- the source relationship is speculative.

## Feedback channel note

A public tool proposal should ask for feedback in a bounded way.

Good feedback questions:

- Does this match a real responsibility-path pain point?
- Is the source relationship clear?
- Are the keywords accurate?
- Is the non-claim visible enough?
- Would this help a reviewer inspect a draft?
- What field is missing?
- Where would this fail in practice?

Feedback is design input.

Feedback is not endorsement, validation, certification, assurance, conformity, or acceptance.

## Non-claims

Discovery metadata, keywords, source links, and paper references do not provide:

- proof
- certification
- validation
- assurance
- conformity assessment
- legal review
- safety review
- compliance review
- fairness review
- production readiness
- source endorsement
- author endorsement
- regulator endorsement
- institutional acceptance
- semantic responsibility proof
- complete provenance
- complete traceability
- AI final-responsibility transfer

## Stop conditions

Stop or revise if a proposal:

- uses keywords that the artifact does not actually address
- implies source endorsement without evidence
- implies author intent without confirmation
- implies standards or regulatory compliance
- claims certification, assurance, validation, conformity, safety, compliance, fairness, or production readiness
- hides uncertainty or missing context
- uses a paper as decoration rather than a real source relationship
- hides the feedback-request nature of the tool
- treats visibility as proof
- treats a checker, YAML file, browser UI, or Lean4 fragment as sufficient by itself

## Next safe step

After this note, a safe next repository step is to add one small metadata template for tool proposals, for example:

- `docs/tool-proposals/template.md`

That template should include area terms, related keywords, source links, RPE translation, tool artifact path, non-claims, and feedback questions.
