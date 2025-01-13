import pytest

from src.domain.music.albums.interfaces.ma.mao import MAO


class TestMAO:
    @pytest.fixture(scope='class')
    def mao(self):
        return MAO()

    @pytest.fixture(scope='class')
    def data(self) -> bytes:
        return bytes()

    @pytest.fixture(scope='class')
    def album_id(self) -> int:
        return 1

    async def test_update_cover(self, data: bytes, album_id: int, mao: MAO) -> None:
        async with pytest.raises(NotImplementedError):
            await mao.update_cover(data=data, album_id=album_id)
