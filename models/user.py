from datetime import datetime
from pydantic import EmailStr, SecretStr, ValidationError, field_serializer
from sqlmodel import SQLModel, Field
from helpers.schema import CreateBase, UpdateBase
from helpers.model import (
    created_at_column,
    updated_at_column,
)


# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str | None = Field(default=None, max_length=255)
    last_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(CreateBase, UserBase):
    set_password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    set_password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)

    # @field_serializer("password", when_used="json")
    # def dump_secret(self, v: str) -> str:
    #     return v.get_secret_value()


# Properties to receive via API on update, all are optional
class UserUpdate(UpdateBase, UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    set_password: str | None = Field(default=None, min_length=8, max_length=40)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


class UserPublic(UserBase):
    hashed_password: str
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = created_at_column()
    updated_at: datetime | None = updated_at_column()


class User(SQLModel, table=True):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    hashed_password: str
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = created_at_column()
    updated_at: datetime | None = updated_at_column()
