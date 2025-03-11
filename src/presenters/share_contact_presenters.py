from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram.types import Message

from src.presentation.bot.keyboards import share_contact_keyboard
from src.misc.files_readers import read_txt
from src.config import settings


class GetShareContactDetailsPresenter:
    def __init__(self, message: "Message") -> None:
        self._message = message

    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "Share_contact_message.txt"
        text = await read_txt(file_path)
        await self._message.answer(
            text=text,
            reply_markup=share_contact_keyboard()
        )


class ShareContactPresenter:
    def __init__(self, message: "Message") -> None:
        self._message = message

    async def present(self) -> None:
        await self._message.answer("Вы успешно отправили контакт")
