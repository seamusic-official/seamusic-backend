from dataclasses import dataclass
from io import BytesIO

from src.dtos.database.albums import (
    CreateAlbumRequestDTO,
    AlbumResponseDTO,
    UpdateAlbumRequestDTO,
    AlbumsResponseDTO
)
from src.enums.type import Type
from src.exceptions import NoRightsException, NotFoundException
from src.repositories import Repositories, DatabaseRepositories
from src.repositories.database.albums import init_albums_repository, AlbumRepository
from src.repositories.media.s3 import init_s3_repository, S3Repository
from src.services.base import BaseService


@dataclass
class AlbumDatabaseRepositories(DatabaseRepositories):
    albums: AlbumRepository


@dataclass
class AlbumRepositories(Repositories):
    database: AlbumDatabaseRepositories
    media: S3Repository


@dataclass
class AlbumService(BaseService):

    repositories: AlbumRepositories

    async def get_user_albums(
        self,
        user_id: int,
        start: int = 1,
        size: int = 10,
    ) -> AlbumsResponseDTO:
        return await self.repositories.database.albums.get_user_albums(
            user_id=user_id,
            offset=start - 1,
            limit=size,
        )

    async def get_user_albums_count(self, user_id: int) -> int:
        return await self.repositories.database.albums.get_user_albums_count(user_id=user_id)

    async def get_all_albums(
        self,
        start: int = 1,
        size: int = 10
    ) -> AlbumsResponseDTO:
        return await self.repositories.database.albums.get_all_albums(offset=start - 1, limit=size)

    async def get_all_albums_count(self) -> int:
        return await self.repositories.database.albums.get_albums_count()

    async def get_one_album(self, album_id: int) -> AlbumResponseDTO:
        album = await self.repositories.database.albums.get_album_by_id(album_id=album_id)

        if album is None:
            raise NotFoundException(f"Album {album_id=} doesn't exist")

        return album

    async def add_album(
        self,
        file_stream: BytesIO,
        file_info: str,
        prod_by: str,
        user_id: int,
        title: str = "Unknown title",
        description: str = "Description",
        co_prod: str | None = None,
    ) -> int:

        file_url = await self.repositories.media.upload_file(
            folder="AUDIOFILES",
            filename=file_info,
            file_stream=file_stream
        )

        album = CreateAlbumRequestDTO(
            name=title,
            picture_url=file_url,
            description=description,
            prod_by=prod_by,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        return await self.repositories.database.albums.create_album(album=album)

    async def update_album_picture(
        self,
        album_id: int,
        file_info: str,
        file_stream: BytesIO,
        user_id: int
    ) -> int:

        album = await self.repositories.database.albums.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        file_url = await self.repositories.media.upload_file(
            folder="PICTURES",
            filename=file_info,
            file_stream=file_stream
        )
        return await self.repositories.database.albums.edit_album(UpdateAlbumRequestDTO(
            id=album.id,
            picture_url=file_url,
            type=Type.album,
            user_id=user_id,
        ))

    async def release_album(
        self,
        album_id: int,
        name: str,
        description: str,
        co_prod: str,
        user_id: int,
    ) -> int:

        album = await self.repositories.database.albums.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        updated_album = UpdateAlbumRequestDTO(
            id=album_id,
            name=name,
            picture_url=album.picture_url,
            description=description,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        return await self.repositories.database.albums.edit_album(album=updated_album)

    async def update_album(
        self,
        user_id: int,
        album_id: int,
        title: str | None = None,
        co_prod: str | None = None,
        description: str | None = None,
    ) -> int:

        album = await self.repositories.database.albums.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        updated_album = UpdateAlbumRequestDTO(
            id=album_id,
            name=title,
            picture_url=album.picture_url,
            description=description,
            co_prod=co_prod,
            type=Type.album,
            user_id=user_id
        )

        return await self.repositories.database.albums.edit_album(album=updated_album)

    async def delete_album(self, album_id: int, user_id: int) -> None:
        album = await self.repositories.database.albums.get_album_by_id(album_id=album_id)

        if not album:
            raise NotFoundException()

        if album.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.albums.delete_album(album_id=album_id, user_id=user_id)


def get_album_repositories() -> AlbumRepositories:
    return AlbumRepositories(
        database=AlbumDatabaseRepositories(albums=init_albums_repository()),
        media=init_s3_repository()
    )


def get_album_service() -> AlbumService:
    return AlbumService(repositories=get_album_repositories())
