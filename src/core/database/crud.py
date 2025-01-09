from sqlalchemy import select

from src.core.database.abstarct.crud import AbstractCRUD
from src.core.database.base import ModelType
from src.core.database.context import DBContext


class CRUD(AbstractCRUD, DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def read(self, id: int) -> ModelType | None:
        async with self.session() as session:
            stmt = (
                select(ModelType)
                .where(ModelType.id == id)
            )
            model = await session.execute(stmt)
            return model

    async def create(self, model: ModelType) -> ModelType | None:
        async with self.session() as session:
            session.add(model)
            await session.commit()
            return model
