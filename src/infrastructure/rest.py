from typing import Optional

import aiohttp

from .exceptions import RestException
from ..core.entities import UserMessage, AssistantMessage
from ..core.interfaces import ChatAssistant, UserRegistration


class ChatAssistantApi(ChatAssistant):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        url = f"{self.base_url}/chat/"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        user_message = {
            "chat_id": user_message.chat_id,
            "role": user_message.role,
            "text": user_message.text
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=url,
                        headers=headers,
                        json=user_message
                ) as response:
                    assistant_message = await response.json()
            return AssistantMessage.model_validate(assistant_message)
        except aiohttp.ClientError as e:
            raise RestException(f"Error while receiving assistant message: {e}")


class UserRegistrationApi(UserRegistration):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def get_user_id(self, phone_number: str) -> Optional[str]:
        try:
            url = f"{self.base_url}/api/v1/getnumber/{phone_number}"
            headers = {"Content-Type": "application/json; charset=UTF-8"}
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    user_id = await response.json()
            return user_id
        except aiohttp.ClientError as e:
            raise RestException(f"Error while receiving phone number: {e}")
