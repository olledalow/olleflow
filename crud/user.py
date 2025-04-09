from helpers.crud import BaseCRUD

from models.user import User
from schemas.user import UserCreate, UserUpdate


class UserCRUD(BaseCRUD[User, UserCreate, UserUpdate]):
    pass


user_crud = UserCRUD(User)
