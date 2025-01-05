from abc import abstractmethod
from datetime import date, datetime
from typing import Literal, Self, Sequence

from src.domain.music.albums.interfaces.base import BaseInterface
from src.domain.music.albums.interfaces.da.models import BaseAlbumModel


class DAO(BaseInterface):
    """
    Data Access Object (DAO) is an abstract class created
    to define and describe necessary functions for data acess.

    It's used in services' layer to manipulate storage data.

    As an abstraction, DAO cannot be used directly - that will
    cause `NotImplementedError` and crash the application. So,
    to provide the data access, a DAO implementation is required.

    DAO implementation is a DAO's subclass designed in a unique way
    for an exact type of storage. It can ONLY be used for CRUD
    operations with data in that type of storage. The implementation
    must be provided to the service's layer via factory to avoid using
    globals.
    """

    @abstractmethod
    async def get_album_by_id(self, album_id: int) -> BaseAlbumModel:
        """
        Gets album by its identificator

        :param album_id: album's numeric identifecator
        :return: instance of BaseAlbumModel subclass
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_album_existance_by_title(self, artist_id: int, title: str) -> bool:
        """
        Checks if album exists in storage by specified artist and title

        :param title: album's title
        :param artist_id: numeric identifecator of an artist who owns the album
        :return: album's existance(boolean)
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_album_existance_by_id(self, album_id: int) -> bool:
        """
        Checks if album exists in storage by its identificator

        :param album_id: album's numericidentificator
        :return: album's existance(boolean)
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, start: int, size: int) -> Sequence[BaseAlbumModel]:
        """
        Gets a paginated sequence with albums sorted by their views

        :param start: start point where objects start being taken from storage.
            Another words, this is just the beginning of the page
        :param size: object's length
        :return: paginated sequence with albums
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_artist_albums(self, artist_id: int) -> Sequence[BaseAlbumModel]:
        """
        Gets a non-paginated sequence with specified artist's albums sorted by
        their creation date

        :param artist_id: artist's numeric identificator
        :return: non-paginated sequence with albums
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def count_artist_albums(self, artist_id: int) -> int:
        """
        Counts albums published by specified artist in storage

        :param artist_id: artist's numeric identificator
        :return: amount of albums
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def count_albums(self) -> int:
        """
        Counts albums in storage

        :return: amount of albums
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_artist_id_by_user_id(self, user_id: int) -> int:
        """
        Gets a numeric identificator of an artist linked to a specified user

        :param user_id: user's numeric identificator
        :return: artist's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_artist_existance_by_id(self, artist_id: int) -> bool:
        """
        Checks if artist exists in storage by its identificator

        :param artist_id: artist's numeric identificator
        :return: artist's existance(boolean)
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def create_album(
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
        picture_url: str | None = None,
        description: str | None = None,
    ) -> int:
        """
        Adds a new album to storage

        :param title: album's title
        :param picture_url: [optional] album's cover url
        :param description: [optional] album's description
        :param album_type: single or album
        :param created_at: creation date
        :param updated_at: last update date & time
        :param viewers_ids: Sequence of numeric identificator of viewers who've seen it
        :param likers_ids: numeric identificators of viewers who've liked it
        :param artists_ids: numeric identificators of artist who work on this album
        :param tracks_ids: numeric identificators of tracks included in this album
        :param tags: album's tags
        :return: new albums's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def update_album(
        self,
        album_id: int,
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
        tags: Sequence[str] | None = None,
    ) -> int:
        """
        Updates an existing album in storage. Almost every argument is optional
        and can be not specified or defined as None. In this case it won't be
        updated.

        :param album_id: the only necessary argument - albums's numeric identificator
        :param title: album's title
        :param picture_url: album's cover url
        :param description: album's description
        :param album_type: single or album
        :param created_at: creation date
        :param updated_at: last update date & time
        :param viewers_ids: Sequence of numeric identificator of viewers who've seen it
        :param likers_ids: numeric identificators of viewers who've liked it
        :param artists_ids: numeric identificators of artist who work on this album
        :param tracks_ids: numeric identificators of tracks included in this album
        :param tags: album's tags
        :return: new albums's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, album_id: int) -> None:
        """
        Deletes an album from storage

        :param album_id: albums's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        pass
