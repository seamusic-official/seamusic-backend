import pytest

from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO


async def test_mao_creation() -> None:
    with pytest.raises(TypeError):
        MAO()  # type: ignore[abstract]


async def test_dao_creation() -> None:
    with pytest.raises(TypeError):
        DAO()  # type: ignore[abstract]
