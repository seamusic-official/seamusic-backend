import pytest

from src.domain.music.albums.api.routes import BaseRouter


async def test_router_creation() -> None:
    with pytest.raises(TypeError):
        BaseRouter()  # type: ignore[abstract]
