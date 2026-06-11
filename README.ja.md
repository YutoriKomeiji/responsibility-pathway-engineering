# Responsibility Pathway Engineering

著作者: Akihisa Ono (小野昭久)

このリポジトリにおける所属表記: Independent

責任経路工学（Responsibility Pathway Engineering）は、人間・AI・組織・制度・業務システムのあいだで、責任がどのように発生し、移動し、停止し、修復され、戻るのかを扱う設計思想です。

本リポジトリは責任追及のためではなく、責任が戻る経路を設計・記述・形式化することを目的とします。

## 状態

Early public specification.

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
4. [docs/phase-1-6-plan.md](docs/phase-1-6-plan.md) - 次の軽量検証フェーズ計画
5. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目
6. [docs/definition.md](docs/definition.md) - 中核定義
7. [docs/eight-elements.md](docs/eight-elements.md) - 8要素モデル
8. [docs/repository-governance.md](docs/repository-governance.md) - リポジトリ運営方針
9. [docs/development-process.md](docs/development-process.md) - 開発プロセス
10. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - schema間の対応関係
11. [docs/validation-checklist.md](docs/validation-checklist.md) - 境界付き検証チェックリスト
12. [docs/validator-boundary.md](docs/validator-boundary.md) - 軽量検証ツールの境界
13. [docs/example-index.md](docs/example-index.md) - 例の索引と読み方
14. [docs/example-review-notes.md](docs/example-review-notes.md) - 例に対する初期レビュー記録

## 例

最小例は `examples/` にあります。

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - AI支援ノードから人間の判断主体へ責任を戻す最小例
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - 証拠不足や曖昧さを検知した後、修復経路へ接続する最小例
- [examples/suspended-pathway.yaml](examples/suspended-pathway.yaml) - 一時停止ライフサイクル状態の最小例

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

チェッカーの境界については [docs/validator-boundary.md](docs/validator-boundary.md) を参照してください。

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
