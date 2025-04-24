import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from src.utils import read_txt
from src.constants import BASE_DIR, ENV_PATH


load_dotenv(ENV_PATH)


class APISettings(BaseSettings):
    url: str = os.getenv("API_BASE_URL")


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


class StaticSettings(BaseSettings):
    static_dir: Path = BASE_DIR / "static"
    template_dir: Path = BASE_DIR / "static" / "templates"
    texts_dir: Path = BASE_DIR / "static" / "texts"


class TyuiuGPTSettings(BaseSettings):
    base_url: str = os.getenv("TYUIU_GPT_API_BASE_URL")


class AuthSettings(BaseSettings):
    base_url: str = os.getenv("AUTH_API_BASE_URL")


class Settings(BaseSettings):
    api: APISettings = APISettings()
    tyuiu_gpt: TyuiuGPTSettings = TyuiuGPTSettings()
    auth: AuthSettings = AuthSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    messages: MessagesSettings = MessagesSettings()
    static: StaticSettings = StaticSettings()
