import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class AppSettings(BaseSettings):
    url: str = os.getenv("APP_BASE_URL")


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class DBSettings(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    name: str = os.getenv("DB_NAME")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


class StaticSettings(BaseSettings):
    static_dir: Path = BASE_DIR / "static"
    template_dir: Path = BASE_DIR / "static" / "templates"
    texts_dir: Path = BASE_DIR / "static" / "texts"


class ChatSettings(BaseSettings):
    base_url: str = os.getenv("CHAT_API_BASE_URL")
    headers: dict = {"Content-Type": "application/json; charset=UTF-8"}


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    chat: ChatSettings = ChatSettings()
    bot: BotSettings = BotSettings()
    db: DBSettings = DBSettings()
    static: StaticSettings = StaticSettings()


settings = Settings()
