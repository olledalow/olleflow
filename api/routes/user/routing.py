from fastapi import APIRouter

from api.routes.user.endpoints import router

PREFIX = "users"

api_router = APIRouter(prefix=f"/{PREFIX}")

api_router.include_router(
    router,
    prefix="/users",
    tags=[f"{PREFIX}/users"],
)
