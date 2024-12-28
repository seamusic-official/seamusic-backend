from datetime import date, datetime
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr

from src.domain.music.albums.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar('ItemType')
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


class ArtistDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


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


class ItemsRequestDTO(BaseRequestDTO):
    start: int = 1
    size: int = 10


class ItemsResponseDTO(BaseResponseDTO, Generic[ItemType]):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


class AlbumRequestDTO(BaseRequestDTO):
    album_id: int
    user_id: int


class AlbumResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    type: AlbumType
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    viewers_ids: list[int]
    likers_ids: list[int]
    artists: list[ArtistDTO]
    tracks: list[TrackDTO]
    tags: list[str]


class AlbumExistanceRequestDTO(BaseRequestDTO):
    artist_id: int
    title: str


class AlbumItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    views: int
    likes: int
    type: AlbumType

    created_at: date
    updated_at: datetime


class PopularAlbumsResponseDTO(ItemsResponseDTO[AlbumItemResponseDTO]):
    pass


class CountAlbumsResponseDTO(BaseResponseDTO):
    amount: int


class ArtistIDRequest(BaseRequestDTO):
    user_id: int


class ArtistIDResponse(BaseResponseDTO):
    artist_id: int


class ArtistAlbumsRequestDTO(BaseRequestDTO):
    artist_id: int


class ArtistAlbumsResponseDTO(ItemsResponseDTO[AlbumItemResponseDTO]):
    pass


class CreateAlbumRequestDTO(BaseRequestDTO):
    title: str
    user_id: int
    picture_url: str | None
    description: str | None
    type: AlbumType

    artists_ids: list[int]
    tags: list[str]

    created_at: date
    updated_at: datetime


class CreateAlbumResponseDTO(BaseResponseDTO):
    id: int


class UpdateAlbumRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    type: AlbumType | None = None

    updated_at: datetime | None = None

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    artists_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateAlbumResponseDTO(BaseResponseDTO):
    id: int


class DeleteAlbumRequestDTO(BaseRequestDTO):
    album_id: int


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
