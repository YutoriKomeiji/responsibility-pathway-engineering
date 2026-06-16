# AI Agent Operation Patterns for Repository Maintenance

This note records a practical operating pattern for AI-assisted repository maintenance in this project.

It is an operations note only. It does not introduce schema changes, checker changes, workflow changes, runtime connectors, production runtime, or Lean formalization.

## Core pattern

AI-assisted repository work should be organized as small, auditable maintenance units.

A safe unit should have:

- a stated purpose
- a bounded file set
- a small diff
- a commit message that matches the work
- a post-hoc audit path
- an explicit boundary for what was not changed

## Human decision boundary

The human maintainer remains the decision owner for:

- what task is authorized
- what scope is acceptable
- what is merged or relied on
- what is reverted or repaired
- what claims are allowed
- when deferred work may restart

The AI assistant may help draft, edit, organize, check, and summarize, but it does not become the final responsibility holder for repository changes.

## AI local judgment boundary

`docs/ai-judgment-node-task-control.md` records a bounded concept for AI Judgment Nodes and task-control boundaries.

Repository maintenance should distinguish final responsibility from intermediate AI operational judgment.

An AI assistant may act as a local judgment node when it selects a next step, recommends whether to continue or stop, chooses which evidence to present, classifies a task as low or high risk, or decides whether a condition appears satisfied.

That local judgment must not be treated as final responsibility, certification, correctness proof, safety proof, compliance proof, production approval, connector correctness proof, runtime correctness proof, or AI final-responsibility transfer.

When local AI judgment affects the task, the report or record should preserve the relevant evidence, missing evidence, selected action, boundary, and human return point.

## Preferred operation loop

Use this loop when possible:

1. Identify a small task.
2. Check the relevant roadmap, inventory, or restart-condition document.
3. Edit one narrow artifact or create one narrow companion note.
4. Fetch the changed file after writing.
5. Report the file, commit, and audit-relevant lines.
6. Leave broad synchronization or risky follow-up work deferred with restart conditions.

## Task classes

### Low-risk maintenance

Usually safe to proceed with post-hoc reporting:

- navigation notes
- provenance reader-path notes
- authorship and notice links
- small roadmap-alignment notes
- deferred-work restart-condition notes
- related-work notes that do not modify schemas or examples

### Medium-risk maintenance

Proceed only when the relevant roadmap or restart-condition document supports it:

- updating large navigation files
- updating task inventory
- connecting related-work notes to checker coverage or example index
- adding small boundary-only examples
- adding review notes

### High-risk work

Do not proceed without explicit restart conditions and usually a design note first:

- schema changes
- checker implementation
- workflow implementation
- runtime-event checking
- JSON fixture checking
- connector work
- production conversion code
- Lean theorem expansion
- high-impact positive examples

## Long-file rule

Long entry files such as `README.md`, `README.ja.md`, `BEACON.md`, `ROADMAP.md`, and `docs/operation-index.md` should not be rewritten broadly unless the change is necessary and easy to audit.

Prefer:

- a short reference
- a companion note
- a roadmap-alignment note
- a restart-condition note

Avoid:

- broad rewrites
- repeated detailed content
- mixing unrelated updates
- changing reader paths and technical scope in the same commit

## Deferred-work rule

If a task is deferred, record or reuse restart conditions.

Before restarting a deferred item, state:

- which deferred item is being restarted
- which restart conditions are satisfied
- which files show those conditions
- what remains out of scope
- why the change is small enough for audit

If those points cannot be stated, keep the item deferred.

## Reporting rule

For post-hoc audit, each report should include:

- changed file
- commit short SHA
- purpose
- boundary
- verification lines when available

The report should not claim certification, legal validity, safety, compliance, fairness, production readiness, connector correctness, runtime correctness, or AI final-responsibility transfer.

## Current relation to RPE

This operation pattern is itself a Responsibility Pathway:

- the human maintainer is the final decision owner
- the AI assistant is a support node
- the AI assistant may also be a local judgment node when it performs bounded task-control judgment
- commits and file fetches are evidence records
- restart conditions are stop and return rules
- deferred work preserves a future return point
- reports support post-hoc review

## Current status

This note documents current operation practice.

It does not authorize broader autonomous operation beyond the boundaries above.