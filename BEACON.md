# BEACON

If you are reading this for the first time, you are not late.

This repository preserves a Responsibility Pathway across time, people, sessions, and AI systems.

BEACON is the short reconnection entrance. Use the repository's current implementation, roadmap, assurance, and review surfaces for their respective evidence and decision roles; BEACON itself is only the routing surface back into them.

## Current position

RPE's current public engineering surface is the **M2 governed-integration line**.

The strict governed path is exposed through Python, REST, MCP stdio, and OpenAPI and includes:

- governed-envelope admission;
- contract compatibility;
- exact Requirement Pack / governance binding;
- governance eligibility;
- applicability and requirement evaluation;
- explicit `allow`, `hold`, `human_gate`, and `deny` outcomes;
- stable reason codes and Human Return;
- responsibility-preserving handoff with `authority_effect = none` and `decision_scope = evaluation_only`;
- bounded caller-content / local-file loading;
- repository/package/runtime parity checks and adversarial failure checks.

The legacy `evaluate_action()` path remains available for compatibility. The explicit strict path is `evaluate_governed_action()`.

For current implementation state, use:

- `README.md` — compact public engineering entrance;
- `READMEforAI.md` — grounded AI/search-reader entrance;
- `docs/m2-governed-integration-current.md` — current M2 implementation boundary;
- `docs/m2-r5-adversarial-closure-evidence.md` — bounded closure evidence;
- `ROADMAP.md` — current planning/gate state.

Do not use the earlier M1 or Phase 3.1 construction records as the current maturity label. They remain historical or specialized evidence.

Current scope remains bounded. RPE evaluates proposals and preserves responsibility handoff; it does not become the downstream execution authority, external-effect verifier, production deployment, legal/compliance determination, or universal safety proof.

## Read first

1. `README.md` or `README.ja.md`
2. `READMEforAI.md` for a grounded AI/search-reader entrance
3. `scripts/demo.py` for the canonical-kernel walkthrough
4. `rpe_kernel/pipeline.py` for the shared decision entry point
5. `docs/verification-assurance-and-open-governance.md` for proof, assurance,
   public-guidance, and open-governance boundaries
6. Published Artifact Catalog: <https://yutorikomeiji.github.io/responsibility-pathway-engineering/>
7. `ROADMAP.md` for the current M2 planning and gate state
8. `docs/operation-index.md` for repository operation and historical construction paths
9. `docs/phase-3-1-current-snapshot.md` when the earlier Phase 3.1 construction state matters
10. `docs/current-task-inventory.md` when tracing earlier task state
11. `docs/overview.md` when external readers need the broader repository map
12. `docs/zenn-level-2-repository-walkthrough-readiness.md` when preparing a Level 2 repository walkthrough article
13. `docs/zenn-publication-readiness-plan.md` before drafting or publishing Zenn-facing public articles
14. `docs/ai-judgment-node-task-control.md` when AI local judgment, task-control loops, stop conditions, or evaluator separation matter
15. `docs/phase-3-1-ai-judgment-node-reader-path-status.md` when the earlier AI Judgment Node reader path matters
16. `docs/phase-3-1-ai-judgment-node-sync-note.md` when the focused AI Judgment Node synchronization unit matters
17. `docs/runtime-event-schema-fixture-alignment.md` when schema/fixture/checker alignment matters
18. `docs/event-to-pathway-relation-checker-plan.md` when future relation-checker planning matters
19. `docs/runtime-event-workflow-current-status.md` when workflow observation matters
20. `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md` when the focused sync-log supplement matters
21. `docs/phase-3-1-sync-log.md`
22. `docs/phase-3-1-roadmap-note.md`
23. `docs/phase-3-1-roadmap-sync-after-readme-recovery.md`
24. `docs/progress-map.md` for rough progress, gates, next gates, and stop conditions
25. `docs/phase-3-1-progress-map-connection.md` when Phase 3.1-specific progress visibility matters
26. `docs/responsibility-pathway-availability.md` when the responsibility pathway is narrowed, incomplete, noisy, or temporarily broken
27. `docs/concepts/index.md`
28. `docs/repair-model.md` and `docs/recovery-pathway-reading.md` when repair or recovery-pathway reading matters
29. `docs/standardization-strategy.md` before expanding world-standard or conformance language
30. `docs/zenn-publication-readiness-connection.md` when connecting Zenn publication planning to public-entry and review-reader paths
31. `docs/connector-target-matrix.md` when choosing future connector target categories before any implementation
32. `docs/connector-target-matrix-connection.md` when connecting connector targets to API future-shape and external product survey notes
33. `docs/example-index.md`
34. `docs/checker-coverage.md`
35. `CHANGELOG.md` only when historical cause tracing or milestone review is needed

