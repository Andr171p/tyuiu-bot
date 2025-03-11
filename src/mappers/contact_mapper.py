from datetime import datetime
from aiogram.types import Message

from src.core.entities import Contact


class ContactMapper:
    @staticmethod
    def from_message(message: Message) -> Contact:
        return Contact(
            user_id=message.from_user.id,
            phone_number=message.contact.phone_number,
            created_at=datetime.now()
        )
