---
applyTo: "schemas/**/*,examples/**/*.json,spec/**/*"
---

# Schema and fixture instructions

- Keep interchange contracts explicit, versionable, and machine-readable.
- Use stable identifiers, reason-code namespaces, and enumerated decisions where appropriate.
- Preserve source provenance, applicability, authority, evidence, human-return, and repair fields rather than hiding them in free text.
- Prefer additive evolution while contracts are experimental; document breaking changes clearly.
- Update representative fixtures whenever a required schema field changes.
- Include synthetic metadata for synthetic examples so they cannot be mistaken for approved legal, standards, or organizational mappings.
- Validate both valid and invalid examples where practical.
- Schema validity is structural evidence only; it does not establish real-world applicability, correctness, or approval.
