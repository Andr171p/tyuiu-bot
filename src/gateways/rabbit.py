from typing import Optional

from faststream.rabbit import RabbitBroker

from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import ChatAssistantGateway


class ChatAssistantRabbitGateway(ChatAssistantGateway):
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        assistant_message = await self._broker.publish(
            user_message,
            queue="chat.user-message",
            reply_to="chat.assistant-message"
        )
        return assistant_message
