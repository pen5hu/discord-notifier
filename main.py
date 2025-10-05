import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def main():
    if not DISCORD_WEBHOOK_URL:
        print(
            "エラー: 環境変数 'DISCORD_WEBHOOK_URL' が設定されていません。",
            file=sys.stderr,
        )
        sys.exit(1)

    message = "✅ Discord通知ボットの定期タスクが実行されました。"
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
        response.raise_for_status()
        print("メッセージが正常に送信されました。")
    except requests.exceptions.RequestException as e:
        print(f"エラー: メッセージの送信に失敗しました: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
