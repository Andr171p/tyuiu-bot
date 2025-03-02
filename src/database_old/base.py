from typing import TypeVar

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from src.config import settings


def get_db_url() -> str:
    return settings.db.url


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


ModelType = TypeVar("ModelType", bound=Base)
