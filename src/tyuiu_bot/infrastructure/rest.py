from typing import Optional

import aiohttp

from .exceptions import RestException
from ..core.entities import UserMessage, AssistantMessage
from ..core.interfaces import ChatAssistant, UserRegistration


class ChatAssistantAPI(ChatAssistant):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        url = f"{self.base_url}/chat/"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=url,
                        headers=headers,
                        json=user_message.model_dump()
                ) as response:
                    data = await response.json()
            return AssistantMessage.model_validate(data)
        except aiohttp.ClientError as e:
            raise RestException(f"Error while receiving assistant message: {e}")


class UserRegistrationAPI(UserRegistration):
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
