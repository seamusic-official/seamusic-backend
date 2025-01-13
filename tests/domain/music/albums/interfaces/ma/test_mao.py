import pytest
from abc import abstractmethod
from dataclasses import dataclass
from types import TracebackType
from typing import Self, AsyncGenerator

from src.domain.music.albums.interfaces.base import BaseInterface
from src.domain.music.albums.interfaces.ma.mao import MAO


@pytest.fixture
def mao_instance():
    return MAO()

@pytest.fixture
def data() -> bytes:
    return b'bytes'

@pytest.fixture
def dao() -> AsyncGenerator[MAO]:
    async with MAO() as _mao:
        yield _mao


class TestMAO:

    async def test_abstract_update_cover(self, data: bytes, album_id: int, mao_instance: MAO) -> str:
        async with pytest.raises(NotImplementedError):
            await mao_instance.update_cover(data=data, album_id=album_id)