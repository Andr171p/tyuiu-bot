import logging

from src.presentation.api.app import create_fastapi_app


logging.basicConfig(level=logging.INFO)

app = create_fastapi_app()

