# Discovery Metadata Linter Design

This note designs a future local linter for Responsibility Pathway Engineering (RPE) tool proposal discovery metadata.

The linter would help maintainers inspect whether tool proposals expose the minimum metadata needed for search, review, source-link discipline, non-claim preservation, and AI-reader traversal honesty.

This note is design-only.

It does not implement a checker, validate any proposal, certify metadata quality, provide assurance, perform conformity assessment, prove source traversal, or approve any downstream use.

## Purpose

RPE tool proposals are intended to be discoverable without becoming overclaims.

A future linter can help check whether a proposal contains fields such as:

- title
- proposal path
- area terms
- related keywords
- source links
- source relationship notes
- implementation surface
- artifact paths
- non-claims
- feedback posture
- repository-boundary status
- AI-reader traversal safety notice

The linter should report missing or suspicious metadata.

It should not decide whether a proposal is true, useful, responsible, safe, compliant, fair, production-ready, assured, conformant, or externally accepted.

## Motivation

Search engines and AI-assisted readers may treat visible file paths, folder names, links, or index entries as if the linked content had been read.

This creates a source traversal risk:

```text
A link is listed.
The linked page is not fetched.
The answer describes the linked page anyway.
```

For RPE, this is a responsibility-path issue.

A proposal should not merely expose links.
It should also preserve the boundary between:

- a link being listed
- a URL being fetched
- a file being read
- a source relationship being understood
- a claim being supported

## Name for the risk

This note uses the working term:

```text
source traversal hallucination
```

Related terms:

- unverified link-following hallucination
- linked-but-unread source drift
- repository path overreach
- AI reader traversal failure
- traversal honesty failure

These are working labels only.
They are not standard terms.

## Future linter scope

The future linter may inspect Markdown tool proposal files under:

```text
docs/tool-proposals/
```

It may later inspect:

```text
docs/tool-proposals/index.md
docs/tool-proposals/index.yaml
docs/tool-proposals/index.json
docs/ai-readable/
site/tool-proposals/
```

The first implementation should remain local and small.

It should not run as a required CI gate until its behavior is stable and reviewed by a human maintainer.

## Minimum metadata checks

A future linter may check that each proposal includes:

```yaml
required_metadata:
  title: true
  short_summary: true
  area_terms: true
  related_keywords: true
  source_links_or_no_source_links_statement: true
  source_relationship_note: true
  rpe_problem_statement: true
  implementation_surface: true
  artifact_path: true
  non_claims: true
  feedback_posture: true
  repository_boundary: true
```

Missing fields should be reported as warnings.

The linter should avoid auto-fixing because missing metadata may indicate unresolved responsibility-path work.

## Source-link checks

For each source link, a future linter may check for:

```yaml
source_link:
  url: "required"
  title: "recommended"
  source_type: "required"
  date_checked: "required"
  relationship_note: "required"
```

The relationship note should make clear that the source is context, not endorsement.

Acceptable phrases may include:

```text
not an endorsement
```

```text
public context only
```

```text
does not claim to represent the authors' intent
```

```text
this proposal extracts one RPE angle
```

The linter should warn when a source link appears without a relationship note.

## Artifact-path checks

Each proposal should point to at least one concrete artifact path.

Examples:

```text
docs/tool-proposals/examples/ai-assurance-traceability-review-record.md
```

```text
templates/ai-assisted-work-responsibility-path.yaml
```

```text
scripts/check_rpe_records.py
```

```text
site/template-helper/index.html
```

```text
Rpe/ResponsibilityHolder.lean
```

The linter may check whether local repository paths exist.

It should not infer that a path is semantically correct merely because it exists.

## Area-term checks

A proposal may list broad area terms such as:

- Responsible AI
- Explainable AI
- Safe AI
- Verified AI
- AI verification
- TEVV
- AI assurance
- conformity assessment
- provenance
- traceability
- record-keeping
- cryptographic verifiability

The linter may check whether area terms are present.

It should not certify that the proposal satisfies those areas.

It may warn if an area term appears in metadata but the file has no corresponding discussion, field, or non-claim boundary.

## Related-keyword checks

Related keywords should describe visible proposal contents.

Examples:

