import pytest
from fastapi.testclient import TestClient
from src.api.app import app


@pytest.fixture(scope='function')
def client() -> TestClient:
    return TestClient(app=app)
