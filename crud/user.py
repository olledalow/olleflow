from typing import Any
from sqlmodel.ext.asyncio.session import AsyncSession
from helpers.crud import BaseCRUD

from models.user import User, UserCreate, UserUpdate

# from schemas.user import UserCreate, UserUpdate


class UserCRUD(BaseCRUD[User, UserCreate, UserUpdate]):
    async def create_user(self, db: AsyncSession, new_user: User) -> User:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user


user_crud = UserCRUD(User)
