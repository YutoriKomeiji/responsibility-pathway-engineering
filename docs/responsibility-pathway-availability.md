# Responsibility Pathway Availability

This note defines responsibility pathway availability as an operation concern for this repository.

It exists because a responsibility pathway may become narrow, incomplete, noisy, or temporarily broken during real maintenance work. The repository should not hide that condition, and it should not claim completeness when the available pathway is degraded.

This note is an operation note only. It is not a certification process, legal review, safety review, compliance review, production approval, connector correctness proof, runtime correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.

## Definition

Responsibility pathway availability means that, when judgment, review, repair, audit, restart, or explanation is needed, a maintainer can still reach enough responsibility-pathway information to understand:

- what is known,
- what was changed,
- what evidence remains,
- what evidence is missing,
- what uncertainty remains,
- what decision is needed next,
- who or what decision process should receive that decision.

Availability is not the same as completeness.

A highly available pathway may still be incomplete. An incomplete pathway may still be useful if the remaining information, missing information, uncertainty, and next judgment point are explicit.

## Degraded pathway states

A responsibility pathway may degrade when:

- a tool or connector behaves unexpectedly,
- a read or write surface changes,
- a session becomes overloaded,
- a log is incomplete,
- a workflow result is unavailable or unobserved,
- a file update is blocked or risky,
- a long file cannot safely be rewritten,
- a maintainer must continue under time, permission, or context constraints,
- an AI-assisted step drifts from the intended operation path.

These conditions do not automatically invalidate all work.

They require the pathway state to be classified before further claims, writes, or public-facing interpretations are made.

## Minimum preservation rule

When the pathway is degraded, preserve the smallest useful state before continuing:

1. what operation was intended,
2. what actually happened,
3. whether repository content changed,
4. which file content, blob SHA, line range, commit, workflow result, or artifact remains available,
5. which expected evidence is missing or unobserved,
6. whether the work can safely continue,
7. what judgment should be returned to the human maintainer or explicit decision process.

This rule favors recoverability over pretending that the pathway remained complete.

## Judgment return rule

When availability is degraded, do not let an AI-assisted maintenance step silently decide that the missing information does not matter.

Return the decision when the next step depends on a priority choice such as:

- continue work with explicit uncertainty,
- stop and preserve state,
- restore or re-fetch evidence,
- defer the change,
- roll back or repair,
- ask for human judgment,
- ask a designated judgment process to choose the priority.

The AI-assisted step may propose options, but it must not convert a degraded pathway into a completeness claim.

## Relationship to other pathway qualities

Use these distinctions:

- availability: whether enough responsibility-pathway information can be reached when needed,
- reachability: whether the evidence path can be followed to specific records, files, lines, commits, or artifacts,
- completeness: whether expected evidence is present and not missing,
- recoverability: whether a degraded or broken pathway can be repaired or narrowed into a usable state,
- continuity: whether the pathway remains understandable across time, sessions, tools, maintainers, and AI-assisted work.

These qualities can diverge.

For example, a pathway may be available but incomplete, reachable but noisy, recoverable but not yet repaired, or continuous across sessions while still missing a specific evidence item.

## Tool-discovery recurrence example

A read-only tool-discovery recurrence during known GitHub file work is a degraded-pathway signal, not automatically a content failure.

If no repository content changed, the discovery result is not used as write grounding, and the next operation returns to a direct GitHub file operation, the pathway remains recoverable.

If the recurrence repeats, changes the basis for a write, hides which file or blob SHA grounded the change, or makes later review harder, it becomes operation noise that should be recorded in the relevant operation note or sync log.

## Boundary

This note does not make degraded pathways acceptable for certification, legal validity, safety, compliance, fairness, production readiness, connector correctness, runtime correctness, Lean completeness, public standardization claims, or AI final-responsibility transfer.

It only says that degraded pathway states should be made visible, preserved where possible, and returned to the responsible maintainer or decision process when priority choices are required.

The human author or maintainer remains responsible for deciding whether work under a degraded pathway should continue, stop, be repaired, be reverted, be published, or be deferred.
