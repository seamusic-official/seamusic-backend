import pytest
from abc import abstractmethod
from datetime import date, datetime
from typing import Literal, Self, Sequence, AsyncGenerator

from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.da.models import BaseAlbumModel


@pytest.fixture
def album_id():
    return 1


@pytest.fixture
def artist_id():
    return 1


@pytest.fixture
def title():
    return ''


@pytest.fixture
def created_at():
    return '2001-7-11'


@pytest.fixture
def updated_at():
    return '2001-7-11 17:46:11'


@pytest.fixture
def viewers_ids():
    return 1


@pytest.fixture
def likers_ids():
    return 1


@pytest.fixture
def artists_ids():
    return 1


@pytest.fixture
def tracks_ids():
    return 1


@pytest.fixture
def tags():
    return "TAGS"


@pytest.fixture
def album_type():
    return 'single'


@pytest.fixture
def start():
    return 1


@pytest.fixture
def size():
    return int


@pytest.fixture
def dao_instance():
    return DAO()


@pytest.fixture
def dao() -> AsyncGenerator[DAO]:
    async with DAO() as _dao:
        yield _dao


class TestDAO:

    async def test_abstract_get_album_by_id(self, album_id: int, dao_instance: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_album_by_id(album_id=album_id)

    async def test_abstract_get_album_existance_by_title(self, artist_id: int, title: str, dao_instance: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_album_existance_by_title(artist_id=artist_id, title=title)

    async def test_abstract_get_album_existance_by_id(self, album_id: int, dao_instance: DAO) -> bool:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_album_existance_by_id(album_id=album_id)

    async def test_abstract_get_popular_albums(self, start: int, size: int, dao_instance: DAO) -> Sequence[BaseAlbumModel]:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_popular_albums(start=start, size=size)

    async def test_abstract_get_artist_albums(self, artist_id: int, dao_instance: DAO) -> Sequence[BaseAlbumModel]:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_artist_albums(artist_id=artist_id)

    async def test_abstract_count_artist_albums(self, artist_id: int, dao_instance: DAO) -> int:
        async with pytest.raises(NotImplementedError):
            await dao_instance.count_artist_albums(artist_id=artist_id)

    async def test_abstract_count_albums(self, dao_instance: DAO) -> int:
        async with pytest.raises(NotImplementedError):
            await dao_instance.count_albums()

    async def test_abstract_get_artist_id_by_user_id(self, user_id: int, dao_instance: DAO) -> int:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_artist_id_by_user_id(user_id=user_id)

    async def test_abstract_get_artist_existance_by_id(self, artist_id: int, dao_instance: DAO) -> bool:
        async with pytest.raises(NotImplementedError):
            await dao_instance.get_artist_existance_by_id(artist_id=artist_id)

    async def test_abstract_create_album(
            self,
            title: str,
            album_type: Literal['album', 'single'],
            created_at: date,
            updated_at: datetime,
            viewers_ids: Sequence[int],
            likers_ids: Sequence[int],
            artists_ids: Sequence[int],
            tracks_ids: Sequence[int],
            tags: Sequence[str],
            dao_instance: DAO,
            picture_url: str | None = None,
            description: str | None = None) -> int:
        async with pytest.raises(NotImplementedError):
            await dao_instance.create_album(title=title, album_type=album_type, created_at=created_at,
                                            updated_at=updated_at,
                                            viewers_ids=viewers_ids, likers_ids=likers_ids, artists_ids=artists_ids,
                                            tracks_ids=tracks_ids, tags=tags, picture_url=picture_url,
                                            description=description)

    async def test_abstract_update_album(
            self,
            album_id: int,
            dao_instance: DAO,
            title: str | None = None,
            picture_url: str | None = None,
            description: str | None = None,
            album_type: Literal['album', 'single'] | None = None,
            created_at: date | None = None,
            updated_at: datetime | None = None,
            viewers_ids: Sequence[int] | None = None,
            likers_ids: Sequence[int] | None = None,
            artists_ids: Sequence[int] | None = None,
            tracks_ids: Sequence[int] | None = None,
            tags: Sequence[str] | None = None) -> int:
        async with pytest.raises(NotImplementedError):
            await dao_instance.update_album(title=title, album_type=album_type, created_at=created_at,
                                            updated_at=updated_at,
                                            viewers_ids=viewers_ids, likers_ids=likers_ids, artists_ids=artists_ids,
                                            tracks_ids=tracks_ids, tags=tags, picture_url=picture_url,
                                            description=description)

    async def test_abstract_delete_album(self, album_id: int, dao_instance: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao_instance.delete_album(album_id=album_id)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        pass