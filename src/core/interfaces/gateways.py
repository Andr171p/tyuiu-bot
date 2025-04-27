from abc import ABC, abstractmethod

from src.core.entities import UserMessage, AssistantMessage


class ChatAssistantGateway(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        raise NotImplemented


class UserAuthGateway(ABC):
    @abstractmethod
    async def check_exists(self, phone_number: str) -> bool:
        raise NotImplemented
