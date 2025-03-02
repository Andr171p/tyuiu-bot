from datetime import datetime

from sqlalchemy import Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base_model import BaseModel
from src.database.models.user_relation_mixin import UserRelationMixin


class ChatModel(UserRelationMixin, BaseModel):
    __tablename__ = "chats"
    
    _user_back_populates = "chats"

    user_message: Mapped[str] = mapped_column(Text)
    chat_bot_message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at})"

    def __repr__(self) -> str:
        return str(self)