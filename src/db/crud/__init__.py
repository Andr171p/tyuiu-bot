__all__ = (
    "BaseCRUD",
    "UserCRUD",
    "ContactCRUD",
    "DialogCRUD"
)

from src.db.crud.base_crud import BaseCRUD
from src.db.crud.user_crud import UserCRUD
from src.db.crud.contact_crud import ContactCRUD
from src.db.crud.dialog_crud import DialogCRUD
