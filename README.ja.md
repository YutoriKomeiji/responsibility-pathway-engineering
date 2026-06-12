# Responsibility Pathway Engineering

著作者: Akihisa Ono (小野昭久)

このリポジトリにおける所属表記: Independent

責任経路工学（Responsibility Pathway Engineering）は、人間・AI・組織・制度・業務システムのあいだで、責任がどのように発生し、移動し、停止し、修復され、戻るのかを扱う設計思想です。

本リポジトリは責任追及のためではなく、責任が戻る経路を設計・記述・形式化することを目的とします。

## 状態

Early public specification.

本リポジトリは、意図的に小さく、仕様優先で維持されています。現在の核が大規模実装よりも定義、例、ライフサイクル境界、チェッカー境界、除外される主張を優先する理由は [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) を参照してください。

Phase 2 は開始済みです。現在の Lean 形式化には、[formal/lean/ResponsibilityPathway/Core.lean](formal/lean/ResponsibilityPathway/Core.lean) に最小 node/pathway model と scoped lifecycle-invariant set が含まれています。これらの invariant は構造的・前提依存・非認証のものです。

Phase 2 の Lean spine は小さな module に分割済みで、`Core.lean` は安定した入口として維持されています。詳細は [formal/lean/README.md](formal/lean/README.md) と [docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md) を参照してください。

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
2. [LUMINALIA.md](LUMINALIA.md) - 設計思想
3. [ROADMAP.md](ROADMAP.md) - 現在と今後のフェーズ
4. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目
5. [docs/minimal-core-rationale.md](docs/minimal-core-rationale.md) - 現在のリポジトリを意図的に小さく保つ理由
6. [docs/phase-1-6-plan.md](docs/phase-1-6-plan.md) - 軽量検証とライフサイクル例の現在地
7. [formal/lean/README.md](formal/lean/README.md) - Lean形式化の境界と現在の invariant candidates
8. [docs/phase-2-lean-split-plan.md](docs/phase-2-lean-split-plan.md) - Phase 2 Lean split plan と non-goals
9. [docs/definition.md](docs/definition.md) - 中核定義
10. [docs/eight-elements.md](docs/eight-elements.md) - 8要素モデル
11. [docs/repository-governance.md](docs/repository-governance.md) - リポジトリ運営方針
12. [docs/development-process.md](docs/development-process.md) - 開発プロセス
13. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - schema間の対応関係
14. [docs/validation-checklist.md](docs/validation-checklist.md) - 境界付き検証チェックリスト
15. [docs/validator-boundary.md](docs/validator-boundary.md) - 軽量検証ツールの境界
16. [docs/checker-coverage.md](docs/checker-coverage.md) - 現在のライフサイクル対応チェッカー範囲
17. [docs/example-index.md](docs/example-index.md) - 例の索引と読み方
18. [docs/example-review-notes.md](docs/example-review-notes.md) - 例に対する初期レビュー記録

## 例

最小例は `examples/` にあります。

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - AI支援ノードから人間の判断主体へ責任を戻す最小例
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - 証拠不足や曖昧さを検知した後、修復経路へ接続する最小例
- [examples/suspended-pathway.yaml](examples/suspended-pathway.yaml) - 一時停止ライフサイクル状態の最小例
- [examples/returning-pathway.yaml](examples/returning-pathway.yaml) - 復帰ライフサイクル状態の最小例
- [examples/closed-pathway.yaml](examples/closed-pathway.yaml) - 閉鎖ライフサイクル状態の最小例

例の目的、境界、今後の追加候補については [docs/example-index.md](docs/example-index.md) を参照してください。

これらは説明用の例であり、法的責任、道徳的責任、安全性、公平性、遵法性、本番利用可能性を主張するものではありません。

## 軽量チェック

境界付きの構造チェッカーは [scripts/check_examples.py](scripts/check_examples.py) にあります。

最小限のPython依存関係をインストールして実行します。

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

同じ境界付き構造チェックは、examples、チェッカー、requirements、またはworkflowが変更された場合に、GitHub Actions の [.github/workflows/check-examples.yml](.github/workflows/check-examples.yml) でも実行されます。

このチェッカーは、限定された構造シグナルと明示された責任境界フィールドだけを確認します。通過結果は、認証済み、安全、遵法、公平、法的に有効、道徳的に解決済み、本番利用可能であることを意味しません。

チェッカーの境界については [docs/validator-boundary.md](docs/validator-boundary.md)、現在のチェック範囲については [docs/checker-coverage.md](docs/checker-coverage.md) を参照してください。

## Lean形式化

現在の Phase 2 Lean work は意図的に最小です。

Lean spine は次に分割されています。

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

`Core.lean` は安定した import entry point として維持されています。

現在、次の6本の scoped invariant candidates が含まれています。

1. 現行最小前提における AI final-responsibility boundary
2. AI return-point boundary
3. repair-record boundary
4. suspension review/return boundary
5. returning no-automatic-continuation boundary
6. closure evidence/reopening boundary

AI final-responsibility boundary は、AI があらゆる将来の法制度・制度設計の下で責任を持ちえないという絶対命題ではありません。現行の最小 RPE model では artificial legal-personhood layer を仮定していないため、AI node を final responsibility holder として扱わない、という前提付きの境界です。将来、法的・制度的・国家的・国際的・利用者/提供者契約上の層を導入する場合は、その層を明示的にモデル化する必要があります。

Lean 形式化は、法的有効性、安全性、遵法性、公平性、道徳的責任の解決、制度的認証、本番利用可能性を示すものではありません。

Lean CI またはローカル Lean build 検証は、まだ本リポジトリでは確立していません。現在の GitHub Actions 自動化は、境界付き Python example checker のみを対象にしています。

## 範囲

- 定義
- 8要素モデル
- YAML仕様
- Lean形式化候補
- 実装例

## リポジトリ原則

本リポジトリ自体を、一つの責任経路として運用します。

読者は、主張から定義へ、定義から仕様へ、仕様から形式化へ、形式化から前提へと戻れる必要があります。

## 境界

本リポジトリは完成した標準や法理論を主張するものではありません。定義と公開内容の責任は人間の著者が負います。AIは補助者であり責任主体ではありません。

## ライセンスと通知

本リポジトリは [MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono (小野昭久).

利用、改変、再配布、サブライセンスはライセンス条件に従って許可されます。ただし、著作権表示およびライセンス表示を保持してください。

著作、帰属、AI補助、責任境界については [NOTICE.md](NOTICE.md) を参照してください。
