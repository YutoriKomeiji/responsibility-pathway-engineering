# Issue Body Warning Checker Plan

This note records a future plan for a warning-only checker over created GitHub issue bodies that use the AI-assisted work Responsibility Pathway Issue Form.

## Purpose

The existing Issue Form checker verifies the Issue Form definition. It does not validate the contents of issues created from that form.

A future issue-body checker may help maintainers notice missing or weak Responsibility Pathway signals in filled issue bodies before review, repair, or follow-up work proceeds.

## Intended status

The future checker should start as warning-only.

Warning-only means:

- it may print warnings for missing or weak fields
- it should not fail CI by default
- it should not block issue creation
- it should not close, edit, label, approve, reject, or assign issues automatically
- it should not decide whether the issue is correct, complete, safe, compliant, fair, legally valid, production ready, externally reviewed, socially accepted, certified, conformance-ready, or responsibility-resolving

## Candidate warning signals

A future checker may warn when a created issue body appears to omit or weaken selected RPE signals such as:

- source reference
- work context
- AI assistance role
- AI assistance boundary
- missing context or uncertainty
- evidence log
- evidence observation timestamp such as `observed_at`
- evidence recording timestamp such as `recorded_at`
- evidence timezone such as `timezone`
- human or institutional review point
- responsibility return point
- repair / reopening path
- non-final-AI responsibility boundary
- explicit non-claim acknowledgement

These warnings should be treated as prompts for human review, not as automatic judgments.

Timestamp warnings should only indicate that the time-order review path may be weak. They must not claim that the evidence is false, stale, invalid, complete, incomplete, legally insufficient, unsafe, non-compliant, unfair, or responsibility-resolving.

## Non-goals

The checker must not claim to validate:

- the truth of the issue body
- the quality of evidence
- the completeness of timestamps
- the correctness of timestamps
- time-zone correctness
- chronological consistency
- the sufficiency of review
- reviewer authority
- legal validity
- safety
- compliance
- fairness
- production readiness
- social acceptance
- certification
- conformance readiness
- final responsibility assignment
- AI final-responsibility transfer

## Possible input sources

Possible future input sources include:

- a saved issue body fixture in the repository
- an exported issue body used for local testing
- a GitHub issue body fetched in a controlled maintainer-side workflow

The first implementation should prefer local fixtures before live GitHub issue reads.

## Possible implementation route

A minimal future route could be:

1. Add one local fixture representing a filled issue body.
2. Add a local warning-only script such as `scripts/check_issue_bodies.py`.
3. Keep the script exit code `0` when only warnings are found.
4. Print warnings with stable labels so maintainers can inspect them.
5. Document that warnings are review prompts only.
6. Add workflow automation only after the local warning behavior is stable.

## Boundary

This is a planning note only.

No issue-body checker is implemented by this note. No workflow is added by this note. No live issue access is introduced by this note.

A future warning-only pass must remain a repository-maintenance signal only. It must not be treated as certification, legal review, safety review, compliance review, fairness review, production approval, conformance evidence, social acceptance proof, timestamp correctness proof, chronological correctness proof, or AI final-responsibility transfer.
