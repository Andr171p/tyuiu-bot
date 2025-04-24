from typing import List

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def share_contact_keyboard() -> ReplyKeyboardMarkup:
    keyboard_buttons: List[List[KeyboardButton]] = [
        [KeyboardButton(text="Поделиться контактом", request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите для получения уведомлений"
    )
    return keyboard


def follow_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="Перейти", url="https://online-service-for-applicants.onrender.com/")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
