# Zenn Publication Readiness Plan

This document defines readiness gates for publishing Responsibility Pathway Engineering updates on Zenn.

It is a publication-planning note only. It is not a publication record, external review result, endorsement, certification, conformance claim, production approval, standardization claim, legal review, safety review, compliance review, fairness review, or AI final-responsibility transfer mechanism.

## Purpose

Zenn is expected to be the first external publication surface for explaining the current RPE GitHub repository.

The purpose of this plan is to decide what must be true before publishing public articles that point readers to the repository.

The plan separates:

- safe public explanation
- repository reader-path readiness
- external-review readiness
- implementation-readiness
- explicitly deferred work
- the publication repository boundary

## Publication levels

| Level | Publication type | Allowed message | Required repository state |
| --- | --- | --- | --- |
| Level 0 | No external publication | Internal construction only. | Repository may still have missing reader paths. |
| Level 1 | Concept introduction | RPE is an early public specification and design framework. | README, BEACON, overview, provenance, and boundary documents are readable. |
| Level 2 | Repository walkthrough | Readers can inspect current definitions, examples, checkers, reader paths, and non-claims. | Operation index, current task inventory, example index, checker coverage, Level 2 walkthrough readiness, and external-review package are reachable. |
| Level 3 | Review request | External readers can give feedback on clarity, overclaim risk, examples, and checker boundaries. | External-review readiness checklist and package note are current. |
| Level 4 | Implementation preview | Future connector/API direction can be discussed as design preview only. | API future shape, external product survey, connector target matrix, and deferred-work boundaries are current. |
| Level 5 | Implementation announcement | A bounded implementation exists and can be inspected. | Not current. Requires separate implementation notes, checker boundaries, and observed workflow records. |

## Current intended publication level

The near-term Zenn target should be Level 2 unless the article scope deliberately requires Level 3 or Level 4 language.

Safe near-term article scopes:

- what Responsibility Pathway Engineering is
- why responsibility paths matter around AI-involved judgment and action
- what the GitHub repository currently contains
- how to read the repository
- what the repository explicitly does not claim
- where repair, recovery-pathway reading, examples, checker boundaries, and deferred work can be inspected
- why future API / connector work remains design-preview only when mentioned
- what external product connection surfaces RPE is observing when the article is explicitly a future-preview article

Unsafe near-term article scopes:

- claiming RPE is a finished standard
- claiming conformance readiness
- claiming certification readiness
- claiming production readiness
- claiming implemented connectors
- claiming legal, safety, compliance, or fairness validation
- claiming semantic correctness of event-to-pathway mapping
- claiming AI can receive final responsibility under the current minimal model
- importing adjacent work from another workspace unless it has a clear RPE-repository role and reader path

## Progress-based article cadence

Zenn articles may be written as the RPE repository reaches reader-explainable progress points.

A repository progress point can trigger an article candidate when:

- the relevant reader path is reachable from the public entry documents;
- the repository state can be explained without relying on private conversation context;
- the article can point to definitions, examples, checker boundaries, non-claims, or deferred-work notes in this repository;
- the article does not require claims stronger than the current repository state supports.

The article file itself belongs in the dedicated Zenn content repository:

- `YutoriKomeiji/zenn-content/articles/`

This RPE repository remains the source for definitions, boundaries, examples, checker scope, reader-path status, and publication-readiness planning.

## Required documents before Zenn publication

Before a Zenn article points readers to the repository, confirm that these documents are reachable and current enough for the article scope:

| Document | Required for | Check |
| --- | --- | --- |
| `README.md` | all publication levels | public entrance is short and boundary-aware |
| `README.ja.md` | Japanese reader entry | Japanese public-reader path is visible |
| `BEACON.md` | restart and current position | current phase and read-first path are visible |
| `docs/overview.md` | repository overview | Phase 3.1 and public-review path are current |
| `docs/provenance.md` | source lineage | public source lineage is traceable |
| `docs/zenn-level-2-repository-walkthrough-readiness.md` | Level 2 repository walkthrough | Level 2 reader path and pre-publication cleanup / scope-fit checks are current |
| `docs/external-review-package-note.md` | review navigation | external-review path is compact |
| `docs/external-review-readiness-checklist.md` | review-readiness | readiness is framed as non-certifying |
| `docs/progress-map.md` | progress language | estimates are planning-only |
| `docs/zenn-article-title-source-check.md` | article title planning | existing Zenn article titles and aligned source inventory are checked before choosing a title |
| `docs/zenn-publication-cadence-note.md` | publication timing | publication timing is based on repository readability, not one-time announcement pressure or calendar rhythm alone |
| `docs/zenn-publication-docs-cleanup-task.md` | public reader-path cleanup | timestamped work-log and sync-note files under `docs/` are reviewed before public walkthrough use |
| `docs/assistant-pathway-maintenance-checklist.md` | conversation-derived repository updates | repository fit is checked before adding conversation-derived material to the public walkthrough path |
| `docs/api-future-shape.md` | API preview article | future API is clearly not implemented |
| `docs/external-product-connection-survey.md` | world-product context | survey is framed as connection-surface observation |
| `docs/deferred-work-restart-conditions.md` | deferred boundary | deferred work remains explicit |
| `docs/zenn-content-publication-handoff.md` | publication repository handoff | article files are prepared under `YutoriKomeiji/zenn-content/articles/`, not in this repository |

