import pytest
from fastapi.testclient import TestClient
from src.api.app import app
from src.repositories.database.base import SQLAlchemyRepository  # noqa: F401


@pytest.fixture(scope='function')
def client() -> TestClient:
    return TestClient(app=app)
