from fastapi import APIRouter

from core.config import district_information
from core.load_locations import weather_forecasts

forcast_router = APIRouter()


@forcast_router.get("/get_coolest_10_districts")
async def get_coolest_10_districts():
    return {"coolest_districts": weather_forecasts.get_coolest_10_districts()}



