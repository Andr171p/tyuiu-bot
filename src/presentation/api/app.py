from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dishka.integrations.fastapi import setup_dishka

from src.presentation.di import container
from src.presentation.api.lifespan import lifespan
from src.presentation.api.v1.routers import (
    webhook_router,
    users_router,
    contacts_router,
    chats_router,
    notifications_router
)


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(webhook_router)
    app.include_router(users_router)
    app.include_router(contacts_router)
    app.include_router(chats_router)
    app.include_router(notifications_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    setup_dishka(
        container=container,
        app=app
    )
    return app
