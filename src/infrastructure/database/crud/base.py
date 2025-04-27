from datetime import datetime

from abc import ABC, abstractmethod
from typing import Sequence, Tuple, Optional

from src.infrastructure.database.models import BaseModel


class CRUD(ABC):

    @abstractmethod
    async def create(self, model: BaseModel) -> int:
        raise NotImplemented

    @abstractmethod
    async def read(self, user_id: int) -> Optional[BaseModel]:
        raise NotImplemented

    @abstractmethod
    async def read_all(self) -> Sequence[BaseModel]:
        raise NotImplemented

    @abstractmethod
    async def count(self) -> int:
        raise NotImplemented

    @abstractmethod
    async def read_count_by_creation_date(self) -> Sequence[Tuple[datetime, int]]:
        raise NotImplemented
