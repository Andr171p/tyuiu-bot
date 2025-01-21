from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def contact_kb() -> InlineKeyboardMarkup:
    keyboard_buttons: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="Хочу получать уведомления", request_contact=True)]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    return keyboard
