# AI支援作業の責任経路 Issue Form デモ

このデモは、GitHub Issue Form の簡単な入力例を示します。

これはデモです。認証、法的レビュー、安全性レビュー、遵法性レビュー、公平性レビュー、本番承認、conformance evidence、社会的受容の証明、AIへの最終責任移転ではありません。

## RPEとしての焦点

このデモは、単に AI を使ったことを示すためのものではありません。

AI支援 review が誤っている、不明確である、不完全である、根拠不足である、または争われた場合に、作業がどこへ戻れるかを示します。

重要な項目は、AI assistance boundary、evidence log、missing context、responsibility return point、repair / reopening path です。

RPEとしての設計上の芯については `docs/issue-form-rpe-originality-note.md` を参照してください。

## シナリオ

maintainer が AI を使って pull request の要約と review risk の洗い出しを行います。

AI は要約と review support を行います。review 判断の責任は maintainer に残ります。

## Issue title の例

AI-assisted work responsibility path: PR review summary for documentation update

## 入力例

### Source reference

Pull request: `#42`

### Work context

ドキュメント更新の pull request が README を更新し、新しい利用説明を追加します。

Requester: contributor

Responsible person or team: repository maintainer

Affected area: public documentation

Expected outcome: certification や production-readiness claims を広げずに、reader path を明確にすること

### AI assistance role

review_support

### AI assistance boundary

AI は pull request を要約し、新しい利用説明にある曖昧さの可能性を指摘し、review questions を提案しました。

AI は pull request を承認していません。正しさ、法的有効性、安全性、遵法性を決めていません。AI は最終責任者ではありません。

### Human or institutional review

Reviewer: repository maintainer

Review status: pending

Approval gate: merge 前の maintainer review

### Approval skip or transfer, if any

Approval skip は発生していません。

### Evidence log

- PR diff
- 変更前後の README
- related issue discussion
- local markdown preview

### Missing context or uncertainty

- 新しい表現が意図より強く読まれる可能性があります。
- 利用説明に non-claim boundary をより明確に書く必要があるかもしれません。

### Responsibility return point

merge 後の表現が読者を誤解させる、過剰主張に見える、または責任境界を曖昧にする場合は repository maintainer に戻します。

### Repair, dispute, or reopening path

表現が読者を誤導した場合、follow-up issue を開くか、README section を patch / revert します。

### Non-claim boundary

この issue は、正しさ、法的有効性、安全性、遵法性、公平性、本番利用可能性、conformance、最終責任の割当を認証しません。

AI支援 review は support record です。

## このデモが示すこと

この例では、issue が次を保存できることを示します。

- AI が何を支援したか
- AI が何を決めていないか
- どの evidence が review されたか
- 誰が review または approve する必要があるか
- 結果が誤っていた場合に責任経路がどこへ戻るか
- 記録をどう修復または再開できるか
