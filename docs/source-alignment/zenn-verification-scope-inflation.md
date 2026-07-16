# Source Alignment: verification-scope-inflation.md

This note records the source-alignment review for a later public Zenn article that was not included in the earlier inventory pass.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/verification-scope-inflation.md`
- Title: `「動く」「通る」「要約される」は信頼の証明ではない――検証範囲の膨張と責任経路チェック`
- Published flag: `true`
- Review status: reviewed

## Article role

The article defines verification-scope inflation as treating a bounded signal as support for a broader claim than it can establish. Examples include:

- executable samples being read as security or production evidence;
- green CI being read as general trustworthiness;
- formalized propositions being read as proof of real-world validity;
- summaries, search surfaces, or citations being read as independent approval.

## Repository alignment

The article is directly aligned with the current repository boundary:

- a checker pass proves only the checks it executed;
- CI success is not certification, deployment approval, or security review;
- Lean results are model-scoped and do not verify the Python runtime;
- schema validity does not establish source interpretation or real-world applicability;
- reference adapters are not production services;
- repository visibility and AI summaries are not external endorsement.

This article provides public-language support for the M1 Governed Reference Kernel scope statements and the internal critical-review findings.

## Repository decision

Status: aligned and high-value.

No new runtime feature is required solely from this article. It should be added to the source inventory and may be cited when explaining why RPE separates implementation evidence, governance eligibility, compatibility, and external claims.

Future changes should continue to state both:

1. what each check establishes;
2. what remains outside that check's evidence scope.
