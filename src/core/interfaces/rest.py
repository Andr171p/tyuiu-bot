from abc import ABC, abstractmethod

from ..entities import UserMessage, AssistantMessage


class ChatAssistant(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> AssistantMessage: pass


class UserRegistration(ABC):
    @abstractmethod
    async def get_user_id(self, phone_number: str) -> str: pass
