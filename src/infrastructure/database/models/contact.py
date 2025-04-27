from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import BaseModel
from src.infrastructure.database.models.mixins import UserRelationMixin


class ContactModel(UserRelationMixin, BaseModel):
    __tablename__ = "contacts"

    _user_back_populates = "contact"
    _user_id_unique = True

    phone_number: Mapped[str]
    is_exists: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(phone_number={self.phone_number}, "
            f"is_exists={self.is_exists}, "
            f"user_id={self.user_id})"
        )

    def __repr__(self) -> str:
        return str(self)
