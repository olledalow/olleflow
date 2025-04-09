from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from helpers.model import (
    created_at_column,
    updated_at_column,
)


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = created_at_column()
    updated_at: Optional[datetime] = updated_at_column()
