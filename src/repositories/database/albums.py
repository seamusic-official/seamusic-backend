from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import Executable, select, func, delete

from src.dtos.database.albums import (
    AlbumRequestDTO,
    AlbumResponseDTO,
    AlbumsResponseDTO,
    ArtistAlbumsRequestDTO,
    ArtistAlbumsResponseDTO,
    CountAlbumResponseDTO,
    CreateAlbumRequestDTO,
    CreateAlbumResponseDTO,
    UpdateAlbumRequestDTO,
    UpdateAlbumResponseDTO,
    DeleteAlbumRequestDTO,
)
from src.dtos.database.base import ItemsRequestDTO, get_items_response
from src.models import ArtistProfile, User, Track, Tag
from src.models.albums import Album
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class AlbumRepository(SQLAlchemyRepository):
    async def get_album(self, request: AlbumRequestDTO) -> AlbumResponseDTO | None:
        model: Album | None = await self.get(Album, request.id)
        return AlbumResponseDTO(
            id=model.id,
            title=model.title,
            picture_url=model.picture_url,
            description=model.description,
            views=0,
            likes=0,
            type=model.type,
            created_at=model.created_at,
            updated_at=model.updated_at
        ) if model else None

    async def get_albums(self, page: ItemsRequestDTO) -> AlbumsResponseDTO:
        query: Executable = select(Album).offset(page.offset).limit(page.limit).order_by(func.count(Album.viewers.id).desc())
        models: Iterable[Album] = await self.scalars(query)
        total = await self.scalar(select(func.count(Album.id)))
        return get_items_response(
            offset=page.offset,
            limit=page.limit,
            total=total,
            items=list(models),
            response_dto=AlbumsResponseDTO,
        )

    async def get_artist_albums(self, request: ArtistAlbumsRequestDTO, page: ItemsRequestDTO) -> ArtistAlbumsResponseDTO:
        query: Executable = select(Album).where(Album.artists.any(ArtistProfile.id == request.artist_id)).offset(page.offset).limit(page.limit).order_by(func.count(Album.viewers.id).desc())
        models: Iterable[Album] = await self.scalars(query)
        total = await self.scalar(select(func.count(Album.id)).where(Album.artists.any(ArtistProfile.id == request.artist_id)))
        return get_items_response(
            offset=page.offset,
            limit=page.limit,
            total=total,
            items=list(models),
            response_dto=AlbumsResponseDTO,
        )

    async def count_albums(self) -> CountAlbumResponseDTO:
        query = select(func.count(Album.id))
        return CountAlbumResponseDTO(amount=await self.scalar(query))

    async def create_album(self, album: CreateAlbumRequestDTO) -> CreateAlbumResponseDTO:
        model = Album(
            title=album.title,
            picture_url=album.picture_url,
            description=album.description,
            type=album.type,
            created_at=album.created_at,
            updated_at=album.updated_at,
            viewers=list(),
            likers=list(),
            artists=list(),
            tracks=list(),
            tags=list(),
        )
        await self.add(model)
        return CreateAlbumResponseDTO(id=model.id)

    async def update_album(self, album: UpdateAlbumRequestDTO) -> UpdateAlbumResponseDTO:
        existing_album: Album = await self.get(Album, album.id)
        model = Album(
            id=album.id,
            title=album.title if album.title else existing_album.title,
            picture_url=album.picture_url if album.picture_url else existing_album.picture_url,
            description=album.description if album.description else existing_album.description,
            type=album.type if album.type else existing_album.type,
            updated_at=album.updated_at if album.updated_at else existing_album.updated_at,
            viewers=await self.scalars(select(User).filter(User.id.in_(album.viewers_ids))) if album.viewers_ids else existing_album.viewers,
            likers=await self.scalars(select(User).filter(User.id.in_(album.likers_ids))) if album.likers_ids else existing_album.likers,
            artists=await self.scalars(select(ArtistProfile).filter(ArtistProfile.id.in_(album.artists_ids))) if album.artists_ids else existing_album.artists,
            tracks=await self.scalars(select(Track).filter(Track.id.in_(album.tracks_ids))) if album.tracks_ids else existing_album.tracks,
            tags=await self.scalars(select(Tag).filter(Tag.name.in_(album.tags))) if album.tags else existing_album.tags,
        )
        await self.merge(model)
        return UpdateAlbumResponseDTO(id=model.id)

    async def delete_album(self, request: DeleteAlbumRequestDTO) -> None:
        query = delete(Album).filter_by(id=request.album_id)
        await self.execute(query)


def init_albums_repository() -> AlbumRepository:
    return AlbumRepository()
