from abc import abstractmethod, ABC
from domain.notification_message import NotificationMessage


class IDiscordRepository(ABC):
    @abstractmethod
    def notify_message(self, message: NotificationMessage) -> bool: ...
