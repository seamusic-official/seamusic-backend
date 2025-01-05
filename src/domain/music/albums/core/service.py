from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from src.domain.music.albums.core.dtos import (
    BaseAlbumRequestDTO,
    BaseAlbumResponseDTO,
    BaseArtistAlbumsRequestDTO,
    BaseArtistAlbumsResponseDTO,
    BaseItemsRequestDTO,
    BaseCreateAlbumRequestDTO,
    BaseCreateAlbumResponseDTO,
    BaseDeleteAlbumRequestDTO,
    BaseLikeAlbumRequestDTO,
    BasePopularAlbumsRequestDTO,
    BasePopularAlbumsResponseDTO,
    BaseUnlikeAlbumRequestDTO,
    BaseUpdateAlbumRequestDTO,
    BaseUpdateAlbumResponseDTO,
    BaseUpdateAlbumCoverRequestDTO,
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
    async def get_album(self, request: BaseAlbumRequestDTO) -> BaseAlbumResponseDTO:
        """
        Gets album by its and user's identificators

        :param request: required parameters' DTO
        :return: DTO with album parameters
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, request: BasePopularAlbumsRequestDTO, page: BaseItemsRequestDTO) -> BasePopularAlbumsResponseDTO:
        """
        Gets and paginates most viewed albums

        :param request: required parameters' DTO
        :param page: pagination settings
        :return: DTO with albums' sequence
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError

    @abstractmethod
    async def get_artists_albums(self, request: BaseArtistAlbumsRequestDTO, page: BaseItemsRequestDTO) -> BaseArtistAlbumsResponseDTO:
        """
        Gets specified artist's albums

        :param request: required parameters' DTO
        :return: DTO with albums' sequence
        :raise NotImplementedError: when called directly by abstract class instance
        :raise ArtistNotFoundError: when specified artist doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def update_cover(self, request: BaseUpdateAlbumCoverRequestDTO) -> None:
        """
        Updates album's cover

        :param request: required parameters' DTO
        :raise NotImplementedError: when called directly by abstract class instance
        :raise NoArtistRightsError: when specified artist doesn't exist in storage
            or the user is not the owner of that artist's profile
        """
        raise NotImplementedError

    @abstractmethod
    async def like_album(self, request: BaseLikeAlbumRequestDTO) -> None:
        """
        Likes the album

        :param request: required parameters' DTO
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def unlike_album(self, request: BaseUnlikeAlbumRequestDTO) -> None:
        """
        Removes the like from the album

        :param request: required parameters' DTO
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def create_album(self, request: BaseCreateAlbumRequestDTO) -> BaseCreateAlbumResponseDTO:
        """
        Creates a new album

        :param request: required parameters' DTO
        :return: DTO with the new album's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise NoArtistRightsError: when a user doesn't have an artist profile
        :raise AlbumAlreasyExistsError: when there's an existing album with same
            title on an artist's page
        """
        raise NotImplementedError

    @abstractmethod
    async def update_album(self, request: BaseUpdateAlbumRequestDTO) -> BaseUpdateAlbumResponseDTO:
        """
        Updates an existing album

        :param request: required parameters' DTO
        :return: DTO with the album's numeric identificator
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, request: BaseDeleteAlbumRequestDTO) -> None:
        """
        Deletes an album

        :param request: required parameters' DTO
        :raise NotImplementedError: when called directly by abstract class instance
        :raise AlbumNotFoundError: when album doesn't exist in storage
        """
        raise NotImplementedError
