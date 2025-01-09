from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection


class AbstractContext(ABC):
    @abstractmethod
    @asynccontextmanager
    async def session(self) -> AsyncSession:
        raise NotImplementedError("session context manager is not implemented")

    @abstractmethod
    @asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        raise NotImplementedError("connect context manager is not implemented")
