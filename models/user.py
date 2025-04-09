from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from helpers.model import (
    created_at_column,
    updated_at_column,
)


class User(SQLModel, table=True):
    email: str = Field(index=True, unique=True)
    hashed_password: str
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = created_at_column()
    updated_at: Optional[datetime] = updated_at_column()
