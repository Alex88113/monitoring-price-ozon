from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    USERNAME_PSQL: str  = Field(min_length=4)
    PASSWORD_PSQL: str  = Field(min_length=4)
    HOST: str = Field(min_length=5)
    PORT: int = Field(ge=0)

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

settings = Settings().model_dump()
