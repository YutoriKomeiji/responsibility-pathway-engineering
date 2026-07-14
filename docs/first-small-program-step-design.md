# First Small Program Step Design

This note defines the first small program step after the initial GitHub Pages reader-aid set.

The purpose is to move from static reader aids toward a bounded local helper without turning Phase 3.1 into connector work, production runtime integration, automatic approval, automatic execution, semantic responsibility checking, or conformance evidence.

This note is planning-only. It is not certification, validation, conformance, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, adapter correctness proof, runtime correctness proof, schema correctness proof, checker correctness proof, or AI final-responsibility transfer.

## Current trigger

The first browser-facing Pages reader-aid pair now exists:

- `site/example-browser/index.html`
- `site/template-helper/index.html`

The next program step should help maintain repository reviewability after those site additions.

## Candidate helper

The first small local helper should be a **site source-reference consistency helper**.

Possible path:

- `scripts/check_site_links.py`

Possible workflow path, only after local behavior is observed:

- `.github/workflows/check-site-links.yml`

## Intended scope

The helper may inspect local static files under `site/` and check simple repository-relative references such as:

- links from `site/catalog.js` to local Pages reader aids
- links from `site/example-browser/index.html` to `examples/*.yaml` or `examples/*.json`
- links from `site/template-helper/index.html` to `templates/*.yaml` and selected `docs/*.md`

The helper may report missing local files, malformed local paths, or unexpected source-reference drift.

## Explicit non-scope

The helper must not check or claim:

- deployed Pages availability
- external URL availability
- HTTP correctness
- browser rendering correctness
- accessibility correctness
- semantic correctness of examples
- YAML or JSON schema validity
- runtime-event schema completeness
- adapter mapping correctness
- responsibility assignment correctness
- connector correctness
- runtime correctness
- legal validity
- safety
- compliance
- fairness
- production readiness
- conformance
- AI final-responsibility transfer

## Relationship to existing checkers

Existing checkers remain separate:

- `scripts/check_examples.py` checks bounded structural signals in selected pathway examples.
- `scripts/check_runtime_events.py` checks bounded structural signals in selected synthetic runtime-event JSON fixtures.

The first site helper should not replace or reinterpret either checker.

A future site helper pass, if implemented, must mean only that selected local site links or source references are present and locally resolvable.

## Implementation order

Recommended order:

1. Create this design note.
2. Add a tiny local script that checks selected repository-relative site links only.
3. Run it locally and record the observation in a short note if useful.
4. Add a workflow only after the local script behavior is stable.
5. Update `docs/checker-coverage.md` only if the helper becomes a maintained checker surface.

## Stop conditions

Stop before implementation if the helper proposal:

- fetches the public website
- depends on network access
- checks external URLs
- makes deployed Pages status look like approval
- claims rendering, accessibility, schema, semantic, runtime, adapter, connector, legal, safety, compliance, fairness, production, or conformance correctness
- mixes site-link checking with example semantic checking
- expands into service-specific connector work
- expands into production runtime work

## Next safe step

Implement at most one tiny local script for selected `site/` source references.

Do not add a workflow in the same step unless the maintainer deliberately chooses to combine them after reviewing the local helper scope.
