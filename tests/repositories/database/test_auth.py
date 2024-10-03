import pytest
from pydantic import EmailStr

from src.dtos.database.auth import (
    ArtistResponseDTO,
    ArtistsResponseDTO,
    CreateArtistRequestDTO,
    CreateProducerRequestDTO,
    CreateUserRequestDTO,
    ProducerResponseDTO,
    ProducersResponseDTO,
    UpdateArtistRequestDTO,
    UpdateProducerRequestDTO,
    UpdateUserRequestDTO,
    UserResponseDTO,
    UsersResponseDTO,
)
from src.repositories.database.auth import UsersRepository, init_users_repository, ArtistsRepository, \
    init_artists_repository, ProducersRepository, init_producers_repository


class TestUsersRepository:
    repository: UsersRepository = init_users_repository()

    async def test_get_user_by_id(self, user_id: int) -> None:
        response = await self.repository.get_user_by_id(user_id=user_id)
        assert isinstance(response, UserResponseDTO | None)

    async def test_get_user_by_email(self, email: EmailStr) -> None:
        response = await self.repository.get_user_by_email(email=email)
        assert isinstance(response, UserResponseDTO | None)

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_users(self, offset: int, limit: int) -> None:
        response = await self.repository.get_users(offset=offset, limit=limit)
        assert isinstance(response, UsersResponseDTO)

    async def test_get_users_count(self) -> None:
        response = await self.repository.get_users_count()
        assert isinstance(response, int)
        assert response >= 0

    async def test_create_user(self, user: CreateUserRequestDTO) -> None:
        response = await self.repository.create_user(user=user)
        assert isinstance(response, int)

    async def test_update_user(self, user: UpdateUserRequestDTO) -> None:
        response = await self.repository.update_user(user=user)
        assert isinstance(response, int)

    async def test_delete_user(self, user_id: int) -> None:
        await self.repository.delete_user(user_id=user_id)


class TestArtistsRepository:
    repository: ArtistsRepository = init_artists_repository()

    async def test_get_artist_id_by_user_id(self, user_id: int) -> None:
        response = self.repository.get_artist_id_by_user_id(user_id=user_id)
        assert isinstance(response, int | None)

    async def test_get_artist_by_id(self, artist_id: int) -> None:
        response = await self.repository.get_artist_by_id(artist_id=artist_id)
        assert isinstance(response, ArtistResponseDTO | None)

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_artists(self, offset: int, limit: int) -> None:
        response = await self.repository.get_artists(offset=offset, limit=limit)
        assert isinstance(response, ArtistsResponseDTO)

    async def test_get_artists_count(self) -> None:
        response = await self.repository.get_artists_count()
        assert isinstance(response, int)
        assert response >= 0

    async def test_create_artist(self, artist: CreateArtistRequestDTO) -> None:
        response = await self.repository.create_artist(artist=artist)
        assert isinstance(response, int)

    async def test_update_artist(self, artist: UpdateArtistRequestDTO) -> None:
        response = await self.repository.update_artist(artist=artist)
        assert isinstance(response, int)


class TestProducersRepository:
    repository: ProducersRepository = init_producers_repository()

    async def test_get_producer_id_by_user_id(self, user_id: int) -> None:
        response = self.repository.get_producer_id_by_user_id(user_id=user_id)
        assert isinstance(response, int | None)

    async def test_get_producer_by_id(self, producer_id: int) -> None:
        response = await self.repository.get_producer_by_id(producer_id=producer_id)
        assert isinstance(response, ProducerResponseDTO | None)

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_producers(self, offset: int, limit: int) -> None:
        response = await self.repository.get_producers(offset=offset, limit=limit)
        assert isinstance(response, ProducersResponseDTO)

    async def test_get_producers_count(self) -> None:
        response = await self.repository.get_producers_count()
        assert isinstance(response, int)
        assert response >= 0

    async def test_create_producer(self, producer: CreateProducerRequestDTO) -> None:
        response = await self.repository.create_producer(producer=producer)
        assert isinstance(response, int)

    async def test_update_producer(self, producer: UpdateProducerRequestDTO) -> None:
        response = await self.repository.update_producer(producer=producer)
        assert isinstance(response, int)
