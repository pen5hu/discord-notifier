# discord-notifier

指定したDiscordのWebhook URLに定期的にメッセージを送信するシンプルなPythonスクリプトです。  
GitHub ActionsなどのCI/CDサービスと組み合わせて、タスクの実行完了を通知するなどの用途に利用できます。

## 必要なもの

- Python 3.13 以上
- [uv](https://github.com/astral-sh/uv)
- [mise](https://mise.jdx.dev/)

## セットアップ方法

1.  **ツールと依存関係をインストールします**
    `mise` を使ってPythonのバージョンを合わせ、`uv` で依存関係をインストールします。
    ```bash
    mise i
    uv sync
    ```

## 実行方法

`uv run` コマンドでスクリプトを実行します。`.env`ファイルが自動的に読み込まれます。

```bash
uv run python main.py
```

成功すると、コンソールに以下のメッセージが表示されます。
> メッセージが正常に送信されました。

## 環境変数

| 環境変数名              | 説明                                     | 必須 |
| ----------------------- | ---------------------------------------- | ---- |
| `DISCORD_WEBHOOK_URL`   | 通知を送信するDiscordのWebhook URL。     | はい |
