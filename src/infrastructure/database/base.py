import uuid
from datetime import datetime
from typing import Annotated, Optional

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


uuid_nullable = Annotated[
    Optional[uuid.UUID],
    mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=True,
        index=True
    )
]
tg_id = Annotated[
    int,
    mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True
    )
]
str_nullable = Annotated[str, mapped_column(nullable=True)]
created_at = Annotated[datetime, mapped_column(DateTime, default=datetime.now)]
