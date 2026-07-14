# Tool Proposal Index Design

This note designs a future index for Responsibility Pathway Engineering (RPE) tool proposals.

The index should help readers, search engines, and AI-assisted discovery tools find small RPE tool proposals by accurate area terms, related keywords, source links, implementation surfaces, and non-claims.

The index is a navigation aid only.

It does not certify, validate, assure, conform, approve, prove, endorse, or accept any proposal, tool, source interpretation, checker result, record, repository, downstream fork, or external use.

## Purpose

The tool proposal index should make it easy to answer questions such as:

- What RPE tool proposals exist?
- Which responsibility-related area does each proposal touch?
- Which source links or public references does it use?
- What implementation surface does it explore?
- What artifact path should a reader inspect?
- What does the proposal explicitly not claim?
- Where can feedback be directed?
- Should the proposal remain inside the RPE repository or later become a separate repository?

The index should improve discoverability without increasing claim strength.

## Scope

The index may include:

- Markdown-only tool proposals
- YAML record-shape proposals
- Python checker proposals
- JavaScript reader-aid proposals
- Lean4 structural-fragment proposals
- mixed prototypes
- paper-to-RPE examples
- source-linked review examples
- non-production adoption examples

The index should not include:

- unrelated notes that are not tool proposals
- broad essays without an inspectable artifact path
- public claims without non-claims
- tools that imply certification or assurance
- external product names as inspiration labels
- entries that use keywords only for search traffic

## Proposed index path

A future concrete index may live at:

```text

docs/tool-proposals/index.md
```

This design note intentionally does not create the final index yet.

It defines the shape first so the first concrete index can be reviewed separately.

## Minimum entry fields

Each index entry should include:

```yaml
proposal:
  title: ""
  path: ""
  status: "draft | prototype | example | design | promoted"
  area_terms: []
  related_keywords: []
  source_links: []
  source_types: []
  implementation_surface: "Markdown | YAML | Python | JavaScript | Lean4 | mixed"
  artifact_paths: []
  non_claims: []
  feedback_requested: true
  repository_boundary: "inside-rpe | candidate-for-promotion | promoted"
```

These fields are for navigation and review.

They are not evidence that a proposal satisfies its area terms, source requirements, or external frameworks.

## Required human-readable columns

A Markdown index may use columns such as:

| Proposal | Area terms | Source context | Surface | Artifact | Non-claim reminder | Feedback |
| --- | --- | --- | --- | --- | --- | --- |
| Example proposal | AI assurance, traceability | public context only | Markdown/YAML | path | not assurance | feedback requested |

The table should stay short enough to read.

Long details should remain in each proposal file.

## Area terms

Area terms should be broad discovery anchors.

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

Area terms must not imply that the proposal satisfies that field.

The index should visibly preserve this boundary.

## Related keywords

Related keywords should describe the actual contents of the proposal.

Examples:

- responsibility holder
- AI-assisted work record
- review gate
- approval status
- evidence route
- missing context
- unchecked sources
- source relationship note
- return path
- traceable decision path
- accountable workflow
- tamper-evident record
- signed manifest
- AI-assisted review note

Do not add keywords merely for search traffic.

If a keyword does not correspond to a visible field, behavior, or explanation in the proposal, do not include it.

## Source-link fields

Each source-linked proposal should expose:

```yaml
source_links:
  - url: ""
    title: ""
    source_type: "paper | preprint | standard | guidance | technical_report | incident_report | project_documentation | benchmark | framework | other"
    date_checked: "YYYY-MM-DD"
    relationship_note: "Used as public context for a responsibility-path concern; not endorsement."
```

The source link is context, not endorsement.

The index should not imply that a source author, publisher, regulator, standard body, project maintainer, or institution has reviewed or accepted the RPE proposal unless that is explicitly documented.

## Implementation surface

Implementation surface should describe how the proposal is expressed.

Supported labels:

- Markdown
- YAML
- Python
- JavaScript
- Lean4
- mixed

Surface labels should not imply maturity.

For example, a Python proposal may be a design note, not an implemented checker.

A Lean4 fragment may preserve a structural distinction under assumptions, not prove real-world responsibility correctness.

## Artifact path discipline

Each entry should point to a concrete artifact path.

Examples:

