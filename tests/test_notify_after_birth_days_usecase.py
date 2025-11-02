import unittest
from datetime import date
from unittest.mock import MagicMock
from usecase.notify_after_birth_days_usecase import NotifyAfterBirthDaysUsecase
from domain.notification_message import NotificationMessage


class TestNotifyAfterBirthDaysUsecase(unittest.TestCase):
    def setUp(self):
        self.mock_discord_repository = MagicMock()
        self.usecase = NotifyAfterBirthDaysUsecase(self.mock_discord_repository)

    def test_create_notification_message_today_is_birthday(self):
        today = date(2023, 1, 15)
        birthday = date(2023, 1, 15)
        result = self.usecase._create_notification_message(birthday, today)
        self.assertTrue(result.ok)
        self.assertIsInstance(result.value, NotificationMessage)
        self.assertEqual(result.value.title, "🎉今日は誕生日です！！おめでとう！！🎉")
        self.assertEqual(result.value.footer_text, "素敵な1日をお過ごしください！！")
        self.assertEqual(result.value.color, 16766720)

    def test_create_notification_message_today_is_birthday_in_future(self):
        today = date(2024, 1, 15)
        birthday = date(2023, 1, 15)
        result = self.usecase._create_notification_message(birthday, today)
        self.assertTrue(result.ok)
        self.assertIsInstance(result.value, NotificationMessage)
        self.assertEqual(result.value.title, "🎉今日は誕生日です！！おめでとう！！🎉")
        self.assertEqual(result.value.footer_text, "素敵な1日をお過ごしください！！")
        self.assertEqual(result.value.color, 16766720)

    def test_create_notification_message_100_days_passed(self):
        today = date(2023, 4, 25)  # 100 days after Jan 15
        birthday = date(2023, 1, 15)
        result = self.usecase._create_notification_message(birthday, today)
        self.assertTrue(result.ok)
        self.assertIsInstance(result.value, NotificationMessage)
        self.assertEqual(
            result.value.title,
            "爆誕からちょうど 100 日が経過しました。記念すべき日ですね！",
        )
        self.assertEqual(
            result.value.footer_text, "※誕生日自体は日数に含まれていません"
        )

    def test_create_notification_message_99_days_passed(self):
        today = date(2023, 4, 24)  # 99 days after Jan 15
        birthday = date(2023, 1, 15)
        result = self.usecase._create_notification_message(birthday, today)
        self.assertTrue(result.ok)
        self.assertIsInstance(result.value, NotificationMessage)
        self.assertEqual(result.value.title, "爆誕から 99 日が経過しました。")
        self.assertEqual(
            result.value.footer_text, "※誕生日自体は日数に含まれていません"
        )

    def test_create_notification_message_leap_year_day_count(self):
        birthday = date(2024, 2, 28)
        today = date(2024, 2, 29)  # 2024年は閏年で2/29が存在する
        result = self.usecase._create_notification_message(birthday, today)
        self.assertTrue(result.ok)
        self.assertIsInstance(result.value, NotificationMessage)
        self.assertEqual(
            result.value.title,
            "爆誕から 1 日が経過しました。",
        )
        self.assertEqual(
            result.value.footer_text, "※誕生日自体は日数に含まれていません"
        )


if __name__ == "__main__":
    unittest.main()
