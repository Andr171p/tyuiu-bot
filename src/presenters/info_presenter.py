from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram.types import Message

from src.misc.files_readers import read_txt
from src.settings import settings


class InfoPresenter:
    def __init__(self, message: "Message") -> None:
        self._message = message

    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "info.txt"
        text = await read_txt(file_path)
        await self._message.answer(text)