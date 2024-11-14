import pytest

from src.dtos.database.albums import (
    AlbumRequestDTO,
    AlbumResponseDTO,
    AlbumsResponseDTO,
    ArtistAlbumsRequestDTO,
    ArtistAlbumsResponseDTO,
    CountAlbumResponseDTO,
    CreateAlbumRequestDTO,
    CreateAlbumResponseDTO,
    DeleteAlbumRequestDTO,
    UpdateAlbumRequestDTO,
    UpdateAlbumResponseDTO,
    
)
from src.dtos.database.auth import UserDTO
from src.dtos.database.base import ItemsRequestDTO
from src.repositories.database.albums import AlbumRepository, init_albums_repository


class TestAlbumRepository:
    repository: AlbumRepository = init_albums_repository()

    @pytest.fixture(scope='class')
    def create_album_request(self) -> CreateAlbumRequestDTO:
        return CreateAlbumRequestDTO(
            title="test",
            picture_url="test",
            description="test",
            type="test",
        )

    @pytest.mark.dependency()
    async def test_create_album(self, create_album_request: CreateAlbumRequestDTO, request: pytest.FixtureRequest) -> None:
        response: CreateAlbumResponseDTO = await self.repository.create_album(album=create_album_request)
        assert isinstance(response, CreateAlbumResponseDTO)
        request.node.album_id = response.id

    @pytest.fixture(scope='session')
    async def album_id(self, request: pytest.FixtureRequest) -> int:
        return 1

    @pytest.fixture(scope='class')
    def update_album_request(self, album_id: int) -> UpdateAlbumRequestDTO:
        return UpdateAlbumRequestDTO(id=album_id)

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album'])
    async def test_get_album(self, album_id: int) -> None:
        response: AlbumResponseDTO | None = await self.repository.get_album(request=AlbumRequestDTO(id=album_id))
        assert isinstance(response, AlbumResponseDTO | None)

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album', 'TestAlbumRepository::test_get_album'])
    async def test_update_album(self, update_album_request: UpdateAlbumRequestDTO, request: pytest.FixtureRequest) -> None:
        response: UpdateAlbumResponseDTO = await self.repository.update_album(album=update_album_request)
        assert isinstance(response, UpdateAlbumResponseDTO)
        request.node.album_id = response.id

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album', 'TestAlbumRepository::test_update_album'])
    @pytest.mark.parametrize("page", [ItemsRequestDTO(offset=i, limit=10 - i) for i in range(10)])
    async def test_get_albums(self, page: ItemsRequestDTO) -> None:
        response: AlbumsResponseDTO = await self.repository.get_albums(page=page)
        assert isinstance(response, AlbumsResponseDTO)

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album', 'TestAlbumRepository::test_update_album'])
    @pytest.mark.parametrize("page", [ItemsRequestDTO(offset=i, limit=10 - i) for i in range(10)])
    async def test_get_artist_albums(self, artist_id: int, page: ItemsRequestDTO) -> None:
        response: ArtistAlbumsResponseDTO = await self.repository.get_artist_albums(
            request=ArtistAlbumsRequestDTO(artist_id=artist_id),
            page=page,
        )
        assert isinstance(response, ArtistAlbumsResponseDTO)

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album', 'TestAlbumRepository::test_update_album'])
    async def test_count_albums(self) -> None:
        response: CountAlbumResponseDTO = await self.repository.count_albums()
        assert isinstance(response, CountAlbumResponseDTO)

    @pytest.mark.dependency(depends=['TestAlbumRepository::test_create_album', 'TestAlbumRepository::test_update_album'])
    async def test_delete_album(self, album_id: int) -> None:
        await self.repository.delete_album(request=DeleteAlbumRequestDTO(album_id=album_id))
