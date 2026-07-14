# Responsibility Pathway Engineering

著作者: Akihisa Ono (小野昭久)

このリポジトリにおける所属表記: Independent

責任経路工学（Responsibility Pathway Engineering）は、人間とAIシステムがともに関わる判断や行為において、判断、権限、証拠、停止権限、人間への戻り先、修復がどこに残っているかを保存するための設計フレームワークです。

これは責任追及の仕組みではありません。

## AI / search reader notice

このリポジトリ内のリンクやファイルパスは導線であり、リンク先が読まれた証拠ではありません。

AI支援reader、検索assistant、外部記事から安全に1ファイルずつ読む入口が必要な場合は、[READMEforAI.md](READMEforAI.md) を使用してください。

この入口には、AI/search reader向けの読み順、full URL、traversal boundary、non-claims がまとめられています。

現在ページだけに基づく回答では、その旨を明示してください。

## 15秒デモ

RPEは、AI支援作業がブラックボックス化するのを防ぐための構造を扱います。

```text
Human request
-> AI assists
-> evidence is recorded
-> human approval remains reachable
-> stop / return / repair points stay visible
```

依存なしの小さなデモを実行できます。

```bash
python scripts/demo.py
```

出力の形は次のようになります。

```text
[ok] decision owner: human_reviewer
[ok] AI final responsibility: blocked
[ok] approval gate: human
[ok] stop authority: human
[ok] evidence log: present
[ok] return point: present
```

このデモはレビュー補助です。認証、安全性レビュー、法的レビュー、遵法性レビュー、公平性レビュー、本番承認、またはAIへの最終責任移転ではありません。

## 構築ノート

