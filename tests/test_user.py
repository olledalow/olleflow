import pytest
from httpx import AsyncClient
from pytest_mock import MockerFixture, MockType

from models.user import User, SQLModel
from schemas.user import UserCreate
from services.user import user_service
from datetime import datetime, timezone


async def make_fake_user(
    email: str = "test@example.com", password: str = "secure123"
) -> User:
    return User(
        email=email,
        hashed_password="secure123H4$SH3D",
        created_at=datetime.now(timezone.utc),
    )


async def test_password_is_hashed_on_create():
    user_in = UserCreate(email="a@b.com", password="plain123")

    result = await user_service.hash_password(user_in.password)

    assert result != user_in.password
    assert "$" in result  # fake hash signature


@pytest.mark.anyio
async def test_create_user(
    async_client: AsyncClient,
    mock_db_session: MockType,
    mocker: MockerFixture,
):
    # Just assign the DB-generated ID in the refresh step
    def assign_id(obj: SQLModel):
        obj.id = 999  # any dummy value just to simulate DB behavior

    mock_db_session.refresh = mocker.AsyncMock(side_effect=assign_id)

    request_data = {
        "email": "realistic_user@dev.com",
        "password": "secure_pw_abc",
    }

    response = await async_client.post("/users/users", json=request_data)
    data = response.json()

    assert response.status_code == 201
    assert data["email"] == request_data["email"]
    assert isinstance(data["id"], int)
    assert data["id"] == 999
