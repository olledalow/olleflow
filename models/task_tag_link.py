from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from helpers.model import (
    created_at_column,
    updated_at_column,
)


class TaskTagLink(SQLModel, table=True):
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)
    created_at: datetime = created_at_column()
    updated_at: Optional[datetime] = updated_at_column()
