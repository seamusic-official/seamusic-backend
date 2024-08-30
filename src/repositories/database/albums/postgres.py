from dataclasses import dataclass

from sqlalchemy import select, delete

from src.converters.repositories.database.sqlalchemy import model_to_response_dto, models_to_dto, request_dto_to_model
from src.dtos.database.albums import (
    AlbumResponseDTO,
    CreateAlbumRequestDTO,
    AlbumsResponseDTO,
    UpdateAlbumRequestDTO
)
from src.models.albums import Album
from src.repositories.database.albums.base import BaseAlbumRepository
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class AlbumRepository(SQLAlchemyRepository, BaseAlbumRepository):
    async def create_album(self, album: CreateAlbumRequestDTO) -> int:
        model = request_dto_to_model(model=Album, request_dto=album)
        await self.add(model)
        return model.id

    async def get_album_by_id(self, album_id: int) -> AlbumResponseDTO | None:
        model = await self.get(Album, album_id)
        return model_to_response_dto(response_dto=AlbumResponseDTO, model=model)

    async def edit_album(self, album: UpdateAlbumRequestDTO) -> int:
        model = request_dto_to_model(model=Album, request_dto=album)
        await self.merge(model)
        return model.id

    async def get_all_albums(self) -> AlbumsResponseDTO:
        query = select(Album)
        albums = list(await self.scalars(query))
        return AlbumsResponseDTO(albums=models_to_dto(models=albums, dto=AlbumResponseDTO))

    async def get_user_albums(self, user_id: int) -> AlbumsResponseDTO:
        query = select(Album).where(Album.user_id == user_id)
        albums = list(await self.scalars(query))
        return AlbumsResponseDTO(albums=models_to_dto(models=albums, dto=AlbumResponseDTO))

    async def delete_album(self, album_id: int, user_id: int) -> None:
        query = delete(Album).where(Album.id == album_id, Album.user_id == user_id)
        await self.execute(query)


def init_postgres_repository() -> AlbumRepository:
    return AlbumRepository()
