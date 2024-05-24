import os
import requests
from enum import Enum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "super-secret-key")
    DISTRICT_DATA_URL: str = os.environ.get("DISTRICT_DATA_URL", "")
    FORCAST_URL: str = os.environ.get("FORCAST_URL", "https://api.open-meteo.com/v1/forecast")


def load_district_location() -> dict:
    if config.DISTRICT_DATA_URL == "":
        raise ValueError("DISTRICT_DATA_URL must be set properly")

    response = requests.get(config.DISTRICT_DATA_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("DISTRICT_DATA_URL must be set properly")


config: Config = Config()
district_information: dict = load_district_location()
