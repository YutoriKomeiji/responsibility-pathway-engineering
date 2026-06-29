# AI支援作業の責任経路 Issue Form 利用ガイド

このガイドは、AI支援作業の責任経路を記録するための GitHub Issue Form の使い方を説明します。

これは利用ガイドです。認証、法的レビュー、安全性レビュー、遵法性レビュー、公平性レビュー、本番承認、conformance evidence、社会的受容の証明、AIへの最終責任移転ではありません。

## RPEとしての違い

この form は、単なる AI利用開示 form ではありません。

AI支援作業が誤っている、不明確である、不完全である、根拠不足である、または争われた場合に、判断、証拠、レビュー、修復、責任がどこへ戻れるかを残すことが RPE としての目的です。

設計上の芯については `docs/issue-form-rpe-originality-note.md` を参照してください。

## 何に使うか

AI支援が関与した作業について、責任経路を GitHub issue として残したい場合に使います。

典型的な用途:

- AI支援による pull request review
- AI支援による issue triage
- AI支援によるドキュメントや仕様の草案作成
- AI支援によるログ要約
- AI支援による incident note 作成
- 人間または組織の review が必要な AI支援の判断補助

## 何を記録するか

Issue Form は次を記録します。

- source reference
- work context
- AI assistance role
- AI assistance boundary
- human or institutional review
- approval skip or transfer がある場合の理由と補償経路
- evidence log
- missing context or uncertainty
- responsibility return point
- repair, dispute, or reopening path
- non-claim boundary

## 使い方

1. GitHub で新しい issue を開きます。
2. `AI-assisted work responsibility path` を選びます。
3. 各項目に短く具体的な情報を入力します。
4. 関連する pull request、文書、incident note、review thread から issue を参照します。
5. review status、evidence、不確実性、return point が変わったら issue を更新します。

## 実務上の効果

この form は、AI支援作業をあとから review しやすくします。

将来の読者が次を確認できます。

- AI は何を支援したのか
- AI は何を決めていないのか
- どの evidence が使われたのか
- 誰が review した、またはこれから review するのか
- 問題があった場合、責任経路はどこに戻るのか
- 作業をどう修復、異議申し立て、再開できるのか

## 使わない場合

この form を、法的レビュー、安全性レビュー、遵法性レビュー、security review、本番承認、外部レビュー、正式な認証の代わりに使わないでください。

AI が最終責任者になったと主張するためにも使わないでください。

## YAML template との関係

`templates/ai-assisted-work-responsibility-path.yaml` は、ファイルとしてコピーできる責任経路記録が必要な場合に使います。

`.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml` は、その記録を GitHub issue として残したい場合に使います。

どちらも lightweight、under-construction、non-certifying です。
