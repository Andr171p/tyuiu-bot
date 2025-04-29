from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    validates
)

from src.core.entities import User, Contact
from .base import (
    Base,
    uuid_nullable,
    tg_id,
    str_nullable,
    created_at
)


class UserModel(Base):
    __tablename__ = "users"

    telegram_id: Mapped[tg_id]
    user_id: Mapped[uuid_nullable]
    username: Mapped[str_nullable]
    created_at: Mapped[created_at]

    contact: Mapped["ContactModel"] = relationship(back_populates="user")

    @validates("user_id")
    def set_registered(self, user_id: str) -> str:
        if user_id is not None and self.contact:
            self.contact.is_registered = True
        return user_id

    @classmethod
    def from_user(cls, user: User) -> "UserModel":
        return cls(
            telegram_id=user.telegram_id,
            user_id=user.user_id,
            username=user.username
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(telegram_id={self.user_id}, username={self.username})"

    def __repr__(self) -> str:
        return str(self)


class ContactModel(Base):
    __tablename__ = "contacts"

    phone_number: Mapped[str]
    is_registered: Mapped[bool]
    created_at: Mapped[created_at]

    telegram_id: Mapped[int] = mapped_column(
        ForeignKey("users.telegram_id"),
        unique=True,
        nullable=False
    )
    user: Mapped["UserModel"] = relationship(
        argument="UserModel",
        back_populates="contact"
    )

    @classmethod
    def from_contact(cls, contact: Contact) -> "ContactModel":
        return cls(
            phone_number=contact.phone_number,
            is_registered=contact.is_registered
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(telegram_id={self.telegram_id}, phone_number={self.phone_number})"

    def __repr__(self) -> str:
        return str(self)
