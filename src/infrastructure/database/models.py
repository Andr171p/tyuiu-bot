from sqlalchemy.orm import Mapped

from src.core.entities import User
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
    phone_number: Mapped[str_nullable]
    created_at: Mapped[created_at]

    @classmethod
    def from_user(cls, user: User) -> "UserModel":
        return cls(
            telegram_id=user.telegram_id,
            user_id=user.user_id,
            username=user.username,
            phone_number=user.phone_number
        )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n"
            f"telegram_id={self.user_id}, \n"
            f"username={self.username},\n"
            f"user_id={self.user_id}\n"
            f"phone_number={self.phone_number},\n"
            f"created_at={self.created_at}\n"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)
