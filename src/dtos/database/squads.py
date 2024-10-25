from datetime import datetime

from pydantic import EmailStr

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO
from src.enums.auth import Role


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


class Artist(BaseDTO):
    id: int
    user: User
    description: str | None = None


class Producer(BaseDTO):
    id: int
    user: User
    description: str | None = None


class Squad(BaseDTO):
    id: int
    views: int
    title: str
    picture_url: str | None
    description: str | None
    admins: list["Producer"]
    producers: list["Producer"]
    producers_sub: list["Producer"]
    artist_sub: list["Artist"]


class SquadResponseDTO(BaseResponseDTO):
    id: int
    views: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    admins: list["Producer"] | None = None
    producers: list["Producer"] | None = None
    producers_sub: list["Producer"] | None = None
    artist_sub: list["Artist"] | None = None


class SquadsResponseDTO(BaseResponseDTO):
    squads: list[SquadResponseDTO]


class CreateSquadRequestDTO(BaseRequestDTO):
    id: int
    views: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    admins: list["Producer"]
    producers: list["Producer"]


class CreateSquadResponseDTO(BaseResponseDTO):
    id: int


class UpdateSquadRequestDTO(BaseRequestDTO):
    id: int | None = None
    views: int | None = None
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    admins: list["Producer"] | None = None
    producers: list["Producer"] | None = None
    producers_sub: list["Producer"] | None = None
    artist_sub: list["Artist"] | None = None


class UpdateSquadResponseDTO(BaseResponseDTO):
    id: int
