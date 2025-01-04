from abc import ABC, abstractmethod
from typing import Callable

from src.domain.music.albums.core.dtos import (
    BasePopularAlbumsRequestDTO,
    BaseAlbumRequestDTO,
    BaseAlbumResponseDTO,
    BaseItemsRequestDTO,
    BaseCreateAlbumRequestDTO,
    BaseCreateAlbumResponseDTO,
    BaseUpdateAlbumRequestDTO,
    BaseUpdateAlbumResponseDTO,
    BaseDeleteAlbumRequestDTO,
    BasePopularAlbumsResponseDTO,
)
from src.domain.music.albums.interfaces.da.dao import DAO


class BaseService(ABC):
    dao_impl_factory: Callable[[], DAO]

    @abstractmethod
    async def get_album(self, request: BaseAlbumRequestDTO) -> BaseAlbumResponseDTO:
        """
        Gets an album
        :param request:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, request: BasePopularAlbumsRequestDTO, page: BaseItemsRequestDTO) -> BasePopularAlbumsResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def create_album(self, request: BaseCreateAlbumRequestDTO) -> BaseCreateAlbumResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def update_album(self, request: BaseUpdateAlbumRequestDTO) -> BaseUpdateAlbumResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, request: BaseDeleteAlbumRequestDTO) -> None:
        raise NotImplementedError
