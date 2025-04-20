from typing import Any
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, Body
from fastapi.exceptions import HTTPException

from schemas.user import user_schemas, UserRead
from models.user import User, UserCreate, UserPublic
from services.user import user_service
from db.session import get_db_session
from helpers.endpoints import init_basic_endpoints, BaseDependencies
from datetime import datetime, timezone

router = APIRouter()


@router.post(
    "", response_model=UserPublic, description="manual endpoint", status_code=201
)
async def create_item(
    *,
    item_in: UserCreate = Body(...),
    db: AsyncSession = Depends(get_db_session),
) -> Any:
    try:
        return await user_service.create_user(db, item_in)
    except IntegrityError as e:
        raise HTTPException(403, str(e))


router = init_basic_endpoints(
    router,
    user_schemas,
    BaseDependencies(get_db_session),
    user_service,
    show_create_item=False,
)
