# Astra Eco

Astraを使うCodexの作業で、品質を保ちながら不要な探索・読み直し・再試行・過剰検証を減らすユーザースキルです。

モデルの自動切り替えやAPI呼び出しを行うプログラムではありません。APIキー、追加パッケージ、常駐プロセスは不要です。公式OpenAI製品ではありません。

## インストール

このリポジトリの `skills/astra-eco` フォルダ全体を、`$CODEX_HOME/skills/astra-eco` にコピーしてください。`CODEX_HOME` が未設定なら `~/.codex/skills/astra-eco` を使います。既存の同名スキルがあれば、差分を確認してから更新してください。

### Windows PowerShell

```powershell
git clone https://github.com/botarhythm/astra-eco.git
$skillBase = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillTarget = Join-Path $skillBase 'skills/astra-eco'
if (Test-Path -LiteralPath $skillTarget) { throw "既存のスキルがあります: $skillTarget" }
New-Item -ItemType Directory -Force -Path (Join-Path $skillBase 'skills') | Out-Null
Copy-Item -LiteralPath './astra-eco/skills/astra-eco' -Destination $skillTarget -Recurse
```

### macOS / Linux

```sh
git clone https://github.com/botarhythm/astra-eco.git
skill_base="${CODEX_HOME:-$HOME/.codex}"
skill_target="$skill_base/skills/astra-eco"
if [ -e "$skill_target" ]; then
  printf '%s\n' "既存のスキルがあります: $skill_target"
else
  mkdir -p "$skill_base/skills"
  cp -R ./astra-eco/skills/astra-eco "$skill_target"
fi
```

Codexの新しいタスクで `$astra-eco` を指定してください。候補に出ない場合はアプリを再起動して確認してください。スキルはAstraへの切り替えを行わないため、Astraを使う場合は利用環境で選択してください。

## 使い方

```text
$astra-eco この不具合を修正し、必要な検証まで完了してください。
```

```text
$astra-eco この実行ログを調べ、品質を落とさず減らせる無駄を診断してください。
```

明示的な呼び出しと、説明に一致する依頼での自動選択に対応します。通常作業では参考資料を毎回読み込まず、依頼に必要な成果物を返します。

## 設計と評価

- [スキル本体](skills/astra-eco/SKILL.md)
- [調査根拠・適用限界](skills/astra-eco/references/evidence.md)
- [比較実験・行動確認ケース](skills/astra-eco/references/evaluation.md)

この版のトークン・費用削減効果は未実測です。品質、全試行の費用、所要時間を同条件で比較してください。「エコ」は作業効率を意味し、電力・CO₂削減を保証しません。

## 配布

MITライセンス。コピー、変更、再配布できます。ライセンス表記を保持してください。
