from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import ContactRepository
from src.core.entities import Contact


contacts_router = APIRouter(
    prefix="/api/v1/contacts",
    tags=["Users who shared contacts"],
    route_class=DishkaRoute
)


@contacts_router.get(
    path="/",
    status_code=status.HTTP_200_OK
)
async def get_contacts(contact_repository: FromDishka[ContactRepository]) -> JSONResponse:
    contacts = await contact_repository.get_all()
    return JSONResponse(content={"contacts": contacts})


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


@contacts_router.get(
    path="/count/",
    status_code=status.HTTP_200_OK
)
async def get_contacts_count(contact_repository: FromDishka[ContactRepository]) -> JSONResponse:
    contacts_count = await contact_repository.get_total_count()
    return JSONResponse(content={"count": contacts_count})
