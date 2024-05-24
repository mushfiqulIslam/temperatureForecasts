from fastapi import APIRouter


forcast_router = APIRouter()


@forcast_router.get("/")
async def root():
    return {"message": "Hello World"}



