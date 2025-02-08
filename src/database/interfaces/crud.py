from abc import ABC, abstractmethod
from typing import Sequence

from src.database.base import ModelType


class BaseCRUD(ABC):
    @abstractmethod
    async def create(self, item: ModelType) -> ModelType:
        raise NotImplemented
    
    @abstractmethod
    async def read_all(self) -> Sequence[ModelType]:
        raise NotImplemented
