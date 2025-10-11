import sys
from dotenv import load_dotenv
from infrastructure.discord_repository import DiscordRepository
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase
from controller.notify_after_birth_days_controller import NotifyAfterBirthDaysController


def notify_after_birth_days():
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


def main():
    args = sys.argv
    if len(args) < 2:
        print("引数を指定してください。", file=sys.stderr)
        sys.exit(1)

    load_dotenv()
    command = args[1]
    if command == "-after-birth-days":
        notify_after_birth_days()
    else:
        print(f"不明なコマンドです: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
