# Operation Document Index

This index explains which operation-related document to read for each maintenance situation.

It is a navigation aid only. It is not a certification process, legal review process, safety review process, compliance process, production approval process, connector correctness proof, adapter correctness proof, or AI final-responsibility transfer mechanism.

## Primary reconnection path

Use this path when restarting work after a pause or when another maintainer, reviewer, or AI-assisted session needs to understand the current repository state.

1. `BEACON.md`
2. `README.md`
3. `docs/operation-index.md`
4. `docs/repository-operation-model.md`
5. the current phase snapshot
6. the relevant sync log or roadmap note
7. `docs/current-task-inventory.md` when choosing the next task
8. `docs/ai-judgment-node-task-control.md` when AI local judgment, task-control loops, stop conditions, or evaluator separation matter
9. `docs/progress-map.md` when checking rough progress, gates, next gates, or stop conditions
10. `docs/concepts/index.md` when concept-level reader paths matter
11. `docs/standardization-strategy.md` when standardization language, grounding discipline, or world-standard preparation matters
12. `docs/external-review-readiness-checklist.md` when preparing or evaluating external review readiness
13. `docs/external-review-package-note.md` when preparing a compact external-review reader package
14. `docs/zenn-publication-readiness-plan.md` when preparing public Zenn publication language or publication gates
15. `docs/zenn-publication-readiness-connection.md` when connecting Zenn publication planning to public-entry and review-reader paths
16. `docs/zenn-publication-ja-reader-note.md` when Japanese Zenn readers need a short repository-reading route
17. `docs/connector-target-matrix.md` when choosing future connector target categories before any implementation
18. `docs/connector-target-matrix-connection.md` when connecting connector target planning to API future shape and external product survey notes
19. `docs/event-to-pathway-relation-checker-plan.md` when considering future relation-checker planning without implementation
20. `docs/example-index.md`
21. `docs/checker-coverage.md`
22. `docs/social-connection-review-navigation.md` when social-connection review paths matter
23. `docs/repository-pathway-gap-inventory.md` when structure breaks or reader-path gaps need to be tracked

`CHANGELOG.md` is not part of the primary construction-time reconnection path. Use it mainly for archival, investigative, historical, or retrospective milestone review.

## Usage phases

Use documents according to the phase of work.

| Work phase | Prefer reading | Use `CHANGELOG.md` when |
| --- | --- | --- |
| Active construction | `BEACON.md`, `README.md`, current snapshot, operation index, sync log, roadmap note, current task inventory, progress map, checker coverage, example index, primary artifact | a prior milestone or boundary change must be investigated |
| Restart or handoff | `BEACON.md`, `README.md`, current snapshot, operation index, sync log, roadmap note, current task inventory, progress map | the restart depends on historical cause tracing |
| Progress review | `docs/progress-map.md`, `docs/phase-3-1-progress-map-connection.md` when Phase 3.1 context matters, current snapshot, current task inventory, operation index, roadmap note | checking when a progress estimate or gate changed |
| Concept-path navigation | `docs/concepts/index.md`, relevant concept note, source-alignment note, example index, checker coverage | checking when a concept boundary changed |
| AI local judgment or task-control boundary review | `docs/ai-judgment-node-task-control.md`, `docs/phase-3-1-ai-judgment-node-connection.md`, `docs/phase-3-1-ai-judgment-node-sync-note.md`, `docs/ai-agent-operation-patterns.md`, current snapshot, current task inventory | checking when AI local judgment, loop-like task control, goal-like stop conditions, evaluator separation, or evidence-selection boundaries changed |
| Social connection or approval-transfer review | `docs/social-connection-review-navigation.md`, `docs/social-connection-exception-cases.md`, `docs/evidence-approval-transfer-alignment.md`, `docs/validation-checklist.md`, `docs/evidence-log.md`, `docs/repository-pathway-gap-inventory.md` | checking when social-connection exceptions, approval-transfer alignment, evidence-log review, or pathway-gap navigation changed |
| Standardization preparation | `docs/standardization-strategy.md`, progress map, README, operation index, current snapshot, concept index, example index, checker coverage | checking when a standardization boundary or language choice changed |
| External review preparation | `docs/external-review-package-note.md`, `docs/external-review-readiness-checklist.md`, README, operation index, current snapshot, current task inventory, checker coverage, example index, schema/fixture alignment, standardization strategy, progress map | checking when external-review scope, package path, readiness, or non-readiness boundaries changed |
| Public publication planning | `docs/zenn-publication-readiness-plan.md`, `docs/zenn-publication-readiness-connection.md`, `docs/zenn-publication-ja-reader-note.md`, README, README.ja, BEACON, overview, external-review package, progress map, deferred-work restart conditions | checking when publication gates, Japanese reader path, public-entry framing, or Zenn article scope changed |
| Connector and API target planning | `docs/connector-target-matrix.md`, `docs/connector-target-matrix-connection.md`, `docs/api-future-shape.md`, `docs/external-product-connection-survey.md`, `docs/adapter-boundary.md`, `docs/deferred-work-restart-conditions.md` | checking when connector target categories, future API surfaces, or external product observation boundaries changed |
| Checker or example interpretation | `docs/checker-coverage.md`, `docs/example-index.md`, `docs/runtime-event-schema-fixture-alignment.md`, `docs/event-to-pathway-relation-checker-plan.md` when relation-checker planning matters, relevant schemas or examples | checking when a rule, coverage boundary, schema-fixture alignment, relation-checker plan, or fixture interpretation changed |
| Workflow observation | `docs/runtime-event-workflow-current-status.md`, `docs/minimal-runtime-fixture-checker-workflow-observation.md`, `docs/repository-security-workflow-observation.md`, `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`, `docs/phase-3-1-sync-log.md`, checker coverage | checking when a bounded workflow result or workflow-observation boundary changed |
| Phase planning | `ROADMAP.md`, roadmap note, progress map, current snapshot, operation index, current task inventory | confirming a past phase milestone |
| Audit, error investigation, or retrospective explanation | `CHANGELOG.md`, sync logs, snapshots, relevant commits and artifacts | this is the intended primary use |

