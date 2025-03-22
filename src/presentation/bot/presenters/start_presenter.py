from aiogram.types import Message

from src.presentation.bot.presenters.base_presenter import BasePresenter
from src.misc.files_readers import read_txt
from src.config import settings


class StartPresenter(BasePresenter):
    @classmethod
    async def present(cls, message: Message, **kwargs) -> None:
        file_path = settings.messages.messages_dir / "start.txt"
        text = await read_txt(file_path)
        await message.answer(text)
