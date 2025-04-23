from faststream.rabbit import RabbitBroker

from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import AbstractChatAssistantGateway


class ChatAssistantRabbitGateway(AbstractChatAssistantGateway):
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        assistant_message = await self._broker.publish(
            user_message,
            queue="chat.user-message",
            rpc=True
        )
        return assistant_message
