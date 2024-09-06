from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.albums import CreateAlbumRequestDTO, AlbumResponseDTO, AlbumsResponseDTO, UpdateAlbumRequestDTO


@dataclass
class BaseAlbumRepository(ABC):

    @abstractmethod
    async def get_album_by_id(self, album_id: int) -> AlbumResponseDTO | None:
        ...

    @abstractmethod
    async def get_all_albums(self, offset: int = 0, limit: int = 10) -> AlbumsResponseDTO:
        ...

    @abstractmethod
    async def get_albums_count(self) -> int:
        ...

    @abstractmethod
    async def get_user_albums(self, user_id: int, offset: int = 0, limit: int = 10) -> AlbumsResponseDTO:
        ...

    @abstractmethod
    async def get_user_albums_count(self, user_id: int) -> int:
        ...

    @abstractmethod
    async def create_album(self, album: CreateAlbumRequestDTO) -> int:
        ...

    @abstractmethod
    async def edit_album(self, album: UpdateAlbumRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_album(self, album_id: int, user_id: int) -> None:
        ...
