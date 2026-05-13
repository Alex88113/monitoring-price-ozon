from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    USERNAME_PSQL: str  = Field(min_length=4)
    PASSWORD_PSQL: SecretStr  = Field(min_length=4)
    HOST: str = Field(min_length=5)
    PORT: int = Field(ge=0)
    DATABASE: str = Field(min_length=4)

    TOKEN_BOT: SecretStr

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

    @property
    def database_url(self) -> str:
        password = self.PASSWORD_PSQL.get_secret_value()
        return f"postgresql://{self.USERNAME_PSQL}:{password}@{self.HOST}:{self.PORT}/{self.DATABASE}"

settings = Settings()


