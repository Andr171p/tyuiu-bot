import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aiogram import Bot

from src.services.sender.base_sender_service import BaseSenderService
from src.services.sender.sender_exception import SenderException


log = logging.getLogger(__name__)


class TelegramSenderService(BaseSenderService):
    def __init__(self, bot: "Bot") -> None:
        self._bot = bot

    async def send_message(self, user_id: int, text: str) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_message(
                chat_id=user_id,
                text=text
            )
            if message:
                is_delivered = True
            log.info("Message delivered successfully to %s", user_id)
        except SenderException as ex:
            log.warning("Message is not delivered with exception %s", ex)
            is_delivered = False
        finally:
            return is_delivered

    async def send_message_with_photo(self, user_id: int, photo: Any, text: str) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_photo(
                chat_id=user_id,
                photo=photo,
                caption=text
            )
            if message:
                is_delivered = True
            log.info(
                "Message with photo delivered successfully to %s",
                user_id
            )
        except SenderException as ex:
            log.warning("Message with photo is not delivered with exception %s", ex)
            is_delivered = False
        finally:
            return is_delivered
