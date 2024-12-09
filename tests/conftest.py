import asyncio
from asyncio.events import AbstractEventLoop
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient

from src.api.app import app


@pytest.fixture(scope="function")
def client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, Any, None]:
    loop = asyncio.new_event_loop()
    try:
        yield loop
    finally:
        loop.close()
