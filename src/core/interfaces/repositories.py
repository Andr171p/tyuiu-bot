from datetime import datetime

from typing import (
    Protocol,
    Generic,
    TypeVar,
    List,
    Optional,
    Tuple
)

from src.core.entities import User, Contact


T = TypeVar("T")


class ReadableRepository(Protocol, Generic[T]):
    async def read(self, user_id: int) -> Optional[T]: pass

    async def list(self) -> List[T]: pass

    async def paginate(self, page: int, limit: int) -> List[T]: pass

    async def count(self) -> int: pass

    async def count_daily(self) -> List[Tuple[datetime, int]]: pass


class CrudRepository(ReadableRepository, Generic[T], Protocol):
    async def create(self, entity: T) -> int: pass
    
    async def update(self, user_id: int, is_exists: bool) -> T: pass
    
    async def delete(self, user_id: int) -> T: pass
    
    
class UserRepository(CrudRepository[User], Protocol):
    pass


class ContactRepository(CrudRepository[Contact], Protocol):
    async def read_by_phone_number(self, phone_number: str) -> Optional[Contact]: pass
    
    async def read_user_id_by_phone_number(self, phone_number: str) -> int: pass
    
    async def read_phone_number_by_user_id(self, user_id: int) -> str: pass
    
    async def list_user_ids(self) -> List[int]: pass
    
    async def read_is_exists(self, is_exists: bool = True) -> List[Contact]: pass
