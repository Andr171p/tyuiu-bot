from typing import Optional, Union

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from ..constants import NOTIFICATION_LEVEL


KEYBOARD = Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]


def get_keyboard_by_notification_level(level: str) -> Optional[KEYBOARD]:
    from ..presentation.bot.keyboards import want_to_change_password_keyboard
    LEVEL_TO_KEYBOARD: dict[NOTIFICATION_LEVEL: KEYBOARD] = {
        "CHANGE_PASSWORD": want_to_change_password_keyboard()
    }
    return LEVEL_TO_KEYBOARD.get(level)
