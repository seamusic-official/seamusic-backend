from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine

from src.api.app import app
from src.core.config import settings
from src.models.base import Base

engine_test = create_async_engine(settings.db_url, echo=True)

user_email = 'test_email@example.com'
user_password = 'test_password'


@pytest.fixture(scope='function')
def client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(autouse=True, scope='session')
async def create_tables() -> AsyncGenerator:
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
