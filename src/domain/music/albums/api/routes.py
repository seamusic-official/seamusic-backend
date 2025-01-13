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
    BaseSUnlikeAlbumRequest,
)


@dataclass
class BaseRouter(ABC):
    async def get_album(self, request: BaseSAlbumRequest) -> BaseSAlbumResponse:
        raise NotImplementedError

    async def get_popular_albums(self, page: BaseSItemsRequest) -> BaseSPopularAlbumsResponse:
        raise NotImplementedError

    async def get_artist_albums(self, request: BaseSArtistAlbumsRequest) -> BaseSArtistAlbumsResponse:
        raise NotImplementedError

    async def update_cover(self, request: BaseSUpdateAlbumCoverRequest) -> None:
        raise NotImplementedError

    async def like_album(self, request: BaseSLikeAlbumRequest) -> None:
        raise NotImplementedError

    async def unlike_album(self, request: BaseSUnlikeAlbumRequest) -> None:
        raise NotImplementedError

    async def create_album(self, request: BaseSCreateAlbumRequest) -> BaseSCreateAlbumResponse:
        raise NotImplementedError

    async def update_album(self, request: BaseSUpdateAlbumRequest) -> BaseSUpdateAlbumResponse:
        raise NotImplementedError

    async def delete_album(self, request: BaseSDeleteAlbumRequest) -> None:
        raise NotImplementedError
