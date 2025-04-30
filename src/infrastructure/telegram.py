import uuid
import base64
import logging

from typing import Optional

from aiogram import Bot
from aiogram.types import (
    InputFile,
    BufferedInputFile,
    URLInputFile
)

from src.core.interfaces import TelegramSender


logger = logging.getLogger(__name__)


class TelegramSenderImpl(TelegramSender):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def send(
            self,
            telegram_id: int,
            text: str,
            image_url: Optional[str] = None,
            image_base64: Optional[str] = None
    ) -> None:
        if image_base64:
            photo = BufferedInputFile(base64.b64decode(image_base64), filename=f"{uuid.uuid4()}.jpg")
            await self.__send_photo(telegram_id, photo, text)
        elif image_url:
            photo = URLInputFile(image_url)
            await self.__send_photo(telegram_id, photo, text)
        await self.__send_message(telegram_id, text)

    async def __send_message(self, telegram_id: int, text: str) -> None:
        try:
            message = await self.bot.send_message(chat_id=telegram_id, text=text)
            if message:
                logger.info("Message delivered successfully to user with id %s", telegram_id)
        except Exception as ex:
            logger.warning("Message is not delivered with error %s", ex)

    async def __send_photo(self, telegram_id: int, photo: InputFile, caption: str) -> None:
        try:
            await self.bot.send_photo(
                chat_id=telegram_id,
                photo=photo,
                caption=caption
            )
            logger.info("Photo message delivered successfully to user with id %s", telegram_id)
        except Exception as ex:
            logger.error("Photo message is not delivered with error: %s", ex)
