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
    SArtistAlbumsRequest,
    SArtistAlbumsResponse,
    SUpdateAlbumCoverRequest,
    SLikeAlbumRequest,
    SCreateAlbumRequest,
    SCreateAlbumResponse,
    SUpdateAlbumRequest,
    SUpdateAlbumResponse,
    SDeleteAlbumRequest,
    SUnlikeAlbumRequest,
)

router_v1 = APIRouter(prefix='/albums')


def get_service() -> BaseService:
    return get_albums_service()


@dataclass
class Router(BaseRouter):
    @router_v1.get(
        path='/{album_id}',
        summary='Get an album by it\'s id',
        response_model=SAlbumResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_album(  # type: ignore[override]
        self,
        request: SAlbumRequest = Depends(SAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> SAlbumResponse:
        album = await service.get_album(album_id=request.album_id, user_id=current_user.id)
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

    @router_v1.get(
        path='/',
        summary='Get popular albums',
        response_model=SPopularAlbumsResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_popular_albums(  # type: ignore[override]
        self,
        page: SItemsRequest = Depends(SItemsRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> SPopularAlbumsResponse:
        albums = await service.get_popular_albums(user_id=current_user.id, start=page.start, size=page.size)
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

    @router_v1.get(
        path='/artist/{artist_id}',
        summary='Get albums made by specified artist',
        response_model=SArtistAlbumsResponse,
        status_code=status.HTTP_200_OK,
    )
    async def get_artist_albums(  # type: ignore[override]
        self,
        request: SArtistAlbumsRequest = Depends(SArtistAlbumsRequest),
        service: BaseService = Depends(get_service),
    ) -> SArtistAlbumsResponse:
        response = await service.get_artists_albums(artist_id=request.artist_id)
        return SArtistAlbumsResponse(
            total=response.total,
            items=list(map(
                lambda item: SAlbumItemResponse(
                    id=item.id,
                    title=item.title,
                    picture_url=item.picture_url,
                    description=item.description,
                    views=item.views,
                    likes=item.likes,
                    type=item.type,
                    created_at=item.created_at,
                    updated_at=item.updated_at,
                ),
                response.items,
            )),
        )

    @router_v1.put(
        path='/{album_id}/cover',
        summary='Update an album cover',
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def update_cover(  # type: ignore[override]
        self,
        request: SUpdateAlbumCoverRequest = Depends(SUpdateAlbumCoverRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> None:
        await service.update_cover(
            album_id=request.album_id,
            user_id=current_user.id,
            data=await request.file.read()
        )

    @router_v1.patch(
        path='/{album_id}/like',
        summary='Like an album',
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def like_album(  # type: ignore[override]
        self,
        request: SLikeAlbumRequest = Depends(SLikeAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> None:
        await service.like_album(
            user_id=current_user.id,
            album_id=request.album_id,
        )

    @router_v1.patch(
        path='/{album_id}/unlike',
        summary='Unlike an album',
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def unlike_album(  # type: ignore[override]
        self,
        request: SUnlikeAlbumRequest = Depends(SLikeAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> None:
        await service.unlike_album(
            user_id=current_user.id,
            album_id=request.album_id,
        )

    @router_v1.post(
        path='/new',
        summary='Create a new album',
        response_model=SCreateAlbumResponse,
        status_code=status.HTTP_201_CREATED,
    )
    async def create_album(  # type: ignore[override]
        self,
        request: SCreateAlbumRequest = Depends(SCreateAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> SCreateAlbumResponse:
        response = await service.create_album(
            user_id=current_user.id,
            title=request.title,
            description=request.description,
            tags=request.tags,
        )
        return SCreateAlbumResponse(id=response.id)

    @router_v1.put(
        path='/{album_id}',
        summary='Update an album',
        response_model=SUpdateAlbumResponse,
        status_code=status.HTTP_201_CREATED,
    )
    async def update_album(  # type: ignore[override]
        self,
        request: SUpdateAlbumRequest = Depends(SUpdateAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> SUpdateAlbumResponse:
        response = await service.update_album(
            album_id=request.id,
            user_id=current_user.id,
            title=request.title,
            description=request.description,
            artists_ids=request.artists_ids,
            tracks_ids=request.tracks_ids,
            tags=request.tags,
        )
        return SUpdateAlbumResponse(id=response.id)

    @router_v1.delete(
        path='/{album_id}',
        summary='Delete an album',
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def delete_album(  # type: ignore[override]
        self,
        request: SDeleteAlbumRequest = Depends(SDeleteAlbumRequest),
        service: BaseService = Depends(get_service),
        current_user: CurrentUser = Depends(get_current_user),
    ) -> None:
        await service.delete_album(
            album_id=request.album_id,
            user_id=current_user.id,
        )
