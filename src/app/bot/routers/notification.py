from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.app.bot.keyboards.contact import share_contact_kb
from src.schemas import ContactSchema
from src.services import NotificationService
from src.misc.files_readers import load_txt_async
from src.config import settings


notification_router = Router()


@notification_router.message(Command("subscribe"))
async def share_contact_for_subscribe(message: Message) -> None:
    file_path = settings.static.texts_dir / "Share_contact_message.txt"
    text = await load_txt_async(file_path)
    await message.answer(
        text=text,
        reply_markup=share_contact_kb()
    )


@notification_router.message(F.contact)
async def subscribe_to_notification(
        message: Message,
        notification_service: FromDishka[NotificationService]
) -> None:
    contact = ContactSchema.from_message(message)
    await notification_service.subscribe(contact)
    await message.answer("Вы успешно отправили контакт")
