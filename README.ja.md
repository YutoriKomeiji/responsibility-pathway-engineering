# Responsibility Pathway Engineering

責任経路工学（Responsibility Pathway Engineering）は、人間・AI・組織・制度・業務システムのあいだで、責任がどのように発生し、移動し、停止し、修復され、戻るのかを扱う設計思想です。

本リポジトリは責任追及のためではなく、責任が戻る経路を設計・記述・形式化することを目的とします。

## 状態

Early public specification.

## はじめに読むもの

初めて読む人、未来の保守者、AIによる継続作業では、次の順番で読むことを推奨します。

1. [BEACON.md](BEACON.md) - 現在地と再接続点
2. [LUMINALIA.md](LUMINALIA.md) - 設計思想
3. [ROADMAP.md](ROADMAP.md) - 現在と今後のフェーズ
4. [CHANGELOG.md](CHANGELOG.md) - 概念上の節目
5. [docs/definition.md](docs/definition.md) - 中核定義
6. [docs/eight-elements.md](docs/eight-elements.md) - 8要素モデル
7. [docs/repository-governance.md](docs/repository-governance.md) - リポジトリ運営方針
8. [docs/development-process.md](docs/development-process.md) - 開発プロセス
9. [docs/schema-cross-reference.md](docs/schema-cross-reference.md) - schema間の対応関係
10. [docs/validation-checklist.md](docs/validation-checklist.md) - 境界付き検証チェックリスト
11. [docs/example-review-notes.md](docs/example-review-notes.md) - 例に対する初期レビュー記録

## 例

最小例は `examples/` にあります。

- [examples/minimal-pathway.yaml](examples/minimal-pathway.yaml) - AI支援ノードから人間の判断主体へ責任を戻す最小例
- [examples/repair-flow.yaml](examples/repair-flow.yaml) - 証拠不足や曖昧さを検知した後、修復経路へ接続する最小例

これらは説明用の例であり、法的責任、道徳的責任、安全性、公平性、遵法性、本番利用可能性を主張するものではありません。

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
