from datetime import datetime

from sqlalchemy import Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database_old.base import Base
from src.database_old.models.mixins import UserRelationMixin


class Message(UserRelationMixin, Base):
    _user_back_populates = "messages"

    user_message: Mapped[str] = mapped_column(Text)
    bot_message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at})"

    def __repr__(self) -> str:
        return str(self)
