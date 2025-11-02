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

    def _create_notification_message(
        self, birthday: date, today=date.today()
    ) -> Result[NotificationMessage, Exception]:
        days_passed = (today - birthday).days

        if today.month == birthday.month and today.day == birthday.day:
            message = NotificationMessage(
                title="🎉今日は誕生日です！！おめでとう！！🎉",
                footer_text="素敵な1日をお過ごしください！！",
                color=16766720,
            )
        elif days_passed > 0 and days_passed % 100 == 0:
            message = NotificationMessage(
                title=f"爆誕からちょうど {days_passed} 日が経過しました。記念すべき日ですね！",
                footer_text="※誕生日自体は日数に含まれていません",
            )
        else:
            message = NotificationMessage(
                title=f"爆誕から {days_passed} 日が経過しました。",
                footer_text="※誕生日自体は日数に含まれていません",
            )

        if not message:
            return Result.Err(Exception("通知メッセージの作成に失敗しました。"))
        return Result.Ok(message)

    def execute(self) -> Result[None, Exception]:
        my_birthday_str = os.getenv("MY_BIRTHDAY")
        if not my_birthday_str:
            logger.error("環境変数MY_BIRTHDAYが設定されていません。")
            return Result.Err(Exception("環境変数MY_BIRTHDAYが設定されていません。"))

        try:
            birthday = datetime.strptime(my_birthday_str, "%Y/%m/%d").date()

            message_result = self._create_notification_message(birthday)
            if not message_result.ok:
                return Result.Err(message_result.error)

            result = self.discord_repository.notify_message(message_result.value)
            if not result.ok:
                return Result.Err(
                    Exception("Discordへのメッセージ送信に失敗しました。")
                )

            return Result.Ok(None)

        except ValueError:
            logger.error(
                "MY_BIRTHDAYの形式が不正です: YYYY/MM/DD形式で設定してください。"
            )
            return Result.Err(
                Exception(
                    "MY_BIRTHDAYの形式が不正です: YYYY/MM/DD形式で設定してください。"
                )
            )
