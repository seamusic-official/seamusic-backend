from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from src.domain.music.albums.core.dtos import (
    BaseAlbumResponseDTO,
    BaseArtistAlbumsResponseDTO,
    BaseCreateAlbumResponseDTO,
    BasePopularAlbumsResponseDTO,
    BaseUpdateAlbumResponseDTO,
)
from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO


@dataclass
class BaseService(ABC):
    """
    BaseService is an abstract class for services' layer. Its subclasses
    provide the application's core, its logic. This is the least typical
    layer in the entire app. Doing it is not a routine(as client-server
    communication or data access), it's a meaningful process, so keep
    careful and be sure you checked everything to avoid security issues.

    As an abstraction, `BaseService` cannot be used directly - that will
    cause `NotImplementedError` and crash the application. So, to provide
    the application's logic, a service subclass is required.

    :param dao_impl_factory: synchronous function for creating DAO
    implementations
    :param mao_impl_factory: synchronous function for creating MAO
    implementations
    """

    dao_impl_factory: Callable[[], DAO]
    mao_impl_factory: Callable[[], MAO]

    @abstractmethod
    async def get_album(self, album_id: int, user_id: int) -> BaseAlbumResponseDTO:
        """
        Gets album by its and user's identificators

        :param album_id: album's numeric identificator
        :param user_id: user's numeric identificator
        :return: DTO with album parameters
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, user_id: int, start: int, size: int) -> BasePopularAlbumsResponseDTO:
        """
        Gets and paginates most viewed albums

        :param user_id: user's numeric identificator
        :param start: start point where objects start being taken from storage.
            Another words, this is just the beginning of the page
        :param size: object's length
        :return: DTO with albums' sequence
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_artists_albums(self, artist_id: int) -> BaseArtistAlbumsResponseDTO:
        """
        Gets specified artist's albums

        :param artist_id: artist's numeric identificator
        :return: DTO with albums' sequence
        :raise NotImplementedError: when called directly by abstract class instance
        :raise ArtistNotFoundError: when specified artist doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def update_cover(self, album_id: int, user_id: int, data: bytes) -> None:
        """
        Updates album's cover

        :param album_id: album's numeric identificator
        :param user_id: user's numeric identificator
        :param data: file data in bytes format
        :raise NotImplementedError: when called directly by abstract class instance
        :raise NoArtistRightsError: when specified artist doesn't exist in storage
            or the user is not the owner of that artist's profile
        """
        raise NotImplementedError

    @abstractmethod
    async def like_album(self, album_id: int, user_id: int) -> None:
        """
        Likes the album

        :param album_id: album's numeric identificator
        :param user_id: user's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def unlike_album(self, album_id: int, user_id: int) -> None:
        """
        Removes the like from the album

        :param album_id: album's numeric identificator
        :param user_id: user's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def create_album(
        self,
        title: str,
        user_id: int,
        description: str | None,
        tags: list[str],
    ) -> BaseCreateAlbumResponseDTO:
        """
        Creates a new album

        :param title: album's title
        :param user_id: user's numeric identificator
        :param description: [optional] album's description
        :param tags: sequence album's tags
        :return: DTO with the new album's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise NoArtistRightsError: when a user doesn't have an artist profile
        :raise AlbumAlreasyExistsError: when there's an existing album with same
            title on an artist's page
        """
        raise NotImplementedError

    @abstractmethod
    async def update_album(
        self,
        album_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None,
        artists_ids: list[int] | None = None,
        tracks_ids: list[int] | None = None,
        tags: list[str] | None = None,
    ) -> BaseUpdateAlbumResponseDTO:
        """
        Updates an existing album. Almost every argument is optional
        and can be not specified or defined as None. In this case it won't be
        updated.

        :param album_id: the only necessary argument - album's numeric identificator
        :param title: new album's title
        :param description: new album's description
        :param artists_ids: sequence of collaborating artists' ids
        :param tracks_ids: sequence of included tracks' ids
        :param tags: sequence of album's tags
        :param user_id: current user's numeric identificator
        :return: DTO with the album's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        :raise NoArtistRightsError: when a user doesn't have an access to this album
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, album_id: int, user_id: int) -> None:
        """
        Deletes an album

        :param album_id: album's numeric identificator
        :param user_id: current user's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        :raise NoArtistRightsError: when a user doesn't have an access to this album
        """
        raise NotImplementedError
