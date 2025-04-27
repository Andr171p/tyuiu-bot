from abc import ABC, abstractmethod

from src.core.entities import UserMessage, AssistantMessage


class ChatAssistant(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> AssistantMessage: pass


class UserRegistration(ABC):
    @abstractmethod
    async def check_registration(self, phone_number: str) -> bool: pass
