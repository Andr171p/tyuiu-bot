from src.presenters.message_presenter import MessagePresenter

from src.misc.files_readers import read_txt
from src.config import settings


class StartPresenter(MessagePresenter):
    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "Start_message.txt"
        text = await read_txt(file_path)
        await self.message.answer(text)