Use `docs/repository-operation-model.md` before broad reader-path synchronization, long-file updates, session handoff, or periodic operation review.

## Current focus

- Keep `README.md` and `README.ja.md` short, aligned, and mobile-reader friendly.
- Keep the published Pages reader paths connected as convenience reader and inspection aids without treating them as validation, certification, or production approval.
- Keep detailed README content in `docs/readme-expanded.md`.
- Keep examples small, readable, and non-certifying.
- Keep repair and recovery-pathway reading connected without implying harm elimination, full recovery, certification, legal validity, safety, compliance, fairness, or production readiness.
- Keep AI Judgment Node task-control language bounded: local AI judgment is pathway-relevant, but it is not final responsibility, verification, certification, safety proof, runtime correctness, or AI final-responsibility transfer.
- Keep progress estimates rough, planning-only, and non-certifying.
- Keep standardization strategy grounded, complementary to existing frameworks, and non-certifying.
- Keep public Zenn publication language explanatory, review-oriented, and boundary-aware; do not treat it as standardization, certification, production readiness, external-review approval, or implemented API / connector announcement.
- Keep conversation-derived material out of the public reader path unless it has a clear RPE-repository role and reader path.
- Keep support-call and missed-support semantics concept-level until deliberately stabilized.
- Keep the current bounded runtime-event checker and workflow observations documented as structural repository-maintenance signals only.
- Keep runtime-event schema/fixture alignment visible without treating it as validation.
- Keep event-to-pathway relation checker planning visible without treating it as current checker behavior or implementation permission.
- Keep API and connector documents as future-shape or connection-surface planning until restart conditions explicitly reopen implementation.
- Keep connector target matrix work synthetic-first and non-implementation until a separate restart review explicitly reopens connector work.
- Keep further runtime-event schema checking, broader JSON fixture checking, event-to-pathway semantic checking, and further runtime fixture checking deferred unless deliberately reopened.
- Keep service-specific connectors and production runtime integration deferred.
- Keep Lean expansion around adapter, runtime-event, support-call, or missed-support concepts deferred.
- Keep Class E positive examples deferred.
- Preserve restartability through operation-index, current snapshots, sync logs, focused sync notes, roadmap notes, progress map, and short changelog milestones.

## Recent bounded check observations

- `Check review-result fixtures #1` observed green on commit `aaaece3`.
- `Check examples #14` observed green on commit `caf285b` for the Class D reversible external action fixture.
- `Check examples #16` observed green on commit `d377be2` for the runtime-event-to-pathway draft example after structural repair.
- `Check examples #17` observed failed on commit `57445b1` because the missed-support example declared `lifecycle_state: returning` without a top-level `returning` block.
- `Check examples #18` observed green on commit `f63678c` after the top-level `returning` block was added.
- `Check runtime events` observed green on run `27501847137` for the first minimal runtime-event workflow.
- `Check runtime events` observed green on run `27607798655` after `examples/minimal-synthetic-runtime-fixture.json` was added to bounded runtime-event checker coverage.

All observed green statuses are bounded repository-maintenance signals only. They are not certification, legal validation, safety validation, compliance validation, fairness validation, moral resolution, production approval, connector correctness proof, runtime correctness proof, schema validation, JSON semantic correctness proof, adapter mapping correctness proof, support-call semantic validation, missed-support correctness validation, Lean completeness proof, standardization certification, progress certification, or AI final-responsibility transfer.

## Do not start yet

Do not start the following without satisfying the relevant restart conditions and reading the current plans first:

- service-specific connectors
- production conversion code
- production runtime integration
- runtime-event schema checker
- broader JSON schema-fixture checker
- further runtime fixture checker beyond the selected minimal synthetic runtime observation fixture
- event-to-pathway relation checker implementation
- event-to-pathway semantic checker
- action-class-specific checker enforcement
- support-call schema fields
- missed-support schema fields
- support-call semantic checker
- missed-support correctness checker
- runtime-event support-call fields
- Class E positive examples
- Lean expansion around adapter, runtime-event, support-call, or missed-support concepts
- conformance-model drafting or public standardization claims before `docs/standardization-strategy.md` conditions are satisfied

## Operating rule

Small commits.
Verified definitions.
Incremental formalization.

Definitions precede proofs.
Proofs precede claims.
Claims precede applications.

The human author or maintainer remains responsible for deciding whether a change should be made, published, relied upon, reverted, repaired, or deferred.
