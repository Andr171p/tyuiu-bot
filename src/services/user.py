import logging

from src.repository import UserRepository
from src.schemas import UserSchema


log = logging.getLogger(__name__)


class UserService:
    user_repository = UserRepository()
    
    async def register(self, user: UserSchema) -> None:
        registered_user = await self.user_repository.add(user)
        log.info("User %s registered successfully", registered_user)
