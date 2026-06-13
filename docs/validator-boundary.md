# Validator Boundary

This document defines the boundary for lightweight validation tools in this repository.

The current bounded checkers are:

- `scripts/check_examples.py`
- `scripts/check_review_results.py`

## Purpose

The checkers are intended to help maintain repository examples and fixtures by detecting missing structural fields, lifecycle-specific structural signals, review-result structural fields, and responsibility-boundary signals.

They support repository maintenance. They do not certify examples, fixtures, records, review results, systems, organizations, workflows, decisions, deployments, action classes, or real-world responsibility outcomes.

## Checker scopes

### `scripts/check_examples.py`

`scripts/check_examples.py` checks pathway examples under `examples/*.yaml`.

It may inspect whether example YAML files contain:

- required top-level keys
- non-empty node lists
- edge lists
- human return-point signals
- AI final responsibility boundary fields
- formalization-scope exclusion signals
- lifecycle-specific structural signals for `originating`, `repaired`, `suspended`, `returning`, and `closed`
- lifecycle-specific structural blocks such as `suspension`, `returning`, and `closure`
- lifecycle-specific boundary signals such as human decision-owner capacity, repair-record presence, automatic-continuation disallowance, reopening-condition records, closure-basis records, and disallowed-interpretation lists
- optional `review_metadata` structure when present

Current action-class boundary:

- `scripts/check_examples.py` does not yet enforce the full Class A-F Action Class Matrix requirement map.
- Existing examples are not retroactively required to satisfy action-class-specific rules unless deliberately migrated.
- `examples/action-class-matrix-minimal.yaml` is a classification-only fixture and should remain low impact.

Future bounded action-class checks may inspect structural signals such as:

- declared `source_aligned_class`
- Class C or higher Approval Gate presence
- Class D or higher rollback or repair path presence
- Class E high-impact and non-autonomous boundary language
- Class F stop trigger, Stop Authority, pending responsibility owner, and restart/return fields

Such future checks must remain bounded repository-maintenance checks.

### `scripts/check_review_results.py`

`scripts/check_review_results.py` checks review-result fixtures under `fixtures/review-results/*.yaml` against `spec/review-result.schema.yaml`.

It may inspect whether review-result fixture YAML files contain:

- YAML parseable structure
- top-level mapping structure
- schema-defined required fields
- allowed `review_scope` values
- allowed `review_status` values
- non-empty `checked_items`
- expected `not_checked` boundary items
- expected `not_claimed` boundary items
- expected `responsibility_boundary` flags

A passing review-result checker result means only that the fixture preserves the bounded structure and responsibility-boundary fields required by the current review-result schema.

It does not mean that the reviewed workflow, organization, system, decision, deployment, record, or real-world responsibility outcome is valid, safe, compliant, fair, complete, morally resolved, certified, approved, or ready for production use.

## GitHub Actions boundary

The repository currently includes bounded GitHub Actions workflows for repository-maintenance checks.

Observed green workflow status means only that the relevant bounded checker completed successfully for the files in that run.

For example, the `Check review-result fixtures` workflow was observed green for run `#1` on commit `aaaece3` on `main`. That observed green status means only that the bounded review-result fixture checker passed for that repository state.

The `Check examples` workflow has also been used to observe bounded structural example checks. Observed green status for examples means only that the current example checker passed for the repository state in that run. It does not certify the examples or their action classes.

It does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional approval, production readiness, real-world responsibility resolution, or AI final-responsibility transfer.

## What the checkers do not check

The checkers do not determine:

- legal validity
- regulatory compliance
- safety
- fairness
- moral accountability
- production readiness
- institutional certification
- real-world responsibility resolution
- real-world harm elimination
- semantic completeness
- operational correctness
- whether an action class is sufficient for a real-world setting
- whether a lifecycle transition is appropriate in a real-world setting
- whether a review result is a legal, safety, compliance, fairness, moral, institutional, or production approval result
- whether closure, repair, suspension, return, continuation, or originating state is justified outside the declared example scope

## Output language

Checker output should remain conservative.

Allowed terms include:

- `PASS: required key present`
- `PASS: lifecycle block present`
- `PASS: lifecycle rule applied`
- `PASS: bounded review-result checks completed without failures`
- `PASS: bounded action-class structural signal present`
- `WARN: optional or weak signal missing`
- `FAIL: required boundary missing`
- `bounded structural checks`
- `bounded repository-maintenance checks`

Avoid terms such as:

- `certified`
- `safe`
- `compliant`
- `fair`
- `legally valid`
- `morally resolved`
- `production ready`
- `approved for use`
- `verified as correct in the real world`
- `action class certified`

## Interpretation

A passing checker result only means that the checked file satisfied the limited structural rules implemented by that checker version.

For lifecycle-aware checks, a passing result only means that the declared lifecycle state has the expected structural signals in the example file. It does not mean that originating, suspension, return, repair, closure, reopening, or continuation would be correct or justified in any real-world context.

For action-class-related checks, a passing result would only mean that the declared action class has the expected structural signals in the example file. It would not mean that the action class is sufficient, safe, legally valid, compliant, fair, morally resolved, institutionally approved, or production ready.

For review-result fixture checks, a passing result only means that the fixture preserves the current required review-result structure, not-checked boundaries, not-claimed boundaries, and responsibility-boundary flags.

A passing result does not mean that the example, fixture, record, review result, workflow, system, organization, decision, deployment, or action class is complete, correct in all contexts, ethically valid, legally valid, safe, fair, compliant, certified, approved, or ready for production use.

## Responsibility boundary

The checkers are maintenance aids.

The human author or maintainer remains responsible for deciding whether an example, fixture, schema, document, checker result, workflow result, or public claim should be changed, published, or relied upon.

AI tools may assist with checker implementation and review, but they are not authors, responsibility holders, legal actors, moral agents, or final decision-makers.

## Future validators

Future validators may become stricter, but each validator should continue to state:

- what it checks
- what it does not check
- what assumptions it uses
- what claims are excluded
- whether the validator is manually run, CI-run, or both

No validator in this repository should imply legal, moral, safety, fairness, compliance, certification, approval, action-class sufficiency, or production-readiness conclusions unless that scope is explicitly defined and justified in a future phase.
