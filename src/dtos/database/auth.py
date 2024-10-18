from datetime import datetime

from pydantic import EmailStr

from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.enums.auth import Role, AccessLevel


class User(BaseDTO):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    created_at: datetime
    updated_at: datetime


class UserResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    created_at: datetime
    updated_at: datetime


class UsersResponseDTO(BaseResponseDTO):
    users: list[UserResponseDTO]


class CreateUserRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    roles: list[Role]
    tags: list[str]
    created_at: datetime
    updated_at: datetime
    access_level: AccessLevel = AccessLevel.user


class UpdateUserRequestDTO(BaseRequestDTO):
    username: str | None = None
    picture_url: str | None = None
    description: str | None = None
    artist_profile_id: int | None = None
    producer_profile_id: int | None = None


class Artist(BaseDTO):
    id: int
    user: UserResponseDTO
    description: str | None = None


class ArtistResponseDTO(BaseResponseDTO):
    id: int
    user: UserResponseDTO
    description: str | None = None


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[ArtistResponseDTO]


class CreateArtistRequestDTO(BaseRequestDTO):
    user_id: int
    description: str | None = None
    is_available: bool = False


class UpdateArtistRequestDTO(BaseRequestDTO):
    id: int
    description: str | None = None
    is_available: bool = False


class Producer(BaseDTO):
    id: int
    user: UserResponseDTO
    description: str | None = None


class ProducerResponseDTO(BaseResponseDTO):
    id: int
    user: UserResponseDTO
    description: str | None = None


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[ProducerResponseDTO]


class CreateProducerRequestDTO(BaseRequestDTO):
    user_id: int
    description: str | None = None
    is_available: bool = False


class UpdateProducerRequestDTO(BaseRequestDTO):
    id: int
    description: str | None = None
    is_available: bool = False
