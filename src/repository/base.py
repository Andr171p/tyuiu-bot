from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseRepository(ABC):
    crud = None

    @abstractmethod
    async def add(self, item: BaseModel) -> BaseModel:
        raise NotImplemented
