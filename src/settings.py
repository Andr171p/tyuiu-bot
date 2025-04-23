import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

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
    messages_dir: Path = BASE_DIR / "messages"


class StaticSettings(BaseSettings):
    static_dir: Path = BASE_DIR / "static"
    template_dir: Path = BASE_DIR / "static" / "templates"
    texts_dir: Path = BASE_DIR / "static" / "texts"


class ChatBotSettings(BaseSettings):
    base_url: str = os.getenv("CHATBOT_API_BASE_URL")


class AuthSettings(BaseSettings):
    base_url: str = os.getenv("AUTH_API_BASE_URL")


class Settings(BaseSettings):
    api: APISettings = APISettings()
    chatbot: ChatBotSettings = ChatBotSettings()
    auth: AuthSettings = AuthSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    messages: MessagesSettings = MessagesSettings()
    static: StaticSettings = StaticSettings()
