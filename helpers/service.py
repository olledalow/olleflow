from typing import Any, TypeVar, Generic, Optional, Sequence

from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from helpers.crud import BaseCRUD
from helpers.schema import CreateBase, UpdateBase, QueryParams
from helpers.exceptions import ItemNotFoundError

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=CreateBase)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=UpdateBase)


class ServiceBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, crud: BaseCRUD[ModelType, CreateSchemaType, UpdateSchemaType]):
        self.crud = crud


class QueryMixin(ServiceBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def get_all_items(
        self, db: AsyncSession, query_params: QueryParams
    ) -> Sequence[ModelType]:
        result = await self.crud.find_all(db, query_params)
        return result

    async def get_item_by_id(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        try:
            return await self.crud.find_by_id_or_raise(db, id)
        except ItemNotFoundError as e:
            raise HTTPException(404, e.__dict__)

    async def get_items_by_params(
        self, db: AsyncSession, params: dict[str, Any]
    ) -> Sequence[ModelType]:
        return await self.crud.find_by_params(db, params)

    async def get_items_by_params_in(
        self, db: AsyncSession, params: dict[str, list[Any]]
    ) -> Sequence[ModelType]:
        return await self.crud.find_by_param_in(db, params)


class CreateMixin(ServiceBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def create_item(
        self, db: AsyncSession, item_in: CreateSchemaType
    ) -> ModelType:
        print("create service")
        return await self.crud.create(db, obj_in=item_in)


class UpdateMixin(ServiceBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def update_item(
        self, db: AsyncSession, id: int, item_in: UpdateSchemaType
    ) -> Optional[ModelType]:
        try:
            db_obj = await self.crud.find_by_id_or_raise(db=db, id=id)
        except ItemNotFoundError as e:
            raise HTTPException(404, e.__dict__)
        update_dict = item_in.model_dump(exclude_unset=True)
        return await self.crud.update(db, db_obj=db_obj, update_data=update_dict)


class DeleteMixin(ServiceBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    async def delete_item(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        try:
            _ = await self.crud.find_by_id_or_raise(db=db, id=id)
        except ItemNotFoundError as e:
            raise HTTPException(404, e.__dict__)
        return await self.crud.delete(db, id)


class DefaultMixins(
    QueryMixin[ModelType, CreateSchemaType, UpdateSchemaType],
    CreateMixin[ModelType, CreateSchemaType, UpdateSchemaType],
    UpdateMixin[ModelType, CreateSchemaType, UpdateSchemaType],
    DeleteMixin[ModelType, CreateSchemaType, UpdateSchemaType],
    Generic[ModelType, CreateSchemaType, UpdateSchemaType],
):
    pass
