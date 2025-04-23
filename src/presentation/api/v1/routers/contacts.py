from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import ContactRepository
from src.core.entities import Contact
from src.schemas import PerDayDistributionResponse

from src.presentation.api.v1.schemas import ContactsResponse, CountResponse


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
    contacts = await contact_repository.list()
    return ContactsResponse(contacts=contacts)


@contacts_router.get(
    path="/count",
    response_model=CountResponse,
    status_code=status.HTTP_200_OK
)
async def get_count(contact_repository: FromDishka[ContactRepository]) -> CountResponse:
    total_count = await contact_repository.count()
    return CountResponse(count=total_count)


@contacts_router.get(
    path="/date-to-count/",
    response_model=PerDayDistributionResponse,
    status_code=status.HTTP_200_OK
)
async def get_per_day_count_distribution(
        contact_repository: FromDishka[ContactRepository]
) -> PerDayDistributionResponse:
    distribution = await contact_repository.get_count_per_day()
    return PerDayDistributionResponse(distribution=distribution)


@contacts_router.get(
    path="/{user_id}",
    response_model=Contact,
    status_code=status.HTTP_200_OK
)
async def get_contact(
        user_id: int,
        contact_repository: FromDishka[ContactRepository]
) -> Contact:
    return await contact_repository.get(user_id)
