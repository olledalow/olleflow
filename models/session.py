from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from helpers.model import (
    created_at_column,
    updated_at_column,
)


class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id")
    user_id: int = Field(foreign_key="user.id")
    started_at: datetime
    ended_at: Optional[datetime] = None
    notes: Optional[str] = None
    created_at: datetime = created_at_column()
    updated_at: Optional[datetime] = updated_at_column()
