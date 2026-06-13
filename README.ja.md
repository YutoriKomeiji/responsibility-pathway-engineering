# Responsibility Pathway Engineering

著作者: Akihisa Ono (小野昭久)

このリポジトリにおける所属表記: Independent

責任経路工学（Responsibility Pathway Engineering）は、人間・AI・組織・制度・業務システムのあいだで、責任がどのように発生し、移動し、停止し、修復され、戻るのかを扱う設計思想です。

本リポジトリは責任追及のためではなく、責任が戻る経路を設計・記述・形式化することを目的とします。

## 出典と公開ソース系譜

著作者自身の開発記録として、Akihisa Ono は 2026-01-18 に公開した note 記事「AI事故は『責任設計』だけでは防げない――最後の砦は『責任経路設計』である」から、**責任経路 / Responsibility Pathway** という概念を考え、使い始めました。

この概念に関する著作者の最初の公開ソース:

- https://note.com/dantarg/n/nb7f28afa6882

当時、著作者は検索結果および辞書を確認し、**責任経路** または **Responsibility Pathway** がこの設計概念を指す一般的な既存用語として確認できないことを確認しました。そのため、既存の標準用語として扱うのではなく、著作者自身がこの概念を定義しました。

最初の定式化は **責任経路を設計する** という表現から始まりました。これは、責任を単なる帰属点としてではなく、判断がどこで発生し、どこで変化し、どこで停止でき、どこで人間へ戻り、運用中にその経路がどのように構造的に維持されるかを設計する、という考え方です。

Responsibility Pathway Design / Responsibility Pathway Engineering の公開ソース系譜に含まれる主要記事は次の通りです。

- 「AI事故は『責任設計』だけでは防げない――最後の砦は『責任経路設計』である」 — https://note.com/dantarg/n/nb7f28afa6882
- 「2026年、AI安全の争点は『ガバナンス』ではない」 — https://note.com/dantarg/n/n7e55212b8ac4
- 「責任経路設計とは何か」 — https://note.com/dantarg/n/na7a65ee28906
- 「責任あるAI（Responsible AI）が実装できない本当の理由」 — https://note.com/dantarg/n/n77367658521c

これらの記事は、本リポジトリの仕様化作業の前後にある、概念・用語・問題意識・初期フレーミングの公開ソース系譜として扱います。

本リポジトリは、この公開ソース系譜を、公開仕様、例、schema、対象範囲を限定した checker、review note、形式化候補へ展開するものです。出典を明記する目的は、用語、概念、およびプロジェクト自体の責任経路を追跡可能にすることです。

この出典記録は、帰属と traceability のための記述です。法的主張、所有権の裁定、盗用・剽窃の告発、認証、本番利用承認ではありません。

## 状態

Early public specification.

本リポジトリは、意図的に小さく、仕様優先で維持されています。現在の核が大規模実装よりも定義、例、ライフサイクル上の制限事項、チェッカーの対象範囲、主張しないことを優先する理由は [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) を参照してください。

Phase 2 は開始済みです。現在の Lean 形式化には、[formal/lean/ResponsibilityPathway/Core.lean](formal/lean/ResponsibilityPathway/Core.lean) に最小 node/pathway model と scoped lifecycle-invariant set が含まれています。これらの invariant は構造的・前提依存・認証ではありません。

Phase 2 の Lean spine は小さな module に分割済みで、`Core.lean` は安定した入口として維持されています。詳細は [formal/lean/README.md](formal/lean/README.md)、[docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md)、[docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md)、[docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md) を参照してください。

企業向けの初期導入ガイドは [docs/enterprise-implementation-profile.md](docs/enterprise-implementation-profile.md) にあります。この文書は、最小形式核を業務手順、証拠記録、確認手順、組織判断層へ接続する方法を示します。ただし、RPE を本番検証器、遵法性エンジン、安全性認証ツール、法的判断システムとして扱うものではありません。

責任経路記録をあとから確認・再確認するための平易な手順は [docs/responsibility-pathway-record-review.md](docs/responsibility-pathway-record-review.md) にあります。この文書は、確認結果を法的・安全性・遵法性・公平性・道徳的解決・本番利用可能性の認証として扱わないための制限事項も示します。

現在の Phase 2.5 企業導入・責任経路記録レビュー snapshot は [docs/phase-2-5-current-snapshot.md](docs/phase-2-5-current-snapshot.md) にあります。

