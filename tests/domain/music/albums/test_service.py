from typing import Sequence

import pytest

from src.app.music.albums.core.service import get_service
from src.domain.music.albums.core.service import BaseService
from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO


class TestBaseService:
    @pytest.fixture(scope='class')
    def album_id(self):
        return 1

    @pytest.fixture(scope='class')
    def artist_id(self):
        return 1

    @pytest.fixture(scope='class')
    def user_id(self):
        return 1

    @pytest.fixture(scope='class')
    def title(self):
        return ''

    @pytest.fixture(scope='class')
    def description(self):
        return ''

    @pytest.fixture(scope='class')
    def tags(self):
        return [""]

    @pytest.fixture(scope='class')
    def data(self):
        return bytes()

    @pytest.fixture(scope='class')
    def dao_instance(self):
        return DAO()

    @pytest.fixture(scope='class')
    def mao_instance(self):
        return MAO()

    @pytest.fixture(scope='class')
    def service(self):
        return get_service()

    async def test_abstract_get_album(self, album_id: int, user_id: int, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.get_album(album_id=album_id, user_id=user_id)

    async def test_abstract_get_popular_albums(self, user_id: int, start: int, size: int, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.get_popular_albums(user_id=user_id, start=start, size=size)

    async def test_abstract_get_artists_albums(self, artist_id: int, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.get_artists_albums(artist_id=artist_id)

    async def test_abstract_update_cover(self, album_id: int, user_id: int, data: bytes, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.update_cover(album_id=album_id, user_id=user_id, data=data)

    async def test_abstract_like_album(self, album_id: int, user_id: int, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.like_album(album_id=album_id, user_id=user_id)

    async def test_abstract_unlike_album(self, album_id: int, user_id: int, service: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service.unlike_album(album_id=album_id, user_id=user_id)

    async def test_abstract_create_album(
        self,
        title: str,
        user_id: int,
        description: str,
        tags: Sequence[str],
        service: BaseService,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await service.create_album(
                title=title,
                user_id=user_id,
                description=description,
                tags=tags
            )

    async def test_abstract_update_album(
        self,
        album_id: int,
        service: BaseService,
        title: str,
        description: str,
        user_id: int,
        artists_ids: Sequence[int],
        tracks_ids: Sequence[int],
        tags: Sequence[str],
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await service.update_album(
                album_id=album_id,
                title=title,
                description=description,
                tags=tags,
                artists_ids=artists_ids,
                tracks_ids=tracks_ids,
                user_id=user_id,
            )

    async def test_abstract_delete_album(
        self,
        album_id: int,
        user_id: int,
        service: BaseService,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await service.delete_album(album_id=album_id, user_id=user_id)
