import logging

from typing import Any, Optional

from aiogram import Bot

from src.core.interfaces import AbstractSenderService


logger = logging.getLogger(__name__)


class TelegramSenderService(AbstractSenderService):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    async def send(self, user_id: int, text: str, photo: Optional[Any] = None) -> bool:
        if photo is not None:
            return await self._send_photo(user_id, photo, text)
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

    async def _send_photo(self, chat_id: int, photo: Any, caption: str) -> bool:
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
