from dataclasses import dataclass
from datetime import date, datetime

from src.app.music.albums.dao import get_postgres_dao
from src.app.music.albums.dtos import (
    AlbumRequestDTO,
    AlbumResponseDTO,
    AlbumItemResponseDTO,
    CreateAlbumRequestDTO,
    CreateAlbumResponseDTO,
    DeleteAlbumRequestDTO,
    ItemsRequestDTO,
    PopularAlbumsResponseDTO,
    UpdateAlbumRequestDTO,
    UpdateAlbumResponseDTO,
)
from src.domain.music.albums.dao import BaseDAO
from src.domain.music.albums.exceptions import AlbumNotFoundError, AlbumAlreasyExistsError, NoArtistRightsError
from src.domain.music.albums.service import BaseService
from src.infrastructure.pages import get_page, get_has_next, get_has_previous


@dataclass
class Service(BaseService):
    dao: BaseDAO

    async def get_album(self, request: AlbumRequestDTO) -> AlbumResponseDTO:
        async with self.dao.open() as session:
            album: dict | None = await session.get_album_by_id(album_id=request.album_id)
            if album:
                album: AlbumResponseDTO = AlbumResponseDTO.model_validate(album)
                viewer_ids = album.viewers_ids.copy()
                viewer_ids.append(request.user_id)
                await session.update_album(album_id=album.id, viewer_ids=viewer_ids)

        if not album:
            raise AlbumNotFoundError()

        return album

    async def get_popular_albums(self, page: ItemsRequestDTO) -> PopularAlbumsResponseDTO:
        async with self.dao.open() as session:
            items: list[dict] = await session.get_popular_albums()
            total: int = await session.count_albums()
        return PopularAlbumsResponseDTO(
            total=total,
            page=get_page(start=page.start, size=page.size),
            has_next=get_has_next(total=total, start=page.start, size=page.size),
            has_previous=get_has_previous(start=page.start, size=page.size),
            size=page.size,
            items=list(map(lambda album: AlbumItemResponseDTO.model_validate(album), items)),
        )

    async def create_album(self, request: CreateAlbumRequestDTO) -> CreateAlbumResponseDTO:
        async with self.dao.open() as session:
            artist_id: int | None = await session.get_artist_id_by_user_id(user_id=request.user_id)
            artist_exists = bool(artist_id)
            if artist_exists:
                album_exists = await session.get_album_existance(title=request.title, artist_id=artist_id)
                if not album_exists:
                    response: int = await session.create_album(
                        title=request.title,
                        picture_url=request.picture_url,
                        description=request.description,
                        type=request.type,
                        created_at=date.today(),
                        updated_at=datetime.now(),
                        artists_ids=[artist_id],
                        tags=request.tags,
                    )

        if not artist_exists:
            raise NoArtistRightsError()
        if album_exists:
            raise AlbumAlreasyExistsError()

        return CreateAlbumResponseDTO(id=response)

    async def update_album(self, request: UpdateAlbumRequestDTO) -> UpdateAlbumResponseDTO:
        async with self.dao.open() as session:
            album_exists = bool(await session.get_album_by_id(album_id=request.id))
            if album_exists:
                response: int = await session.update_album(
                    album_id=request.id,
                    title=request.title,
                    picture_url=request.picture_url,
                    description=request.description,
                    type='single' if len(request.tracks_ids) == 1 else 'album',
                    updated_at=datetime.now(),
                    viewer_ids=request.viewer_ids,
                    likers_ids=request.likers_ids,
                    artists_ids=request.artists_ids,
                    tracks_ids=request.tracks_ids,
                    tags=request.tags,
                )

        if not album_exists:
            raise AlbumNotFoundError()

        return UpdateAlbumResponseDTO(id=response)

    async def delete_album(self, request: DeleteAlbumRequestDTO) -> None:
        async with self.dao.open() as session:
            album_exists = bool(await session.get_album_by_id(album_id=request.album_id))
            if album_exists:
                await session.delete_album(album_id=request.album_id)


def get_service() -> Service:
    return Service(dao=get_postgres_dao())
