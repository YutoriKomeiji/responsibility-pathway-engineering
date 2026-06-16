# Security Policy

This repository accepts security reports for repository-maintenance risks, documentation-process risks, checker or workflow risks, and accidental exposure risks.

This policy is a reporting and triage path only. It is not a security certification, production-readiness claim, legal review, compliance review, safety review, vulnerability bounty program, connector correctness proof, runtime correctness proof, or AI final-responsibility transfer mechanism.

## Scope

In scope:

- accidental credential, token, secret, or private-key exposure in repository content
- GitHub Actions workflow risks
- dependency or supply-chain risks in repository-maintenance tooling
- unsafe checker behavior that could mislead maintainers or reviewers
- documentation paths that could cause a security-sensitive overclaim
- files or examples that accidentally imply production credentials, real customer data, or private operational data

Out of scope:

- production-service vulnerabilities, because this repository is not a production runtime
- service-specific connector behavior, because service connectors are currently deferred
- real-world legal, safety, compliance, fairness, or moral responsibility determinations
- requests to certify RPE, approve deployment, or validate production systems
- social engineering, phishing, spam, or denial-of-service testing

## Reporting

Please do not put secrets, private exploit details, credentials, private logs, or sensitive operational data in a public issue.

Preferred reporting path:

1. Open a minimal public issue that says a private security report is needed, without sensitive details; or
2. Contact the repository maintainer through the account contact path listed by the maintainer profile if available.

If a public issue is used, include only:

- affected file or area, if safe to disclose
- general issue class, such as `workflow permission`, `secret exposure`, `dependency risk`, or `documentation overclaim`
- whether immediate maintainer review is requested

## Maintainer triage path

When a report is received:

1. Preserve the report path and available evidence.
2. Avoid expanding public detail until exposure risk is understood.
3. Decide whether a private fix, public issue, or public documentation correction is appropriate.
4. If repository content changed, keep the change small and reviewable.
5. Record any security-relevant repository-operation change in the appropriate operation document.

## Current security posture

The repository currently uses bounded repository-maintenance workflows and synthetic examples. Workflow passes and checker passes remain bounded repository-maintenance signals only.

This repository does not currently claim production runtime security, connector security, deployment approval, schema security certification, dependency security certification, or conformance evidence.

## Maintainer responsibilities

The human maintainer remains responsible for deciding whether a reported issue should be fixed, disclosed, deferred, reverted, or escalated.

AI assistance may help draft, inspect, or organize repository changes, but it does not assume final responsibility for security decisions.
