from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram.types import Message

from abc import ABC, abstractmethod


class BasePresenter(ABC):
    _message: "Message"

    @abstractmethod
    async def present(self) -> None:
        raise NotImplemented
