from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.infrastructure.database.models.contact_model import ContactModel


class UserModel(BaseModel):
    __tablename__ = "users"
    
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    contact: Mapped["ContactModel"] = relationship(back_populates="user")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(user_id={self.user_id}, username={self.username})"

    def __repr__(self) -> str:
        return str(self)