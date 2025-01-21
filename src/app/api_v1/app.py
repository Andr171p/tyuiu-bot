import logging

from fastapi import FastAPI

from src.app.api_v1.lifespan import lifespan
from src.app.api_v1.routers import (
    wh_router,
    admin_router
)


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    lifespan=lifespan
)

app.include_router(wh_router)
app.include_router(admin_router)
