from fastapi import FastAPI
from fastapi_utilities import repeat_at

from api import router
from core.config import config
from core.weather_forecasts import weather_forecasts


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Temperature forecasts",
        description="Temperature forecasts",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
    )

    weather_forecasts.preload_weather_forecast()
    init_routers(app_=app_)
    return app_


app = create_app()


@repeat_at(cron="0 0 * * *")
async def schedule_event():
    weather_forecasts.reload_weather_forecast()
