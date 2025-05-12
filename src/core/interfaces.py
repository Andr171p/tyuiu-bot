from typing import List, Optional

from abc import ABC, abstractmethod
from uuid import UUID

from .dto import UserReadDTO, NotificationCreateDTO, NotificationReadDTO
from .entities import User, UserMessage, AssistantMessage


class TelegramSender(ABC):
    @abstractmethod
    async def send(self, telegram_id: int, text: str) -> Optional[int]: pass

    @abstractmethod
    async def send_with_photo(self, telegram_id: int, photo: str, text: str) -> Optional[int]: pass


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> None: pass

    @abstractmethod
    async def read(self, telegram_id: int) -> Optional[UserReadDTO]: pass

    @abstractmethod
    async def update(self, telegram_id: int, **kwargs) -> None: pass

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> Optional[UserReadDTO]: pass


class NotificationRepository(ABC):
    @abstractmethod
    async def create(self, notification: NotificationCreateDTO) -> None: pass

    @abstractmethod
    async def read(self, notification_id: UUID) -> Optional[NotificationReadDTO]: pass

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> List[NotificationReadDTO]: pass


class ChatAssistant(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]: pass


class UserRegistration(ABC):
    @abstractmethod
    async def get_user_id(self, phone_number: str) -> UUID: pass