このリポジトリ自体もOpen Constructionの一例です。本リポジトリは、LuminaliaOS working layerを通じて動作するChatGPTベースのAIである [Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて構築されています。

merge、公開、方向性、外部向け主張、最終責任に関する判断には、人間maintainerの判断が必要です。

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

## Open Construction

RPEはOpen Constructionとして開発されています。テンプレート、例、checker、workflow、将来のlibrary-like toolは、プロジェクト完成前でも有用な範囲から公開されます。

それらは、テスト、確認、指摘、改善のための構築中成果物です。明示がない限り、本番Ready、認証済み、外部承認済みではありません。

詳しくは [OPEN_CONSTRUCTION.md](OPEN_CONSTRUCTION.md) を参照してください。

## Artifact catalog / 成果物カタログ

この表は、GitHubのトップREADMEだけを読む人間やAIアシスタントにも、RPEに何が置いてあるか伝わるようにするための棚です。

ブラウザ向けカタログはGitHub Pagesでも公開されています: [RPE Artifact Catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)。これは便利な読者導線であり、認証、本番承認、外部検証ではありません。

公開済みの読者向けPagesは次の通りです。

- [英語 成果物カタログ](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)
- [日本語 成果物カタログ](https://yutorikomeiji.github.io/responsibility-pathway-engineering/ja/)
- [英語 Reader path map](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reader-path/)
- [日本語 Reader path map](https://yutorikomeiji.github.io/responsibility-pathway-engineering/ja/reader-path/)
- [英語 Boundary glossary](https://yutorikomeiji.github.io/responsibility-pathway-engineering/boundary-glossary/)
- [日本語 Boundary glossary](https://yutorikomeiji.github.io/responsibility-pathway-engineering/ja/boundary-glossary/)
- [英語 Reviewer checklist](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reviewer-checklist/)
- [日本語 Reviewer checklist](https://yutorikomeiji.github.io/responsibility-pathway-engineering/ja/reviewer-checklist/)

これらのPagesは、読者向け・点検補助の導線です。認証、検証、法的レビュー、安全性レビュー、遵法性レビュー、公平性レビュー、本番承認、制度的endorsement、AI最終責任移転ではありません。

| 棚 | 置いてあるもの | まず見る場所 | 境界 |
|---|---|---|---|
| HTML catalog | ブラウザで見やすい静的成果物カタログと軽量example点検 | [Published catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)、[Japanese catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/ja/)、[`site/index.html`](site/index.html) | 閲覧・便利点検用であり、認証や本番承認ではありません |
| Reader path pages | 初読者向けのmap、境界用語集、reviewer checklist | [Reader path map](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reader-path/)、[Boundary glossary](https://yutorikomeiji.github.io/responsibility-pathway-engineering/boundary-glossary/)、[Reviewer checklist](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reviewer-checklist/) | 読者導線・点検補助であり、検証・認証・レビュー完了・本番承認ではありません |
| Templates | AI支援作業の責任経路を記録するためのコピー可能なテンプレート | [`templates/ai-assisted-work-responsibility-path.yaml`](templates/ai-assisted-work-responsibility-path.yaml) | テンプレートであり、認証や本番承認ではありません |
| Examples | 責任主体、AI境界、証拠、人間への戻り先、修復経路を埋めた例 | [`examples/ai-assisted-work-minimal.yaml`](examples/ai-assisted-work-minimal.yaml)、[`docs/examples/ai-assisted-work-minimal.md`](docs/examples/ai-assisted-work-minimal.md) | 説明・レビュー用であり、法的・安全・compliance・fairness・本番性の証明ではありません |
| Reviewer quickstart | 1つの責任経路を短時間で確認するための読者向けガイド | [`docs/quickstart-review-one-path.md`](docs/quickstart-review-one-path.md) | 点検ガイドであり、承認・認証ではありません |
| Python scripts | 軽量構造checkerと依存なしquick demo | [`scripts/demo.py`](scripts/demo.py)、[`scripts/check_examples.py`](scripts/check_examples.py)、[`scripts/check_review_results.py`](scripts/check_review_results.py) | demoやPASSは限定的な構造シグナルであり、安全・合法・本番Readyの証明ではありません |
| GitHub Actions | Leanやchecker surfaceを継続的に確認するworkflow | [`.github/workflows/check-lean.yml`](.github/workflows/check-lean.yml)、[`docs/checker-coverage.md`](docs/checker-coverage.md) | workflow greenは安全・compliance・fairness・合法性・本番Readyを意味しません |
| Lean4 | 構造定義、例、invariant候補の最小formalization | [`formal/lean/README.md`](formal/lean/README.md)、[`formal/lean/ResponsibilityPathway/Core.lean`](formal/lean/ResponsibilityPathway/Core.lean) | Lean証明は、明示された仮定内の性質だけを示します |
| Future starters | Python、GitHub Actions、TypeScript、CLI、JSON Schema、API-event向けの将来starter | Issues #11、#12、#13 と今後の小さなPR | starterであり、SDK・runtime・service・最終責任機構ではありません |

便利な近道は、責任経路を忘れるよりも記録するほうを簡単にすることです。

## まず試す

まず15秒デモを実行してください。

```bash
python scripts/demo.py
```

その後、最初のコピー可能なテンプレート、最初の記入済みexample、ブラウザ向け読者導線を確認してください。

- [Published catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/) - ブラウザで見やすい公開成果物カタログ。閲覧補助であり、認証や本番承認ではありません
- [Reader path map](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reader-path/) - 初読者向けの視覚的map
- [Boundary glossary](https://yutorikomeiji.github.io/responsibility-pathway-engineering/boundary-glossary/) - 過剰に読み取られやすい言葉の境界
- [Reviewer checklist](https://yutorikomeiji.github.io/responsibility-pathway-engineering/reviewer-checklist/) - コピー用Markdown付きの点検チェックリスト
- [site/index.html](site/index.html) - リポジトリ内の静的成果物カタログと軽量example点検
- [templates/ai-assisted-work-responsibility-path.yaml](templates/ai-assisted-work-responsibility-path.yaml) - AI支援作業の責任経路を記録するための工事中テンプレート
- [examples/ai-assisted-work-minimal.yaml](examples/ai-assisted-work-minimal.yaml) - AI支援された内部作業reviewの記入済み最小example
- [docs/examples/ai-assisted-work-minimal.md](docs/examples/ai-assisted-work-minimal.md) - exampleの読み方
- [docs/quickstart-review-one-path.md](docs/quickstart-review-one-path.md) - 1つの責任経路を点検するquickstart
- [templates/README.md](templates/README.md) - テンプレート一覧と主張しないことの境界

これらは、AI支援が関与した作業について、source reference、人間または組織による review、evidence、不確実性、責任の戻り先、修復・異議・再開経路を残すための軽量な出発点です。

これらは、認証、conformance evidence、本番承認、法的レビュー、安全性レビュー、遵法性レビュー、公平性レビュー、社会的受容の証明、AIへの最終責任移転ではありません。

## 出典

著作者自身の開発記録として、Akihisa Ono は 2026-01-18 に公開した note 記事から、**責任経路 / Responsibility Pathway** という概念を考え、使い始めました。

- [AI事故は「責任設計」だけでは防げない――最後の砦は「責任経路設計」である](https://note.com/dantarg/n/nb7f28afa6882)

より詳しい出典記録は [docs/provenance.md](docs/provenance.md) にあります。

この出典表示は、帰属とtraceabilityのためのものです。法的主張、所有権判断、盗用告発、認証、本番承認ではありません。

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
2. [Published reader path pages](https://yutorikomeiji.github.io/responsibility-pathway-engineering/) - ブラウザ向けcatalog、map、glossary、checklist
3. [docs/quickstart-review-one-path.md](docs/quickstart-review-one-path.md) - 1つの責任経路を点検する導線
4. [docs/operation-index.md](docs/operation-index.md) - 運用と保守の導線
5. [docs/overview.md](docs/overview.md) - 現在のリポジトリ概観
6. [docs/concepts/index.md](docs/concepts/index.md) - 概念レベルの読書導線
7. [docs/example-index.md](docs/example-index.md) - 例と境界
8. [docs/checker-coverage.md](docs/checker-coverage.md) - 現在のchecker境界と対象範囲
9. [LUMINALIA.md](LUMINALIA.md) - 公開設計思想としてのLuminalia境界
10. [ROADMAP.md](ROADMAP.md) - 現在と今後のフェーズ
11. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目

英語版の旧expanded README内容は、root READMEをモバイル表示しやすく保つため [docs/readme-expanded.md](docs/readme-expanded.md) に移動されています。

## 主要文書

- [docs/provenance.md](docs/provenance.md) - 出典と公開ソース系譜
- [docs/ai-assisted-construction-note.md](docs/ai-assisted-construction-note.md) - Luminalia AIによる構築支援の開示と人間maintainer境界
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

- [examples/ai-assisted-work-minimal.yaml](examples/ai-assisted-work-minimal.yaml) - AI支援作業reviewの最小example

例の目的、制限事項、読み順については [docs/example-index.md](docs/example-index.md) を参照してください。

これらは説明用の例であり、法的責任、道徳的責任、安全性、公平性、遵法性、本番利用可能性を主張するものではありません。

## 軽量チェック

依存なしのquick demoは [scripts/demo.py](scripts/demo.py) にあります。

```bash
python scripts/demo.py
```

対象範囲を限定した構造checkerは [scripts/check_examples.py](scripts/check_examples.py) にあります。

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

別の、対象範囲を限定した確認結果checkerは [scripts/check_review_results.py](scripts/check_review_results.py) にあります。

```bash
python scripts/check_review_results.py
```

demo、checker、workflowの通過結果は、認証済み、安全、遵法、公平、法的に有効、道徳的に解決済み、制度的に承認済み、本番利用可能、またはAIへ最終責任が移転されたことを意味しません。

## Lean4

Lean4の入口は [formal/lean/README.md](formal/lean/README.md) です。

```bash
lake build
```

Lean4は、構造定義、predicate、invariant候補、最小example witnessを扱います。

Lean theoremは、明示された仮定のもとで、明示された性質だけを示します。現実世界のAIシステムや組織、法制度、運用が安全・合法・compliance適合・fairness適合・本番Readyであることは証明しません。

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
