# Provenance of Responsibility Pathway / 責任経路

This document records the public source lineage and authorship traceability for **責任経路 / Responsibility Pathway** and **Responsibility Pathway Engineering** in this repository.

It expands the concise provenance statements in `README.md` and `README.ja.md`.

This is an attribution and traceability record. It is not a certification record or production approval record.

## Author

Akihisa Ono (小野昭久)

Repository affiliation: Independent

## Core provenance statement

According to the author's own development record, Akihisa Ono began thinking about and using the concept of **責任経路 / Responsibility Pathway** from the note article:

- "AI事故は『責任設計』だけでは防げない――最後の砦は『責任経路設計』である"
- URL: https://note.com/dantarg/n/nb7f28afa6882
- Published: 2026-01-18

At that time, the author checked available search results and dictionaries and did not find **責任経路** or **Responsibility Pathway** as an established ordinary term for this design concept.

Therefore, the author defined the concept instead of treating it as a pre-existing standard term.

The initial formulation began from the expression:

- **責任経路を設計する**

The phrase means designing responsibility not merely as a point of attribution, but as a flow or path that preserves where judgment arises, where it changes, where it can stop, where it returns to humans, and how that pathway remains structurally maintained during operation.

## Public source lineage

The current public source lineage includes the following articles.

### First public source

- "AI事故は『責任設計』だけでは防げない――最後の砦は『責任経路設計』である"
- URL: https://note.com/dantarg/n/nb7f28afa6882
- Role: first public source for the author's Responsibility Pathway concept and the expression **責任経路を設計する**

### Major public source articles

- "2026年、AI安全の争点は『ガバナンス』ではない"
  - URL: https://note.com/dantarg/n/n7e55212b8ac4
  - Role: connects Responsibility Pathway Design to AI safety, support, and governance limits.

- "責任経路設計とは何か"
  - URL: https://note.com/dantarg/n/na7a65ee28906
  - Role: explains the concept of Responsibility Pathway Design directly.

- "責任あるAI（Responsible AI）が実装できない本当の理由"
  - URL: https://note.com/dantarg/n/n77367658521c
  - Role: connects the difficulty of implementing Responsible AI to the absence of responsibility pathways.

These articles are treated as public source lineage for the concept, terminology, motivation, and early framing of responsibility pathway design before and alongside this repository's specification work.

## Repository development path

This repository develops the public source lineage into:

- definitions
- concept models
- examples
- schemas
- bounded checkers
- review notes
- roadmap notes
- operation documents
- formalization candidates

The repository's aim is to preserve return paths from claims to definitions, from definitions to specifications, from specifications to examples and formalization candidates, and from formalization candidates back to explicit assumptions.

## Relation to README files

`README.md` provides the English public entry point.

`README.ja.md` provides the Japanese public entry point.

Both contain concise provenance statements.

This document is the detailed provenance record that those README sections may point to.

## Boundary of this provenance record

This document records attribution and traceability.

It does not establish:

- legal responsibility determination
- safety certification
- compliance certification
- fairness certification
- moral resolution
- institutional approval
- production readiness
- connector correctness
- adapter correctness
- runtime correctness
- AI final-responsibility transfer

The claim preserved here is narrower:

- Akihisa Ono began using **責任経路 / Responsibility Pathway** as this design concept from the 2026-01-18 public note article.
- The author checked search results and dictionaries at the time and did not find it as an established ordinary term for this design concept.
- The author therefore defined and developed the concept, beginning from the expression **責任経路を設計する**.
- This repository records and develops that public source lineage.

## Roadmap alignment

This provenance work belongs primarily to:

- Phase 0: foundation, authorship, public entry points, notice, citation, source traceability
- Phase 1: concept models and source mapping from public articles to canonical repository definitions

It does not unlock:

- schema changes
- checker changes
- workflow changes
- runtime connectors
- production runtime
- Lean formalization

Those later layers must continue to follow the roadmap, checker boundaries, runtime-event checking plan, and current task inventory.

## Future maintenance

When new public source articles, formal papers, repository milestones, or external references become important for tracing the concept, add them here only if they clarify provenance.

Do not use this document as a changelog, certification record, or replacement for `AUTHORSHIP.md`, `NOTICE.md`, `CITATION.cff`, or `CHANGELOG.md`.
