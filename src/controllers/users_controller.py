from aiogram.types import Message

from src.core.use_cases import UsersUseCase
from src.mappers import UserMapper, ContactMapper
from src.presenters import StartPresenter, ShareContactPresenter


class UsersController:
    def __init__(self, users_use_case: UsersUseCase) -> None:
        self._users_use_case = users_use_case

    async def register_after_start(self, message: Message) -> None:
        user = UserMapper.from_message(message)
        await self._users_use_case.register(user)
        await StartPresenter(message).present()

    async def share_contact(self, message: Message) -> None:
        contact = ContactMapper.from_message(message)
        await self._users_use_case.share_contact(contact)
        is_user_exist = await self._users_use_case.check_exist(message.from_user.id)
        await ShareContactPresenter(message).present(is_user_exist)
