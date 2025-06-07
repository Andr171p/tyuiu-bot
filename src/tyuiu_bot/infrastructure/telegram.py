from typing import Optional

import uuid
import base64
import logging

from aiogram import Bot
from aiogram.types import BufferedInputFile

from .exceptions import TelegramError
from ..core.interfaces import TelegramSender
from ..core.dto import KEYBOARD


class TelegramBotSender(TelegramSender):
    def __init__(self, bot: Bot) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.bot = bot

    async def send(
            self,
            telegram_id: int,
            text: str,
            keyboard: Optional[KEYBOARD] = None
    ) -> Optional[int]:
        try:
            message = await self.bot.send_message(
                chat_id=telegram_id,
                text=text,
                reply_markup=keyboard
            )
            self.logger.info("Message with id %s delivered successfully", telegram_id)
            return message.message_id
        except Exception as e:
            self.logger.error("Error while sending message with id %s: %s", telegram_id, e)
            raise TelegramError(f"Error while sending message with id {telegram_id}: {e}") from e

    async def send_with_photo(
            self,
            telegram_id: int,
            photo: str,
            text: str,
            keyboard: Optional[KEYBOARD] = None
    ) -> Optional[int]:
        try:
            photo = BufferedInputFile(base64.b64decode(photo), filename=f"{uuid.uuid4()}.jpg")
            message = await self.bot.send_photo(
                chat_id=telegram_id,
                photo=photo,
                caption=text,
                reply_markup=keyboard
            )
            self.logger.info("Photo with id %s delivered successfully", telegram_id)
            return message.message_id
        except Exception as e:
            self.logger.error("Error while sending photo with id %s: %s", telegram_id, e)
            raise TelegramError(f"Error while sending photo with id {telegram_id}: {e}") from e
