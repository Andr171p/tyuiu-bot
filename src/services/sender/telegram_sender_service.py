import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram import Bot

from src.services.sender.base_sender_service import BaseSenderService
from src.services.sender.sender_exception import SenderException
from src.dto import TelegramMessage, TelegramWithPhotoMessage


log = logging.getLogger(__name__)


class TelegramSenderService(BaseSenderService):
    def __init__(self, bot: "Bot") -> None:
        self._bot = bot

    async def send_message(self, telegram_message: TelegramMessage) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_message(
                chat_id=telegram_message.user_id,
                text=telegram_message.text
            )
            if message:
                is_delivered = True
            log.info("Message delivered successfully to %s", telegram_message.user_id)
        except SenderException as ex:
            log.warning("Message is not delivered with exception %s", ex)
            is_delivered = False
        finally:
            return is_delivered

    async def send_message_with_photo(self, telegram_message: TelegramWithPhotoMessage) -> bool:
        is_delivered: bool = False
        try:
            message = await self._bot.send_photo(
                chat_id=telegram_message.user_id,
                photo=telegram_message.photo,
                caption=telegram_message.text
            )
            if message:
                is_delivered = True
            log.info(
                "Message with photo delivered successfully to %s",
                telegram_message.user_id
            )
        except SenderException as ex:
            log.warning("Message with photo is not delivered with exception %s", ex)
            is_delivered = False
        finally:
            return is_delivered
