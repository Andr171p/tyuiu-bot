import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

from .constants import ENV_PATH, POSTGRES_DRIVER


load_dotenv(ENV_PATH)


class BotSettings(BaseSettings):
    TOKEN: str = os.getenv("BOT_TOKEN")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")


class PostgresSettings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_NAME")

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+{POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


class RabbitSettings(BaseSettings):
    RABBIT_HOST: str = os.getenv("RABBIT_HOST")
    RABBIT_PORT: int = os.getenv("RABBIT_PORT")
    RABBIT_USER: str = os.getenv("RABBIT_USER")
    RABBIT_PASSWORD: str = os.getenv("RABBIT_PASSWORD")

    @property
    def rabbit_url(self) -> str:
        return f"amqp://{self.RABBIT_USER}:{self.RABBIT_PASSWORD}@{self.RABBIT_HOST}:{self.RABBIT_PORT}"


class APISettings(BaseSettings):
    TYUIU_GPT_URL: str = os.getenv("TYUIU_GPT_URL")
    REGISTRATION_URL: str = os.getenv("REGISTRATION_URL")


class Settings(BaseSettings):
    api: APISettings = APISettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