- responsibility holder
- AI-assisted work record
- review gate
- approval status
- evidence route
- missing context
- unchecked sources
- source relationship note
- return path
- traceable decision path
- accountable workflow
- tamper-evident record
- signed manifest
- AI-assisted review note

The linter may warn if keywords appear only in metadata and nowhere else in the proposal.

This is a weak signal, not proof of misuse.

## Non-claim checks

Every proposal should preserve non-claims.

The linter may check for reminders such as:

- not certification
- not validation
- not assurance
- not conformity assessment
- not legal review
- not safety review
- not compliance review
- not fairness review
- not production approval
- not source endorsement
- not AI final-responsibility transfer

The linter should treat missing non-claims as a serious warning.

A linter pass should not mean the non-claims are complete, legally sufficient, or socially adequate.

## Feedback-posture checks

The linter may check whether feedback is framed as design input.

Safe phrases:

```text
Feedback is welcome as design input.
```

```text
Feedback is not endorsement, validation, certification, assurance, conformity, acceptance, or approval.
```

Unsafe patterns may include:

```text
Feedback proves this works.
```

```text
Positive feedback validates the tool.
```

```text
Community reaction is assurance.
```

The linter should warn but not decide social meaning.

## Repository-boundary checks

The linter may check whether a proposal says whether it remains inside the RPE repository or may later become a separate repository.

Suggested values:

- inside-rpe
- candidate-for-promotion
- promoted
- archived

The linter should warn if repository promotion is described as validation, proof, assurance, or production readiness.

## AI reader traversal safety notice

A future linter may check whether AI-readable files, indexes, or proposal pages include a traversal safety notice.

Suggested notice:

```text
AI reader notice:
Links and file paths listed in this repository are navigation hints, not evidence that the linked content has been read.
Before summarizing a linked file or external source, fetch that exact full URL or use explicitly provided file content.
When answering from the current page only, say "based only on the current page."
```

The notice should avoid pretending to control an external AI system.

It should be framed as a reader-safety and retrieval-integrity instruction.

## Traversal map checks

A future linter may check whether an AI-readable repository guide exposes:

- repository purpose
- reading order
- directory map
- key file list
- index links
- non-claims
- full URL list
- unread-link warning
- current-page-only answer instruction

This would support readers that cannot reliably traverse repository links.

The linter should not assume that external AI systems obey the guide.

## Possible report shape

A future local checker may output:

```text
RPE discovery metadata report

Checked files: 3
Warnings: 5
Errors: 0

WARN docs/tool-proposals/examples/example.md
- missing source relationship note
- area term "AI assurance" appears without local non-claim "not assurance"
- linked file path appears without traversal safety reminder

PASS docs/tool-proposals/examples/ai-assurance-traceability-review-record.md
- required metadata present
- source relationship note present
- non-claims present
- feedback posture present
```

The report is maintenance output only.

It is not approval, validation, assurance, conformance evidence, or proof.

## Suggested CLI shape

A later Python script may use a small interface such as:

```bash
python scripts/check_discovery_metadata.py docs/tool-proposals
```

Optional later flags:

```bash
python scripts/check_discovery_metadata.py docs/tool-proposals --include-ai-readable
```

```bash
python scripts/check_discovery_metadata.py docs/tool-proposals --json
```

This note does not create that script.

## Human review remains required

A linter can check whether selected strings, fields, and paths are present.

It cannot determine whether:

- source interpretation is correct
- area terms are proportionate
- a proposal is useful
- a responsibility holder is socially adequate
- evidence is complete
- risk is acceptable
- a tool is production-ready
- a source author endorses the proposal
- an AI reader actually fetched linked content

Human or institutional review remains required.

## Stop conditions

Stop or revise if the linter design:

- treats metadata presence as correctness
- treats source links as endorsement
- treats link listing as source reading
- treats path existence as semantic support
- treats a pass result as validation
- claims certification, assurance, conformity, legal review, safety review, compliance review, fairness review, or production readiness
- hides missing context
- hides uncertainty
- makes AI the final responsibility holder
- implies external AI systems will obey the traversal notice

## Next safe step

After this design note, the next planned step is:

```text
docs/ai-readable/repository-reading-guide-design.md
```

That note should design a dedicated AI-readable reading guide with repository purpose, read order, directory map, key file list, full URL list, non-claims, and traversal safety notice.

A later, separate step may add a short README notice that points to the guide.