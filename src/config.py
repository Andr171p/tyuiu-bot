import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class BotSettings(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class DBSettings(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    name: str = os.getenv("DB_NAME")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    db: DBSettings = DBSettings()


settings = Settings()
