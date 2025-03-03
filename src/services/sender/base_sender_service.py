from typing import Any
from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    async def send_message(self, user_id: int, text: str) -> bool:
        raise NotImplemented

    @abstractmethod
    async def send_message_with_photo(self, user_id: int, photo: Any, text: str) -> bool:
        raise NotImplemented
