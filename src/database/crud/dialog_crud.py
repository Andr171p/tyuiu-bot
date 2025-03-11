from typing import TYPE_CHECKING, Sequence, List, Tuple
from datetime import datetime

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager
    
from sqlalchemy import select, func
    
from src.database.crud.base_crud import BaseCRUD
from src.database.models import DialogModel


class DialogCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager
        
    async def create(self, dialog: DialogModel) -> int:
        async with self._manager.session() as session:
            session.add(dialog)
            id = dialog.id
            await session.commit()
        return id
    
    async def read_by_user_id(self, user_id: int) -> Sequence[DialogModel] | None:
        async with self._manager.session() as session:
            stmt = (
                select(DialogModel)
                .where(DialogModel.user_id == user_id)
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> Sequence[DialogModel] | None:
        offset = (page - 1) * limit
        async with self._manager.session() as session:
            stmt = (
                select(DialogModel)
                .where(DialogModel.user_id == user_id)
                .offset(offset)
                .limit(limit)   
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_all(self) -> Sequence[DialogModel] | None:
        async with self._manager.session() as session:
            stmt = select(DialogModel)
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_count_by_user_id(self, user_id: int) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count())
                .select_from(DialogModel)
                .where(DialogModel.user_id == user_id)
            )
            dialogs_count = await session.execute(stmt)
        return dialogs_count.scalar_one_or_none()
    
    async def read_total_count(self) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count())
                .select_from(DialogModel)
            )
            dialogs_count = await session.execute(stmt)
        return dialogs_count.scalar_one_or_none()

    async def read_count_per_day(self) -> List[Tuple[datetime, int]]:
        async with self._manager.session() as session:
            stmt = (
                select(
                    func.date(DialogModel.created_at).label("date"),
                    func.count().label("count")
                )
                .group_by(func.date(DialogModel.created_at))
                .order_by(func.date(DialogModel.created_at))
            )
            counts_per_days = await session.execute(stmt)
        return counts_per_days.all()
