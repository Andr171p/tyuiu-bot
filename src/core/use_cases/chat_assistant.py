from src.core.entities import UserMessage
from src.core.interfaces import AbstractChatAssistantGateway


class ChatAssistant:
    def __init__(self, chat_assistant_gateway: AbstractChatAssistantGateway) -> None:
        self._chat_assistant_gateway = chat_assistant_gateway

    async def answer(self, chat_id: str, text: str) -> str:
        user_message = UserMessage(chat_id=chat_id, text=text)
        assistant_message = await self._chat_assistant_gateway.answer(user_message)
        return assistant_message.text
