import logging
import os
import sys
from dotenv import load_dotenv
from common.result import Result
from infrastructure.discord_repository import DiscordRepository
from common.logging_config import setup_logging
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)


def notify_after_birth_days():
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    # repository
    discord_repository = DiscordRepository(webhook_url=webhook_url)

    # usecase
    notify_after_birth_days_usecase = NotifyAfterBirthDaysUsecase(discord_repository)

    return notify_after_birth_days_usecase.execute()


COMMANDS = {
    "-after-birth-days": notify_after_birth_days,
}


def main():
    if len(sys.argv) != 2:
        logger.warning("サブコマンドが不足しています")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd not in COMMANDS:
        logger.warning(f"不明なコマンドです: {cmd}")
        sys.exit(1)

    result: Result[None, Exception] = COMMANDS[cmd]()
    if not result.ok:
        logger.error("処理が失敗しました。")
        sys.exit(1)

    logger.info("処理が正常に完了しました。")
    sys.exit(0)


if __name__ == "__main__":
    main()
