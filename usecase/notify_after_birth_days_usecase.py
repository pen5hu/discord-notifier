import logging
import os
from datetime import datetime, date
from common.result import Result
from domain.discord_repository_interface import IDiscordRepository
from domain.notification_message import NotificationMessage

logger = logging.getLogger(__name__)


class NotifyAfterBirthDaysUsecase:
    discord_repository: IDiscordRepository

    def __init__(self, discord_repository: IDiscordRepository):
        self.discord_repository = discord_repository

    def execute(self) -> Result[None, Exception]:
        my_birthday_str = os.getenv("MY_BIRTHDAY")
        if not my_birthday_str:
            logger.error("環境変数MY_BIRTHDAYが設定されていません。")
            return Result.Err(Exception("環境変数MY_BIRTHDAYが設定されていません。"))

        try:
            birthday = datetime.strptime(my_birthday_str, "%Y/%m/%d").date()
        except ValueError:
            logger.error(
                "MY_BIRTHDAYの形式が不正です: YYYY/MM/DD形式で設定してください。"
            )
            return Result.Err(
                Exception(
                    "MY_BIRTHDAYの形式が不正です: YYYY/MM/DD形式で設定してください。"
                )
            )

        today = date.today()
        days_passed = (today - birthday).days

        message = NotificationMessage(
            title=f"誕生日から {days_passed} 日が経過",
            footer_text="※誕生日自体は日数に含まれていません",
        )
        if not message:
            return Result.Err(Exception("通知メッセージの作成に失敗しました。"))

        result = self.discord_repository.notify_message(message)
        if not result.ok:
            return Result.Err(Exception("Discordへのメッセージ送信に失敗しました。"))

        return Result.Ok(None)
