import pytest
import pytest_mock
from httpx import AsyncClient, ASGITransport
from main import app
from db.session import get_db_session


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def mock_db_session(mocker: pytest_mock.MockerFixture):
    """Generic mock DB session with async-compatible methods."""
    mock_session = mocker.MagicMock()
    mock_session.add.return_value = None
    mock_session.commit = mocker.AsyncMock()
    mock_session.refresh = mocker.AsyncMock()
    return mock_session


@pytest.fixture(autouse=True)
def override_get_db(mock_db_session: pytest_mock.MockerFixture):
    """Overrides FastAPI's get_db dependency for all tests."""

    def _override():
        yield mock_db_session

    app.dependency_overrides[get_db_session] = _override


@pytest.fixture
async def async_client():
    """Returns an async test client wired into the FastAPI app."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
