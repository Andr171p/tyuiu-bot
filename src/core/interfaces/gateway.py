from abc import ABC, abstractmethod

from src.core.entities import UserMessage, AssistantMessage


class AbstractChatAssistantGateway(ABC):
    @abstractmethod
    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        raise NotImplemented
