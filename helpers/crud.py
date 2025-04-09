# base/crud.py
from typing import TypeVar, Type, Optional, Any, Sequence, Generic
from sqlmodel import SQLModel, select, desc, asc
from sqlmodel.ext.asyncio.session import AsyncSession
from helpers.schema import UpdateBase, CreateBase, QueryParams, DirectionEnum
from helpers.exceptions import ItemNotFoundError
from datetime import datetime, timezone

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=CreateBase)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=UpdateBase)


class BaseCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def find_by_id(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        return await db.get(self.model, id)

    async def find_by_id_or_raise(self, db: AsyncSession, id: int) -> ModelType:
        db_obj = await db.get(self.model, id)
        if not db_obj:
            raise ItemNotFoundError(self.model.__name__, id)
        return db_obj

    async def find_all(
        self, db: AsyncSession, query_params: QueryParams
    ) -> Sequence[ModelType]:
        statement = select(self.model)

        # Optional ordering
        if query_params.order_by:
            field = getattr(self.model, query_params.order_by, None)
            if field is not None:
                order_func = (
                    desc if query_params.direction == DirectionEnum.desc else asc
                )
                statement = statement.order_by(order_func(field))

        # Pagination
        statement = statement.offset(query_params.offset).limit(query_params.limit)

        result = await db.exec(statement)
        return result.all()

    async def find_by_params(
        self, db: AsyncSession, params: dict[str, Any]
    ) -> Sequence[ModelType]:
        result = await db.exec(select(self.model).where(**params))
        return result.all()

    async def find_by_param_in(
        self, db: AsyncSession, params: dict[str, list[Any]]
    ) -> Sequence[ModelType]:
        """
        :param params: Dict[str, List] - key: name of column to filter by,
                    value: list to run the IN query against
        :return: list of ModelType
        """
        if not params:
            return []

        column_name, values = next(iter(params.items()))
        column_attr = getattr(self.model, column_name)

        statement = select(self.model).where(column_attr.in_(values))
        result = await db.exec(statement=statement)
        return result.all()

    async def create(
        self, db: AsyncSession, obj_in: CreateSchemaType | dict[str, Any]
    ) -> ModelType:
        print("create crud")
        if isinstance(obj_in, dict):
            obj_data = obj_in
        else:
            obj_data = obj_in.model_dump()

        obj_data["created_at"] = datetime.now(timezone.utc)

        db_obj = self.model(**obj_data)
        print("@@@@@@@@@@@@@@@@@@@@@@@@" * 10)
        print(db_obj)
        print("@@@@@@@@@@@@@@@@@@@@@@@@" * 10)

        db.add(db_obj)
        await db.commit()
        await db.refresh(obj_in)

        return db_obj

    async def delete(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        obj = await self.find_by_id(db, id)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj

    async def update(
        self, db: AsyncSession, db_obj: ModelType, update_data: dict[str, Any]
    ) -> ModelType:
        for field, value in update_data.items():
            setattr(db_obj, field, value)

        db_obj.updated_at = datetime.now(timezone.utc)

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
