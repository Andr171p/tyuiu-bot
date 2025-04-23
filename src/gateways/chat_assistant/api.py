from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import AbstractChatAssistantGateway

from src.infrastructure.apis import ChatAssistantAPI


class ChatAssistantAPIGateway(AbstractChatAssistantGateway):
    def __init__(self, chat_assistant_api: ChatAssistantAPI) -> None:
        self._chat_assistant_api = chat_assistant_api

    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        response = await self._chat_assistant_api.answer(user_message.chat_id, user_message.text)
        return AssistantMessage.model_validate(response)
