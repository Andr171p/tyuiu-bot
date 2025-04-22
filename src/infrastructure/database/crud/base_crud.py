from typing import TYPE_CHECKING, Sequence, Union, List, Tuple
from datetime import datetime

if TYPE_CHECKING:
    from src.infrastructure.database.database_manager import DatabaseManager
    from src.infrastructure.database.models import BaseModel

from abc import ABC, abstractmethod


class BaseCRUD(ABC):
    _manager: "DatabaseManager"
    
    @abstractmethod
    async def create(self, model: "BaseModel") -> int:
        raise NotImplemented
    
    @abstractmethod
    async def read_all(self) -> Sequence["BaseModel"]:
        raise NotImplemented
    
    @abstractmethod
    async def read_by_user_id(
        self, 
        user_id: int
    ) -> Union["BaseModel", Sequence["BaseModel"]]:
        raise NotImplemented
    
    @abstractmethod
    async def read_total_count(self) -> int:
        raise NotImplemented

    @abstractmethod
    async def read_count_per_day(self) -> List[Tuple[datetime, int]]:
        raise NotImplemented
