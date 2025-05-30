from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def share_contact_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [[KeyboardButton(text="Поделиться контактом", request_contact=True)]]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите для получения уведомлений"
    )


def follow_to_register_keyboard(url: str) -> InlineKeyboardMarkup:
    inline_keyboard = [[InlineKeyboardButton(text="Зарегистрироваться", url=url)]]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def want_to_change_password_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard = [
        [InlineKeyboardButton(text="Да", callback_data="change-password")],
        [InlineKeyboardButton(text="Нет", callback_data="cancel-changing-password")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
