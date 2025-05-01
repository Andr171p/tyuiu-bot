from datetime import datetime

from abc import ABC, abstractmethod
from typing import (
    List,
    Optional,
    Tuple,
    Sequence
)

from ..entities import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User: pass

    @abstractmethod
    async def read(self, telegram_id: int) -> Optional[User]: pass

    @abstractmethod
    async def update(self, telegram_id: int, **kwargs) -> User: pass

    @abstractmethod
    async def list(self) -> List[User]: pass

    @abstractmethod
    async def list_registered(self) -> List[User]: pass

    @abstractmethod
    async def paginate(self, page: int, limit: int) -> List[User]: pass

    @abstractmethod
    async def paginate_registered(self, page: int, limit: int) -> List[User]: pass

    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> Optional[User]: pass

    @abstractmethod
    async def get_by_phone_number(self, phone_number: str) -> Optional[User]: pass

    @abstractmethod
    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int: pass

    @abstractmethod
    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> Optional[str]: pass

    @abstractmethod
    async def get_telegram_id_by_user_id(self, user_id: str) -> int: pass

    @abstractmethod
    async def get_telegram_ids(self) -> Sequence[int]: pass

    @abstractmethod
    async def get_telegram_ids_by_phone_numbers(self, phone_numbers: List[str]) -> Sequence[int]: pass

    @abstractmethod
    async def get_telegram_ids_by_user_ids(self, user_ids: List[str]) -> Sequence[int]: pass

    @abstractmethod
    async def count(self) -> int: pass

    @abstractmethod
    async def count_phone_numbers(self) -> int: pass

    @abstractmethod
    async def count_registered(self) -> int: pass

    @abstractmethod
    async def count_daily(self) -> Sequence[Tuple[datetime, int]]: pass
