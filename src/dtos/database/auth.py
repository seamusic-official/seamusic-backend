from datetime import datetime, date

from pydantic import EmailStr, Field

from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.enums.auth import Role, AccessLevel


class User(BaseDTO):
    id: int
    username: str
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    birthday: datetime


class UserResponseDTO(BaseResponseDTO):
    id: int
    username: str
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    birthday: datetime


class UsersResponseDTO(BaseResponseDTO):
    users: list[User]


class CreateUserRequestDTO(BaseRequestDTO):
    username: str
    email: EmailStr
    password: str | None
    picture_url: str | None = None
    roles: list[Role]
    birthday: date
    tags: list[str]
    access_level: AccessLevel


class UpdateUserRequestDTO(BaseRequestDTO):
    username: str | None = None
    picture_url: str | None = None
    description: str | None = None
    artist_profile_id: int | None = None
    producer_profile_id: int | None = None


class Artist(BaseDTO):
    id: int
    user: User
    description: str | None = None


class ArtistResponseDTO(BaseResponseDTO):
    id: int
    user: User
    description: str | None = None


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[Artist]


class CreateArtistRequestDTO(BaseRequestDTO):
    user_id: int
    description: str | None = Field(max_length=255)
    is_available: bool = False


class UpdateArtistRequestDTO(BaseRequestDTO):
    id: int
    description: str | None = Field(max_length=255)
    is_available: bool = False


class Producer(BaseDTO):
    id: int
    user: User
    description: str | None = None


class ProducerResponseDTO(BaseResponseDTO):
    id: int
    user: User
    description: str | None = None


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[Producer]


class CreateProducerRequestDTO(BaseRequestDTO):
    user_id: int
    description: str | None = Field(max_length=255)
    is_available: bool = False


class UpdateProducerRequestDTO(BaseRequestDTO):
    id: int
    description: str | None = Field(max_length=255)
    is_available: bool = False
