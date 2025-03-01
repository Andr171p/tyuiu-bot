from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base_model import BaseModel
from src.db.models.user_relation_mixin import UserRelationMixin


class ContactModel(UserRelationMixin, BaseModel):
    __tablename__ = "contacts"
    
    _user_back_populates = "contact"
    _user_id_unique = True

    phone_number: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(phone_number={self.phone_number}, user_id={self.user_id})"

    def __repr__(self) -> str:
        return str(self)