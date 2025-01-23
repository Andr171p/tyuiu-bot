import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from dishka.integrations.fastapi import setup_dishka

from src.app.container import container
from src.app.api_v1.lifespan import lifespan
from src.app.api_v1.routers import (
    wh_router,
    admin_router,
    statistics_router,
    notification_router
)


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(wh_router)
app.include_router(statistics_router)
app.include_router(admin_router)
app.include_router(notification_router)

setup_dishka(
    container=container,
    app=app
)
