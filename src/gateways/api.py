from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import ChatAssistantGateway, UserAuthGateway
from src.infrastructure.apis import ChatAssistantAPI, UserAuthAPI


class ChatAssistantAPIGateway(ChatAssistantGateway):
    def __init__(self, chat_assistant_api: ChatAssistantAPI) -> None:
        self._chat_assistant_api = chat_assistant_api

    async def answer(self, user_message: UserMessage) -> AssistantMessage:
        response = await self._chat_assistant_api.answer(user_message.chat_id, user_message.text)
        return AssistantMessage.model_validate(response)


class UserAuthAPIGateway(UserAuthGateway):
    def __init__(self, user_auth_api: UserAuthAPI) -> None:
        self._user_auth_api = user_auth_api

    async def check_exists(self, phone_number: str) -> bool:
        return await self._user_auth_api.is_exists(phone_number)
