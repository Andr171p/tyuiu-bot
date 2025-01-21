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
