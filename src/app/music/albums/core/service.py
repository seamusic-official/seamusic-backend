from dataclasses import dataclass
from datetime import date, datetime
from typing import Callable

from src.app.music.albums.core.dtos import (
    AlbumRequestDTO,
    AlbumResponseDTO,
    AlbumItemResponseDTO,
    ArtistDTO,
    CreateAlbumRequestDTO,
    CreateAlbumResponseDTO,
    DeleteAlbumRequestDTO,
    ItemsRequestDTO,
    PopularAlbumsResponseDTO,
    TrackDTO,
    UpdateAlbumRequestDTO,
    UpdateAlbumResponseDTO,
    PopularAlbumsRequestDTO,
    ArtistAlbumsRequestDTO,
    ArtistAlbumsResponseDTO,
    LikeAlbumRequestDTO,
    UnlikeAlbumRequestDTO,
)
from src.app.music.albums.interfaces.da.dao import get_postgres_dao_implementation
from src.app.music.albums.interfaces.ma.mao import get_s3_mao_implementation
from src.domain.music.albums.core.dtos import BaseUpdateAlbumCoverRequestDTO
from src.domain.music.albums.core.exceptions import (
    AlbumNotFoundError,
    AlbumAlreasyExistsError,
    NoArtistRightsError,
    ArtistNotFoundError,
)
from src.domain.music.albums.core.service import BaseService
from src.domain.music.albums.interfaces.da.dao import DAO
from src.domain.music.albums.interfaces.ma.mao import MAO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous


