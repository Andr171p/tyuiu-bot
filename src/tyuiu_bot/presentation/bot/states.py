from aiogram.fsm.state import StatesGroup, State


class ChangePasswordForm(StatesGroup):
    new_password = State()
    confirm_password = State()
