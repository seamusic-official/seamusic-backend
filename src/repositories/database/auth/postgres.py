from dataclasses import dataclass

from pydantic import EmailStr
from sqlalchemy import select, delete, func

from src.converters.repositories.database.sqlalchemy import model_to_response_dto, models_to_dto, request_dto_to_model
from src.dtos.database.auth import (
    Artist,
    ArtistResponseDTO,
    ArtistsResponseDTO,
    CreateArtistRequestDTO,
    CreateProducerRequestDTO,
    CreateUserRequestDTO,
    Producer,
    ProducerResponseDTO,
    ProducersResponseDTO,
    UpdateArtistRequestDTO,
    UpdateProducerRequestDTO,
    UpdateUserRequestDTO,
    User as _User,
    UserResponseDTO,
    UsersResponseDTO,
)
from src.models.auth import User, ArtistProfile, ProducerProfile
from src.repositories.database.auth.base import BaseUsersRepository, BaseArtistsRepository, BaseProducersRepository
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class UsersRepository(BaseUsersRepository, SQLAlchemyRepository):
    async def get_user_by_id(self, user_id: int) -> UserResponseDTO | None:
        user = await self.get(User, user_id)
        return model_to_response_dto(model=user, response_dto=UserResponseDTO)

    async def get_user_by_email(self, email: EmailStr) -> UserResponseDTO | None:
        query = select(User).filter_by(email=email)
        user = await self.scalar(query)
        return model_to_response_dto(model=user, response_dto=UserResponseDTO)

    async def get_users(self, offset: int = 0, limit: int = 10) -> UsersResponseDTO:
        query = select(User).offset(offset).limit(limit).order_by(User.updated_at.desc())
        users = list(await self.scalars(query))
        return UsersResponseDTO(users=models_to_dto(models=users, dto=_User))

    async def get_users_count(self) -> int:
        query = select([func.count()]).select_from(User)
        return await self.scalar(query)

    async def create_user(self, user: CreateUserRequestDTO) -> int:
        model = request_dto_to_model(request_dto=user, model=User)
        await self.add(model)
        return model.id

    async def update_user(self, user: UpdateUserRequestDTO) -> int:
        model = request_dto_to_model(request_dto=user, model=User)
        await self.merge(model)
        return model.id

    async def delete_user(self, user_id: int) -> None:
        query = delete(User).filter_by(id=user_id)
        await self.execute(query)


@dataclass
class ArtistsRepository(BaseArtistsRepository, SQLAlchemyRepository):
    async def get_artist_id_by_user_id(self, user_id: int) -> int | None:
        query = select(User.artist_profile).filter_by(id=user_id)
        return await self.scalar(query)

    async def get_artist_by_id(self, artist_id: int) -> ArtistResponseDTO | None:
        artist = await self.get(ArtistProfile, artist_id)
        return model_to_response_dto(model=artist, response_dto=ArtistResponseDTO)

    async def get_artists(self, offset: int = 0, limit: int = 10) -> ArtistsResponseDTO:
        query = select(ArtistProfile).offset(offset).limit(limit).order_by(ArtistProfile.updated_at.desc())
        artists = list(await self.scalars(query))
        return ArtistsResponseDTO(artists=models_to_dto(models=artists, dto=Artist))

    async def get_artists_count(self) -> int:
        query = select([func.count()]).select_from(ArtistProfile)
        return await self.scalar(query)

    async def create_artist(self, artist: CreateArtistRequestDTO) -> int:
        model = request_dto_to_model(request_dto=artist, model=ArtistProfile)
        await self.add(model)
        return model.id

    async def update_artist(self, artist: UpdateArtistRequestDTO) -> int:
        model = request_dto_to_model(request_dto=artist, model=ArtistProfile)
        await self.merge(model)
        return model.id


@dataclass
class ProducersRepository(BaseProducersRepository, SQLAlchemyRepository):
    async def get_producer_id_by_user_id(self, user_id: int) -> int | None:
        query = select(User.producer_profile).filter_by(id=user_id)
        return await self.scalar(query)

    async def get_producer_by_id(self, producer_id: int) -> ProducerResponseDTO | None:
        producer = await self.get(ProducerProfile, producer_id)
        return model_to_response_dto(model=producer, response_dto=ProducerResponseDTO)

    async def get_producers(self, offset: int = 0, limit: int = 10) -> ProducersResponseDTO:
        query = select(ProducerProfile).offset(offset).limit(limit).order_by(ProducerProfile.updated_at.desc())
        producers = list(await self.scalars(query))
        return ProducersResponseDTO(producers=models_to_dto(models=producers, dto=Producer))

    async def get_producers_count(self) -> int:
        query = select([func.count()]).select_from(ProducerProfile)
        return await self.scalar(query)

    async def create_producer(self, producer: CreateProducerRequestDTO) -> int:
        model = request_dto_to_model(request_dto=producer, model=ProducerProfile)
        await self.add(model)
        return model.id

    async def update_producer(self, producer: UpdateProducerRequestDTO) -> int:
        model = request_dto_to_model(request_dto=producer, model=ProducerProfile)
        await self.merge(model)
        return model.id


def init_users_postgres_repository() -> UsersRepository:
    return UsersRepository()


def init_artists_postgres_repository() -> ArtistsRepository:
    return ArtistsRepository()


def init_producers_postgres_repository() -> ProducersRepository:
    return ProducersRepository()
