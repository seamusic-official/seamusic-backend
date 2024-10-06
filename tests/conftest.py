import pytest
from fastapi.testclient import TestClient

from src.api.app import app
from src.core.config import settings
from src.repositories.database.base import SQLAlchemyRepository  # noqa: F401


@pytest.fixture(scope='function')
def client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(scope='session')
def replace_db_url(mocker):  # type: ignore[no-untyped-def]
    mocker.patch('settings.db_url', new=settings.db_url_test)
