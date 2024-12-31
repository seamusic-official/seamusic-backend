from dataclasses import dataclass
from datetime import date, datetime

from src.app.music.albums.core.converters import get_from_models_converter
from src.app.music.albums.core.dtos import (
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
from src.app.music.albums.da.converters import get_from_dto_converter
from src.app.music.albums.da.dao import get_postgres_dao_implementation
from src.domain.music.albums.core.converter import BaseConverter as CoreConverter
from src.domain.music.albums.core.exceptions import AlbumNotFoundError, AlbumAlreasyExistsError, NoArtistRightsError
from src.domain.music.albums.core.service import BaseService
from src.domain.music.albums.da.converter import BaseConverter as DAConverter
from src.domain.music.albums.da.dao import DAO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous


@dataclass
class Service(BaseService):
    dao_impl: type[DAO]
    dao_converter: type[DAConverter]
    core_converter: type[CoreConverter]

    async def get_album(self, request: AlbumRequestDTO) -> AlbumResponseDTO:
        async with self.dao_impl() as session:
            request = await self.dao_converter(dao_implementation=session).album_request(album_id=request.id)
            response = await session.get_album_by_id(**request)
            if response:
                album = await self.core_converter(dao_implementation=session).album_response(album=response)
                viewer_ids = album.viewers_ids.copy()
                viewer_ids.append(request.user_id)
                request = await self.dao_converter(dao_implementation=session).update_album_request(album_id=album.id, viewer_ids=viewer_ids)
                await session.update_album(**request)

        if not album:
            raise AlbumNotFoundError()

        return album

    async def get_popular_albums(self, page: ItemsRequestDTO) -> PopularAlbumsResponseDTO:
        async with self.dao_impl() as session:
            request = await self.dao_converter(dao_implementation=session).popular_albums_request(page.start, page.size)
            response = await session.get_popular_albums(**request)
            items = await self.core_converter(dao_implementation=session).popular_albums_response(response)
            response = await session.count_albums()
            total = await self.core_converter(dao_implementation=session).count_albums_response(response)
        return PopularAlbumsResponseDTO(
            total=total,
            page=get_page(start=page.start, size=page.size),
            has_next=get_has_next(total=total, start=page.start, size=page.size),
            has_previous=get_has_previous(start=page.start, size=page.size),
            size=page.size,
            items=list(map(lambda album: AlbumItemResponseDTO.model_validate(album), items)),
        )

    async def create_album(self, request: CreateAlbumRequestDTO) -> CreateAlbumResponseDTO:
        async with self.dao_impl() as session:
            artist_id_request = await self.dao_converter(dao_implementation=session).artist_id_by_user_id_request(user_id=request.user_id)
            artist_id_response = await session.get_artist_id_by_user_id(**artist_id_request)
            artist_id = await self.core_converter(dao_implementation=session).artist_id_response(artist_id_response)
            artist_exists = bool(artist_id)
            if artist_exists:
                album_exists_request = await self.dao_converter(dao_implementation=session).album_existance_request(title=request.title, artist_id=artist_id)
                album_exists_response = await session.get_album_existance(**album_exists_request)
                album_exists = await self.core_converter(dao_implementation=session).album_existance_response(album_exists_response)
                if not album_exists:
                    create_album_request = await self.dao_converter(dao_implementation=session).create_album_request(
                        title=request.title,
                        picture_url=request.picture_url,
                        description=request.description,
                        album_type=request.type,
                        created_at=date.today(),
                        updated_at=datetime.now(),
                        viewers_ids=list(),
                        likers_ids=list(),
                        artists_ids=[artist_id],
                        tracks_ids=list(),
                        tags=request.tags,
                    )
                    create_album_response = await session.create_album(**create_album_request)
                    response = CreateAlbumResponseDTO(**await self.core_converter(dao_implementation=session).create_album_response(create_album_response))

        if not artist_exists:
            raise NoArtistRightsError()
        if album_exists:
            raise AlbumAlreasyExistsError()

        return response

    async def update_album(self, request: UpdateAlbumRequestDTO) -> UpdateAlbumResponseDTO:
        async with self.dao_impl() as session:
            album_exists_request = await self.dao_converter(ao_implementation=session).album_request(album_id=request.id)
            album_exists_response = await session.get_album_by_id(**album_exists_request)
            album_exists = await self.core_converter(dao_implementation=session).album_existance_response(album_exists_response)
            if album_exists:
                update_album_request = await self.dao_converter(dao_implementation=session).update_album_request(
                    album_id=request.id,
                    title=request.title,
                    picture_url=request.picture_url,
                    description=request.description,
                    album_type='single' if len(request.tracks_ids) == 1 else 'album',
                    updated_at=datetime.now(),
                    viewers_ids=None,
                    likers_ids=None,
                    artists_ids=request.artists_ids,
                    tracks_ids=request.tracks_ids,
                    tags=request.tags,
                )
                update_album_response = await session.update_album(**update_album_request)
                response = UpdateAlbumResponseDTO(**await self.core_converter(dao_implementation=session).update_album_response(update_album_response))

        if not album_exists:
            raise AlbumNotFoundError()

        return response

    async def delete_album(self, request: DeleteAlbumRequestDTO) -> None:
        async with self.dao_impl() as session:
            album_exists_request = await self.dao_converter(dao_implementation=session).album_request(album_id=request.album_id)
            album_exists_response = await session.get_album_by_id(album_exists_request)
            album_exists = await self.core_converter(dao_implementation=session).album_existance_response(album_exists_response)
            if album_exists:
                delete_album_request = await self.dao_converter(dao_implementation=session).delete_album_request(album_id=request.album_id)
                await session.delete_album(**delete_album_request)


def get_service() -> Service:
    return Service(
        dao_impl=get_postgres_dao_implementation(),
        dao_converter=get_from_dto_converter(),
        core_converter=get_from_models_converter(),
    )
