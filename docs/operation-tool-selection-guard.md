# Operation Tool Selection Guard

This note records a small repository-maintenance guard for choosing GitHub tools during AI-assisted maintenance.

It was added after harmless tool-selection mistakes where the wrong read surface was used while trying to inspect or update repository files.

## Rule

Choose the narrowest tool that matches the intended operation.

For repository file work in this repository, use the direct GitHub repository tools as the primary path, not a tool-discovery or connector-discovery layer.

A read-only tool-discovery recurrence does not by itself stop repository work if repository content was not changed and the next operation returns to a direct GitHub file operation.

## Repository file reading

Use repository file reading when the goal is to inspect an existing file on the default branch.

Expected operation:

- call the direct GitHub file reader by repository path
- inspect line ranges
- cite the fetched file lines

Do not use pull-request patch tools for this purpose.

Do not use tool-discovery actions, resource-listing actions, or connector-discovery actions as a substitute for repository file reading when the correct GitHub file reader is already available.

If a read-only tool-discovery call occurs anyway, treat it as a recoverable operation drift only when it did not change repository content and did not become the basis for a file write.

## Repository file writing

Use repository file writing when the goal is to add or replace a repository file.

Expected operation:

- for a new file, call the direct GitHub create-file operation
- for an existing file, first fetch the current file and use its current blob SHA
- then call the direct GitHub update-file operation
- verify by fetching the updated file or relevant line range

Do not use tool-discovery actions, resource-listing actions, or connector-discovery actions as a pre-write step when the repository, path, and intended GitHub operation are already known.

A file write should be grounded in a direct GitHub file fetch of the current repository path and current blob SHA, not in a tool-discovery result.

## Pull-request patch reading

Use pull-request patch retrieval only when all of the following are known:

- repository name
- pull request number
- changed file path
- the goal is to inspect a PR diff or patch, not the current repository file

If no pull request number is part of the task, do not use PR patch retrieval.

## Write operations

Use create-file operations only when adding a new file.

Use update-file operations only after fetching the current file and using its current blob SHA.

Do not update long navigation files unless the edit is small, necessary, and easy to audit.

## Tool-discovery recurrence tolerance

If an AI-assisted maintenance step calls a tool-discovery layer while direct GitHub file tools are already available, classify the event before changing the repository.

Treat the recurrence as a tolerable read-only drift when all of the following hold:

1. no repository content was changed by the tool-discovery call,
2. the tool-discovery result is not used as the basis for a file write,
3. the next repository operation returns to a direct GitHub file read or write,
4. the recurrence does not obscure which file content, blob SHA, or line range grounded the change.

Treat the recurrence as operation noise that should be recorded here or in the relevant sync log when it repeats within the same responsibility unit, changes the basis for a write, causes the wrong file surface to be used, or makes later review of the responsibility path harder.

This applies especially to work on known files such as `BEACON.md`, `README.md`, `docs/operation-index.md`, `docs/current-task-inventory.md`, `docs/phase-3-1-sync-log.md`, `docs/phase-3-1-current-snapshot.md`, and other known repository paths.

## Recovery rule

If the wrong read or discovery surface is used and no write occurred:

1. state that the repository was not changed,
2. do not use the discovery result as write grounding,
3. resume with one narrow direct GitHub file operation,
4. record the recurrence only if it affects future maintainability or reviewability.

The purpose is not to justify tool-discovery as a preferred path. The purpose is to keep work moving while preserving a recoverable responsibility path.

## Boundary

This guard is an operation note only.

It does not change schemas, checkers, workflows, runtime connectors, production runtime, or Lean files.
