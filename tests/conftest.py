import pytest
from fastapi.testclient import TestClient

from src.app.main import app


@pytest.fixture(scope="function")
def client() -> TestClient:
    return TestClient(app=app)
