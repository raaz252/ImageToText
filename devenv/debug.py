from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    debug :bool = False
    echo_active:bool = False
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def getSettings():
    return Settings()