対象範囲を限定した確認結果 schema は [spec/review-result.schema.yaml](spec/review-result.schema.yaml) にあります。この schema は、確認結果が何を確認し、何を確認しておらず、何を主張していないかを記録するための公開仕様です。

対象範囲を限定した確認結果チェッカーは [scripts/check_review_results.py](scripts/check_review_results.py) にあります。このチェッカーは、review-result fixture に required fields、許可された review scope/status、期待される not-checked / not-claimed 項目、responsibility-boundary flags があるかを確認します。これは構造確認であり、認証ではありません。

`Check review-result fixtures` GitHub Actions workflow は、`main` の commit `aaaece3` に対する run `#1` で green 観測済みです。この green は、その時点の bounded repository-maintenance check が通ったことだけを意味し、認証ではありません。

Phase 3 の入口となる制限事項は [docs/reference-implementation-boundary.md](docs/reference-implementation-boundary.md) にあります。Reference implementation を追加する前に読む文書です。

Source-aligned Action Class Matrix には、Class A-F を読むための classification-only fixture、Class C Approval-Required 内部文書更新例、Class D Reversible External Action 例、Class F Emergency Stop 例が追加済みです。これらの例は構造的な例であり、認証ではありません。

Phase 3.1 は adapter boundary と runtime-event bridge から開始しています。[docs/adapter-boundary.md](docs/adapter-boundary.md) と [docs/phase-3-1-current-snapshot.md](docs/phase-3-1-current-snapshot.md) を参照してください。最初の runtime-event-to-pathway 例は [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml) です。これは synthetic、vendor-neutral、review-required の draft example であり、service-specific connector や production runtime ではありません。

リポジトリ運用モデルは [docs/repository-operation-model.md](docs/repository-operation-model.md) にあります。この文書は、多段階更新運用、snapshot、sync log、roadmap note、checker 観測方針、長文ファイル更新方針、認証ではない運用上の制限事項を記録します。

運用文書索引は [docs/operation-index.md](docs/operation-index.md) にあります。この文書は、保守状況ごとにどの運用文書を読むべきかを整理します。

## 著作者と引用

本リポジトリは Akihisa Ono (小野昭久) によって、独立した公開仕様および設計フレームワークとして著作・保守されています。

著作者表示、帰属、所属表記の明確化、引用メタデータについては次を参照してください。

- [AUTHORSHIP.md](AUTHORSHIP.md)
- [AUTHORS.md](AUTHORS.md)
- [CITATION.cff](CITATION.cff)
- [NOTICE.md](NOTICE.md)

## はじめに読むもの

初めて読む人、未来の保守者、AIによる継続作業では、次の順番で読むことを推奨します。

