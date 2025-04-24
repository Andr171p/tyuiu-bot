from abc import ABC, abstractmethod

from src.core.entities import UserMessage, AssistantMessage


class AbstractChatAssistantGateway(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        raise NotImplemented


class AbstractUserAuthGateway(ABC):
    @abstractmethod
    async def is_exists(self, phone_number: str) -> bool:
        raise NotImplemented
