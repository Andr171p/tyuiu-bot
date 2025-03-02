from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager
    
from sqlalchemy import select, func
    
from src.database.crud.base_crud import BaseCRUD
from src.database.models import ChatModel


class ChatCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager
        
    async def create(self, chat: ChatModel) -> int:
        async with self._manager.session() as session:
            session.add(chat)
            id = chat.id
            await session.commit()
        return id
    
    async def read_by_user_id(self, user_id: int) -> Sequence[ChatModel] | None:
        async with self._manager.session() as session:
            stmt = (
                select(ChatModel)
                .where(ChatModel.user_id == user_id)
            )
            chats = await session.execute(stmt)
        return chats.scalars().all()
    
    async def read_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> Sequence[ChatModel] | None:
        offset = (page - 1) * limit
        async with self._manager.session() as session:
            stmt = (
                select(ChatModel)
                .where(ChatModel.user_id == user_id)
                .offset(offset)
                .limit(limit)   
            )
            chats = await session.execute(stmt)
        return chats.scalars().all()
    
    async def read_all(self) -> Sequence[ChatModel] | None:
        async with self._manager.session() as session:
            stmt = select(ChatModel)
            chats = await session.execute(stmt)
        return chats.scalars().all()
    
    async def read_count_by_user_id(self, user_id: int) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count)
                .select_from(ChatModel)
                .where(ChatModel.user_id == user_id)
            )
            chats_count = await session.execute(stmt)
        return chats_count.scalar_one_or_none()
    
    async def read_total_count(self) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count)
                .select_from(ChatModel)
            )
            chats_count = await session.execute(stmt)
        return chats_count.scalar_one_or_none()
