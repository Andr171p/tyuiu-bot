from typing import Union

from fastapi import APIRouter, status, Query, HTTPException
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.entities import Contact
from src.core.interfaces import ContactRepository
from src.presentation.api.v1.schemas import (
    ContactsResponse,
    ContactsPageResponse,
    CountResponse,
    ContactUpdate,
    PhoneNumberQuery,
    DailyCountResponse
)


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
async def get_contacts(
        contact_repository: FromDishka[ContactRepository]
) -> ContactsResponse:
    contacts = await contact_repository.list()
    return ContactsResponse(contacts=contacts)


@contacts_router.get(
    path="/search",
    response_model=Contact,
    status_code=status.HTTP_200_OK
)
async def search_by_phone_number(
        phone_number: PhoneNumberQuery,
        contact_repository: FromDishka[ContactRepository]
) -> Contact:
    contact = await contact_repository.get_by_phone_number(phone_number)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@contacts_router.get(
    path="/count",
    response_model=CountResponse,
    status_code=status.HTTP_200_OK
)
async def get_count(contact_repository: FromDishka[ContactRepository]) -> CountResponse:
    total_count = await contact_repository.count()
    return CountResponse(count=total_count)


@contacts_router.get(
    path="/daily-count/",
    response_model=DailyCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_daily_count(
        contact_repository: FromDishka[ContactRepository]
) -> DailyCountResponse:
    date_to_count = await contact_repository.daily_count()
    return DailyCountResponse(distribution=date_to_count)


@contacts_router.get(
    path="/{user_id}",
    response_model=Contact,
    status_code=status.HTTP_200_OK
)
async def get_contact(
        user_id: int,
        contact_repository: FromDishka[ContactRepository]
) -> Contact:
    contact = await contact_repository.get(user_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@contacts_router.patch(
    path="/{user_id}",
    response_model=Contact,
    status_code=status.HTTP_200_OK
)
async def update_contact(
        user_id: int,
        contact_update: ContactUpdate,
        contact_repository: FromDishka[ContactRepository]
) -> Contact:
    contact = await contact_repository.update(user_id, is_exists=contact_update.is_exists)
    return contact
