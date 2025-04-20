from sqlmodel import Field
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.types import TIMESTAMP

# from sqlalchemy.sql import func


def created_at_column() -> datetime:
    return Field(sa_column=Column(TIMESTAMP(timezone=True), nullable=False))


def updated_at_column() -> datetime | None:
    return Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=True,
        ),
    )


# class BaseModelMixin:
#     id: Optional[int] = Field(default=None, primary_key=True)
#     # created_at: datetime
#     # updated_at: Optional[datetime] = None
#     created_at: datetime = created_at_column()
#     updated_at: Optional[datetime] = updated_at_column()
