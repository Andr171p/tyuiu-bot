from typing import Optional

from faststream.rabbit import RabbitBroker

from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import AbstractChatAssistantGateway, AbstractUserAuthGateway

from src.infrastructure.apis import ChatAssistantAPI, UserAuthAPI


class ChatAssistantAPIGateway(AbstractChatAssistantGateway):
    def __init__(self, chat_assistant_api: ChatAssistantAPI) -> None:
        self._chat_assistant_api = chat_assistant_api

    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        response = await self._chat_assistant_api.answer(user_message.chat_id, user_message.text)
        return AssistantMessage.model_validate(response)


class ChatAssistantRabbitGateway(AbstractChatAssistantGateway):
    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        assistant_message = await self._broker.publish(
            user_message,
            queue="chat.user-message",
            reply_to="chat.assistant-message"
        )
        return assistant_message


class UserAuthAPIGateway(AbstractUserAuthGateway):
    def __init__(self, user_auth_api: UserAuthAPI) -> None:
        self._user_auth_api = user_auth_api

    async def is_exists(self, phone_number: str) -> bool:
        return await self._user_auth_api.is_exists(phone_number)
