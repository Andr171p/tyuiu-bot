from datetime import datetime

from typing import TypeVar

from sqlalchemy import BigInteger, DateTime, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    DeclarativeBase
)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


ModelType = TypeVar("ModelType", bound=Base)


class UserModel(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    contact: Mapped["ContactModel"] = relationship(back_populates="user")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(user_id={self.user_id}, username={self.username})"

    def __repr__(self) -> str:
        return str(self)


class ContactModel(Base):
    __tablename__ = "contacts"

    phone_number: Mapped[str]
    is_exists: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(DateTime)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
        unique=True,
        nullable=False
    )
    user: Mapped["UserModel"] = relationship(
        argument="UserModel",
        back_populates="contact"
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(phone_number={self.phone_number}, "
            f"is_exists={self.is_exists}, "
            f"user_id={self.user_id})"
        )

    def __repr__(self) -> str:
        return str(self)
