import io
import base64
import logging

from typing import Optional, Union

from aiogram import Bot
from aiogram.types import InputFile

from src.core.interfaces import AbstractSenderService


logger = logging.getLogger(__name__)


class TelegramSenderService(AbstractSenderService):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    async def send(
            self,
            user_id: int,
            text: str,
            photo_url: Optional[str] = None,
            photo_base64: Optional[str] = None
    ) -> bool:
        if photo_base64 is not None:
            photo = InputFile(io.BytesIO(base64.b64decode(photo_base64)))
            return await self._send_photo(user_id, photo, text)
        elif photo_url is not None:
            return await self._send_photo(user_id, photo_url, text)
        return await self._send_message(user_id, text)

    async def _send_message(self, chat_id: int, text: str) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_message(
                chat_id=chat_id,
                text=text
            )
            if message:
                is_delivered = True
            logger.info("Message delivered successfully to %s", chat_id)
        except Exception as ex:
            logger.warning("Message is not delivered with error %s", ex)
            is_delivered = False
        finally:
            return is_delivered

    async def _send_photo(self, chat_id: int, photo: Union[InputFile, str], caption: str) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption
            )
            if message:
                is_delivered = True
            logger.info("Photo delivered successfully to %s", chat_id)
        except Exception as ex:
            logger.warning("Photo is not delivered with error %s", ex)
            is_delivered = False
        finally:
            return is_delivered
