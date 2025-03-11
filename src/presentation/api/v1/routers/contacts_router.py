from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import ContactRepository
from src.core.entities import Contact
from src.schemas import ContactsResponse, ContactsCountResponse


contacts_router = APIRouter(
    prefix="/api/v1/contacts",
    tags=["Users who shared contacts"],
    route_class=DishkaRoute
)


@contacts_router.get(
    path="/",
    response_model=ContactsResponse,
    status_code=status.HTTP_200_OK
)
async def get_contacts(contact_repository: FromDishka[ContactRepository]) -> ContactsResponse:
    contacts = await contact_repository.get_all()
    return ContactsResponse(contacts=contacts)


@contacts_router.get(
    path="/count/",
    response_model=ContactsCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_contacts_count(contact_repository: FromDishka[ContactRepository]) -> ContactsCountResponse:
    contacts_count = await contact_repository.get_total_count()
    return ContactsCountResponse(count=contacts_count)


@contacts_router.get(
    path="/{user_id}/",
    response_model=Contact,
    status_code=status.HTTP_200_OK
)
async def get_contact_by_user_id(
        user_id: int,
        contact_repository: FromDishka[ContactRepository]
) -> Contact:
    contact = await contact_repository.get_by_user_id(user_id)
    return contact
