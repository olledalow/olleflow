from helpers.schema import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None


class TaskRead(TaskBase):
    id: int
    created_at: datetime
