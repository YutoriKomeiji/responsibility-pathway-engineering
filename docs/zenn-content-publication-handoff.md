# Zenn Content Publication Handoff

This note records the publication handoff boundary between this Responsibility Pathway Engineering repository and the dedicated Zenn content repository.

It is a handoff and planning note only. It is not a publication record, external review result, endorsement, certification, conformance claim, production approval, standardization claim, legal review, safety review, compliance review, fairness review, API implementation, connector implementation, runtime implementation, or AI final-responsibility transfer mechanism.

## Dedicated publication repository

Zenn publication content should be moved or drafted in the dedicated Zenn repository when the publication gate is satisfied:

- repository: `YutoriKomeiji/zenn-content`
- article directory: `articles/`

This RPE repository remains the source repository for specifications, boundaries, examples, checkers, reader paths, and publication-readiness planning.

The Zenn content repository is the publication surface for article drafts and published article files.

## Handoff rule

Do not treat a documentation note in this repository as a Zenn article by itself.

When a Zenn article is ready to publish, the maintainer should:

1. confirm the article scope against `docs/zenn-publication-readiness-plan.md`;
2. confirm the Japanese reader path against `docs/zenn-publication-ja-reader-note.md`;
3. confirm that the article does not exceed repository-supported claims;
4. prepare the article file under `YutoriKomeiji/zenn-content/articles/`;
5. preserve links back to this repository's public reader path;
6. keep claims weaker than or equal to the current RPE repository state;
7. avoid implying external review, certification, conformance, production readiness, implemented API routes, or implemented connectors unless such status is separately documented and valid.

## Source-of-truth split

| Material | Source location | Publication location |
| --- | --- | --- |
| RPE definitions | this repository | linked or summarized in Zenn |
| repository status | this repository | summarized in Zenn |
| non-claims and boundaries | this repository | summarized and linked in Zenn |
| examples and checkers | this repository | summarized and linked in Zenn |
| Zenn article draft | Zenn content repository | `articles/` |
| published article text | Zenn content repository | Zenn platform |

## Article migration timing

Move or draft article text in the Zenn content repository only when:

- the relevant publication level is identified;
- required documents are reachable;
- public claims are boundary-checked;
- API and connector material is clearly framed as future-shape or design-preview if not implemented;
- Japanese reader guidance is available when the article is Japanese;
- the human maintainer is ready to publish or stage the article.

## Boundary

This note does not authorize:

- publishing an article before readiness gates are checked;
- treating this repository as the Zenn article repository;
- treating article text as a specification source of truth;
- presenting future API or connector design as implemented;
- presenting synthetic examples as production evidence;
- presenting checker or workflow success as certification;
- presenting RPE as externally reviewed, standardized, certified, or production-ready.

The human author or maintainer remains responsible for deciding whether any article should be drafted, migrated, published, revised, retracted, repaired, relied upon, or deferred.
