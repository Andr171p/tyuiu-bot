__all__ = (
    "BaseCRUD",
    "UserCRUD",
    "ContactCRUD",
    "DialogCRUD"
)

from src.database.crud.base_crud import BaseCRUD
from src.database.crud.user_crud import UserCRUD
from src.database.crud.contact_crud import ContactCRUD
from src.database.crud.dialog_crud import DialogCRUD