1. [BEACON.md](BEACON.md) - 現在地と再接続点
2. [docs/repository-operation-model.md](docs/repository-operation-model.md) - 多段階更新、snapshot、sync log、長文ファイル更新方針のためのリポジトリ運用モデル
3. [docs/operation-index.md](docs/operation-index.md) - 運用関連文書の索引
4. [docs/overview.md](docs/overview.md) - source alignment 後の現在のリポジトリ概観
5. [docs/source-alignment/zenn-source-alignment-synthesis.md](docs/source-alignment/zenn-source-alignment-synthesis.md) - Zenn資料からの source-alignment synthesis
6. [docs/concepts/core-elements.md](docs/concepts/core-elements.md) - 8要素モデルに接続された operational roles and controls
7. [docs/action-class-matrix.md](docs/action-class-matrix.md) - source-aligned Class A-F action classification design aid
8. [examples/action-class-matrix-minimal.yaml](examples/action-class-matrix-minimal.yaml) - Action Class Matrix の classification-only fixture
9. [examples/internal-document-update.yaml](examples/internal-document-update.yaml) - Class C Approval-Required 内部文書更新例
10. [examples/emergency-stop-flow.yaml](examples/emergency-stop-flow.yaml) - Class F Emergency Stop / stop-and-await 例
11. [examples/reversible-external-action.yaml](examples/reversible-external-action.yaml) - Class D Reversible External Action 例
12. [docs/adapter-boundary.md](docs/adapter-boundary.md) - runtime connector の前に読む adapter の対象範囲と制限事項
13. [docs/phase-3-1-current-snapshot.md](docs/phase-3-1-current-snapshot.md) - Phase 3.1 adapter / runtime-event の現在地
14. [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml) - synthetic runtime-event-to-pathway draft example
15. [LUMINALIA.md](LUMINALIA.md) - 設計思想
16. [ROADMAP.md](ROADMAP.md) - 現在と今後のフェーズ
17. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目
18. [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) - 現在のリポジトリを意図的に小さく保つ理由
19. [docs/enterprise-implementation-profile.md](docs/enterprise-implementation-profile.md) - 企業向けの最小導入プロファイルと層の分離
20. [docs/responsibility-pathway-record-review.md](docs/responsibility-pathway-record-review.md) - 責任経路記録を確認・再確認するための平易な手順
21. [docs/phase-2-5-current-snapshot.md](docs/phase-2-5-current-snapshot.md) - Phase 2.5 企業導入・責任経路記録レビューの現在地
22. [docs/reference-implementation-boundary.md](docs/reference-implementation-boundary.md) - Phase 3 reference implementation の前に読む制限事項
23. [docs/phase-1-6-plan.md](docs/phase-1-6-plan.md) - 軽量検証とライフサイクル例の現在地
24. [formal/lean/README.md](formal/lean/README.md) - Lean形式化の対象範囲と現在の invariant candidates
25. [docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md) - Phase 2 Lean の現在地と再開点
26. [docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md) - Phase 2 Lean split plan と non-goals
27. [docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md) - Phase 2 Lean theorem role index
28. [docs/definition.md](docs/definition.md) - 中核定義
29. [docs/eight-elements.md](docs/eight-elements.md) - 8要素モデル
30. [docs/repository-governance.md](docs/repository-governance.md) - リポジトリ運営方針
31. [docs/development-process.md](docs/development-process.md) - 開発プロセス
32. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - schema間の対応関係
33. [spec/review-result.schema.yaml](spec/review-result.schema.yaml) - 対象範囲を限定した確認結果の出力 schema
34. [spec/runtime-event.schema.yaml](spec/runtime-event.schema.yaml) - draft vendor-neutral runtime event schema
35. [docs/validation-checklist.md](docs/validation-checklist.md) - 対象範囲を限定した検証チェックリスト
36. [docs/validator-boundary.md](docs/validator-boundary.md) - 軽量検証ツールの対象範囲と制限事項
37. [docs/checker-coverage.md](docs/checker-coverage.md) - 現在のライフサイクル対応チェッカー範囲
38. [docs/example-index.md](docs/example-index.md) - 例の索引と読み方
39. [docs/example-review-notes.md](docs/example-review-notes.md) - 例に対する初期レビュー記録

## 例

最小例は `examples/` にあります。

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - AI支援ノードから人間の判断主体へ責任を戻す最小例
- [examples/action-class-matrix-minimal.yaml](examples/action-class-matrix-minimal.yaml) - Class A-F を読むための Action Class Matrix classification-only fixture
- [examples/internal-document-update.yaml](examples/internal-document-update.yaml) - Class C Approval-Required 内部文書更新例
- [examples/emergency-stop-flow.yaml](examples/emergency-stop-flow.yaml) - Class F Emergency Stop / stop-and-await 例
- [examples/reversible-external-action.yaml](examples/reversible-external-action.yaml) - rollback / correction path を持つ Class D Reversible External Action 例
- [examples/runtime-event-to-pathway-minimal.yaml](examples/runtime-event-to-pathway-minimal.yaml) - human review を必要とする synthetic runtime-event-to-pathway draft example
- [examples/record-review-minimal.yaml](examples/record-review-minimal.yaml) - 任意の review metadata と、確認結果が保証しないことを含む最小の責任経路記録レビュー例
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - 証拠不足や曖昧さを検知した後、修復経路へ接続する最小例
- [examples/suspended-pathway.yaml](examples/suspended-pathway.yaml) - 一時停止ライフサイクル状態の最小例
- [examples/returning-pathway.yaml](examples/returning-pathway.yaml) - 復帰ライフサイクル状態の最小例
- [examples/closed-pathway.yaml](examples/closed-pathway.yaml) - 閉鎖ライフサイクル状態の最小例

例の目的、制限事項、今後の追加候補については [docs/example-index.md](docs/example-index.md) を参照してください。

これらは説明用の例であり、法的責任、道徳的責任、安全性、公平性、遵法性、本番利用可能性を主張するものではありません。

Review-result output fixture は pathway example とは分けて `fixtures/review-results/` に置かれています。

