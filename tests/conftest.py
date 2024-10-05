import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.api.app import app
from src.core.config import settings
from src.repositories.database.base import SQLAlchemyRepository  # noqa: F401

engine_test = create_async_engine(settings.db_url_test, echo=True)
sessionmaker_test = async_sessionmaker(engine_test)


@pytest.fixture(scope='function')
def client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(scope='session')
def replace_sessionmaker(mocker):  # type: ignore[no-untyped-def]
    mocker.patch('SQLAlchemyRepository.sessionmaker', new=sessionmaker_test)
