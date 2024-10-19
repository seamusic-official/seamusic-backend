from datetime import datetime

from src.dtos.database.auth import User
from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class Squad(BaseDTO):
    id: int
    name: str
    admins: list[User]
    picture_url: str | None
    description: str | None
    created_at: datetime


class SquadResponseDTO(BaseResponseDTO):
    id: int
    name: str
    admins: list[User]
    picture_url: str | None
    description: str | None
    file_url: str | None
    created_at: datetime


class SquadsResponseDTO(BaseResponseDTO):
    squads: list[SquadResponseDTO]


class CreateSquadRequestDTO(BaseRequestDTO):
    id: int
    name: str
    admins: list[User]
    picture_url: str | None = None
    description: str | None = None
    file_url: str | None = None
    created_at: datetime


class CreateSquadResponseDTO(BaseResponseDTO):
    id: int


class UpdateSquadRequestDTO(BaseRequestDTO):
    id: int | None = None
    name: str | None = None
    admins: list[User] | None = None
    picture_url: str | None = None
    description: str | None = None
    file_url: str | None = None
    created_at: datetime | None = None


class UpdateSquadResponseDTO(BaseResponseDTO):
    id: int
