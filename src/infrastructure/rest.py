import logging
import aiohttp
from typing import Optional

from src.core.entities import UserMessage, AssistantMessage
from src.core.interfaces import ChatAssistant, UserRegistration


logger = logging.getLogger(__name__)


class ChatAssistantApi(ChatAssistant):
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def answer(self, user_message: UserMessage) -> Optional[AssistantMessage]:
        url = f"{self._base_url}/chat/"
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
        except aiohttp.ClientError as ex:
            logger.error(ex)


class UserRegistrationApi(UserRegistration):
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def check_registration(self, phone_number: str) -> Optional[bool]:
        try:
            url = f"{self._base_url}/api/v1/getnumber/{phone_number}"
            headers = {"Content-Type": "application/json; charset=UTF-8"}
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    is_exists = await response.json()
            return is_exists
        except aiohttp.ClientError as ex:
            logger.error(ex)
