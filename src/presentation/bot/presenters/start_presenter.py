from aiogram.types import Message

from src.presentation.bot.presenters.base_presenter import BasePresenter
from src.misc.files_readers import read_txt
from src.config import settings


class StartPresenter(BasePresenter):
    def __init__(self, message: Message) -> None:
        self._message = message

    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "Start_message.txt"
        text = await read_txt(file_path)
        await self._message.answer(text)
