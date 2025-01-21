from src.repository.base import BaseRepository
from src.database.crud import UserCRUD
from src.database.models import User
from src.schemas import UserSchema


class UserRepository(BaseRepository):
    crud = UserCRUD()

    async def get_by_user_id(self, user_id: int) -> UserSchema | None:
        user = await self.crud.read_by_user_id(user_id)
        if user is None:
            return
        return UserSchema(**user.__dict__)

    async def add(self, user: UserSchema) -> UserSchema:
        added_user = await self.crud.create(User(**user.dict()))
        return UserSchema(**added_user.__dict__)
