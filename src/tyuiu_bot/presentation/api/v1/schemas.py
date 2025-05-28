from typing import Annotated

from uuid import UUID

from fastapi import Query, Form


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(XXX)XXX-XX-XX")
]

UserIdUpdate = Annotated[
    UUID,
    Form(..., description="ID пользователя в сервисе регистрации")
]
