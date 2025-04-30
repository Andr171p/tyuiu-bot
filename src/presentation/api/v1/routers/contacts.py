from typing import Union

from fastapi import APIRouter, status, Query, HTTPException
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.entities import CreatedContact
from src.core.interfaces import ContactRepository
from src.presentation.api.v1.schemas import (
    ContactsResponse,
    ContactsPageResponse,
    CountResponse,
    PhoneNumberQuery,
    DailyCount,
    DailyCountResponse
)
from src.constants import (
    GE_PAGINATED,
    DEFAULT_PAGE,
    DEFAULT_LIMIT,
    DEFAULT_IS_PAGINATED
)


contacts_router = APIRouter(
    prefix="/api/v1/contacts",
    tags=["Users who shared contacts"],
    route_class=DishkaRoute
)


@contacts_router.get(
    path="/",
    response_model=Union[ContactsResponse, ContactsPageResponse],
    status_code=status.HTTP_200_OK
)
async def get_contacts(
        contact_repository: FromDishka[ContactRepository],
        is_paginated: bool = Query(default=DEFAULT_IS_PAGINATED),
        page: int = Query(ge=GE_PAGINATED, default=DEFAULT_PAGE),
        limit: int = Query(ge=GE_PAGINATED, default=DEFAULT_LIMIT)
) -> Union[ContactsResponse, ContactsPageResponse]:
    if is_paginated:
        total = await contact_repository.count()
        contacts = await contact_repository.paginate(page, limit)
        return ContactsPageResponse(
            total=total,
            page=page,
            limit=limit,
            contacts=contacts
        )
    contacts = await contact_repository.list()
    return ContactsResponse(contacts=contacts)


@contacts_router.get(
    path="/search",
    response_model=CreatedContact,
    status_code=status.HTTP_200_OK
)
async def search_by_phone_number(
        phone_number: PhoneNumberQuery,
        contact_repository: FromDishka[ContactRepository]
) -> CreatedContact:
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
    count = await contact_repository.count()
    return CountResponse(count=count)


@contacts_router.get(
    path="/count-daily",
    response_model=DailyCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_count_daily(
        contact_repository: FromDishka[ContactRepository]
) -> DailyCountResponse:
    counts = await contact_repository.count_daily()
    return DailyCountResponse(
        daily=[DailyCount(date=date, count=count) for date, count in counts]
    )


@contacts_router.get(
    path="/{user_id}",
    response_model=CreatedContact,
    status_code=status.HTTP_200_OK
)
async def get_contact(
        user_id: str,
        contact_repository: FromDishka[ContactRepository]
) -> CreatedContact:
    contact = await contact_repository.get_by_user_id(user_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
