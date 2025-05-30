from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dishka.integrations.fastapi import setup_dishka

from src.tyuiu_bot.ioc import container
from .lifespan import lifespan
from .v1.routers import (
    webhook_router,
    users_router,
    notifications_router
)


def create_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(webhook_router)
    app.include_router(users_router)
    app.include_router(notifications_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    setup_dishka(container=container, app=app)
    return app
