import logging
from typing import List

from aiogram import Bot
from aiogram.types import InputFile


log = logging.getLogger(__name__)


class SenderService:
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    async def send_message(
            self,
            user_id: int,
            text: str
    ) -> None:
        try:
            await self._bot.send_message(
                chat_id=user_id,
                text=text
            )
            log.info("Message sent successfully to %s", user_id)
        except Exception as _ex:
            log.warning("Message not delivered with exception: %s", _ex)

    async def send_message_to_users(
            self,
            user_ids: List[int],
            text: str
    ) -> None:
        for user_id in user_ids:
            await self.send_message(
                user_id=user_id,
                text=text
            )
        log.info("Broadcast finished")

    async def send_message_with_photo(
            self,
            user_id: int,
            photo: InputFile,
            text: str
    ) -> None:
        ...
