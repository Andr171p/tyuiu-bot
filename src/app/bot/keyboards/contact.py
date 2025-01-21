from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def share_contact_kb() -> ReplyKeyboardMarkup:
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