## 軽量チェック

対象範囲を限定した構造チェッカーは [scripts/check_examples.py](scripts/check_examples.py) にあります。

最小限のPython依存関係をインストールして実行します。

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

同じ構造チェックは、examples、チェッカー、requirements、またはworkflowが変更された場合に、GitHub Actions の [.github/workflows/check-examples.yml](.github/workflows/check-examples.yml) でも実行されます。

このチェッカーは、限定された構造シグナルと明示された責任範囲フィールドだけを確認します。通過結果は、認証済み、安全、遵法、公平、法的に有効、道徳的に解決済み、本番利用可能であることを意味しません。

例に `review_metadata` が含まれる場合、チェッカーは review metadata の構造と、確認結果が保証しないことも任意で確認します。

runtime-event-to-pathway example は、現時点では pathway example としてのみチェックされます。このチェッカーは `spec/runtime-event.schema.yaml` や `examples/adapter-input-event-minimal.json` のような JSON fixture をまだ検証しません。

別の、対象範囲を限定した確認結果チェッカーは [scripts/check_review_results.py](scripts/check_review_results.py) にあります。

```bash
python scripts/check_review_results.py
```

このチェッカーは review-result fixture の構造と責任範囲フィールドの保持だけを確認します。通過結果は、法的検証、安全認証、遵法認証、公平性認証、道徳的解決、制度的認証、本番承認、AIへの最終責任移転を意味しません。

review-result checker は [.github/workflows/check-review-results.yml](.github/workflows/check-review-results.yml) により GitHub Actions でも実行されます。`Check review-result fixtures` workflow は `main` の commit `aaaece3` に対する run `#1` で green 観測済みです。この結果は、その時点の bounded repository-maintenance check が通ったことだけを意味します。

チェッカーの対象範囲と制限事項については [docs/validator-boundary.md](docs/validator-boundary.md)、現在のチェック範囲については [docs/checker-coverage.md](docs/checker-coverage.md) を参照してください。

## Lean形式化

現在の Phase 2 Lean work は意図的に最小です。

Lean spine は次に分割されています。

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

`Core.lean` は安定した import entry point として維持されています。

現在の Phase 2 snapshot は [docs/phase-2-current-snapshot.md](docs/phase-2-current-snapshot.md) にあります。

Theorem role index は [docs/phase-2-lean-theorem-index.md](docs/phase-2-lean-theorem-index.md) にあります。

現在、次の6本の scoped invariant candidates が含まれています。

1. 現行最小前提における AI final-responsibility の制限
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

AI final-responsibility の制限は、AI があらゆる将来の法制度・制度設計の下で責任を持ちえないという絶対命題ではありません。現行の最小 RPE model では artificial legal-personhood layer を仮定していないため、AI node を final responsibility holder として扱わない、という前提付きの制限です。将来、法的・制度的・国家的・国際的・利用者/提供者契約上の層を導入する場合は、その層を明示的にモデル化する必要があります。

Lean 形式化は、法的有効性、安全性、遵法性、公平性、道徳的責任の解決、制度的認証、本番利用可能性を示すものではありません。

最小 Lean toolchain、Lake package、GitHub Actions workflow を追加済みです。

```bash
lake build
```

workflow は [.github/workflows/check-lean.yml](.github/workflows/check-lean.yml) で定義されています。これは現在の Lean package build のみを確認するためのものです。Lean build の通過は、法的有効性、安全性、遵法性、公平性、道徳的責任の解決、制度的認証、本番利用可能性を意味しません。

## 初期スコープ

- 定義
- 8要素モデル
- Runtime responsibility pathways
- Return point model
- Formalization candidates (Lean)
- Reference specifications
- Examples

## リポジトリ原則

このリポジトリ自体も Responsibility Pathway として運用されます。

読者は、主張から定義へ、定義から仕様へ、仕様から形式化へ、形式化から前提へ戻れる必要があります。

## 責任の所在

人間の著作者が、すべての定義と主張に責任を持ちます。AI tools は草案作成や実装を補助しますが、責任を引き受けません。

## ライセンスと通知

このリポジトリは [MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono (小野昭久).

ライセンス条件に従い、著作権表示とライセンス表示を保持する限り、再利用、改変、配布、サブライセンスが可能です。

著作者表示、帰属、AI支援、責任の範囲については [NOTICE.md](NOTICE.md) を参照してください。
