# services/user_service.py
from sqlmodel.ext.asyncio.session import AsyncSession
from models.user import User
from schemas.user import UserCreate, UserUpdate
from helpers.service import DefaultMixins
from crud.user import user_crud, UserCRUD
from datetime import datetime, timezone


class UserService(DefaultMixins[User, UserCreate, UserUpdate]):
    item_crud: UserCRUD = user_crud

    async def hash_password(self, password: str):
        return password + "H4$SH3D"

    async def create_user(self, db: AsyncSession, user: UserCreate) -> User:
        new_user = User(
            email=user.email,
            hashed_password=await self.hash_password(user.password),
            created_at=datetime.now(timezone.utc),
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return new_user


user_service = UserService(user_crud)
