from dataclasses import dataclass

from fastapi import APIRouter, Depends, status

from src.app.music.albums.api.utils import CurrentUser, get_current_user
from src.app.music.albums.core.service import get_service as get_albums_service
from src.domain.music.albums.api.routes import BaseRouter
from src.domain.music.albums.core.service import BaseService
from src.presentation.albums.schemas import (
    SAlbumRequest,
    SAlbumResponse,
    SArtist,
    STrack,
    SAlbumItemResponse,
    SPopularAlbumsResponse,
    SItemsRequest,
)

router = APIRouter(prefix='/albums')


def get_service() -> BaseService:
    return get_albums_service()


@dataclass
class Router(BaseRouter):
    @router.get(
        path='/{album_id}',
        summary='Get an album by it\'s id',
        response_model=SAlbumResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_album(
        self,
        request: SAlbumRequest = Depends(SAlbumRequest),
        service: BaseService = Depends(get_service),
        curren_user: CurrentUser = Depends(get_current_user),
    ) -> SAlbumResponse:
        album = await service.get_album(album_id=request.album_id, user_id=curren_user.id)
        return SAlbumResponse(
            id=album.id,
            title=album.title,
            picture_url=album.picture_url,
            description=album.description,
            type=album.type,
            views=album.views,
            likes=album.likes,
            created_at=album.created_at,
            updated_at=album.updated_at,
            artists=list(map(
                lambda artist: SArtist(
                    id=artist.id,
                    username=artist.username,
                    description=artist.description,
                    picture_url=artist.picture_url,
                    user_id=artist.user_id,
                ),
                list(album.artists),
            )),
            tracks=list(map(
                lambda track: STrack(
                    id=track.id,
                    title=track.title,
                    description=track.description,
                    picture_url=track.picture_url,
                    file_url=track.file_url,
                    views=track.views,
                    likes=track.likes,
                    created_at=track.created_at,
                    updated_at=track.updated_at,
                ),
                list(album.tracks),
            )),
            tags=list(album.tags),
        )

    @router.get(
        path='/popular',
        summary='Get a list of popular albums',
        response_model=SPopularAlbumsResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_popular_albums(
        self,
        page: SItemsRequest = Depends(SItemsRequest),
        service: BaseService = Depends(get_service),
        curren_user: CurrentUser = Depends(get_current_user),
    ) -> SPopularAlbumsResponse:
        albums = await service.get_popular_albums(user_id=curren_user.id, start=page.start, size=page.size)
        return SPopularAlbumsResponse(
            has_next=albums.has_next,
            has_previous=albums.has_previous,
            total=albums.total,
            page=albums.page,
            size=albums.size,
            items=list(map(
                lambda album: SAlbumItemResponse(
                    id=album.id,
                    title=album.title,
                    picture_url=album.picture_url,
                    description=album.description,
                    views=album.views,
                    likes=album.likes,
                    type=album.type,
                    created_at=album.created_at,
                    updated_at=album.updated_at,
                ),
                albums.items,
            ))
        )


    @router.get()