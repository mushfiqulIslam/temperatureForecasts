from fastapi import FastAPI

from api import router
from core.load_locations import weather_forecasts


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Temperature forecasts",
        description="Temperature forecasts ",
        version="1.0.0"
    )

    weather_forecasts.preload_weather_forecast()
    init_routers(app_=app_)
    return app_


app = create_app()
