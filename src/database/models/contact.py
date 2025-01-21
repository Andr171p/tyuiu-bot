from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.database.models.mixins import UserRelationMixin


class Contact(UserRelationMixin, Base):
    _user_back_populates = "contact"
    _user_id_unique = True

    phone_number: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(phone_number={self.phone_number}, user_id={self.user_id})"

    def __repr__(self) -> str:
        return str(self)