```text

docs/tool-proposals/examples/ai-assurance-traceability-review-record.md

templates/ai-assisted-work-responsibility-path.yaml

scripts/check_rpe_records.py

site/template-helper/index.html

Rpe/ResponsibilityHolder.lean
```

If there is no artifact path, the entry may not be ready for the index.

## Non-claim reminder

Every entry should include a short non-claim reminder.

Examples:

- not certification
- not validation
- not assurance
- not conformity assessment
- not legal review
- not safety review
- not compliance review
- not fairness review
- not production approval
- not source endorsement
- not AI final-responsibility transfer

The index should prefer compact reminders and let each proposal file contain the full boundary.

## Feedback field

Each entry should show whether feedback is requested.

Possible values:

- feedback requested
- feedback not yet requested
- internal design only
- archived

Feedback should be treated as design input.

Feedback is not endorsement, validation, certification, assurance, conformance, approval, acceptance, or external review.

## Repository-boundary field

The index should show whether a proposal remains inside the RPE repository or may later need promotion.

Suggested values:

- `inside-rpe`
- `candidate-for-promotion`
- `promoted`
- `archived`

Meaning:

- `inside-rpe`: proposal is part of the core RPE documentation, examples, or small prototype set.
- `candidate-for-promotion`: proposal may become a separate repository if it needs its own lifecycle.
- `promoted`: proposal moved to a separate repository by human maintainer decision.
- `archived`: proposal is retained for history but not recommended as a current path.

Repository promotion must not be treated as validation.

## Initial candidate entry

A first concrete index may include:

```yaml
proposal:
  title: "Traceability review record for AI assurance evidence notes"
  path: "docs/tool-proposals/examples/ai-assurance-traceability-review-record.md"
  status: "example"
  area_terms:
    - "AI assurance"
    - "Responsible AI"
    - "traceability"
    - "record-keeping"
    - "TEVV"
  related_keywords:
    - "responsibility holder"
    - "AI-assisted review record"
    - "evidence route"
    - "review gate"
    - "approval status"
    - "return path"
  source_types:
    - "preprint"
  implementation_surface: "Markdown and YAML"
  artifact_paths:
    - "docs/tool-proposals/examples/ai-assurance-traceability-review-record.md"
  non_claims:
    - "not assurance"
    - "not validation"
    - "not conformity assessment"
    - "not source endorsement"
    - "not AI final-responsibility transfer"
  feedback_requested: true
  repository_boundary: "inside-rpe"
```

This is an index candidate only.

It does not claim that the indexed proposal provides assurance, validation, conformity assessment, TEVV, source endorsement, or production readiness.

## Index update rules

When adding a new proposal entry, check:

1. The proposal file exists.
2. The proposal has a short summary.
3. The proposal has accurate area terms.
4. The proposal has related keywords that match the actual content.
5. Source links include relationship notes when used.
6. The implementation surface is accurate.
7. Non-claims are visible.
8. Feedback posture is clear.
9. Repository-boundary status is clear.
10. No external acceptance is implied.

If any item is unclear, do not add the entry yet.

## Future machine-readable index

A later PR may add a machine-readable index such as:

```text

docs/tool-proposals/index.yaml
```

or:

```text

docs/tool-proposals/index.json
```

That file should be treated as navigation metadata only.

It should not be treated as conformance evidence, assurance evidence, source endorsement, certification, or validation.

## Future public documentation page

A later public page may render the index into a reader-facing page.

Possible page path:

```text

site/tool-proposals/index.html
```

The page should include:

- proposal title
- source relationship reminder
- area terms
- related keywords
- artifact path
- non-claim reminder
- feedback status

The page should not turn the index into an approval surface.

## Stop conditions

Stop or revise if the index:

- uses keywords the proposal does not actually address
- hides source relationship notes
- hides non-claims
- treats source links as endorsement
- treats index inclusion as validation
- implies certification, assurance, conformity, legal review, safety review, compliance review, fairness review, production readiness, or external acceptance
- treats feedback as approval
- treats repository promotion as proof
- makes AI the final responsibility holder

## Next safe step

After this index design note, the next planned step is:

```text

docs/tooling/discovery-metadata-linter-design.md
```

That note should design a small future Python linter that checks whether tool proposal metadata contains required discovery fields, source relationship notes, non-claims, and feedback posture.
