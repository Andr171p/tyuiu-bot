from src.core.database.models import Message
from src.core.database.crud import CRUD


class MessageService(CRUD):
    async def add_message(self, message: Message) -> Message | None:
        db_message = await self._create(message)
        return db_message
