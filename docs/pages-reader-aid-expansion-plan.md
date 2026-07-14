# Pages Reader-Aid Expansion Plan

This note records the browser-facing GitHub Pages reader-aid expansion for Responsibility Pathway Engineering.

It existed before implementation so that Example browser and Template helper pages remained bounded reader aids rather than becoming certification, validation, implementation, or approval surfaces.

This plan is a planning and maintenance note only. It is not a certification record, conformance claim, external review finding, legal review, safety review, compliance review, fairness review, production approval, standardization claim, runtime correctness proof, connector correctness proof, schema correctness proof, checker correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.

## Current status

Initial implementation is complete.

The first browser-facing reader-aid pair now exists under `site/`:

- `site/example-browser/index.html`
- `site/template-helper/index.html`

The Artifact Catalog shelf has been connected to both pages through `site/catalog.js`.

These pages are still reader and inspection aids only. They do not replace repository Markdown files, source YAML or JSON files, planning notes, checker coverage notes, human review, external review, approval, validation, certification, or maintainer responsibility.

## Implemented reader aid 1: Example browser page

Purpose:

- help first readers find current example and fixture files from a browser
- group examples by reader purpose rather than by implementation maturity
- point back to source files and existing documentation
- make example boundaries easier to inspect

Source references:

- `docs/example-index.md`
- `docs/checker-coverage.md`
- `examples/minimal-pathway.yaml`
- `examples/action-class-matrix-minimal.yaml`
- `examples/internal-document-update.yaml`
- `examples/missed-support-boundary-minimal.yaml`
- `examples/reversible-external-action.yaml`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`

Required boundary:

The Example browser page must not imply that examples are certified, validated, production-ready, legally valid, safe, compliant, fair, complete, or approved for real-world use.

A browser page may summarize where an example is and how to read it, but source files and review notes remain the reference artifacts.

## Implemented reader aid 2: Template helper page

Purpose:

- help first readers find the first copyable template
- show the template's intended inspection role
- point back to source files and planning notes
- keep lightweight adoption distinct from implementation maturity

Source references:

- `templates/ai-assisted-work-responsibility-path.yaml`
- `docs/lightweight-durable-quality-implementation-strategy.md`
- `docs/public-adoption-and-fork-strategy.md`
- `docs/repository-construction-status-labels.md`
- `docs/zenn-level-2-repository-walkthrough-readiness.md`

Required boundary:

The Template helper page must not imply that a copied template creates a valid responsibility record, completes review, proves compliance, approves production use, or transfers final responsibility to AI.

A helper page may explain how to inspect the template shape, but it must preserve human and maintainer responsibility.

## Reader-path files to check after implementation

After adding either page, review whether updates are needed in:

- `README.md`
- `README.ja.md`
- `BEACON.md`
- `OPEN_CONSTRUCTION.md`
- `docs/operation-index.md`
- `docs/overview.md`
- `docs/progress-map.md`
- `docs/external-review-readiness-checklist.md`
- `docs/external-review-package-note.md`
- `docs/phase-3-1-roadmap-note.md`
- `ROADMAP.md`

Do not update every file automatically. Update only the files where the new page materially improves reader orientation.

## Stop conditions

Stop if a proposed site or follow-up change:

- summarizes examples without linking to source files
- hides checker limitations
- makes examples sound validated or production-ready
- makes templates sound like completed governance records
- implies certification, conformance, legal validity, safety, compliance, fairness, production approval, runtime correctness, connector correctness, schema correctness, checker correctness, Lean completeness, or AI final-responsibility transfer
- duplicates too much content from source files
- becomes too long to review clearly

## Next safe step

The initial Example browser and Template helper pages are now implemented.

Next safe work is one of:

1. keep the small reader-path synchronization current where the new pages materially improve orientation
2. check the deployed Pages links after the maintainer confirms deployment
3. create a short first-program design note before writing the next local helper

Do not proceed directly from these Pages aids into service-specific connector work, production runtime integration, automatic approval, automatic execution, semantic correctness checking, or conformance evidence.
