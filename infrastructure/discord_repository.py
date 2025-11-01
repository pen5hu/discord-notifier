import logging
from domain.discord_repository_interface import IDiscordRepository
from domain.notification_message import NotificationMessage
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout, HTTPError

logger = logging.getLogger(__name__)


class DiscordRepository(IDiscordRepository):
    webhook_url: str

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def notify_message(self, message: NotificationMessage) -> bool:
        if not self.webhook_url:
            logger.error(
                "エラー: 環境変数 'DISCORD_WEBHOOK_URL' が設定されていません。",
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

            logger.info("Discordにメッセージが正常に送信されました。")
            return True

        except ConnectionError as e:
            logger.error(f"エラー: Discordへの接続に失敗しました: {str(e)}")
            return False
        except Timeout as e:
            logger.error(
                f"エラー: Discordへのリクエストがタイムアウトしました: {str(e)}",
            )
            return False
        except HTTPError as e:
            logger.error(
                f"エラー: DiscordからHTTPエラーが返されました: {str(e)}",
            )
            return False
        except RequestException as e:
            logger.error(
                f"エラー: Discordへのリクエスト中にエラーが発生しました: {str(e)}",
            )
            return False
        except Exception as e:
            logger.error(f"エラー: 予期しないエラーが発生しました: {str(e)}")
            return False
