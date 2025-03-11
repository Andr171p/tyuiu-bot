from src.presenters.message_presenter import MessagePresenter
from src.presentation.bot.keyboards import share_contact_keyboard
from src.misc.files_readers import read_txt
from src.config import settings


class GetShareContactDetailsPresenter(MessagePresenter):
    async def present(self) -> None:
        file_path = settings.messages.messages_dir / "Share_contact_message.txt"
        text = await read_txt(file_path)
        await self.message.answer(
            text=text,
            reply_markup=share_contact_keyboard()
        )


class ShareContactPresenter(MessagePresenter):
    async def present(self) -> None:
        await self.message.answer("Вы успешно отправили контакт")
