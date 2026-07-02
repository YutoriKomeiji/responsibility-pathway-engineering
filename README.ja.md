# Responsibility Pathway Engineering

著作者: Akihisa Ono (小野昭久)

このリポジトリにおける所属表記: Independent

責任経路工学（Responsibility Pathway Engineering）は、人間とAIシステムがともに関わる判断や行為において、判断、権限、証拠、停止権限、人間への戻り先、修復がどこに残っているかを保存するための設計フレームワークです。

これは責任追及の仕組みではありません。

## なぜ重要か

AIシステムは、出力を生成するだけではありません。判断、推薦、分類、ツール利用、証拠生成、ときには行為の準備にも関与します。

そのとき重要なのは、出力が正しかったかだけではありません。責任の経路が見える状態で、人間や組織へ戻れる状態だったかです。

- 判断がどこで発生したか
- 誰または何が関与したか
- どこで承認が必要だったか
- どこで行為を停止できたか
- どこで人間へ戻れたか
- どの証拠が残ったか
- 誰が修復または再接続できたか

責任経路工学は、これらを設計対象として扱います。

## 現在の状態

Early public specification.

本リポジトリは、意図的に仕様優先で維持されています。大規模な実装層よりも先に、定義、例、ライフサイクル境界、checker境界、出典、主張しないことを優先しています。

## まず試す

実用上の形をすぐ確認したい場合は、最初のコピー可能なテンプレートから始めてください。

- [templates/ai-assisted-work-responsibility-path.yaml](templates/ai-assisted-work-responsibility-path.yaml) - AI支援作業の責任経路を記録するための工事中テンプレート
- [templates/README.md](templates/README.md) - テンプレート一覧と主張しないことの境界

このテンプレートは、AI支援が関与した作業について、source reference、人間または組織による review、evidence、不確実性、責任の戻り先、修復・異議・再開経路を残すための軽量な出発点です。

このテンプレートは、認証、conformance evidence、本番承認、法的レビュー、安全性レビュー、遵法性レビュー、公平性レビュー、社会的受容の証明、AIへの最終責任移転ではありません。

## 出典

著作者自身の開発記録として、Akihisa Ono は 2026-01-18 に公開した note 記事から、**責任経路 / Responsibility Pathway** という概念を考え、使い始めました。

- [AI事故は「責任設計」だけでは防げない――最後の砦は「責任経路設計」である](https://note.com/dantarg/n/nb7f28afa6882)

より詳しい出典記録は [docs/provenance.md](docs/provenance.md) にあります。

この出典記録は、帰属と traceability のための記述です。法的主張、所有権の裁定、盗用・剽窃の告発、認証、本番利用承認ではありません。

## このリポジトリが主張しないこと

本リポジトリは、次のものを提供すると主張しません。

- 法的責任の決定
- 安全性認証
- 遵法性認証
- 公平性認証
- 道徳的責任の解決
- 制度的承認
- 本番利用可能性
- agent runtime
- RACI、HITL、Guardrails、ISO/IEC 42001、human oversight framework の置き換え
- AIへの最終責任移転

本リポジトリ内の schema、例、checker、Lean ファイルは、いずれも構造的・前提依存・非認証です。

## はじめに読むもの

初めて読む人、未来の保守者、AIによる継続作業では、次の順番で読むことを推奨します。

1. [BEACON.md](BEACON.md) - 現在地と再接続点
2. [docs/operation-index.md](docs/operation-index.md) - 運用と保守の導線
3. [docs/overview.md](docs/overview.md) - 現在のリポジトリ概観
4. [docs/concepts/index.md](docs/concepts/index.md) - 概念レベルの読書導線
5. [docs/example-index.md](docs/example-index.md) - 例と境界
6. [docs/checker-coverage.md](docs/checker-coverage.md) - 現在のchecker境界と対象範囲
7. [LUMINALIA.md](LUMINALIA.md) - 公開設計思想としてのLuminalia境界
8. [ROADMAP.md](ROADMAP.md) - 現在と今後のフェーズ
9. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目

英語版の旧expanded README内容は、root READMEをモバイル表示しやすく保つため [docs/readme-expanded.md](docs/readme-expanded.md) に移動されています。

## 主要文書

- [docs/provenance.md](docs/provenance.md) - 出典と公開ソース系譜
- [AUTHORSHIP.md](AUTHORSHIP.md) - 著作者表示と責任境界
- [NOTICE.md](NOTICE.md) - notice、帰属、AI支援境界
- [CITATION.cff](CITATION.cff) - 引用メタデータ
- [docs/deferred-work-restart-conditions.md](docs/deferred-work-restart-conditions.md) - deferred work の再開条件
- [docs/current-task-inventory.md](docs/current-task-inventory.md) - 現在のtask inventory
- [docs/external-review-package-note.md](docs/external-review-package-note.md) - 外部レビュー向けの短い読書パッケージ
- [docs/external-review-readiness-checklist.md](docs/external-review-readiness-checklist.md) - 認証ではないレビュー準備チェックリスト
- [docs/progress-map.md](docs/progress-map.md) - 概算の進捗・gate・停止条件マップ
- [docs/zenn-level-2-repository-walkthrough-readiness.md](docs/zenn-level-2-repository-walkthrough-readiness.md) - 公開説明向けのrepository walkthrough readiness
- [docs/zenn-publication-readiness-plan.md](docs/zenn-publication-readiness-plan.md) - 認証ではない公開準備gate
- [docs/api-future-shape.md](docs/api-future-shape.md) - 将来APIの設計preview。実装ではない
- [docs/external-product-connection-survey.md](docs/external-product-connection-survey.md) - 外部connection surfaceの観測note
- [docs/connector-target-matrix.md](docs/connector-target-matrix.md) - 将来connector target matrix。synthetic-firstであり実装ではない
- [formal/lean/README.md](formal/lean/README.md) - Lean形式化の境界

## 例

最小例は `examples/` にあります。

例の目的、制限事項、読み順については [docs/example-index.md](docs/example-index.md) を参照してください。

これらは説明用の例であり、法的責任、道徳的責任、安全性、公平性、遵法性、本番利用可能性を主張するものではありません。

## 軽量チェック

対象範囲を限定した構造チェッカーは [scripts/check_examples.py](scripts/check_examples.py) にあります。

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

別の、対象範囲を限定した確認結果チェッカーは [scripts/check_review_results.py](scripts/check_review_results.py) にあります。

```bash
python scripts/check_review_results.py
```

checkerやworkflowの通過結果は、認証済み、安全、遵法、公平、法的に有効、道徳的に解決済み、制度的に承認済み、本番利用可能、またはAIへ最終責任が移転されたことを意味しません。

## リポジトリ原則

このリポジトリ自体も Responsibility Pathway として運用されます。

読者は、主張から定義へ、定義から仕様へ、仕様から形式化へ、形式化から前提へ戻れるべきです。

## 境界

すべての定義と主張について、人間の著作者が責任を持ちます。AI tools は草案作成や実装を支援しますが、責任を引き受けません。

## ライセンスとnotice

このリポジトリは [MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono (小野昭久).

再利用、改変、配布、sublicensing はライセンス条件に従って許可されます。ただし、著作権表示とライセンス表示を保持する必要があります。

著作者表示、帰属、AI支援、責任境界については [NOTICE.md](NOTICE.md) を参照してください。
