from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from helpers.model import (
    created_at_column,
    updated_at_column,
)


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    priority: int = Field(default=1)  # 1 = low, 2 = med, 3 = high
    user_id: int = Field(foreign_key="user.id")
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    completed_at: Optional[datetime] = None
    created_at: datetime = created_at_column()
    updated_at: Optional[datetime] = updated_at_column()
