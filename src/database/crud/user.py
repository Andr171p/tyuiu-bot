from sqlalchemy import select

from src.database.models import User
from src.database.context import DBContext


class UserCRUD(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def read_by_user_id(self, user_id: int) -> User | None:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def create(self, user: User) -> User | None:
        async with self.session() as session:
            session.add(user)
            await session.commit()
        return user
