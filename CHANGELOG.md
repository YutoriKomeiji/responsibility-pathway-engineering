# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

### Authorship clarification and Phase 1.6 entry established

- `AUTHORSHIP.md` added to clarify independent authorship, attribution, and repository-primary authorship information
- `AUTHORS.md` updated with independent affiliation signal and authorship clarification link
- `CITATION.cff` added as machine-readable citation metadata
- `README.md` and `README.ja.md` updated with author, independent repository affiliation, and authorship/citation links
- `docs/phase-1-6-plan.md` added as the next lightweight validation phase plan
- `README.md` and `README.ja.md` updated with Phase 1.6 plan links in the reader path

### Phase 1.5 examples, attribution, and reader path established

- `docs/schema-cross-reference.md` added to explain how the split schema files relate to each other
- `docs/validation-checklist.md` added as a bounded review guide for schema instances
- `examples/minimal-pathway.yaml` added as the first minimal Responsibility Pathway example
- `examples/repair-flow.yaml` added as the first minimal repair-flow example
- Japanese comments added to examples to support Japanese readers without changing schema keys
- `docs/example-index.md` added as an index and reading guide for current and future examples
- `docs/example-review-notes.md` added as initial bounded review notes for examples
- `README.md` and `README.ja.md` updated with schema-document, example, example-index, and example-review links
- `LICENSE` added under the MIT License
- Copyright notice standardized as `Akihisa Ono (小野昭久)`
- `NOTICE.md` added to clarify authorship, attribution, AI-assistance, derivative-use responsibility, and responsibility boundaries
- README license sections now link to `NOTICE.md`

### Phase 1.5 minimal schema split established

- Initial schema split completed under `spec/`
- `spec/node.schema.yaml` added
- `spec/action-class.schema.yaml` added
- `spec/return-point.schema.yaml` added
- `spec/evidence-log.schema.yaml` added
- `spec/repair.schema.yaml` added
- `spec/pathway.schema.yaml` added
- Responsibility Pathway can now be described as a composition of nodes, edges, roles, lifecycle state, evidence logs, return points, repairs, and responsibility boundaries
- Validation-oriented rules now exist for AI final responsibility boundary, stop/return references, repair records, evidence sufficiency, and high-impact action requirements

### v0.2.0 Concept model and specification binding

- Source mapping from public Zenn articles to canonical repository definitions added
- Runtime Model added
- Responsibility Node model added
- Return Point model added
- Repair Model added
- Value and Cost Flow model added
- Stop Authority model added
- Evidence Log model added
- Action Class Matrix added
- Approval Gate model added
- Decision Owner model added
- Core YAML specification expanded to version 0.2.0
- AI participation clarified as pathway-node participation, not final responsibility authorship
- Formalization boundary clarified: formal claims must remain bound to explicit definitions, assumptions, and model scope

### Foundation established

- Repository created
- README and README.ja added
- Responsibility Pathway definition published
- Eight-element model published
- Core YAML specification added
- Lean scaffold created
- BEACON established
- LUMINALIA philosophy established
- ROADMAP established
