from domain.discord_repository_interface import IDiscordRepository
from domain.notification_message import NotificationMessage
import requests
import sys
from requests.exceptions import RequestException, ConnectionError, Timeout, HTTPError


class DiscordRepository(IDiscordRepository):
    webhook_url: str

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def notify_message(self, message: NotificationMessage) -> bool:
        if not self.webhook_url:
            print(
                "エラー: 環境変数 'DISCORD_WEBHOOK_URL' が設定されていません。",
                file=sys.stderr,
            )
            return False

        try:
            payload = {
                "embeds": [
                    {
                        "title": message.title,
                        "description": message.description,
                        "color": message.color,
                        "footer": {
                            "text": message.footer_text,
                        },
                    }
                ]
            }

            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=30,  # 30秒のタイムアウトを設定
            )
            response.raise_for_status()  # HTTPエラーがあれば例外を発生

            print("Discordにメッセージが正常に送信されました。")
            return True

        except ConnectionError as e:
            print(f"エラー: Discordへの接続に失敗しました: {str(e)}", file=sys.stderr)
            return False
        except Timeout as e:
            print(
                f"エラー: Discordへのリクエストがタイムアウトしました: {str(e)}",
                file=sys.stderr,
            )
            return False
        except HTTPError as e:
            print(
                f"エラー: DiscordからHTTPエラーが返されました: {str(e)}",
                file=sys.stderr,
            )
            return False
        except RequestException as e:
            print(
                f"エラー: Discordへのリクエスト中にエラーが発生しました: {str(e)}",
                file=sys.stderr,
            )
            return False
        except Exception as e:
            print(f"エラー: 予期しないエラーが発生しました: {str(e)}", file=sys.stderr)
            return False
