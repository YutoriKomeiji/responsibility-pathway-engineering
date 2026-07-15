# Corda Custom Agent

Corda is the repository-scoped Luminalia GitHub Implementation Agent for Responsibility Pathway Engineering.

## Agent profile

The custom agent profile is stored at:

```text
.github/agents/corda.agent.md
```

After the profile is available on the default branch, GitHub surfaces that support repository custom agents can present Corda as an agent choice for work in this repository.

## How to invoke Corda

Choose Corda in a supported GitHub Copilot agent selector, or address the role directly in Copilot Chat:

```text
Corda, inspect the current repository state and propose the smallest runnable vertical slice for the requested feature.
```

Useful task forms include:

```text
Corda, implement this issue as a draft PR. Do not merge it.
```

```text
Corda, inspect the affected workflows before changing README.md and preserve their exact-string contracts.
```

```text
Corda, add fixtures, deterministic checks, and CI for this external-kernel component.
```

## Instruction layers

Corda should operate with these repository instruction layers:

1. `.github/agents/corda.agent.md` — selected agent role.
2. `.github/copilot-instructions.md` — repository-wide Copilot direction.
3. `AGENTS.md` — implementation loop and Human Gate rules.
4. `.github/instructions/*.instructions.md` — path-specific technical guidance.

Personal Copilot instructions may add the user's preferred name, tone, and general working style. Repository files remain the source for RPE-specific behavior.

## Scope

This file defines an implementation role and invocation path. It does not grant new GitHub permissions, bypass branch protection, approve merges, publish artifacts, or make Corda a responsibility holder.

To use the same named agent in another personal repository, copy or synchronize the agent profile and the relevant instruction files into that repository. Organization-wide distribution can be considered later if the repositories move under a shared organization policy.
