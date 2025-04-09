from typing import Any
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi import APIRouter, Depends, Body

from schemas.user import user_schemas, UserRead, UserCreate
from models.user import User
from services.user import user_service
from db.session import get_db_session
from helpers.endpoints import init_basic_endpoints, BaseDependencies
from datetime import datetime, timezone

router = APIRouter()


@router.post(
    "", response_model=UserRead, description="manual endpoint", status_code=201
)
async def create_item(
    *,
    item_in: UserCreate = Body(...),
    db: AsyncSession = Depends(get_db_session),
) -> Any:

    return await user_service.create_user(db, item_in)


router = init_basic_endpoints(
    router,
    user_schemas,
    BaseDependencies(get_db_session),
    user_service,
    show_create_item=False,
)

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
#     #db_user = crud.get_user_by_email(db, email=user.email)
#     print(user.email)
#     print(user.password)
#     print(user)
#     user_data = {"email": user.email, "hashed_password": user.password+"H4$H"}
#     db_user = services.user.item_crud.create(db, user_data)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @router.get("/users/{user_id}", response_model=schemas.User)
# def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
#     # db_user = crud.get_user(db, user_id=user_id)
#     db_user = services.user.item_crud.find_by_id(db, user_id)

#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.get("/users/", response_model=List[schemas.User])
# def get_users(db: AsyncSession = Depends(get_db)):
#     db_user = services.user.item_crud.get(db)

#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.get("/users/{user_id}/EXTRA")
# def get_users_extra(user_id: int, db: AsyncSession = Depends(get_db)):
#     print("LULULU")
#     db_user = services.user.extra_service_func(db, user_id)

#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     print(type(db_user))
#     print(db_user)
#     return db_user

# @router.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @router.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @router.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


# @router.get("", response_model=List[schemas.OrderInDB])
# def get_items(
#     *,
#     db: AsyncSession = Depends(deps.get_db),
#     filter_obj=Depends(deps.filter_obj),
#     query_options=Depends(deps.query_options),
#     customer_ids=Depends(deps.get_loggedin_user_customers),
# ) -> Any:
#     print("*" * 100)
#     print(customer_ids)
#     print("*" * 100)
#     if customer_ids:
#         customer_query = (
#             db.query(services.order.item_crud.model)
#             .filter(services.order.item_crud.model.customer_id.in_(customer_ids))
#             .filter(services.order.item_crud.model.d == 0)
#         )
#         return services.order.item_crud.advanced_query(
#             db, filter_obj, query_options, customer_query
#         )
#     return services.order.get_items(db, filter_obj, query_options)


# @router.post("")
# def create_item(
#     *,
#     db: AsyncSession = Depends(deps.get_db),
#     item_in: schemas.order.create,
#     customer_ids=Depends(deps.get_loggedin_user_customers),
# ):
#     if customer_ids:
#         if item_in.customer_id not in customer_ids:
#             raise HTTPException(
#                 403,
#                 {
#                     "message": "Az adott vevő nem engedélyezett a felhasználó számára",
#                     "error": f"customer '{item_in.customer_id}' "
#                     "is not an allowed customer for user",
#                 },
#             )
#     return services.order.create_item(db, item_in)


# @router.put("/{id}")
# def update_item(
#     *,
#     id: int,
#     item_in: schemas.order.update,
#     db: AsyncSession = Depends(deps.get_db),
#     customer_ids=Depends(deps.get_loggedin_user_customers),
# ):
#     if customer_ids:
#         order = services.order.item_crud.find_by_id_or_raise(db, id, True)
#         if order.customer_id not in customer_ids:
#             raise HTTPException(
#                 403,
#                 {
#                     "message": "Az adott vevő nem engedélyezett a felhasználó számára",
#                     "error": f"customer '{order.customer_id}' "
#                     "is not an allowed customer for user",
#                 },
#             )
#     return services.order.update_item(db, id, item_in)


# @router.delete("/{id}")
# def delete_item(
#     *,
#     id: int,
#     db: AsyncSession = Depends(deps.get_db),
#     customer_ids=Depends(deps.get_loggedin_user_customers),
# ):
#     if customer_ids:
#         order = services.order.item_crud.find_by_id_or_raise(db, id, True)
#         if order.customer_id not in customer_ids:
#             raise HTTPException(
#                 403,
#                 {
#                     "message": "Az adott vevő nem engedélyezett a felhasználó számára",
#                     "error": f"customer '{order.customer_id}' "
#                     "is not an allowed customer for user",
#                 },
#             )
#     return services.order.delete_item(db, id)
