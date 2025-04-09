from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def user_exists_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="Перейти", url="https://online-service-for-applicants.onrender.com/")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
