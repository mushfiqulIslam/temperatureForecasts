from fastapi import APIRouter

from api.v1 import v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")


__all__ = ["router"]