# Operation Tool Selection Guard

This note records a small repository-maintenance guard for choosing GitHub tools during AI-assisted maintenance.

It was added after harmless tool-selection mistakes where the wrong read surface was used while trying to inspect or update repository files.

## Rule

Choose the narrowest tool that matches the intended operation.

For repository file work in this repository, use the direct GitHub repository tools, not a tool-discovery or connector-discovery layer.

## Repository file reading

Use repository file reading when the goal is to inspect an existing file on the default branch.

Expected operation:

- call the direct GitHub file reader by repository path
- inspect line ranges
- cite the fetched file lines

Do not use pull-request patch tools for this purpose.

Do not use tool-discovery actions, resource-listing actions, or connector-discovery actions as a substitute for repository file reading when the correct GitHub file reader is already available.

## Repository file writing

Use repository file writing when the goal is to add or replace a repository file.

Expected operation:

- for a new file, call the direct GitHub create-file operation
- for an existing file, first fetch the current file and use its current blob SHA
- then call the direct GitHub update-file operation
- verify by fetching the updated file or relevant line range

Do not use tool-discovery actions, resource-listing actions, or connector-discovery actions as a pre-write step when the repository, path, and intended GitHub operation are already known.

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

## Repeated tool-discovery mistake

If an AI-assisted maintenance step repeatedly calls a tool-discovery layer while direct GitHub file tools are already available:

1. stop the discovery loop,
2. state that no repository content was changed by the mistaken tool-discovery call,
3. resume with exactly one direct GitHub file operation,
4. record the recurrence here or in the relevant sync log if it affects future maintainability.

This applies especially to work on known files such as `BEACON.md`, `README.md`, `docs/operation-index.md`, `docs/current-task-inventory.md`, `docs/phase-3-1-sync-log.md`, `docs/phase-3-1-current-snapshot.md`, and other known repository paths.

## Recovery rule

If the wrong read tool is used and no write occurred:

1. stop the mistaken loop,
2. state that the repository was not changed,
3. record or apply a guard if the mistake can recur,
4. resume with one narrow operation.

## Boundary

This guard is an operation note only.

It does not change schemas, checkers, workflows, runtime connectors, production runtime, or Lean files.
