from typing import Sequence

from sqlalchemy import select

from src.database.models import Message
from src.database.context import DBContext


class MessageCRUD(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create(self, message: Message) -> Message | None:
        async with self.session() as session:
            session.add(message)
            await session.commit()
        return message

    async def read_all(self) -> Sequence[Message] | None:
        async with self.session() as session:
            stmt = select(Message)
            messages = await session.execute(stmt)
        return messages.scalars().all()
