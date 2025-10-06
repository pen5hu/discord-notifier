import os
import sys
from dotenv import load_dotenv
from infrastructure.discord_repository import DiscordRepository
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase
from controller.notify_after_birth_days_controller import NotifyAfterBirthDaysController


def main():
    load_dotenv()
    print(f"DEBUG: DISCORD_WEBHOOK_URL exists? {bool(os.getenv('DISCORD_WEBHOOK_URL'))}")

    # repository
    discord_repository = DiscordRepository()

    # usecase
    notify_after_birth_days_usecase = NotifyAfterBirthDaysUsecase(discord_repository)

    # controller
    notify_after_birth_days_controller = NotifyAfterBirthDaysController(
        notify_after_birth_days_usecase
    )

    success = notify_after_birth_days_controller.execute()
    if success:
        print("処理が正常に完了しました。")
        sys.exit(0)
    else:
        print("処理が失敗しました。", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
