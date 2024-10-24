from datetime import datetime

from pydantic import EmailStr

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO
from src.enums.auth import Role


class Beat(BaseDTO):
    id: int
    title: str
    description: str | None = None
    prod_by: str | None = None
    picture_url: str | None = None
    file_url: str
    co_prod: str | None = None
    type: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime


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


class Producer(BaseDTO):
    id: int
    user: User
    description: str | None = None


class Tag(BaseDTO):
    name: str


class Soundkit(BaseDTO):
    title: str
    views: int
    picture_url: str | None
    description: str | None
    file_path: str
    liked_users: list["User"]
    created_at: datetime
    updated_at: datetime
    producers: list["Producer"]
    beat: list["Beat"]
    tags: list["Tag"]


class SoundkitResponseDTO(BaseResponseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    liked_users: list["User"]
    created_at: datetime
    updated_at: datetime
    producers: list["Producer"]
    beat: list["Beat"]
    tags: list["Tag"]
    views: int


class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list[SoundkitResponseDTO]


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    liked_users: list["User"] | None = None
    producers: list["Producer"] | None = None
    beat: list["Beat"] | None = None
    tags: list["Tag"] | None = None


class CreateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    title: str | None
    picture_url: str | None
    description: str | None
    file_path: str | None
    liked_users: list["User"] | None = None
    producers: list["Producer"] | None = None
    beat: list["Beat"] | None = None
    tags: list["Tag"] | None = None


class UpdateSoundkitResponseDTO(BaseResponseDTO):
    id: int