@dataclass
class Service(BaseService):
    dao_impl_factory: Callable[[], DAO]
    mao_impl_factory: Callable[[], MAO]

    async def get_album(self, request: AlbumRequestDTO) -> AlbumResponseDTO:
        async with self.dao_impl_factory() as session:
            response = await session.get_album_by_id(album_id=request.album_id)
            if response and request.user_id not in response.viewers_ids:
                viewers_ids = list(response.viewers_ids).copy()
                viewers_ids.append(request.user_id)
                await session.update_album(album_id=response.id, viewers_ids=viewers_ids)

        if not response:
            raise AlbumNotFoundError()

        return AlbumResponseDTO(
            id=response.id,
            title=response.title,
            picture_url=response.picture_url,
            description=response.description,
            type=response.type,
            views=len(response.viewers_ids),
            likes=len(response.likers_ids),
            created_at=response.created_at,
            updated_at=response.updated_at,
            artists=list(map(lambda artist: ArtistDTO(
                id=artist.id,
                username=artist.username,
                description=artist.description,
                picture_url=artist.picture_url,
                user_id=artist.user_id,
            ), response.artists)),
            tracks=list(map(lambda track: TrackDTO(
                id=track.id,
                title=track.title,
                description=track.description,
                picture_url=track.picture_url,
                file_url=track.file_url,
                views=len(track.viewers_ids),
                likes=len(track.likers_ids),
                created_at=track.created_at,
                updated_at=track.updated_at,
            ), response.tracks)),
            tags=list(map(lambda tag: tag.name, response.tags)),
        )

    async def get_popular_albums(self, request: PopularAlbumsRequestDTO, page: ItemsRequestDTO) -> PopularAlbumsResponseDTO:
        async with self.dao_impl_factory() as session:
            items = await session.get_popular_albums(start=page.start, size=page.size)
            total = await session.count_albums()

            for item in items:
                if request.user_id not in item.viewers_ids:
                    viewers_ids = list(item.viewers_ids).copy()
                    viewers_ids.append(request.user_id)
                    await session.update_album(album_id=item.id, viewers_ids=viewers_ids)

        return PopularAlbumsResponseDTO(
            total=total,
            page=get_page(start=page.start, size=page.size),
            has_next=get_has_next(total=total, start=page.start, size=page.size),
            has_previous=get_has_previous(start=page.start, size=page.size),
            size=page.size,
            items=list(map(lambda album: AlbumItemResponseDTO(
                id=album.id,
                title=album.title,
                picture_url=album.picture_url,
                description=album.description,
                views=len(album.viewers_ids),
                likes=len(album.likers_ids),
                type=album.type,
                created_at=album.created_at,
                updated_at=album.updated_at,
            ), items)),
        )

    async def get_artists_albums(self, request: ArtistAlbumsRequestDTO, page: ItemsRequestDTO) -> ArtistAlbumsResponseDTO:
        async with self.dao_impl_factory() as session:
            artists_exists = await session.get_artist_existance_by_id(artist_id=request.artist_id)
            if artists_exists:
                items = await session.get_artist_albums(artist_id=request.artist_id)
                total = await session.count_artist_albums(artist_id=request.artist_id)

        if not artists_exists:
            raise ArtistNotFoundError()

        return ArtistAlbumsResponseDTO(
            size=page.size,
            has_next=get_has_next(size=page.size, start=page.start, total=total),
            has_previous=get_has_previous(start=page.start, size=page.size),
            total=total,
            page=get_page(start=page.start, size=page.size),
            items=list(map(
                lambda album: AlbumItemResponseDTO(
                    id=album.id,
                    title=album.title,
                    picture_url=album.picture_url,
                    description=album.description,
                    views=len(album.viewers_ids),
                    likes=len(album.likers_ids),
                    type=album.type,
                    created_at=album.created_at,
                    updated_at=album.updated_at,
                ),
                items,
            )),
        )

    async def like_album(self, request: LikeAlbumRequestDTO) -> None:
        async with self.dao_impl_factory() as session:
            album = await session.get_album_by_id(album_id=request.album_id)
            album_exists = bool(album)
            if album_exists and request.user_id not in album.likers_ids:
                likers_ids = list(album.likers_ids).copy()
                likers_ids.append(request.user_id)
                await session.update_album(album_id=album.id, likers_ids=likers_ids)

        if not album_exists:
            raise AlbumNotFoundError()

    async def unlike_album(self, request: UnlikeAlbumRequestDTO) -> None:
        async with self.dao_impl_factory() as session:
            album = await session.get_album_by_id(album_id=request.album_id)
            album_exists = bool(album)
            if album_exists and request.user_id in album.likers_ids:
                likers_ids = list(album.likers_ids).copy()
                likers_ids.remove(request.user_id)
                await session.update_album(album_id=album.id, likers_ids=likers_ids)

        if not album_exists:
            raise AlbumNotFoundError()

    async def update_cover(self, request: BaseUpdateAlbumCoverRequestDTO) -> None:
        async with self.dao_impl_factory() as dao_session:
            artist_id = await dao_session.get_artist_id_by_user_id(user_id=request.user_id)
            album = await dao_session.get_album_by_id(album_id=request.album_id)
            artist_exists = bool(artist_id)
            album_artist_ids = list(map(lambda artist: artist.id, album.artists))
            artists_rights = artist_id in album_artist_ids
            if artist_exists and artists_rights:
                async with self.mao_impl_factory() as mao_session:
                    cover_url = await mao_session.update_cover(data=request.data, album_id=request.album_id)
                await dao_session.update_album(album_id=request.album_id, picture_url=cover_url)

        if not artist_exists or not artists_rights:
            raise NoArtistRightsError()

    async def create_album(self, request: CreateAlbumRequestDTO) -> CreateAlbumResponseDTO:
        async with self.dao_impl_factory() as session:
            artist_id = await session.get_artist_id_by_user_id(user_id=request.user_id)
            artist_exists = bool(artist_id)
            if artist_exists:
                album_exists = await session.get_album_existance_by_title(artist_id=artist_id, title=request.title)
                if not album_exists:
                    album_id = await session.create_album(
                        title=request.title,
                        picture_url=None,
                        description=request.description,
                        album_type='album',
                        created_at=date.today(),
                        updated_at=datetime.now(),
                        viewers_ids=list(),
                        likers_ids=list(),
                        artists_ids=[artist_id],
                        tracks_ids=list(),
                        tags=request.tags,
                    )

        if not artist_exists:
            raise NoArtistRightsError()
        if album_exists:
            raise AlbumAlreasyExistsError()

        return CreateAlbumResponseDTO(id=album_id)

    async def update_album(self, request: UpdateAlbumRequestDTO) -> UpdateAlbumResponseDTO:
        async with self.dao_impl_factory() as session:
            album_exists = await session.get_album_existance_by_id(album_id=request.id)
            if album_exists:
                album_id = await session.update_album(
                    album_id=request.id,
                    title=request.title,
                    picture_url=request.picture_url,
                    description=request.description,
                    album_type=None if not request.tracks_ids else 'single' if len(request.tracks_ids) == 1 else 'album',
                    updated_at=datetime.now(),
                    created_at=None,
                    viewers_ids=None,
                    likers_ids=None,
                    artists_ids=request.artists_ids,
                    tracks_ids=request.tracks_ids,
                    tags=request.tags,
                )

        if not album_exists:
            raise AlbumNotFoundError()

        return UpdateAlbumResponseDTO(id=album_id)

    async def delete_album(self, request: DeleteAlbumRequestDTO) -> None:
        async with self.dao_impl_factory() as session:
            album_exists = await session.get_album_existance_by_id(album_id=request.album_id)
            if album_exists:
                await session.delete_album(album_id=request.album_id)

        if not album_exists:
            raise AlbumNotFoundError()


def get_service() -> Service:
    return Service(
        dao_impl_factory=get_postgres_dao_implementation,
        mao_impl_factory=get_s3_mao_implementation,
    )
