import uuid
from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, Text, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as POSTGRES_UUID

from .base import Base


class UserModel(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[UUID | None] = mapped_column(
        POSTGRES_UUID(as_uuid=True),
        unique=True,
        nullable=True
    )
    first_name: Mapped[str | None] = mapped_column(nullable=True)
    last_name: Mapped[str | None] = mapped_column(nullable=True)
    username: Mapped[str | None] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(unique=True)
    status: Mapped[int]

    notifications: Mapped[list["NotificationModel"]] = relationship(back_populates="user")

    __table_args__ = (
        Index("id_index", "telegram_id", "user_id"),
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n"
            f"telegram_id={self.telegram_id},\n"
            f"user_id={self.user_id},\n"
            f"first_name={self.first_name},\n"
            f"last_name={self.last_name},\n"
            f"username={self.username},\n"
            f"phone_number={self.phone_number},\n"
            f"created_at={self.created_at}\n"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)


class NotificationModel(Base):
    __tablename__ = "notifications"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.user_id"), unique=False, nullable=False)
    notification_id: Mapped[UUID] = mapped_column(
        POSTGRES_UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    level: Mapped[str] = mapped_column(nullable=False)
    photo: Mapped[str | None] = mapped_column(nullable=True)
    text: Mapped[str] = mapped_column(Text)
    status: Mapped[str]
    message_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=True)

    user: Mapped["UserModel"] = relationship(back_populates="notifications")
