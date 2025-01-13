import pytest

from src.domain.music.albums.api.routes import BaseRouter
from src.domain.music.albums.api.schemas import (
    BaseSAlbumRequest,
    BaseSItemsRequest,
    BaseSArtistAlbumsRequest,
    BaseSUpdateAlbumCoverRequest,
    BaseSLikeAlbumRequest,
    BaseSUnlikeAlbumRequest,
    BaseSCreateAlbumRequest,
    BaseSUpdateAlbumRequest,
    BaseSDeleteAlbumRequest,
)


class TestBaseRouter:
    @pytest.fixture(scope='class')
    def album_request(self):
        return BaseSAlbumRequest()

    @pytest.fixture(scope='class')
    def page(self):
        return BaseSItemsRequest()

    @pytest.fixture(scope='class')
    def artist_albums_request(self):
        return BaseSArtistAlbumsRequest()

    @pytest.fixture(scope='class')
    def update_cover_request(self):
        return BaseSUpdateAlbumCoverRequest()

    @pytest.fixture(scope='class')
    def like_request(self):
        return BaseSLikeAlbumRequest()

    @pytest.fixture(scope='class')
    def unlike_request(self):
        return BaseSUnlikeAlbumRequest()

    @pytest.fixture(scope='class')
    def create_request(self):
        return BaseSCreateAlbumRequest()

    @pytest.fixture(scope='class')
    def update_request(self):
        return BaseSUpdateAlbumRequest()

    @pytest.fixture(scope='class')
    def delete_request(self):
        return BaseSDeleteAlbumRequest()

    async def test_get_album(self, album_request: BaseSAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_album(request=album_request)

    async def test_get_popular_albums(self, page: BaseSItemsRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_popular_albums(page=page)

    async def test_get_artist_albums(self, artist_albums_request: BaseSArtistAlbumsRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_artist_albums(request=artist_albums_request)

    async def test_update_cover(self, update_cover_request: BaseSUpdateAlbumCoverRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.update_cover(request=update_cover_request)

    async def test_like_album(self, like_request: BaseSLikeAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.like_album(request=like_request)

    async def test_unlike_album(self, unlike_request: BaseSUnlikeAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.unlike_album(request=unlike_request)

    async def test_create_album(self, create_request: BaseSCreateAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.create_album(request=create_request)

    async def test_update_album(self, update_request: BaseSUpdateAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.update_album(request=update_request)

    async def test_delete_album(self, delete_request: BaseSDeleteAlbumRequest, router: BaseRouter) -> None:
        async with pytest.raises(NotImplementedError):
            await router.delete_album(request=delete_request)
