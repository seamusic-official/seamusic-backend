from datetime import date, datetime
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr

from src.domain.auth.artists.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")
AlbumType = Literal['album', 'single']
AccessLevel = Literal['user', 'admin', 'superuser']
PremiumLevel = Literal['none', 'bot', 'full']


class AlbumDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int
    type: AlbumType

    created_at: date
    updated_at: datetime


class TrackDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


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


class ArtistResponseDTO(BaseResponseDTO):
    id: int
    username: str
    followers: list[UserDTO]
    tracks: list[TrackDTO]
    albums: list[AlbumDTO]
    tags: list[str]
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ArtistItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[ArtistItemResponseDTO]


class CreateArtistRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class CreateArtistResponseDTO(BaseResponseDTO):
    id: int


class UpdateArtistRequestDTO(BaseRequestDTO):
    id: int
    username: str | None = None
    followers_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    albums_ids: list[int] | None = None
    tags: list[str] | None = None
    user_id: int | None = None
    description: str | None = None
    picture_url: str | None = None


class UpdateArtistResponseDTO(BaseResponseDTO):
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
