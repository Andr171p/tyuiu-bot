from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from dishka.integrations.aiogram import FromDishka

from faststream.rabbit import RabbitBroker

from .states import ChangePasswordForm
from .templates import START_TEMPLATE, INFO_TEMPLATE, SUBSCRIPTION_DETAIL_TEMPLATE
from .keyboards import follow_to_register_keyboard, share_contact_keyboard

from ...core.services import SubscriptionService, PasswordChangeService
from ...core.dto import UserContactDTO, NewPasswordDTO
from ...core.exceptions import ConfirmedPasswordError
from ...core.entities import UserMessage
from ...constants import WEBSITE_URL


router = Router()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(START_TEMPLATE)


@router.message(Command("info"))
async def info(message: Message) -> None:
    await message.answer(INFO_TEMPLATE)


@router.message(Command("subscribe"))
async def get_subscription_details(message: Message) -> None:
    await message.answer(text=SUBSCRIPTION_DETAIL_TEMPLATE, reply_markup=share_contact_keyboard())


@router.message(F.contact)
async def subscribe(message: Message, subscription_service: FromDishka[SubscriptionService]) -> None:
    contact = UserContactDTO(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        phone_number=message.contact.phone_number
    )
    status = await subscription_service.subscribe(contact)
    if status == "READY":
        await message.answer("Вы успешно поделились контактом")
    elif status == "REGISTRATION_REQUIRE":
        await message.answer(
            """<b>Контакт успешно отправлен.</b>
            Осталось зарегистрироваться на нашем сайте...
            """,
            reply_markup=follow_to_register_keyboard(WEBSITE_URL)
        )


@router.callback_query(F.data == "cancel-password-changing")
async def cancel_changing_password(message: Message) -> None:
    await message.answer("Смена пароля отменена")


@router.callback_query(F.data == "change-password")
async def send_change_password_form(message: Message, state: FSMContext) -> None:
    await message.answer("Введите новый пароль: ")
    await state.set_state(ChangePasswordForm.new_password)


@router.message(ChangePasswordForm.new_password)
async def enter_new_password(message: Message, state: FSMContext) -> None:
    await state.update_data(new_password=message.text)
    await message.answer("Теперь подтвердите пароль: ")
    await state.set_state(ChangePasswordForm.confirm_password)


@router.message(ChangePasswordForm.confirm_password)
async def confirm_and_change_password(
        message: Message,
        state: FSMContext,
        password_change_service: FromDishka[PasswordChangeService]
) -> None:
    await state.update_data(confirm_password=message.text)
    change_password_data = await state.get_data()
    try:
        new_password = NewPasswordDTO(
            telegram_id=message.from_user.id,
            new_password=change_password_data["new_password"],
            confirmed_password=change_password_data["confirm_password"]
        )
    except ConfirmedPasswordError:
        await message.answer(f"Вы не подтвердили пароль...")
        await state.clear()
        await state.set_state(ChangePasswordForm.new_password)
        return
    is_changed = await password_change_service.change_password(new_password)
    if is_changed:
        await message.answer("Вы успешно сменили пароль")
    else:
        await message.answer("Произошла ошибка при смене пароля, попробуйте позже")


@router.message(F.text)
async def chat(message: Message, broker: FromDishka[RabbitBroker]) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_message = UserMessage(chat_id=message.from_user.id, text=message.text)
    await broker.publish(user_message, queue="chat.user-messages")
