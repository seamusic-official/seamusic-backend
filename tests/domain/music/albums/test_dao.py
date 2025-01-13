from datetime import date, datetime
from typing import Literal, Self, Sequence, AsyncGenerator

import pytest

from src.domain.music.albums.interfaces.da.dao import DAO


class TestDAO:
    @pytest.fixture(scope='class')
    def album_id(self):
        return 1

    @pytest.fixture(scope='class')
    def artist_id(self):
        return 1

    @pytest.fixture(scope='class')
    def title(self):
        return ''

    @pytest.fixture(scope='class')
    def created_at(self):
        return date.today()

    @pytest.fixture(scope='class')
    def updated_at(self):
        return datetime.now()

    @pytest.fixture(scope='class')
    def viewers_ids(self):
        return [1]

    @pytest.fixture(scope='class')
    def likers_ids(self):
        return [1]

    @pytest.fixture(scope='class')
    def artists_ids(self):
        return [1]

    @pytest.fixture(scope='class')
    def tracks_ids(self):
        return [1]

    @pytest.fixture(scope='class')
    def tags(self):
        return [""]

    @pytest.fixture(scope='class')
    def album_type(self):
        return 'single'

    @pytest.fixture(scope='class')
    def start(self):
        return 1

    @pytest.fixture(scope='class')
    def size(self):
        return 1

    @pytest.fixture(scope='class')
    def dao(self) -> AsyncGenerator[DAO]:
        async with DAO() as _dao:
            yield _dao

    async def test_get_album_by_id(self, album_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_album_by_id(album_id=album_id)

    async def test_get_album_existance_by_title(self, artist_id: int, title: str, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_album_existance_by_title(artist_id=artist_id, title=title)

    async def test_get_album_existance_by_id(self, album_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_album_existance_by_id(album_id=album_id)

    async def test_get_popular_albums(self, start: int, size: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_popular_albums(start=start, size=size)

    async def test_get_artist_albums(self, artist_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_artist_albums(artist_id=artist_id)

    async def test_count_artist_albums(self, artist_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.count_artist_albums(artist_id=artist_id)

    async def test_count_albums(self, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.count_albums()

    async def test_get_artist_id_by_user_id(self, user_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_artist_id_by_user_id(user_id=user_id)

    async def test_get_artist_existance_by_id(self, artist_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.get_artist_existance_by_id(artist_id=artist_id)

    async def test_create_album(
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
            dao: DAO,
            picture_url: str | None = None,
            description: str | None = None) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.create_album(
                title=title,
                album_type=album_type,
                created_at=created_at,
                updated_at=updated_at,
                viewers_ids=viewers_ids,
                likers_ids=likers_ids,
                artists_ids=artists_ids,
                tracks_ids=tracks_ids,
                tags=tags,
                picture_url=picture_url,
                description=description,
            )

    async def test_update_album(
        self,
        album_id: int,
        dao: DAO,
        title: str,
        picture_url: str,
        description: str,
        album_type: Literal['album', 'single'],
        created_at: date,
        updated_at: datetime,
        viewers_ids: Sequence[int],
        likers_ids: Sequence[int],
        artists_ids: Sequence[int],
        tracks_ids: Sequence[int],
        tags: Sequence[str],
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.update_album(
                album_id=album_id,
                title=title,
                album_type=album_type,
                created_at=created_at,
                updated_at=updated_at,
                viewers_ids=viewers_ids,
                likers_ids=likers_ids,
                artists_ids=artists_ids,
                tracks_ids=tracks_ids,
                tags=tags,
                picture_url=picture_url,
                description=description,
            )

    async def test_delete_album(self, album_id: int, dao: DAO) -> None:
        async with pytest.raises(NotImplementedError):
            await dao.delete_album(album_id=album_id)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        pass
