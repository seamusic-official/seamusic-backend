import pytest

from src.domain.music.albums.core.service import BaseService


async def test_service_creation() -> None:
    with pytest.raises(TypeError):
        BaseService()  # type: ignore[abstract, call-arg]
