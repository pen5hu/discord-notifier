import logging
import os
import sys
from dotenv import load_dotenv
from infrastructure.discord_repository import DiscordRepository
from logging_config import setup_logging
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase
from controller.notify_after_birth_days_controller import NotifyAfterBirthDaysController

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)


def notify_after_birth_days():
    # repository
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    discord_repository = DiscordRepository(webhook_url=webhook_url)

    # usecase
    notify_after_birth_days_usecase = NotifyAfterBirthDaysUsecase(discord_repository)

    # controller
    notify_after_birth_days_controller = NotifyAfterBirthDaysController(
        notify_after_birth_days_usecase
    )

    success = notify_after_birth_days_controller.execute()
    if success:
        logger.info("処理が正常に完了しました。")
        sys.exit(0)
    else:
        logger.error("処理が失敗しました。")
        sys.exit(1)


def main():
    args = sys.argv
    if len(args) < 2:
        logger.warning("引数を指定してください。")
        sys.exit(1)

    command = args[1]
    if command == "-after-birth-days":
        notify_after_birth_days()
    else:
        logger.warning(f"不明なコマンドです: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
