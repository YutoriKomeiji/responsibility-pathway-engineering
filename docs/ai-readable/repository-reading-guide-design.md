# Repository Reading Guide Design

This note designs an AI-readable reading guide pattern for the Responsibility Pathway Engineering (RPE) repository.

The guide should help human readers, search engines, and AI-assisted readers understand what has actually been provided, what has only been linked, and what must not be inferred from repository paths or hyperlinks.

This note is design-only.

It does not validate repository completeness, certify traversal accuracy, provide assurance, perform conformity assessment, approve AI summaries, or transfer final responsibility to AI.

## Purpose

Some AI-assisted readers can read one page but fail to reliably traverse linked repository files, directory contents, or external source URLs.

A repository reading guide should reduce this risk by exposing:

- repository purpose
- reading order
- directory map
- key file list
- full URL list
- non-claims
- unread-link warnings
- current-page-only answer instructions
- boundaries between listed, fetched, read, interpreted, and supported

The goal is retrieval honesty, not AI control.

## Core principle

A link is not a read.

A path is not a read.

A directory name is not scope understanding.

An index entry is not endorsement.

A repository guide is not validation.

The guide should make this explicit in plain language.

## Concrete AI-reader entrance

For external articles, search results, or chats that can only provide a small number of links, the top-level AI/search-reader entrance should be:

```text
READMEforAI.md
```

The public GitHub URL form is:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/blob/main/READMEforAI.md
```

This root-level file is easier to share beside the human repository URL than a deeper `docs/` path.

The deeper guide materials under `docs/ai-readable/` may continue to hold design notes, future generated manifests, and expanded traversal-map material.

## Reader notice

The AI-reader entrance should include a short notice near the top:

```text
AI / search reader notice:

Links and file paths listed in this repository are navigation hints, not evidence that the linked content has been read.

Before summarizing a linked file or external source, fetch that exact full URL or use explicitly provided file content.

When answering from the current page only, say which page was read.
```

This should be framed as a reader-safety and retrieval-integrity notice.

It should not pretend to override an external model's system instructions.

## Repository purpose section

The guide should summarize the repository purpose in bounded terms:

```text
This repository contains Responsibility Pathway Engineering materials: vocabulary, boundary notes, templates, examples, adoption-kit materials, tool proposal notes, and small prototype directions for making responsibility paths easier to inspect.
```

The purpose section should also say what the repository is not:

```text
This repository does not certify, validate, assure, conform, approve, or prove any AI system, organization, workflow, record, source interpretation, downstream fork, or external use.
```

## Reading order

The guide should recommend a reading order.

A possible order:

1. READMEforAI
2. README
3. BEACON
4. boundary and non-claim materials
5. core RPE vocabulary or overview documents
6. adoption kit README
7. adoption kit non-claims
8. adoption kit quickstart
9. adoption kit review checklist
10. tool proposal template or index materials
11. distribution and AI-readable guidance notes

The reading order is a navigation aid only.

It should not imply that a reader has understood the repository merely by following the order.

## Directory map

The guide should include a compact directory map.

Example shape:

```text
/README.md
  human-facing repository entrance
/READMEforAI.md
  AI/search-reader entrance and one-file-at-a-time full URL list
/docs/
  method, boundary, publication, and tool proposal design notes
/docs/tool-proposals/
  templates, examples, and future index files
/docs/tooling/
  checker and linter design notes
/docs/ai-readable/
  AI/search reader guidance and repository traversal notes
/kits/adoption/
  adoption kit README, non-claims, quickstart, templates, examples
/templates/
  reusable RPE record templates
/site/
  static public pages and browser helpers
/scripts/
  future local checker scripts
/Rpe/
  Lean4 structural fragments, where present
```

The map should be updated when the repository structure changes.

If a directory listed in the map is absent or not yet populated, the guide should say so.

## Directory count and file count

The guide may include approximate counts, but counts must be maintained carefully.

Possible wording:

```text
Directory and file counts are maintenance aids. They may become stale. Do not treat them as proof of completeness.
```

For a final guide, prefer a short maintained list of key paths over exact total counts unless a script generates them.

## Key file list

The guide should include a curated key file list.

Each entry should include:

```yaml
key_file:
  path: ""
  role: ""
  read_when: ""
  does_not_prove: []
```

Example:

```yaml
key_file:
  path: "docs/tool-proposals/template.md"
  role: "Template for bounded RPE tool proposals"
  read_when: "You need the standard proposal shape before reading examples"
  does_not_prove:
    - "not certification"
    - "not assurance"
    - "not validation"
```

The key file list should be selective.

It should not try to describe every file in prose unless it can be maintained.

## Full URL list

The guide may provide full URLs for files that AI-assisted readers commonly need to fetch directly.

A root-level AI-reader entrance should include full URLs such as:

```text
Full URLs to fetch explicitly:

