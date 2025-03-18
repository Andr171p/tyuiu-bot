from typing import Any
from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    async def send_message(self, *args) -> bool:
        raise NotImplemented

    @abstractmethod
    async def send_message_with_photo(self, *args) -> bool:
        raise NotImplemented
