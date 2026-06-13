# Phase 3.1 Runtime Roadmap Reference

This short note records the ROADMAP reference that should be added after the minimal runtime fixture synchronization.

It exists because direct long-file roadmap updates should remain small and reviewable.

## Intended ROADMAP reference

Phase 3.1 now includes:

- `docs/minimal-runtime-candidate-design.md` as the boundary note before selecting a runtime candidate
- `examples/minimal-synthetic-runtime-fixture.json` as the first synthetic, local, non-production runtime-like observation fixture for reading and review
- `docs/phase-3-1-sync-log.md` as the detailed synchronization record for the runtime fixture reader-path update

## Boundary

The minimal synthetic runtime fixture is not a production runtime.

It is not a service-specific connector.

It is not a runtime workflow.

It is not a checker implementation.

It does not approve, execute, certify, or transfer final responsibility.

## Review intent

The fixture and its connected documents are intended to help future open-source reviewers inspect boundaries, responsibility paths, examples, schema assumptions, checker limits, runtime fixture limits, and deferred implementation choices.

Open-source review does not itself certify the repository or approve production use.

## Next use

Use this note when adding a short ROADMAP reference or when explaining why the ROADMAP should not be expanded into production runtime work yet.