## Article title gate

Before choosing a new Zenn article title or scope, read `docs/zenn-article-title-source-check.md`.

The article title gate requires that:

- the dedicated `YutoriKomeiji/zenn-content/articles/` repository path has been checked;
- existing explicit-title articles are treated as occupied title and scope territory;
- hash / legacy filename articles from the RPE source-alignment inventory are not ignored;
- the latest article is excluded from immediate reuse unless the maintainer explicitly reopens it;
- the next title does not duplicate the already published Responsibility Pathway / RPE definition series.

## Publication cadence gate

Before treating a Zenn article as timely, read `docs/zenn-publication-cadence-note.md`.

A Zenn article should be considered when the repository has grown into a reader-explainable state.

Do not publish only because time has passed.

## Scope-fit gate

Before adding conversation-derived material to the repository or to a public walkthrough article, check whether it has a clear RPE-repository role.

If the material belongs to another workspace, such as a separate Drive folder, article repository, private continuity record, or external project, keep it out of the RPE repository unless a repository-specific responsibility unit and reader path are named.

This gate is meant to prevent public-reader confusion, not to block valid RPE work.

## Article gate checklist

Before publication, check:

- [ ] The article states that RPE is an early public specification.
- [ ] The article links to the repository entrance, not only to deep documents.
- [ ] The article distinguishes concept, repository state, review request, and future preview.
- [ ] The article title and scope were checked against `docs/zenn-article-title-source-check.md`.
- [ ] The article timing was checked against `docs/zenn-publication-cadence-note.md`.
- [ ] The article scope was checked against the scope-fit gate.
- [ ] The article repository boundary was checked against `docs/zenn-content-publication-handoff.md`.
- [ ] Timestamped work-log or sync-note files under `docs/` were reviewed for public-facing reader-path cleanup.
- [ ] Conversation-derived material was checked for repository fit before being included in the public walkthrough path.
- [ ] The article does not imply certification, conformance, production readiness, or standardization completion.
- [ ] The article does not imply external review has already approved the project.
- [ ] The article does not imply current API routes are implemented.
- [ ] The article does not imply current connectors exist.
- [ ] The article does not use observed checker or workflow success as correctness proof.
- [ ] The article points readers to non-claims and deferred boundaries.
- [ ] The article keeps responsibility with the human author or responsible institution.

## Recommended first Zenn article set

A safe first article set would be:

1. Repository guide: how to read the GitHub repository.
2. Current-state article: what has changed since the earlier Zenn Responsibility Pathway / RPE article series.
3. Boundary article: what the current repository does not claim.
4. API / connector preview article: what may be built later and why it remains deferred.
5. External product connection article: what current AI products expose as connection surfaces and what RPE observes from them.

These should be published as explanatory notes, not as standardization announcements.

Do not duplicate the existing Responsibility Pathway definition and motivation articles unless the maintainer explicitly decides to write a revision or follow-up.

## Stop conditions

Do not publish a Zenn article if:

- the repository entrance contradicts the article;
- the article relies on a document that is not linked from a public reader path;
- the article uses maturity language stronger than the repository supports;
- the title or scope duplicates an existing Zenn article without an explicit revision purpose;
- the article is only being published because time passed, not because the repository state is explainable;
- checker or workflow results are described as validation rather than bounded maintenance signals;
- future API or connector work is described as implemented;
- deferred work is presented as current capability;
- adjacent non-RPE workspace material is imported without a clear RPE-repository role and reader path;
- the article file is created in this repository instead of `YutoriKomeiji/zenn-content/articles/`;
- the article creates avoidable legal, safety, compliance, fairness, or certification implications.

## Next safe repository action

If Zenn publication planning continues, the next safe action is to connect this plan from a reader-path document such as:

- `docs/operation-index.md`
- `docs/current-task-inventory.md`
- `docs/phase-3-1-public-entry-sync-note.md`

Do not rewrite long documents solely to duplicate this plan.

The human author or maintainer remains responsible for deciding whether a Zenn article should be drafted, published, revised, relied upon, retracted, repaired, or deferred.
