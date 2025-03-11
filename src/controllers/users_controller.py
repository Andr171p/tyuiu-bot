from aiogram.types import Message

from src.core.use_cases import UsersUseCase
from src.mappers import UserMapper
from src.presenters import StartPresenter


class UsersController:
    def __init__(self, users_use_case: UsersUseCase) -> None:
        self._users_use_case = users_use_case

    async def register_after_start(self, message: Message) -> None:
        user = UserMapper.from_message(message)
        await self._users_use_case.register(user)
        await StartPresenter(message=message).present()
