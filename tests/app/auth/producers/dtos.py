from datetime import date, datetime
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr

from src.domain.auth.producers.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")
AlbumType = Literal['album', 'single']
AccessLevel = Literal['user', 'admin', 'superuser']
PremiumLevel = Literal['none', 'bot', 'full']


class UserDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    access_level: AccessLevel = 'user'
    telegram_id: int | None = None
    premium_level: PremiumLevel = 'none'

    is_active: bool
    is_adult: bool
    is_verified: bool

    created_at: date
    updated_at: datetime


class BeatpackDTO(BaseDTO):
    id: int
    title: str
    description: str | None = None
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class BeatDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class SquadDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None

    created_at: date
    updated_at: datetime


class SoundkitDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class ItemsRequestDTO(BaseRequestDTO):
    offset: int = 0
    limit: int = 10


class ItemsResponseDTO(BaseResponseDTO, Generic[ItemType]):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


class ProducerResponseDTO(BaseResponseDTO):
    id: int
    username: str
    followers: list[UserDTO]
    beats: list[BeatDTO]
    sqauds: list[SquadDTO]
    tags: list[str]
    beatpacks: list[BeatpackDTO]
    soundkits: list[SoundkitDTO]
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ProducerItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[ProducerResponseDTO]


class CreateProducerRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class CreateProducerResponseDTO(BaseResponseDTO):
    id: int


class UpdateProducerRequestDTO(BaseRequestDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int | None = None
    followers_ids: list[int] | None = None
    beats_ids: list[int] | None = None
    sqauds_ids: list[int] | None = None
    tags: list[str] | None = None
    beatpacks_ids: list[int] | None = None
    soundkits_ids: list[int] | None = None


class UpdateProducerResponseDTO(BaseResponseDTO):
    id: int


def get_items_response(  # type: ignore[no-untyped-def]
    offset: int,
    limit: int,
    total: int,
    items: list[ItemType],
    response_dto: type[ItemsResponseDTO]
):
    return response_dto(
        total=total,
        page=get_page(start=offset, size=limit),
        has_next=get_has_next(total=total, start=offset, size=limit),
        has_previous=get_has_previous(start=offset, size=limit),
        size=limit,
        items=items,
    )
