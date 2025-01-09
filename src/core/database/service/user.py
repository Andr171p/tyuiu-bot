from sqlalchemy import select

from src.core.database.models import User
from src.core.database.context import DBContext


class UserService(DBContext):
    async def get_user_by_user_id(self, user_id: int) -> User | None:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
            return user.scalar_one_or_none()

    async def add_user(self, user: User) -> User | None:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            return user
