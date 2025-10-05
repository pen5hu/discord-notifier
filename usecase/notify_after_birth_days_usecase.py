from domain.discord_repository_interface import IDiscordRepository
from domain.notification_message import NotificationMessage


class NotifyAfterBirthDaysUsecase:
    discord_repository: IDiscordRepository

    def __init__(self, discord_repository: IDiscordRepository):
        self.discord_repository = discord_repository

    def execute(self) -> bool:
        message = NotificationMessage()
        if not message.content:
            return False

        success = self.discord_repository.notify_message(message)
        if not success:
            return False

        return True
