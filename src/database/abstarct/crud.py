from abc import ABC, abstractmethod

from src.database.base import ModelType


class AbstractCRUD(ABC):
    @abstractmethod
    async def create(self, item: ModelType) -> ModelType:
        raise NotImplemented