If the purpose does not match the document, change the reading path or update path before continuing.

## BEACON and snapshot roles

`BEACON.md` and current snapshots are complementary but separate.

Use `BEACON.md` as the reconnection entrance:

- current focus
- read-first order
- restart pointer
- short boundary reminders
- compact continuity signal across sessions

Use the current phase snapshot as the detailed current-state record:

- current artifacts
- current synchronization state
- observed bounded checks
- detailed deferred boundaries
- next low-risk work
- stop conditions
- restart details

Do not let `BEACON.md` become a full snapshot or a second changelog.

Do not let a current snapshot replace the short reconnection role of `BEACON.md`.

When BEACON grows too large, preserve detailed state in the relevant snapshot, sync log, roadmap note, checker coverage, example index, or progress map, then keep BEACON focused on reconnection.

## Root README role

`README.md` is the short public entrance.

Use it for:

- compact project definition
- why the project matters
- short provenance entry
- non-certifying boundary reminder
- primary reader links

Do not let root `README.md` become the full documentation body.

Expanded previous README content is preserved at `docs/readme-expanded.md` so that the root README can remain mobile-renderer friendly.

## Operation documents

| Document | Use when |
| --- | --- |
| `docs/repository-operation-model.md` | You need the current repository-wide operating model, document purpose and usage phase policy, staged update operation, synchronization unit operation, session load and handoff policy, commit granularity policy, periodic operation review policy, long-file update policy, workflow observation policy, sync-log and roadmap-note separation policy, or restart rule. |
| `docs/current-task-inventory.md` | You need the current P0-P4 task inventory across active and near-active phases before selecting the next task. |
| `docs/social-connection-review-navigation.md` | You need the focused reader path for social-connection review involving approval skip, responsibility transfer, evidence logging, explanation paths, affected-party visibility, or later review, dispute, repair, or return paths. |
| `docs/repository-pathway-gap-inventory.md` | You need to track structure breaks, reader-path gaps, social-connection cluster links, or large-index update risks before broad navigation changes. |
| `docs/ai-judgment-node-task-control.md` | You need the bounded concept and operation boundary for AI Judgment Nodes, task-control loops, stop conditions, evaluator separation, evidence visibility, judgment versus execution, and human or institutional return gates. |
| `docs/phase-3-1-ai-judgment-node-connection.md` | You need the focused Phase 3.1 reader-path connection for AI local judgment and task-control boundaries without rewriting the full current snapshot. |
| `docs/phase-3-1-ai-judgment-node-sync-note.md` | You need the focused synchronization record for the AI Judgment Node task-control boundary unit. |
| `docs/external-review-readiness-checklist.md` | You need to inspect whether the repository is readable enough for external review without treating readiness as certification, conformance, correctness, production approval, or public standardization. |
| `docs/external-review-package-note.md` | You need a compact external-review reader package, suggested reviewer questions, non-readiness boundaries, and reviewer handoff path without treating it as an endorsement or certification package. |
| `docs/zenn-publication-readiness-plan.md` | You need Zenn publication levels, article gates, required documents, stop conditions, or safe public article scope before drafting or publishing public-facing Zenn material. |
| `docs/zenn-publication-readiness-connection.md` | You need the focused connection between Zenn publication planning, public-entry documents, external-review readiness, future API preview, external product survey, and deferred-work boundaries. |
| `docs/zenn-publication-ja-reader-note.md` | You need a short Japanese reader path for readers arriving from Zenn or other Japanese public articles. |
| `docs/connector-target-matrix.md` | You need candidate external system categories, observable events, candidate RPE mapping focus, first safe synthetic forms, and deferred connector boundaries before choosing any connector target. |
| `docs/connector-target-matrix-connection.md` | You need the focused connection between connector target planning, API future-shape planning, external product survey observations, adapter boundary, and deferred-work restart conditions. |
| `docs/event-to-pathway-relation-checker-plan.md` | You need the future event-to-pathway relation checker plan before considering any relation checker implementation or event-to-pathway structural relation check. |
| `docs/repository-security-workflow-observation.md` | You need the first observed bounded repository security hygiene workflow result and its non-certifying interpretation. |
| `docs/progress-map.md` | You need rough progress estimates, gate status, next gates, recommended order, or progress-related stop conditions. |
| `docs/development-process.md` | You need the standard work cycle for concept, definition, specification, example, checker, or formalization work. |
| `docs/repository-governance.md` | You need the governance principles that preserve return paths from claims to definitions, specifications, formalization, and assumptions. |
| `docs/operation-tool-selection-guard.md` | You need to choose the correct GitHub read/write tool during AI-assisted maintenance, especially after a read-tool selection mistake. |
| `docs/operation-improvement-log.md` | You need durable records of repeated operation drift, recovery-path improvements, future operation behavior changes, or maintenance lessons that should not remain hidden. |
| `docs/focused-note-reconnection-rule.md` | You need the reconnection ladder, orphan-prevention checklist, or recovery-path requirement for focused notes, companion notes, connection notes, or escape notes. |
| `docs/assistant-pathway-maintenance-checklist.md` | You need assistant-side in-session maintenance checks before new responsibility units, after blocked writes, after focused-note creation, after repeated tool drift, or when document count and boundary repetition grow. |
| `docs/document-redundancy-review-plan.md` | You need the low-risk method for reviewing document overlap, duplication, navigation sprawl, or unclear authoritative reader paths without immediately merging, deleting, renaming, or rewriting documents. |
| `docs/document-redundancy-review-findings-operation-rules.md` | You need the first findings note for operation-rules and operation-guards redundancy review, including initial role classification and why merge/delete is not yet appropriate. |
| `docs/document-redundancy-review-findings-checker-plans.md` | You need the findings note for checker coverage and checker-plan redundancy review, including current coverage versus future plan separation. |
| `docs/document-redundancy-review-findings-operation-logs.md` | You need the findings note for operation-log, improvement-log, sync-log, and workflow-observation redundancy review, including durable lessons versus phase/state records. |
| `docs/responsibility-pathway-availability.md` | You need to classify a narrowed, incomplete, noisy, or temporarily broken responsibility pathway and decide what residual evidence, missing evidence, uncertainty, and next judgment should be preserved or returned. |
| `BEACON.md` | You need the current reconnection entrance, compact read-first order, current focus, and restart pointer. |
| `README.md` | You need the short public entrance and primary reader links. |
| `docs/readme-expanded.md` | You need the previous expanded README content after root README lightweight recovery. |
| `ROADMAP.md` | You need phase-level direction, next low-risk work, phase rules, or deferred work. |
| `CHANGELOG.md` | You need archival milestones, serious error investigation support, historical cause tracing, or retrospective explanation of when and why a boundary or policy changed. |

