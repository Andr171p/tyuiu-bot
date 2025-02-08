from typing import Sequence

from sqlalchemy import select

from src.database.models import Message
from src.database.interfaces import BaseCRUD
from src.database.manager_provider import get_database_manager


class MessageCRUD(BaseCRUD):
    def __init__(self, manager = get_database_manager()) -> None:
        self._manager = manager

    async def create(self, message: Message) -> Message | None:
        async with self._manager.session() as session:
            session.add(message)
            await session.commit()
        return message
    
    async def read_by_user_id(self, user_id: int) -> Sequence[Message] | None:
        async with self._manager.session() as session:
            stmt = (
                select(Message)
                .where(Message.user_id == user_id)
            )
            messages = await session.execute(stmt)
        return messages.scalars().all()

    async def read_all(self) -> Sequence[Message] | None:
        async with self._manager.session() as session:
            stmt = select(Message)
            messages = await session.execute(stmt)
        return messages.scalars().all()
