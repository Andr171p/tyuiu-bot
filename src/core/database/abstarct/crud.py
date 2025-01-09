from abc import ABC, abstractmethod

from src.core.database.base import ModelType


class AbstractCRUD(ABC):
    @abstractmethod
    async def read(self, id: int) -> ModelType | None:
        raise NotImplementedError("read method is not implemented")

    @abstractmethod
    async def create(self, model: ModelType) -> ModelType | None:
        raise NotImplementedError("create method is not implemented")