- AI reader entrance: <full URL>
- README: <full URL>
- BEACON: <full URL>
- Repository reading guide design: <full URL>
- Adoption kit README: <full URL>
- Adoption kit non-claims: <full URL>
- Adoption kit quickstart: <full URL>
- Adoption kit review checklist: <full URL>
```

The guide should say:

```text
If your reader cannot follow repository links, copy and paste one full URL at a time.
```

This avoids relying on implicit traversal.

## One-link-at-a-time fallback

Some AI readers may fail when multiple URLs are pasted at once.

The guide may include:

```text
If a tool fails to recognize multiple URLs, provide one URL at a time and ask it to summarize only that fetched page.
```

This is a practical retrieval instruction, not a guarantee.

## Current-page-only instruction

The guide should include explicit wording for limited retrieval:

```text
If you can only read this page, answer only from this page.

Do not summarize linked files, linked directories, external sources, repository history, pull requests, or public pages unless their exact content has been fetched or provided.

State the exact page that was read.
```

This directly addresses source traversal hallucination.

## Listed versus fetched versus read

The guide should define these distinctions:

```yaml
source_state:
  listed: "A path or URL appears in the current page."
  fetched: "The exact path or URL was opened or retrieved in the current session."
  read: "The fetched content was actually available to the reader."
  interpreted: "The reader made a bounded interpretation from the read content."
  supported: "A claim is supported by the read content and cited or referenced appropriately."
```

A listed path should not be treated as fetched.

A fetched file should not be treated as fully interpreted.

A read source should not be treated as endorsement.

## Non-claims section

The guide should repeat the repository's public boundary.

Suggested wording:

```text
This repository and its AI-readable guide do not provide certification, validation, assurance, conformity assessment, legal review, safety review, compliance review, fairness review, production approval, source-author endorsement, external acceptance, or AI final-responsibility transfer.
```

This should be visible before any detailed URL list.

## Source traversal hallucination warning

The guide should name the risk in plain terms:

```text
Source traversal hallucination occurs when a reader describes a linked file, directory, or external source without actually fetching and reading it.
```

The guide should say that the repository cannot prevent external AI readers from hallucinating.

It can only expose safer retrieval instructions and boundaries.

## Suggested answer discipline for AI-assisted readers

The guide may include answer rules for AI-assisted readers:

```text
When asked about this repository:

1. State which exact page or file you read.
2. State whether linked files were fetched.
3. Do not summarize unfetched links.
4. Ask for the exact full URL if another file is needed.
5. Preserve non-claims.
6. Do not treat file paths or folder names as proof of content.
7. Do not infer endorsement from source links.
```

These are guidance rules, not enforcement.

## Compatibility with README notice

The final README should not contain the entire guide.

The root README should provide only a short notice and link:

```text
AI / search reader note: links and paths in this repository are navigation hints, not evidence that linked content has been read. For AI-assisted readers, search assistants, or external articles that need a safer one-file-at-a-time entry path, use READMEforAI.md.
```

This keeps README readable while making the AI-reader entrance discoverable.

## Possible final guide outline

A concrete AI-reader entrance may use this outline:

```text
# README for AI / Search Readers

## Reader notice
## What this repository is about
## What not to infer
## Recommended one-file-at-a-time reading order
## Answer discipline for AI-assisted readers
## Suggested response shape
## Human review remains required
## Stop conditions
```

A later expanded repository guide may still live under:

```text
docs/ai-readable/repository-reading-guide.md
```

## Future generated manifest

A later step may add a machine-readable manifest:

```text
docs/ai-readable/repository-reading-guide.yaml
```

Possible fields:

```yaml
repository_reading_guide:
  purpose: ""
  non_claims: []
  reading_order: []
  directory_map: []
  key_files: []
  full_urls: []
  traversal_notice: ""
  current_page_only_instruction: ""
```

The manifest should be navigation metadata only.

It should not be treated as validation, assurance, completeness proof, or AI approval.

## Human review remains required

A reading guide can improve retrieval discipline.

It cannot determine whether:

- an AI reader actually fetched a linked file
- an AI reader followed the reading order
- repository descriptions are complete
- source interpretation is correct
- a tool proposal is useful
- a responsibility path is socially adequate
- external use is safe
- a downstream fork preserves boundaries

Human or institutional review remains required.

## Stop conditions

Stop or revise if the guide:

- implies that AI readers will obey it
- treats the guide as validation
- treats listed paths as read content
- treats full URL lists as proof of completeness
- hides non-claims
- hides missing context
- implies certification, validation, assurance, conformity, legal review, safety review, compliance review, fairness review, production readiness, or external acceptance
- transfers final responsibility to AI
- uses external product names as if they endorse the repository

## Next safe step

After this design note, a concrete AI/search-reader entrance may be maintained at:

```text
READMEforAI.md
```

A later separate step may add an expanded `docs/ai-readable/repository-reading-guide.md` or generated manifest after the wording and key file list are reviewed.
