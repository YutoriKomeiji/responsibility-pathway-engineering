# Responsibility Pathway Engineering

[![Value Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml)
[![Security Hygiene](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml)
[![Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml)

**AIエージェントの「提案」と「実行してよい」を分ける、責任判断のためのOSSです。**

Responsibility Pathway Engineering（責任経路工学 / RPE）は、AIや自動化システムが外部操作へ進む前に、適用する要件、承認・証拠の不足、判断理由、次の責任担当を機械可読な形で確認するためのPythonベースの責任評価レイヤーです。

## 何を解決するのか

AIエージェントでは、モデルが「この操作を行う」と提案したことが、そのまま「システムが実行してよい」という扱いにつながることがあります。

RPEは、その間に小さな判断ポイントを追加します。

- 必要な承認や証拠がなければ、黙って続行せず`human_gate`などの判断を返す
- 続行・保留・人間判断・拒否の理由を、安定した理由コードで返す
- 評価時の証拠と、外部システムで実際に処理が完了した証拠を混同しない
- 既存のエージェントや実行基盤の前段に追加でき、RPE自身は実行主体にならない

最短の比較デモは次で確認できます。

```bash
python scripts/value_demo.py
```

詳しくは [`docs/why-rpe.md`](docs/why-rpe.md) を参照してください。

```text
AIが操作を提案
      ↓
RPEが要件・承認・証拠・ガバナンス状態を評価
      ↓
allow / hold / human_gate / deny
      ↓
理由コード・不足情報・責任の引き渡し先
      ↓
既存の実行基盤、人間、制度、後段ランタイム
```

## 今すぐ使える範囲

現在の公開実装では、次を利用できます。

- 複数のRequirement Packに対する適用判定と評価
- 互換性を維持したPython API `evaluate_action()`
- ガバナンスを必須にしたPython API `evaluate_governed_action()`
- Requirement Packとガバナンス情報のID・バージョン固定
- RESTリファレンスAPI
- MCP stdioツール
- OpenAPI 3.1定義
- 呼び出し元のJSON文字列または明示指定したローカルファイルからの読み込み
- `authority_effect = none`、`decision_scope = evaluation_only`を保持する責任引き渡し情報
- スキーマ、テスト用フィクスチャ、回帰テスト、CIチェック

現在の詳細な実装状態は [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md) に記録しています。

## 導入

現在のリファレンス実装はPython 3.11+で動作し、追加の外部依存はありません。

```bash
python -m pip install .
```

### 互換API

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

### ガバナンス必須API

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

ガバナンス必須の経路では、次の順で評価します。

```text
入力受付
  ↓
契約バージョンの互換性
  ↓
Requirement Packとガバナンス情報の結び付け
  ↓
ガバナンス状態の確認
  ↓
適用条件の判定
  ↓
要件評価
  ↓
総合判断
  ↓
責任の引き渡し情報
```

## 対応インターフェース

| インターフェース | 互換API | ガバナンス必須API | ドキュメント |
|---|---|---|---|
| Python | `evaluate_action()` | `evaluate_governed_action()` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| REST | `POST /v1/evaluate` | `POST /v1/evaluate/governed` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| MCP stdio | `rpe_evaluate_action` | `rpe_evaluate_governed_action` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |
| OpenAPI 3.1 | 両方を定義 | 両方を定義 | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |

これらのアダプターは提案された操作を評価します。外部操作の実行、デプロイ承認、リリース公開、外部作用の確認、最終責任の移転は行いません。

## 重要な権限境界

RPEの`allow`は**評価結果**であり、実行許可トークンではありません。

RPE単体では次を行いません。

- 外部操作を実行する
- デプロイを承認する
- 外部システムで処理が完了したことを検証する
- APIレスポンスやレシートだけを外部作用の証明として扱う
- 修復可能という理由だけで修復権限を付与する
- 再開可能という理由だけで再開権限を付与する
- 最終責任をAIへ移す

**評価時の証拠と、外部作用の証拠は別です。** 修復準備と修復権限、再開準備と再開権限も分けて扱います。

## ローカル読み込みの範囲

現在のローダーが受け入れるのは、次の2種類です。

- 呼び出し元から渡されたUTF-8 JSON
- 明示指定されたローカルファイル

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

現在のローダーはURL取得、外部レジストリ探索、パッケージの自動インストール、取得元の信頼判定を行いません。

ファイルを読めたことは、そのデータが正しい、承認済み、法的に有効、現在の状況に適用できることを意味しません。

## デモと公開サイト

価値を最短で確認するデモ:

```bash
python scripts/value_demo.py
```

より広い評価フローを確認するデモ:

```bash
python scripts/demo.py
```

ブラウザ向けの公開カタログ: [`site/index.html`](site/index.html)

デモやCIの成功は、そのテスト条件でチェックが通ったことを示します。セキュリティ認証、法令適合、本番承認、実環境でのリスク削減効果、外部作用の完了証明ではありません。

## 開発中の範囲と既知の制約

RPEは継続開発中ですが、明示された範囲では実際に試して統合できます。リポジトリ全体を一律に「利用不可」とは扱いません。

現在、RPE自身が提供していない主な領域は次のとおりです。

- 本番環境向けの認証・認可基盤
- リモート取得元の信頼判定
- 外部操作の実行・リトライ・照合・修復・再開
- 任意の環境に対するセキュリティ保証
- 自動的な法令解釈・適合判定・認証

利用時は、対象インターフェースの対応範囲と既知の制約を確認してください。バグ、攻撃事例、統合上の問題、反例、改善提案を歓迎します。

- [サポート](SUPPORT.md)
- [セキュリティ報告](SECURITY.md)
- [コントリビューション](CONTRIBUTING.md)

## 長期方向

RPEは、法令、公的ガイドライン、標準、組織ポリシー、専門職上の義務などについて、人間や制度が確認した解釈を、限定された機械可読コントロールとして扱える公開基盤を目指しています。

RPE自身が法令やガイドラインを自動解釈したり、法的・組織的な権限を生成したりすることは設計目標ではありません。

## 検証・保証・公開ガバナンス

RPEは「安全です」という一括した主張ではなく、対象と条件を限定した検証可能な主張を積み上げます。

形式化されたモデルで証明できる性質があっても、それだけでPython実装全体、入力データの正当性、法的有効性、本番環境の安全性まで証明されたとは扱いません。

詳しくは [`docs/verification-assurance-and-open-governance.md`](docs/verification-assurance-and-open-governance.md) と [`docs/claim-boundary-promotion.ja.md`](docs/claim-boundary-promotion.ja.md) を参照してください。

## 主要リンク

- [RPEを使う理由](docs/why-rpe.md)
- [現在のM2実装状態](docs/m2-governed-integration-current.md)
- [Python API](docs/python-package-api.md)
- [Requirement Packガバナンス](docs/requirement-pack-governance.md)
- [互換性ポリシー](docs/contract-compatibility-policy.md)
- [ロードマップ](ROADMAP.md)
- [公開カタログ](site/index.html)
- [AI/Search Reader](READMEforAI.md)

## 開発とライセンス

著作者: **Akihisa Ono（小野昭久）**  
Repository affiliation: Independent

RPEはOpen Constructionとして [Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて開発されています。方向性、レビュー、マージ、公開上の主張、デプロイ判断、最終責任は人間のメンテナーが担います。

[MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono（小野昭久）。
