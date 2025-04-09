# base/schema.py
from datetime import datetime
from pydantic import BaseModel
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type, Generic, TypeVar
from fastapi import Query


class DirectionEnum(str, Enum):
    asc = "ASC"
    desc = "DESC"


class QueryParams(BaseModel):
    limit: int = Query(100, alias="$take")
    offset: int = Query(0, alias="$skip")
    order_by: Optional[str] = Query(None, alias="$order_by")
    direction: DirectionEnum = Query(DirectionEnum.asc, alias="$direction")


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class ReadBase(BaseModel):
    pass
    # class Config:
    #     from_attributes = True


class CreateBase(BaseModel):
    pass

    # Internal-only fields: auto-filled by the backend

    # class Config:
    #     from_attributes = True


class UpdateBase(BaseModel):
    pass
    # updated_at: Optional[datetime]

    # Internal-only fields: auto-filled by the backend
    # class Config:
    #     from_attributes = True


class ResponseBase(BaseModel):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


ReadType = TypeVar("ReadType", bound=ReadBase)
CreateType = TypeVar("CreateType", bound=CreateBase)
UpdateType = TypeVar("UpdateType", bound=UpdateBase)
ResponseType = TypeVar("ResponseType", bound=ResponseBase)


@dataclass
class CommonSchemas(Generic[ReadType, CreateType, UpdateType, ResponseType]):
    query: Type[ReadType]
    create: Type[CreateType]
    update: Type[UpdateType]
    response: Type[ResponseType]