## Concept navigation

Use `docs/concepts/index.md` when concept-level documents or reader paths matter.

Current concept-navigation anchors include:

- `docs/concepts/core-elements.md`
- `docs/concepts/support-call-policy.md`
- `docs/concepts/missed-support-review-signal.md`
- `docs/related-work/strategic-decision-support.md`
- `docs/examples/missed-support-current-status.md`

Concept notes remain concept-level unless restart conditions explicitly reopen schema, checker, workflow, runtime, connector, or Lean work.

## AI local judgment and task-control navigation

Use `docs/ai-judgment-node-task-control.md` when discussing whether an AI system is only a support node or also acts as a local judgment node inside a Responsibility Pathway.

Use `docs/phase-3-1-ai-judgment-node-connection.md` when Phase 3.1 runtime-event, adapter-boundary, loop-like task control, goal-like stop condition, evaluator separation, evidence-selection, continuation, retry, escalation, or human-return discussions need a focused reader path.

Use `docs/phase-3-1-ai-judgment-node-sync-note.md` when reviewing the synchronization unit that added the AI Judgment Node concept and its Phase 3.1 connection.

These notes do not authorize autonomous task-control implementation, automatic approval, automatic execution, schema expansion, checker expansion, workflow expansion, production connectors, production runtime integration, conformance checks, Lean expansion, or AI final-responsibility transfer.

