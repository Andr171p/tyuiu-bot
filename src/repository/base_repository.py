from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.database.crud import BaseCRUD

from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseRepository(ABC):
    _crud: "BaseCRUD"

    @abstractmethod
    async def save(self, entity: BaseModel) -> int:
        raise NotImplemented
    
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> List[BaseModel] | BaseModel:
        raise NotImplemented

    @abstractmethod
    async def get_all(self) -> List[BaseModel]:
        raise NotImplemented
    
    @abstractmethod
    async def get_total_count(self) -> int:
        raise NotImplemented
