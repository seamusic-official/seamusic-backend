from datetime import date, datetime
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr

from src.domain.auth.producers.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar('ItemType')
AccessLevel = Literal['user', 'admin', 'superuser']
PremiumLevel = Literal['none', 'bot', 'full']
AlbumType = Literal['album', 'single']
Subject = Literal[
    'album',
    'beat',
    'beatpack',
    'soundkit',
    'track',
]


class CommentDTO(BaseDTO):
    id: int
    text: str

    subject: Subject
    subject_id: int

    created_at: datetime
    updated_at: datetime


class LicenseDTO(BaseDTO):
    id: int
    title: str
    text: str
    description: str

    created_at: date
    updated_at: datetime


class ArtistDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class ProducerDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class PlaylistDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int

    created_at: date
    updated_at: datetime


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


class UserResponseDTO(BaseResponseDTO):
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

    comments: list['CommentDTO']
    licenses: list['LicenseDTO']
    followed_artists: list['ArtistDTO']
    saved_playlists: list['PlaylistDTO']
    followed_producers: list['ProducerDTO']
    saved_albums: list['AlbumDTO']
    followed_tags: list[str]


class UserItemResponseDTO(BaseResponseDTO):
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


class UsersResponseDTO(BaseResponseDTO):
    users: list[UserItemResponseDTO]


class CreateUserRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    access_level: AccessLevel = 'user'
    telegram_id: int | None = None
    premium_level: PremiumLevel = 'none'

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    is_active: bool
    is_adult: bool
    is_verified: bool


class CreateUserResponseDTO(BaseResponseDTO):
    id: int


class UpdateUserRequestDTO(BaseRequestDTO):
    id: int
    username: str | None = None
    description: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    picture_url: str | None = None
    access_level: AccessLevel | None = None
    telegram_id: int | None = None
    premium_level: PremiumLevel | None = None

    is_active: bool | None = None
    is_adult: bool | None = None
    is_verified: bool | None = None

    updated_at: datetime = datetime.now()

    comments_ids: list[int] | None = None
    messages_ids: list[int] | None = None
    licenses_ids: list[int] | None = None
    followed_artists_ids: list[int] | None = None
    saved_playlists_ids: list[int] | None = None
    followed_producers_ids: list[int] | None = None
    saved_albums_ids: list[int] | None = None
    followed_tags: list[str] | None = None


class UpdateUserResponseDTO(BaseResponseDTO):
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
