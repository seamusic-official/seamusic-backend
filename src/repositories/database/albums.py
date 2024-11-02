from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import Executable, select

from src.dtos.database.albums import (
    AlbumRequestDTO,
    AlbumResponseDTO,
    AlbumsResponseDTO,
    AlbumItemResponseDTO,
)
from src.models.albums import Album
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class AlbumRepository(SQLAlchemyRepository):
    async def get_album(self, request: AlbumRequestDTO) -> AlbumResponseDTO:
        model: Album | None = await self.get(Album, request.id)
        return AlbumResponseDTO.model_validate(model) if model else None

    async def get_albums(self, offset: int = 0, limit: int = 10) -> AlbumsResponseDTO:
        query: Executable = select(Album).offset(offset).limit(limit).order_by(len(Album.viewers))
        models: Iterable[Album] = await self.scalars(query)
        return AlbumsResponseDTO(albums=list(map(
            lambda album: AlbumItemResponseDTO.model_validate(album),
            models
        )))

    # async def create_album(self, album: CreateAlbumRequestDTO) -> int:
    #     model = request_dto_to_model(model=Album, request_dto=album)
    #     await self.add(model)
    #     return model.id
    #
    # async def edit_album(self, album: UpdateAlbumRequestDTO) -> int:
    #     model = request_dto_to_model(model=Album, request_dto=album)
    #     await self.merge(model)
    #     return model.id
    #
    # async def get_all_albums(self, offset: int = 0, limit: int = 10) -> AlbumsResponseDTO:
    #     query = select(Album).offset(offset).limit(limit).order_by(Album.updated_at.desc())
    #     albums = list(await self.scalars(query))
    #     return AlbumsResponseDTO(albums=models_to_dto(models=albums, dto=AlbumResponseDTO))
    #
    # async def get_albums_count(self) -> int:
    #     query =
    #     return await self.scalar(query)
    #     await self.scalar(select(func.count(Album.id)))
    #
    # async def get_user_albums(self, user_id: int, offset: int = 0, limit: int = 10) -> AlbumsResponseDTO:
    #     query = select(Album).filter_by(user_id=user_id).offset(offset).limit(limit).order_by(Album.updated_at.desc())
    #     albums = list(await self.scalars(query))
    #     return AlbumsResponseDTO(albums=models_to_dto(models=albums, dto=AlbumResponseDTO))
    #
    # async def get_user_albums_count(self, user_id: int) -> int:
    #     query = select(func.count(Album.id)).filter_by(user_id=user_id)
    #     return await self.scalar(query)
    #
    # async def delete_album(self, album_id: int, user_id: int) -> None:
    #     query = delete(Album).filter_by(id=album_id, user_id=user_id)
    #     await self.execute(query)


def init_albums_repository() -> AlbumRepository:
    return AlbumRepository()
