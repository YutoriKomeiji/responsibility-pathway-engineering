# Current Parallel Work Plan

This note records the current parallel operating plan for repository organization and task progression.

It is a companion note to `docs/current-task-inventory.md`, not a replacement.

## Work tracks

### Track A: repository organization

Goal:

- keep authorship, provenance, navigation, restart conditions, and AI-assisted maintenance rules easy to audit.

Current artifacts:

- `docs/provenance.md`
- `docs/provenance-reader-path.md`
- `docs/deferred-work-restart-conditions.md`
- `docs/ai-agent-operation-patterns.md`
- `docs/roadmap-alignment-provenance-and-support.md`

Next safe actions:

1. Add only short references from long entry files when safe.
2. Keep long-file edits small.
3. Use companion notes when broad synchronization would be hard to audit.
4. Keep post-hoc audit reporting tied to file, commit, purpose, and boundary.

### Track B: task progression

Goal:

- continue roadmap-aligned work without unlocking schemas, checkers, runtime, connectors, or Lean before their restart conditions are satisfied.

Current active areas:

- provenance preservation and source-lineage traceability
- support-call policy as related work and concept-level mapping
- deferred-work restart conditions
- repository operation practice for AI-assisted maintenance

Next safe actions:

1. Map support-call policy to existing RPE concepts in a short concept note.
2. Keep missed-support as a future review signal only.
3. Keep schema and checker work deferred.
4. Update task inventory only when the new companion notes have stabilized.

## Do now

Safe to continue:

- focused companion notes
- short authorship or provenance references
- operation practice notes
- roadmap-alignment notes
- restart-condition notes

## Do not do yet

Do not start yet:

- support-call schema fields
- missed-support schema fields
- runtime-event checker implementation
- runtime-event workflow
- service-specific connectors
- production conversion code
- production runtime integration
- Lean expansion around runtime or support-call policy
- positive high-impact examples

## Audit rule

Each completed step should be reported with:

- file path
- commit short SHA
- what changed
- why it is in scope
- what remains deferred

## Current next candidate

The next useful small task is:

- create a support-call concept mapping note that connects strategic decision support to existing RPE concepts without changing schemas or examples.
