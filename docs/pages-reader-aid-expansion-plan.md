# Pages Reader-Aid Expansion Plan

This note plans the next browser-facing GitHub Pages reader aids for Responsibility Pathway Engineering.

It exists before implementation so that Example browser and Template helper pages remain bounded reader aids rather than becoming certification, validation, implementation, or approval surfaces.

This plan is a planning note only. It is not a certification record, conformance claim, external review finding, legal review, safety review, compliance review, fairness review, production approval, standardization claim, runtime correctness proof, connector correctness proof, schema correctness proof, checker correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.

## Current trigger

The compact `ROADMAP.md` identifies the next browser-facing reader-aid candidates as:

- Example browser page
- Template helper page

The current published Pages reader path already helps first readers orient, but the next additions should remain small and source-linked.

## Candidate 1: Example browser page

Purpose:

- help first readers find current example and fixture files from a browser
- group examples by reader purpose rather than by implementation maturity
- point back to source files and existing documentation
- make example boundaries easier to inspect

Suggested source references:

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

## Candidate 2: Template helper page

Purpose:

- help first readers find the first copyable template
- show the template's intended inspection role
- point back to source files and planning notes
- keep lightweight adoption distinct from implementation maturity

Suggested source references:

- `templates/ai-assisted-work-responsibility-path.yaml`
- `docs/lightweight-durable-quality-implementation-strategy.md`
- `docs/public-adoption-and-fork-strategy.md`
- `docs/repository-construction-status-labels.md`
- `docs/zenn-level-2-repository-walkthrough-readiness.md`

Required boundary:

The Template helper page must not imply that a copied template creates a valid responsibility record, completes review, proves compliance, approves production use, or transfers final responsibility to AI.

A helper page may explain how to inspect the template shape, but it must preserve human and maintainer responsibility.

## Implementation order

Use this order unless the maintainer deliberately changes it:

1. Add one Pages reader aid at a time.
2. Start with the Example browser page if example navigation is the immediate need.
3. Start with the Template helper page if lightweight adoption explanation is the immediate need.
4. After adding a page, update only the reader-path files that need the new link.
5. Keep each page short enough to review on GitHub mobile.

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

Stop before implementation if a proposed page:

- summarizes examples without linking to source files
- hides checker limitations
- makes examples sound validated or production-ready
- makes templates sound like completed governance records
- implies certification, conformance, legal validity, safety, compliance, fairness, production approval, runtime correctness, connector correctness, schema correctness, checker correctness, Lean completeness, or AI final-responsibility transfer
- duplicates too much content from source files
- becomes too long to review clearly

## Next safe step

Choose exactly one first Pages reader aid:

- Example browser page
- Template helper page

Then create a small implementation PR for that one page only.
