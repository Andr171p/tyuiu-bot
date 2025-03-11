from aiogram.types import Message
from pydantic import BaseModel


class MessagePresenter(BaseModel):
    message: Message

    async def present(self) -> None:
        raise NotImplementedError
