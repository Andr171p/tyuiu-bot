from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, AsyncIterator

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection


class BaseManager(ABC):
    @abstractmethod
    @asynccontextmanager
    async def session(self) -> "AsyncSession":
        raise NotImplemented

    @abstractmethod
    @asynccontextmanager
    async def connect(self) -> AsyncIterator["AsyncConnection"]:
        raise NotImplemented
