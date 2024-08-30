from fastapi import UploadFile, File, APIRouter, Depends, status

from src.enums.type import Type
from src.schemas.albums import (
    Album,
    SAddAlbumResponse,
    SAlbumResponse,
    SAllAlbumsResponse,
    SDeleteAlbumResponse,
    SMyAlbumsResponse,
    SReleaseAlbumsRequest,
    SReleaseAlbumsResponse,
    SUpdateAlbumPictureResponse,
    SUpdateAlbumRequest,
    SUpdateAlbumResponse,
)
from src.schemas.auth import User
from src.services.albums import get_album_service, AlbumService
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream

albums = APIRouter(prefix="/albums", tags=["Albums"])


@albums.get(
    path="/my",
    summary="Get current user's albums",
    response_model=SMyAlbumsResponse,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SMyAlbumsResponse}},
)
async def get_my_albums(
    service: AlbumService = Depends(get_album_service),
    user: User | None = Depends(get_current_user),
) -> SMyAlbumsResponse:

    albums_ = list(map(
        lambda album: Album(
            id=album.id,
            created_at=album.created_at,
            updated_at=album.updated_at,
            is_available=album.is_available,
            title=album.title,
            picture_url=album.picture_url,
            description=album.description,
            co_prod=album.co_prod,
            type=Type.album,
        ),
        await service.get_user_albums(user_id=user.id)
    ))

    return SMyAlbumsResponse(albums=albums_)


@albums.get(
    path="/",
    summary="Get all albums",
    response_model=SAllAlbumsResponse,
    responses={status.HTTP_200_OK: {"model": SAllAlbumsResponse}},
)
async def all_albums(service: AlbumService = Depends(get_album_service)) -> SAllAlbumsResponse:

    albums_ = await service.get_all_albums()
    albums_ = list(map(lambda album: Album.from_db_model(model=album), albums_))

    return SAllAlbumsResponse(albums=albums_)


@albums.get(
    path="/{album_id}",
    summary="Get one album by its ID",
    response_model=SAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAlbumResponse}},
)
async def get_one_album(
    album_id: int,
    service: AlbumService = Depends(get_album_service)
) -> SAlbumResponse:

    album = await service.get_one_album(album_id=album_id)
    return SAlbumResponse.from_db_model(model=album)


@albums.post(
    path="/new",
    summary="Create an album",
    response_model=SAddAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SAddAlbumResponse}},
)
async def add_album(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SAddAlbumResponse:

    album_id = await service.add_album(
        prod_by=user.username,
        user_id=user.id,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file=file),
    )

    return SAddAlbumResponse(id=album_id)


@albums.post(
    path="/{albums_id}/picture",
    summary="Update a picture for one album by id",
    response_model=SUpdateAlbumPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateAlbumPictureResponse}},
)
async def update_album_picture(
    album_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SUpdateAlbumPictureResponse:

    album_id = await service.update_album_picture(
        album_id=album_id,
        user_id=user.id,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file),
    )

    return SUpdateAlbumPictureResponse(id=album_id)


@albums.post(
    path="/{album_id}/release",
    summary="Release one album by id",
    response_model=SReleaseAlbumsResponse,
    responses={status.HTTP_200_OK: {"model": SReleaseAlbumsResponse}},
)
async def release_albums(
    album_id: int,
    albums_data: SReleaseAlbumsRequest,
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SReleaseAlbumsResponse:

    album_id = await service.release_album(
        album_id=album_id,
        name=albums_data.name,
        description=albums_data.description,
        co_prod=albums_data.co_prod,
        user_id=user.id
    )

    return SReleaseAlbumsResponse(id=album_id)


@albums.put(
    path="/{album_id}/update",
    summary="Edit album (title, description, prod_by) by id",
    response_model=SUpdateAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateAlbumResponse}},
)
async def update_album(
    album_id: int,
    data: SUpdateAlbumRequest,
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SUpdateAlbumResponse:

    album_id = await service.update_album(
        user_id=user.id,
        album_id=album_id,
        title=data.title,
        co_prod=data.co_prod,
        description=data.description,
    )

    return SUpdateAlbumResponse(id=album_id)


@albums.delete(
    path="/{album_id}/delete",
    summary="Delete album by id",
    response_model=SDeleteAlbumResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteAlbumResponse}},
)
async def delete_albums(
    album_id: int,
    user: User = Depends(get_current_user),
    service: AlbumService = Depends(get_album_service)
) -> SDeleteAlbumResponse:

    await service.delete_album(album_id=album_id, user_id=user.id)

    return SDeleteAlbumResponse()
