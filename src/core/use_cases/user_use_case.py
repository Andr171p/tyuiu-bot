from src.repository import UserRepository
from src.core.entities import User


class UserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        
    async def register(self, user: User) -> None:
        if await self._user_repository.get_by_user_id(user.user_id):
            return
        await self._user_repository.add(user)
