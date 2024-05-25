from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    MONGO_DATABASE: str
    MONGO_DATABASE_URI: str

settings = Settings()