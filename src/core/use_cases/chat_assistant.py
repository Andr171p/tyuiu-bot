from typing import Optional

from src.infrastructure.apis import ChatAssistantAPI
from src.repository import DialogRepository


class ChatAssistant:
    def __init__(self) -> None:
        ...

    async def answer(self, chat_id: str, text: str) -> str:
        ...
