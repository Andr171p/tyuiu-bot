import logging
import aiohttp
from typing import Optional, Any


logger = logging.getLogger(__name__)


class ChatAssistantAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def answer(self, chat_id: str, text: str) -> Optional[dict]:
        url = f"{self._base_url}/chat/"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        user_message = {
            "chat_id": chat_id,
            "role": "user",
            "text": text
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=url,
                        headers=headers,
                        json=user_message
                ) as response:
                    assistant_message = await response.json()
            return assistant_message
        except aiohttp.ClientError as ex:
            logger.error(ex)


class UserAuthAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def is_exists(self, phone_number: str) -> Optional[Any]:
        try:
            url = f"{self._base_url}/api/v1/getnumber/{phone_number}"
            headers = {"Content-Type": "application/json; charset=UTF-8"}
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
        except aiohttp.ClientError as ex:
            logger.error(ex)

