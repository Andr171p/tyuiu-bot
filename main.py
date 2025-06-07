import logging

from src.tyuiu_bot.presentation.api import create_fastapi_app


logging.basicConfig(level=logging.INFO)

app = create_fastapi_app()

