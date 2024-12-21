from datetime import datetime, date
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr

from src.domain.music.tracks.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")
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


class TrackResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    views: int
    likes: int
    producers: list[ProducerDTO]
    tags: list[str]


class TrackItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[TrackItemResponseDTO]


class CreateTrackRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    created_at: date
    updated_at: datetime

    tags: list[str]


class CreateTrackResponseDTO(BaseResponseDTO):
    id: int


class UpdateTrackRequestDTO(BaseRequestDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    updated_at: datetime

    viewers_ids: list[int]
    likers_ids: list[int]
    producers_ids: list[int]
    tags: list[str]


class UpdateTrackResponseDTO(BaseResponseDTO):
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
