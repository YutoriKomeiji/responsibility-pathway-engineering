# Operation Tool Selection Guard

This note records a small repository-maintenance guard for choosing GitHub tools during AI-assisted maintenance.

It was added after a harmless tool-selection mistake where a pull-request patch retrieval action was used while trying to inspect a repository file.

## Rule

Choose the narrowest tool that matches the intended operation.

## Repository file reading

Use repository file reading when the goal is to inspect an existing file on the default branch.

Expected operation:

- fetch a repository file by path
- inspect line ranges
- cite the fetched file lines

Do not use pull-request patch tools for this purpose.

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

## Recovery rule

If the wrong read tool is used and no write occurred:

1. stop the mistaken loop,
2. state that the repository was not changed,
3. record or apply a guard if the mistake can recur,
4. resume with one narrow operation.

## Boundary

This guard is an operation note only.

It does not change schemas, checkers, workflows, runtime connectors, production runtime, or Lean files.
