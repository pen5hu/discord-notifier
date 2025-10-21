# discord-notifier

指定したDiscordのWebhook URLにメッセージを送信するシンプルなPythonスクリプトです。  
GitHub ActionsなどのCI/CDサービスと組み合わせて、定期的に確認したい内容を通知することに使います

## 必要なもの

- [mise](https://mise.jdx.dev/)
- Python 3.13
- [uv](https://github.com/astral-sh/uv)


## セットアップ方法

`mise` を使ってPythonのバージョンを合わせ、`uv` で依存関係をインストールします。

```bash
mise i
uv sync
```

## 実行方法

`uv run` コマンドでスクリプトを実行します。

```bash
uv run python main.py
```

## linter formatter

`ruff` を使用して以下のコマンドで実行します。

linter

```bash
uv run ruff check .
```

linter（自動修正）

```bash
uv run ruff check --fix .
```

fomatter

```bash
uv run ruff format .
```

## 環境変数

| 環境変数名              | 説明                                     | 必須 |
| ----------------------- | ---------------------------------------- | ---- |
| `DISCORD_WEBHOOK_URL`   | 通知を送信するDiscordのWebhook URL。     | はい |
| `MY_BIRTHDAY` |誕生日の年月日、現在が誕生日から何日経過したかを計算するために使用します。 | はい |


