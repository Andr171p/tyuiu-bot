__all__ = (
    "UsersResponse",
    "UsersCountResponse",
    "ContactsResponse",
    "ContactsCountResponse",
    "DialogsResponse",
    "DialogsCountResponse"
)

from src.presentation.api.v1.schemas.users_schemas import UsersResponse, UsersCountResponse
from src.presentation.api.v1.schemas.contacts_schemas import ContactsResponse, ContactsCountResponse
from src.presentation.api.v1.schemas.chats_schemas import DialogsResponse, DialogsCountResponse
