from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str

    model_config = ConfigDict(
        extra="ignore",
        env_file="../.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


config = Settings()
