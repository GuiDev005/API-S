from pydantic import Field
from email.policy import default
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default = 'postgresql+asyncpg://workout:workout@localhost/workout')

settings = Settings()