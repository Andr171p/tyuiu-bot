from typing import (
    Protocol,
    Generic,
    TypeVar,
    List,
    Optional,
    Sequence,
    Any
)

from src.core.entities import User, Contact
from src.dto import CreationDateCountDTO


T = TypeVar("T")


class Repository(Protocol, Generic[T]):
    async def save(self, entity: T) -> int:
        raise NotImplemented

    async def get(self, user_id: int) -> Optional[T]:
        raise NotImplemented

    async def list(self) -> List[T]:
        raise NotImplemented


class AnalyticsRepository(Protocol):
    async def count(self) -> int:
        raise NotImplemented

    async def count_by_creation_date(self) -> List[CreationDateCountDTO]:
        raise NotImplemented


class UserRepository(Repository[User], AnalyticsRepository, Protocol):
    pass


class ContactRepository(Repository[Contact], AnalyticsRepository, Protocol):
    async def update(self, user_id: int, **kwargs: Any) -> Contact:
        raise NotImplemented

    async def get_by_phone_number(self, phone_number: str) -> Optional[Contact]:
        raise NotImplemented

    async def get_user_id_by_phone_number(self, phone_number: str) -> Optional[int]:
        raise NotImplemented

    async def get_phone_number_by_user_id(self, user_id: int) -> Optional[str]:
        raise NotImplemented

    async def list_user_ids(self) -> Sequence[Optional[int]]:
        raise NotImplemented
