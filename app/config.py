# It inherits from BaseSettings, and it adds a few more settings
from pydantic import BaseSettings


# It inherits from BaseSettings, and it adds a few more settings
class Settings(BaseSettings):
    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    ALGORITHM: str

    class Config:
        env_file = './.env'


settings = Settings()
