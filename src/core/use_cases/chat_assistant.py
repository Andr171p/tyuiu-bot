from typing import Optional

from src.core.entities import UserMessage
from src.core.interfaces import ChatAssistantGateway


class ChatAssistant:
    def __init__(self, chat_assistant_gateway: ChatAssistantGateway) -> None:
        self._chat_assistant_gateway = chat_assistant_gateway

    async def answer(self, chat_id: str, text: str) -> Optional[str]:
        user_message = UserMessage(chat_id=chat_id, text=text)
        assistant_message = await self._chat_assistant_gateway.answer(user_message)
        return assistant_message.text if assistant_message is not None else None
