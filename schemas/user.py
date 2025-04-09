from helpers.schema import (
    BaseModel,
    ReadBase,
    CreateBase,
    UpdateBase,
    ResponseBase,
    CommonSchemas,
)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase, CreateBase):
    password: str


class UserUpdate(UserBase, UpdateBase):
    pass


class UserRead(UserBase, ReadBase):
    id: int
    hashed_password: str


class UserResponse(UserBase, ResponseBase):
    pass


user_schemas: CommonSchemas[UserRead, UserCreate, UserUpdate, UserResponse] = (
    CommonSchemas(
        query=UserRead, create=UserCreate, update=UserUpdate, response=UserResponse
    )
)
