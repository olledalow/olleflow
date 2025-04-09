# services/user_service.py
from sqlmodel.ext.asyncio.session import AsyncSession
from models.user import User
from schemas.user import UserCreate, UserUpdate
from helpers.service import DefaultMixins
from crud.user import user_crud, UserCRUD


class UserService(DefaultMixins[User, UserCreate, UserUpdate]):
    item_crud: UserCRUD = user_crud

    async def create_user(self, db: AsyncSession, user: User) -> User:
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user


user_service = UserService(user_crud)
