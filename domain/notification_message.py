import datetime


class NotificationMessage:
    content: str

    def __init__(self):
        self.content = f"Notification at {datetime.datetime.now()}"

