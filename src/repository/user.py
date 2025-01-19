from src.database.service import UserService
from src.database.models import User
from src.schemas import UserSchema


class UserRepository:
    user_service = UserService()

    @classmethod
    async def get_user_by_user_id(cls, user_id: int) -> UserSchema:
        user = await cls.user_service.get_user_by_user_id(user_id)
        return UserSchema(**user.__dict__)

    @classmethod
    async def add_user(cls, user: UserSchema) -> UserSchema:
        added_user = await cls.user_service.add_user(User(**user.dict()))
        return UserSchema(**added_user.__dict__)
