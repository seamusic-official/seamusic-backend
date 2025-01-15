from abc import ABC
from dataclasses import dataclass

from src.domain.music.albums.api.schemas import (
    BaseSAlbumRequest,
    BaseSAlbumResponse,
    BaseSItemsRequest,
    BaseSPopularAlbumsResponse,
    BaseSArtistAlbumsResponse,
    BaseSArtistAlbumsRequest,
    BaseSUpdateAlbumCoverRequest,
    BaseSLikeAlbumRequest,
    BaseSCreateAlbumRequest,
    BaseSCreateAlbumResponse,
    BaseSUpdateAlbumRequest,
    BaseSUpdateAlbumResponse,
    BaseSDeleteAlbumRequest,
    BaseSUnlikeAlbumRequest, BaseCurrentUser,
)
from src.domain.music.albums.core.service import BaseService


@dataclass
class BaseRouter(ABC):
    async def get_album(
        self,
        request: BaseSAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSAlbumResponse:
        raise NotImplementedError

    async def get_popular_albums(
        self,
        page: BaseSItemsRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSPopularAlbumsResponse:
        raise NotImplementedError

    async def get_artist_albums(
        self,
        request: BaseSArtistAlbumsRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSArtistAlbumsResponse:
        raise NotImplementedError

    async def update_cover(
        self,
        request: BaseSUpdateAlbumCoverRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    async def like_album(
        self,
        request: BaseSLikeAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    async def unlike_album(
        self,
        request: BaseSUnlikeAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    async def create_album(
        self,
        request: BaseSCreateAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSCreateAlbumResponse:
        raise NotImplementedError

    async def update_album(
        self,
        request: BaseSUpdateAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSUpdateAlbumResponse:
        raise NotImplementedError

    async def delete_album(
        self,
        request: BaseSDeleteAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError
