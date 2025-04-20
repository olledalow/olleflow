# services/user_service.py
from sqlmodel.ext.asyncio.session import AsyncSession
from models.user import User, UserCreate, UserUpdate

# from schemas.user import UserCreate, UserUpdate
from helpers.service import DefaultMixins
from crud.user import user_crud, UserCRUD
from datetime import datetime, timezone
from core.security import get_password_hash


class UserService(DefaultMixins[User, UserCreate, UserUpdate]):
    crud: UserCRUD = user_crud

    async def create_user(self, db: AsyncSession, user_create: UserCreate) -> User:
        new_user = User.model_validate(
            user_create,
            update={
                "hashed_password": get_password_hash(user_create.set_password),
                "created_at": datetime.now(timezone.utc),
            },
        )
        return await self.crud.create_user(db=db, new_user=new_user)


user_service = UserService(user_crud)
