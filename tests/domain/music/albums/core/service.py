import pytest
from abc import abstractmethod
from datetime import date, datetime
from typing import Literal, Self, Sequence, AsyncGenerator

from src.domain.music.albums.core.dtos import (
    BaseAlbumResponseDTO,
    BaseArtistAlbumsResponseDTO,
    BaseCreateAlbumResponseDTO,
    BasePopularAlbumsResponseDTO,
    BaseUpdateAlbumResponseDTO,
)
from src.domain.music.albums.core.service import BaseService
from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO


@pytest.fixture
def album_id():
    return 1


@pytest.fixture
def artist_id():
    return 1


@pytest.fixture
def user_id():
    return 1


@pytest.fixture
def title():
    return ''


@pytest.fixture
def description():
    return 'Test album description'


@pytest.fixture
def tags():
    return ["tag1", "tag2"]


@pytest.fixture
def data():
    return b'example bytes data for cover update'


@pytest.fixture
def dao_instance():
    return DAO()


@pytest.fixture
def mao_instance():
    return MAO()


@pytest.fixture
def service_instance():
    return BaseService(
        dao_impl_factory=lambda: dao_instance,
        mao_impl_factory=lambda: mao_instance
    )


class TestBaseService:

    async def test_abstract_get_album(self, album_id: int, user_id: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.get_album(album_id=album_id, user_id=user_id)

    async def test_abstract_get_popular_albums(self, user_id: int, start: int, size: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.get_popular_albums(user_id=user_id, start=start, size=size)

    async def test_abstract_get_artists_albums(self, artist_id: int, start: int, size: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.get_artists_albums(artist_id=artist_id, start=start, size=size)

    async def test_abstract_update_cover(self, album_id: int, user_id: int, data: bytes, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.update_cover(album_id=album_id, user_id=user_id, data=data)

    async def test_abstract_like_album(self, album_id: int, user_id: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.like_album(album_id=album_id, user_id=user_id)

    async def test_abstract_unlike_album(self, album_id: int, user_id: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.unlike_album(album_id=album_id, user_id=user_id)

    async def test_abstract_create_album(
            self,
            title: str,
            user_id: int,
            description: str,
            tags: Sequence[str],
            service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.create_album(
                title=title,
                user_id=user_id,
                description=description,
                tags=tags
            )

    async def test_abstract_update_album(
            self,
            album_id: int,
            service_instance: BaseService,
            title: str | None = None,
            description: str | None = None,
            artists_ids: Sequence[int] | None = None,
            tracks_ids: Sequence[int] | None = None,
            tags: Sequence[str] | None = None
    ) -> BaseUpdateAlbumResponseDTO:
        async with pytest.raises(NotImplementedError):
            await service_instance.update_album(
                album_id=album_id,
                title=title,
                description=description,
                tags=tags
            )

    async def test_abstract_delete_album(self, album_id: int, service_instance: BaseService) -> None:
        async with pytest.raises(NotImplementedError):
            await service_instance.delete_album(album_id=album_id)