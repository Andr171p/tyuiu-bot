import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .utils import read_txt
from .constants import BASE_DIR, ENV_PATH


load_dotenv(ENV_PATH)


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")
    webhook_url: str = os.getenv("WEBHOOK_URL")


class PostgresSettings(BaseSettings):
    pg_user: str = os.getenv("PG_USER")
    pg_password: str = os.getenv("PG_PASSWORD")
    pg_host: str = os.getenv("PG_HOST")
    pg_port: int = os.getenv("PG_PORT")
    pg_name: str = os.getenv("PG_NAME")

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_name}"


class RabbitSettings(BaseSettings):
    rabbit_host: str = os.getenv("RABBIT_HOST")
    rabbit_port: int = os.getenv("RABBIT_PORT")
    rabbit_user: str = os.getenv("RABBIT_USER")
    rabbit_password: str = os.getenv("RABBIT_PASSWORD")

    @property
    def rabbit_url(self) -> str:
        return f"amqp://{self.rabbit_user}:{self.rabbit_password}@{self.rabbit_host}:{self.rabbit_port}"


class MessagesSettings(BaseSettings):
    start: str = read_txt(BASE_DIR / "messages" / "start.txt")
    info: str = read_txt(BASE_DIR / "messages" / "info.txt")
    subscription: str = read_txt(BASE_DIR / "messages" / "subscription.txt")
    error: str = read_txt(BASE_DIR / "messages" / "error.txt")


class TyuiuGPTSettings(BaseSettings):
    url: str = os.getenv("TYUIU_GPT_URL")


class RegistrationSettings(BaseSettings):
    url: str = os.getenv("REGISTRATION_URL")


class MainSiteSettings(BaseSettings):
    url: str = "https://online-service-for-applicants.onrender.com/"


class Settings(BaseSettings):
    tyuiu_gpt: TyuiuGPTSettings = TyuiuGPTSettings()
    registration: RegistrationSettings = RegistrationSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
    messages: MessagesSettings = MessagesSettings()
    main_site: MainSiteSettings = MainSiteSettings()
