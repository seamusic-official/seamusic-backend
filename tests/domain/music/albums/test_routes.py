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
    BaseCurrentUser,
)
from src.domain.music.albums.core.service import BaseService
from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO


class TestBaseRouter:
    @pytest.fixture(scope='class')
    def album_request(self):
        return BaseSAlbumRequest(album_id=1)

    @pytest.fixture(scope='class')
    def page(self):
        return BaseSItemsRequest(start=1, size=1)

    @pytest.fixture(scope='class')
    def artist_albums_request(self):
        return BaseSArtistAlbumsRequest(artist_id=1)

    @pytest.fixture(scope='class')
    def update_cover_request(self):
        return BaseSUpdateAlbumCoverRequest(album_id=1, file=bytes())

    @pytest.fixture(scope='class')
    def like_request(self):
        return BaseSLikeAlbumRequest(album_id=1)

    @pytest.fixture(scope='class')
    def unlike_request(self):
        return BaseSUnlikeAlbumRequest(album_id=1)

    @pytest.fixture(scope='class')
    def create_request(self):
        return BaseSCreateAlbumRequest(title='', description='', tags=[''])

    @pytest.fixture(scope='class')
    def update_request(self):
        return BaseSUpdateAlbumRequest(
            id=1,
            title='',
            description='',
            picture_url='',
            tracks_ids=[1],
            artists_ids=[1],
            tags=[''],
        )

    @pytest.fixture(scope='class')
    def delete_request(self):
        return BaseSDeleteAlbumRequest(album_id=1)

    @pytest.fixture(scope='class')
    def service(self):
        return BaseService(
            dao_impl_factory=lambda: DAO(),
            mao_impl_factory=lambda: MAO(),
        )

    @pytest.fixture(scope='class')
    def user(self):
        return BaseCurrentUser(id=1)

    async def test_get_album(
        self,
        album_request: BaseSAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_album(request=album_request, service=service, current_user=user)

    async def test_get_popular_albums(
        self,
        page: BaseSItemsRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_popular_albums(page=page, service=service, current_user=user)

    async def test_get_artist_albums(
        self,
        artist_albums_request: BaseSArtistAlbumsRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.get_artist_albums(request=artist_albums_request, service=service, current_user=user)

    async def test_update_cover(
        self,
        update_cover_request: BaseSUpdateAlbumCoverRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.update_cover(request=update_cover_request, service=service, current_user=user)

    async def test_like_album(
        self,
        like_request: BaseSLikeAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.like_album(request=like_request, service=service, current_user=user)

    async def test_unlike_album(
        self,
        unlike_request: BaseSUnlikeAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.unlike_album(request=unlike_request, service=service, current_user=user)

    async def test_create_album(
        self,
        create_request: BaseSCreateAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.create_album(request=create_request, service=service, current_user=user)

    async def test_update_album(
        self,
        update_request: BaseSUpdateAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.update_album(request=update_request, service=service, current_user=user)

    async def test_delete_album(
        self,
        delete_request: BaseSDeleteAlbumRequest,
        router: BaseRouter,
        service: BaseService,
        user: BaseCurrentUser,
    ) -> None:
        async with pytest.raises(NotImplementedError):
            await router.delete_album(request=delete_request, service=service, current_user=user)
