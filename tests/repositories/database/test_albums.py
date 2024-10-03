import pytest

from src.dtos.database.albums import (
    AlbumResponseDTO,
    CreateAlbumRequestDTO,
    AlbumsResponseDTO,
    UpdateAlbumRequestDTO,
)
from src.repositories.database.albums import AlbumRepository, init_albums_repository


class TestAlbumRepository:
    repository: AlbumRepository = init_albums_repository()

    async def test_create_album(self, album: CreateAlbumRequestDTO) -> None:
        response = await self.repository.create_album(album=album)
        assert isinstance(response, int)

    async def test_get_album_by_id(self, album_id: int) -> None:
        result = await self.repository.get_album_by_id(album_id=album_id)
        assert isinstance(result, AlbumResponseDTO | None)

    async def test_edit_album(self, album: UpdateAlbumRequestDTO) -> None:
        result = await self.repository.edit_album(album=album)
        assert isinstance(result, int)

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_all_albums(self, offset: int, limit: int) -> None:
        response = await self.repository.get_all_albums(offset=offset, limit=limit)
        assert isinstance(response, AlbumsResponseDTO)

    async def test_get_albums_count(self) -> None:
        response = await self.repository.get_albums_count()
        assert isinstance(response, int)
        assert response >= 0

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_user_albums(self, user_id: int, offset: int, limit: int) -> None:
        response = await self.repository.get_user_albums(user_id=user_id, offset=offset, limit=limit)
        assert isinstance(response, AlbumsResponseDTO)

    async def test_get_user_albums_count(self, user_id: int) -> None:
        response = await self.repository.get_user_albums_count(user_id=user_id)
        assert isinstance(response, int)
        assert response >= 0

    async def test_delete_album(self, album_id: int, user_id: int) -> None:
        await self.repository.delete_album(album_id=album_id, user_id=user_id)
