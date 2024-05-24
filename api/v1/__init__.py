from fastapi import APIRouter

from api.v1.api import forcast_router

v1_router = APIRouter()
v1_router.include_router(forcast_router, prefix="/forcast", tags=["forcast"])