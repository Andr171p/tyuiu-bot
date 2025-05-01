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
    user: str = os.getenv("PG_USER")
    password: str = os.getenv("PG_PASSWORD")
    host: str = os.getenv("PG_HOST")
    port: int = os.getenv("PG_PORT")
    name: str = os.getenv("PG_NAME")

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class RabbitSettings(BaseSettings):
    host: str = os.getenv("RABBIT_HOST")
    port: int = os.getenv("RABBIT_PORT")
    user: str = os.getenv("RABBIT_USER")
    password: str = os.getenv("RABBIT_PASSWORD")

    @property
    def rabbit_url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}"


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
