from aiogram.types import Message

from src.presentation.bot.keyboards import share_contact_keyboard, user_exists_keyboard
from src.misc.files_readers import read_txt
from src.config import settings


class GetShareContactDetailsPresenter:
    def __init__(self, message: Message) -> None:
        self._message = message

    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "share_contact.txt"
        text = await read_txt(file_path)
        await self._message.answer(
            text=text,
            reply_markup=share_contact_keyboard()
        )


class ShareContactPresenter:
    def __init__(self, message: Message) -> None:
        self._message = message

    async def present(self, is_user_exist: bool) -> None:
        await self._message.answer("Вы успешно отправили контакт")
        if not is_user_exist:
            await self._message.answer(
                text="Вы также можете воспользоваться нашим сервисом",
                reply_markup=user_exists_keyboard()
            )
