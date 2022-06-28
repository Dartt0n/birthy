from functools import cached_property, lru_cache

from pydantic import BaseSettings


# BaseSettings class from pydantic provides convenient way to handle environment variables
class Config(BaseSettings):
    class Config:  # Base Settings Config
        keep_untouched = (cached_property,)

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    TELEGRAM_TOKEN: str

    @cached_property
    def DATABASE_URL(self) -> str:
        return f"postgres://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:5432/{self.DATABASE_NAME}"


# we should cache result to do IO operation (read & load from .env file) only once
@lru_cache
def get_config():
    return Config()  # type: ignore # load from .env file


# export variable
config = get_config()
