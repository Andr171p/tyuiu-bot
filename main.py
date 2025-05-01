import logging

from src.presentation.api.app import create_fastapi_app


logging.basicConfig(level=logging.INFO)

app = create_fastapi_app()

from src.settings import AppSettings

print(AppSettings().url)
