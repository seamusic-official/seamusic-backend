from abc import ABC, abstractmethod
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


class BaseService(ABC):
    dao_impl_factory: Callable[[], DAO]
    mao_impl_factory: Callable[[], MAO]

    @abstractmethod
    async def get_album(self, request: BaseAlbumRequestDTO) -> BaseAlbumResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, request: BasePopularAlbumsRequestDTO, page: BaseItemsRequestDTO) -> BasePopularAlbumsResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def get_artists_albums(self, request: BaseArtistAlbumsRequestDTO, page: BaseItemsRequestDTO) -> BaseArtistAlbumsResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def update_cover(self, request: BaseUpdateAlbumCoverRequestDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def like_album(self, request: BaseLikeAlbumRequestDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def unlike_album(self, request: BaseUnlikeAlbumRequestDTO) -> None:
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
