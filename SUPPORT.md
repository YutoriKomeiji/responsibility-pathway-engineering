# Support and Field Feedback

RPE is actively developed and intended to be tried within documented boundaries.

## What to report

Public issues are welcome for:

- installation or integration failures;
- unexpected `allow`, `hold`, `human_gate`, or `deny` behavior;
- unclear reason codes or Human Return / responsibility handoff behavior;
- adapter or OpenAPI drift;
- Requirement Pack / governance binding confusion;
- performance or non-functional problems;
- documentation gaps;
- adversarial cases that do not require confidential disclosure;
- examples where RPE is too heavy to integrate;
- examples where RPE blocks too much, too little, or at the wrong point.

A field report is evidence for that environment and scenario. It is not automatically a universal product, safety, legal, compliance, or production claim.

## Useful report format

Please include where practical:

1. RPE commit/tag/version;
2. Python/platform/runtime environment;
3. interface used: Python / REST / MCP / OpenAPI / loader;
4. minimal input or synthetic reproduction;
5. expected outcome;
6. observed outcome;
7. whether the issue concerns usability, correctness, security, performance, compatibility, or documentation;
8. any workaround found.

## Security-sensitive reports

Do not publish exploit details, secrets, private logs, credentials, or sensitive operational data in a public issue. Follow [`SECURITY.md`](SECURITY.md).

## Current support philosophy

`Under construction` does not mean `do not use`.

RPE distinguishes supported, preview, experimental, research, not-implemented, and unsupported surfaces. Users are encouraged to try supported or preview surfaces within their documented boundaries and report failures.

The maintainer may change `0.x` interfaces as the design evolves. Breaking changes should be versioned and accompanied by migration guidance where practical.
