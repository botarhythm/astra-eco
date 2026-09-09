# 設計根拠

確認日: 2026-09-09。以下は適用条件付きの根拠であり、このスキルの削減率を実証するものではない。Astra固有の独立した比較実測は未実施。

| 一次資料 | 採用する知見 | 適用限界 |
|---|---|---|
| [OpenAI: Astra guide](https://developers.openai.com/api/docs/guides/latest-model) | 指示の矛盾を避け、確認と検証の量をタスクに合わせる | 公式の行動ガイドであり、このスキルの比較試験ではない |
| [GitHub: task-level efficiency](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/) | 情報を落とす圧縮は再取得を増やし得る。反復ログとソースを区別する | Copilotの特定構成での結果。全圧縮ツールの否定ではない |
| [VS Code: token efficiency](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot) | 必要時のツール読み込みを対応環境で利用する | 他モデル・実行基盤の測定値をAstraに転用しない |
| [Manus: context engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) | 安定した文脈、外部ファイル、失敗情報の保持 | 2025年の開発経験。ツールの動的読み込みを避ける助言は現在の全環境に一般化しない |
| [AI Badger: handoff experiment](https://github.com/PVRLabs/aibadger/blob/main/docs/articles/can-ai-badger-reduce-local-coding-agent-token-usage/index.md) | 必要情報を絞った引き継ぎを評価候補にする | 単一の自己評価実験。外部圧縮費用を含む全工程で再評価が必要。合格条件やリスクの一律削除は採用しない |
| [Stanford: agent token consumption](https://digitaleconomy.stanford.edu/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/) | 自己採点より実測と反復比較を使う | 研究対象モデルの結果。Astraの消費量を予測する式ではない |

## API最適化を扱う場合

[Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)、[Batch](https://developers.openai.com/api/docs/guides/batch)、[Flex](https://developers.openai.com/api/docs/guides/flex-processing) の現行仕様と利用環境を確認する。単価、対応機能、保持条件を固定値としてスキルに埋め込まない。キャッシュヒット率、トークン数、費用は異なる指標である。

## 採用しないルール

- 常に最低または最大の推論設定にする。
- あらゆる入力を要約する、ソースや差分を一律に切り捨てる。
- 並列化だけで総費用が減ると仮定する。
- 必要なテストを省く、必ず全テストを繰り返す。
- 根拠なく一定の削減率や品質不変を保証する。

更新時は、対象モデル・実行基盤・比較方法・品質への影響を確認する。新しい記事を見つけただけでルールを増やさない。
