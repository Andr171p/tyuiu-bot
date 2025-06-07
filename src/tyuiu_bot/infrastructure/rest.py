from typing import Optional

from uuid import UUID

import aiohttp

from .exceptions import APIError
from .constants import STATUS_200_OK
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
            raise APIError(f"Error while receiving assistant message: {e}") from e


class UserRegistrationAPI(UserRegistration):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    async def get_user_id(self, phone_number: str) -> Optional[str]:
        url = f"{self.base_url}/api/v1/getnumber/{phone_number}"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    user_id = await response.json()
            return user_id
        except aiohttp.ClientError as e:
            raise APIError(f"Error while receiving phone number: {e}") from e

    async def update_password(self, user_id: UUID, hash_password: str) -> bool:
        url = f"{self.base_url}/api/v1/authorizations/replace/password"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        json = {"user_id": str(user_id), "new_password": hash_password}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(url, headers=headers, json=json) as response:
                    return True if response.status == STATUS_200_OK else False
        except aiohttp.ClientError as e:
            raise APIError(f"Error while updating password: {e}") from e
