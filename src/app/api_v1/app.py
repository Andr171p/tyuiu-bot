import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from dishka.integrations.fastapi import setup_dishka

from src.app.container import container
from src.app.api_v1.lifespan import lifespan
from src.app.api_v1.routers import (
    wh_router,
    admin_router,
    users_router,
    subscribers_router,
    messages_router,
    notifications_router
)


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(wh_router)
app.include_router(admin_router)
app.include_router(users_router)
app.include_router(subscribers_router)
app.include_router(messages_router)
app.include_router(notifications_router)

setup_dishka(
    container=container,
    app=app
)
