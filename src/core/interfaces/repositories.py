from abc import ABC, abstractmethod
from typing import List, Optional

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
    async def paginate(self, page: int, limit: int) -> List[User]: pass
    
    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> Optional[User]: pass

    @abstractmethod
    async def get_by_user_ids(self, user_ids: List[str]) -> List[User]: pass
    
    @abstractmethod
    async def get_by_phone_number(self, phone_number: str) -> User: pass

    @abstractmethod
    async def get_by_phone_numbers(self, phone_numbers: List[str]) -> List[User]: pass

    @abstractmethod
    async def get_telegram_id_by_user_id(self, user_id: str) -> int: pass

    @abstractmethod
    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int: pass
