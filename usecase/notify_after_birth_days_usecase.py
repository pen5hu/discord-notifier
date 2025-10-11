import os
import sys
from datetime import datetime, date
from domain.discord_repository_interface import IDiscordRepository
from domain.notification_message import NotificationMessage


class NotifyAfterBirthDaysUsecase:
    discord_repository: IDiscordRepository

    def __init__(self, discord_repository: IDiscordRepository):
        self.discord_repository = discord_repository

    def execute(self) -> bool:
        my_birthday_str = os.getenv("MY_BIRTHDAY")
        if not my_birthday_str:
            print("環境変数MY_BIRTHDAYが設定されていません。", file=sys.stderr)
            return False

        try:
            birthday = datetime.strptime(my_birthday_str, "%Y/%m/%d").date()
        except ValueError:
            print(
                "MY_BIRTHDAYの形式が不正です: YYYY/MM/DD形式で設定してください。",
                file=sys.stderr,
            )
            return False

        today = date.today()
        days_passed = (today - birthday).days

        message = NotificationMessage(f"誕生日から{days_passed}日が経過しました。")
        if not message.content:
            return False

        success = self.discord_repository.notify_message(message)
        if not success:
            return False

        return True