## Social connection review navigation

Use `docs/social-connection-review-navigation.md` when approval skip, responsibility transfer, evidence logging, explanation paths, affected-party visibility, or later review, dispute, repair, or return paths are reviewed in real social contexts.

Use `docs/repository-pathway-gap-inventory.md` when social-connection review documents or other focused notes may be disconnected from the primary reader path.

These notes do not decide legal liability, social acceptability, compliance, safety, fairness, certification, production readiness, conformance, or AI final-responsibility transfer.

## Standardization navigation

Use `docs/standardization-strategy.md` when discussing world-standard preparation, external standardization language, grounding discipline, anti-overclaim boundaries, relationship to existing standards and frameworks, future conformance discussion, or whether a claim should be deferred.

The standardization strategy positions RPE as an open specification effort and future standardization candidate preparation, not as a finished standard, certification scheme, legal authority, safety certification process, compliance framework, production approval process, connector correctness proof, runtime correctness proof, or AI final-responsibility transfer mechanism.

Use this document before writing public-facing claims that may sound like certification, legal validity, safety proof, compliance proof, production readiness, connector correctness, runtime correctness, or AI final-responsibility transfer.

## Progress navigation

Use `docs/progress-map.md` when the question is how far the repository has progressed, which gate is active, what the next gate is, or which work must remain deferred.

Use `docs/phase-3-1-progress-map-connection.md` when progress visibility specifically concerns Phase 3.1 and the maintainer needs the focused reader path without rewriting the full Phase 3.1 snapshot.

The progress map records approximate planning estimates only. It does not certify progress, prove maturity, establish conformance, or replace external review.

Use it to avoid both false urgency and premature standardization claims.

## External review navigation

Use `docs/external-review-package-note.md` when preparing a compact handoff package for an external reviewer.

Use `docs/external-review-readiness-checklist.md` when preparing for external review or asking whether reviewers can inspect the repository without mistaking it for certification, conformance evidence, production readiness, or finished standardization.

The checklist should be used before expanding public-facing review claims, external-review package notes, conformance-model drafting, or standardization language.

Neither the package note nor the readiness checklist is a substitute for external review findings. They are navigation, readiness, and non-readiness notes only.

## Zenn publication navigation

Use `docs/zenn-publication-readiness-plan.md` when deciding what can safely be published on Zenn and what publication level is supported by the repository state.

Use `docs/zenn-publication-readiness-connection.md` when connecting Zenn publication planning to public-entry documents, external-review readiness, future API or connector previews, external product connection-surface observations, and deferred-work boundaries.

Use `docs/zenn-publication-ja-reader-note.md` when Japanese public readers need a short reading route from Zenn or other Japanese-facing articles into the repository.

Zenn publication planning is not an external review result, certification package, conformance package, standardization claim, production approval, or implemented API / connector announcement.

## Connector target navigation

Use `docs/connector-target-matrix.md` when choosing or comparing future external system categories for connector-adjacent modeling.

Use `docs/connector-target-matrix-connection.md` when connecting connector target planning to API future-shape planning, external product connection-surface observations, adapter-boundary notes, and deferred-work restart conditions.

Connector target planning is not connector implementation, external service integration, production runtime integration, conformance evidence, certification evidence, correctness proof, or final-responsibility transfer.

## Event-to-pathway relation checker planning

Use `docs/event-to-pathway-relation-checker-plan.md` before considering any checker that compares a runtime-event JSON fixture with a pathway YAML example.

The plan defines structurally checkable relation signals such as source-reference preservation, review requirement preservation, evidence and missing-context preservation, actor and responsibility-boundary preservation, excluded-claim preservation, and lifecycle compatibility.

It does not authorize implementation by itself. It should be read before any future event-to-pathway relation checker work, schema expansion, semantic checking, adapter mapping check, runtime correctness check, or conformance language.

## Task inventory navigation

Use `docs/current-task-inventory.md` when selecting the next repository task or checking active P0-P4 priorities.

The inventory is not a roadmap, guarantee, commitment, certification, conformance plan, legal plan, compliance plan, production plan, or AI final-responsibility transfer.
