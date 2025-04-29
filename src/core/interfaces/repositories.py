from datetime import datetime

from typing import (
    Protocol,
    Generic,
    TypeVar,
    List,
    Optional,
    Tuple,
    Sequence
)

from ..entities import User, Contact, CreatedUser, CreatedContact


T = TypeVar("T")


class ReadableRepository(Protocol, Generic[T]):
    async def list(self) -> List[T]: pass

    async def paginate(self, page: int, limit: int) -> List[T]: pass

    async def count(self) -> int: pass

    async def count_daily(self) -> Sequence[Tuple[datetime, int]]: pass

    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int: pass


class CrudRepository(ReadableRepository, Generic[T], Protocol):
    async def create(self, entity: T) -> T: pass

    async def read(self, telegram_id: int) -> Optional[T]: pass
    
    
class UserRepository(CrudRepository[User], Protocol):
    async def get_by_user_id(self, user_id: str) -> Optional[CreatedUser]: pass

    async def update(self, telegram_id: int, user_id: str) -> CreatedUser: pass


class ContactRepository(CrudRepository[Contact], Protocol):
    async def get_by_phone_number(self, phone_number: str) -> Optional[CreatedContact]: pass
    
    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> str: pass
    
    async def list_of_telegram_ids(self) -> Sequence[int]: pass
    
    async def get_registered(self, is_registered: bool = True) -> List[CreatedContact]: pass
