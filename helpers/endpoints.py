from dataclasses import dataclass
from typing import Any, Callable
from collections.abc import AsyncGenerator

from fastapi import APIRouter, Depends, Body
from sqlmodel.ext.asyncio.session import AsyncSession

from helpers.schema import (
    CommonSchemas,
    CreateType,
    UpdateType,
    ReadType,
    ResponseType,
    QueryParams,
)
from helpers.service import DefaultMixins, ModelType, CreateSchemaType, UpdateSchemaType


@dataclass
class BaseDependencies:
    get_db_session: Callable[[], AsyncGenerator[AsyncSession, None]]


def init_basic_endpoints(
    router: APIRouter,
    schemas: CommonSchemas[ReadType, CreateType, UpdateType, ResponseType],
    deps: BaseDependencies,
    service: DefaultMixins[ModelType, CreateSchemaType, UpdateSchemaType],
    show_get_all_items: bool = True,
    show_get_item: bool = True,
    show_create_item: bool = True,
    show_update_item: bool = True,
    show_delete_item: bool = True,
):
    if show_get_all_items:

        @router.get(
            "", response_model=list[schemas.response], description="auto generated endpoint"  # type: ignore
        )
        async def get_all_items(  # type: ignore
            query_params: QueryParams = Depends(),
            db: AsyncSession = Depends(deps.get_db_session),
        ) -> Any:
            return await service.get_all_items(db, query_params)

    if show_get_item:

        @router.get(
            "/{id}",
            response_model=schemas.response,
            description="auto generated endpoint",
        )
        async def get_item(  # type: ignore
            id: int,
            db: AsyncSession = Depends(deps.get_db_session),
        ) -> Any:
            return await service.get_item_by_id(db, id)

    if show_create_item:

        @router.post(
            "", response_model=schemas.response, description="auto generated endpoint"
        )
        async def create_item(  # type: ignore
            *,
            item_in: schemas.create = Body(...),
            db: AsyncSession = Depends(deps.get_db_session),
        ) -> Any:
            print("create endpoint")
            return await service.create_item(db, item_in)

    if show_update_item:

        @router.put(
            "/{id}",
            response_model=schemas.response,
            description="auto generated endpoint",
        )
        async def update_item(  # type: ignore
            *,
            id: int,
            item_in: schemas.update = Body(...),
            # item_in: schemas.update = Depends(lambda: Body(...)),
            db: AsyncSession = Depends(deps.get_db_session),
        ) -> Any:
            return await service.update_item(db, id, item_in)

    if show_delete_item:

        @router.delete(
            "/{id}",
            response_model=schemas.response,
            description="auto generated endpoint",
        )
        async def delete_item(  # type: ignore
            *,
            id: int,
            db: AsyncSession = Depends(deps.get_db_session),
        ) -> Any:
            return await service.delete_item(db, id)

    return router

    # if show_create_multi:

    #     @router.post("/multi", response_model=List[schemas.query])  # type: ignore
    #     def create_multi(
    #         *,
    #         items_in: List[schemas.create],  # type: ignore
    #         db: AsyncSession = Depends(deps.get_db_session),
    #     ) -> Any:

    #         return [  # type: ignore
    #             schemas.create.from_orm(res)  # type: ignore
    #             for res in service.create_multi(db, item_in_list=items_in)
    #         ]

    # return router
