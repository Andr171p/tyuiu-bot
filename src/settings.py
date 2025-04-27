import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from src.utils import read_txt


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class AppSettings(BaseSettings):
    url: str = os.getenv("HTTPS_DOMAIN")


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class PostgresSettings(BaseSettings):
    user: str = os.getenv("PG_USER")
    password: str = os.getenv("PG_PASSWORD")
    host: str = os.getenv("PG_HOST")
    port: int = os.getenv("PG_PORT")
    name: str = os.getenv("PG_NAME")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


class MessagesSettings(BaseSettings):
    start: str = read_txt(BASE_DIR / "messages" / "start.txt")
    info: str = read_txt(BASE_DIR / "messages" / "info.txt")
    subscription: str = read_txt(BASE_DIR / "messages" / "subscription.txt")
    error: str = read_txt(BASE_DIR / "messages" / "error.txt")


class TyuiuGPTSettings(BaseSettings):
    url: str = os.getenv("TYUIU_GPT_API")


class UserAuthSettings(BaseSettings):
    url: str = os.getenv("USER_AUTH_API")


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    tyuiu_gpt: TyuiuGPTSettings = TyuiuGPTSettings()
    user_auth: UserAuthSettings = UserAuthSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    messages: MessagesSettings = MessagesSettings()
