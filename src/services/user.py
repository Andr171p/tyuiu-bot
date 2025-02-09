import logging
from typing import List

from src.repository import UserRepository
from src.schemas import UserSchema


log = logging.getLogger(__name__)


class UserService:
    user_repository = UserRepository()
    
    async def register(self, user: UserSchema) -> None:
        if await self.user_repository.get_by_user_id(user.user_id) is not None:
            log.info("User %s alreasy registered", user.user_id)
            return
        registered_user = await self.user_repository.add(user)
        log.info("User %s registered successfully", registered_user)
