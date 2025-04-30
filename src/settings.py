import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from .utils import read_txt
from .constants import BASE_DIR, ENV_PATH


load_dotenv(ENV_PATH)


class AppSettings(BaseSettings):
    url: str = os.getenv("URL")


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class PostgresSettings(BaseSettings):
    user: str = os.getenv("PG_USER")
    password: str = os.getenv("PG_PASSWORD")
    host: str = os.getenv("PG_HOST")
    port: int = os.getenv("PG_PORT")
    name: str = os.getenv("PG_NAME")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


class RabbitSettings(BaseSettings):
    host: str = os.getenv("RABBIT_HOST")
    port: int = os.getenv("RABBIT_PORT")
    user: str = os.getenv("RABBIT_USER")
    password: str = os.getenv("RABBIT_PASSWORD")

    url: str = f"amqp://{user}:{password}@{host}:{port}"


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
    app: AppSettings = AppSettings()
    tyuiu_gpt: TyuiuGPTSettings = TyuiuGPTSettings()
    registration: RegistrationSettings = RegistrationSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    rabbit: RabbitSettings = RabbitSettings()
    messages: MessagesSettings = MessagesSettings()
    main_site: MainSiteSettings = MainSiteSettings()
