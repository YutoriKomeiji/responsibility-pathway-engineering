# Zenn Publication Japanese Reader Note

この文書は、Zenn などの日本語公開記事から本リポジトリへ来た読者のための短い案内です。

これは公開記事そのものではありません。また、外部レビュー結果、認証、標準化完了、conformance、法的判断、安全性認証、遵法性認証、公平性認証、本番利用承認、API 実装、Connector 実装、AI への最終責任移転を意味しません。

## まず読むもの

日本語の公開記事から来た場合は、まず次を読んでください。

1. `README.ja.md` - 日本語入口
2. `BEACON.md` - 現在地と再接続入口
3. `docs/operation-index.md` - 目的別の文書案内
4. `docs/overview.md` - 現在のリポジトリ概観
5. `docs/zenn-publication-readiness-plan.md` - Zenn 公開前の判断基準
6. `docs/zenn-publication-readiness-connection.md` - Zenn 公開計画と公開入口の接続
7. `docs/external-review-package-note.md` - 外部レビュー向け読書パッケージ
8. `docs/external-review-readiness-checklist.md` - 認証ではないレビュー準備チェックリスト
9. `docs/progress-map.md` - 概算の進捗・gate・停止条件
10. `docs/api-future-shape.md` - 将来 API の設計プレビュー
11. `docs/external-product-connection-survey.md` - 外部製品の接続面観測メモ
12. `docs/connector-target-matrix.md` - 将来 Connector 対象の設計プレビュー表

## 読み方

このリポジトリは、現時点では「完成した標準」ではなく、初期の公開仕様・設計フレームワークです。

読むときは、次を分けてください。

- 現在すでに書かれている定義・例・境界
- 現在の構造チェックで確認していること
- 構造チェックで確認していないこと
- 将来の API / Connector についての設計プレビュー
- まだ deferred として止めている実装作業
- Zenn 公開で説明してよい範囲

## Zenn 公開で説明してよい範囲

近い公開記事では、次の説明が安全です。

- 責任経路工学とは何か
- なぜ AI 参加型の判断・行為で責任経路が必要になるか
- GitHub リポジトリの読み方
- 何を主張していないか
- API / Connector はまだ future-shape であり、実装済みではないこと
- 世界の AI 製品や workflow 製品の接続面をどのように観測しているか
- 将来 Connector 対象を synthetic-first に整理していること

## まだ主張しないこと

次は、現在のリポジトリからは主張しません。

- 標準化完了
- 認証済み
- conformance ready
- 本番利用可能
- 実装済み Connector
- 実装済み public API
- 外部レビューで承認済み
- 法的有効性
- 安全性
- 遵法性
- 公平性
- runtime correctness
- adapter correctness
- AI への最終責任移転

## API / Connector の位置づけ

`docs/api-future-shape.md` と `docs/connector-target-matrix.md` は、完成予想図に近い設計プレビューです。

これらは、どのような入力、draft output、review、外部システムカテゴリを将来扱うかを整理するための文書です。

実装、外部サービス接続、live log 取り込み、個人情報処理、本番 runtime ではありません。

## 人間の責任

本リポジトリの定義、主張、公開、修正、撤回、保留の判断については、人間の著作者または保守者が責任を持ちます。AI ツールは支援しますが、責任主体にはなりません。
