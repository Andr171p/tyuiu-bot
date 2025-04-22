from typing import List
from abc import ABC, abstractmethod

from pydantic import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    async def save(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def get(self, user_id: int) -> BaseModel:
        raise NotImplemented

    @abstractmethod
    async def list(self) -> List[BaseModel]:
        raise NotImplemented
