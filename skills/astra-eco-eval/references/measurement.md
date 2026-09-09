# 最小の実測記録

1実行1行のJSONL。会話本文、ソース、秘密情報は保存不要。通常作業中の追加LLM呼び出しはしない。既存の計測値を後から転記または変換する。自動ログ変換は未実装であり、ログの項目定義を確認せず取り込まない。

```json
{"run_id":"example-01","kind":"task","variant":"eco","model":"gpt-6-astra","effort":"high","skill_version":"commit-id","passed":null,"input_tokens":null,"output_tokens":null,"duration_seconds":null,"cost_usd":null}
```

- `run_id`: 一意の匿名ID。同じ実行を重複登録しない。
- `kind`: `task` または `evaluation`。
- `variant`: `baseline` または `eco`。baselineはスキルを読み込まなかった実行に限る。会話途中で「無視して」と言っても未使用条件にはならない。
- `model`, `effort`, `skill_version`: 確認できた値。欠測はnull。baselineのskill_versionはnull。
- `passed`: 事前の合格条件を満たすtrue、満たさないfalse、未評価null。モデルの完了宣言だけでtrueにしない。
- `input_tokens`, `output_tokens`: 対象実行全体の使用量。キャッシュ入力が入力の内数、推論が出力の内数なら加算しない。累積ログは各イベントを合計せず、対象区間の差分を使う。カウンタリセット・再開・子エージェントの範囲が不明ならnull。
- `duration_seconds`: 壁時計時間。ユーザー待ち等を含む場合は比較条件を揃える。
- `cost_usd`: 実測のAPI費用のみ。Codex利用枠をドル換算しない。不明はnull。

必要なら `task_id`, `start_commit`, `acceptance_id`, `harness_version`, `cache_condition` を追加できる。現行集計器はそれらによるペア比較を行わない。

まず自然に発生する作業を観測する。A/Bを行う場合は同じタスク・開始状態・合格条件・モデル設定・実行基盤を揃え、順序とキャッシュ条件を記録し、複数回比較する。少数例を一般化しない。評価用実行は別途依頼された範囲でのみ行う。

記録はリポジトリ外または無視対象の `work/` に保存する。スクリプトは標準出力に集計JSONだけを出し、記録ファイルを書き換えない。評価自体の観測値は次回の集計で扱えばよく、自己計測のために再帰的な評価を起動しない。
