from datetime import date, datetime
from typing import Generic, TypeVar, Literal

from pydantic import EmailStr, BaseModel

from src.domain.music.albums.core.dtos import (
    BasePopularAlbumsRequestDTO,
    BasePopularAlbumsResponseDTO,
    BaseUserDTO,
    BaseArtistDTO,
    BaseTrackDTO,
    BaseItemsRequestDTO,
    BaseAlbumRequestDTO,
    BaseAlbumResponseDTO,
    BaseAlbumItemResponseDTO,
    BaseArtistAlbumsRequestDTO,
    BaseCreateAlbumRequestDTO,
    BaseDeleteAlbumRequestDTO,
    BaseUpdateAlbumResponseDTO,
    BaseUpdateAlbumRequestDTO,
    BaseCreateAlbumResponseDTO,
    BaseArtistAlbumsResponseDTO,
    BaseLikeAlbumRequestDTO,
    BaseUnlikeAlbumRequestDTO,
    BaseUpdateAlbumCoverRequestDTO,
)
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar('ItemType')
AlbumType = Literal['album', 'single']
AccessLevel = Literal['user', 'admin', 'superuser']
PremiumLevel = Literal['none', 'bot', 'full']


class UserDTO(BaseUserDTO, BaseModel):
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


class ArtistDTO(BaseArtistDTO, BaseModel):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class TrackDTO(BaseTrackDTO, BaseModel):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class ItemsRequestDTO(BaseItemsRequestDTO, BaseModel):
    start: int = 1
    size: int = 10


class ItemsResponseDTO(Generic[ItemType], BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


class AlbumRequestDTO(BaseAlbumRequestDTO, BaseModel):
    album_id: int
    user_id: int


class AlbumResponseDTO(BaseAlbumResponseDTO, BaseModel):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    type: AlbumType
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    artists: list[ArtistDTO]
    tracks: list[TrackDTO]
    tags: list[str]


class AlbumItemResponseDTO(BaseAlbumItemResponseDTO, BaseModel):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    views: int
    likes: int
    type: AlbumType

    created_at: date
    updated_at: datetime


class PopularAlbumsRequestDTO(BasePopularAlbumsRequestDTO):
    user_id: int


class PopularAlbumsResponseDTO(  # type: ignore[misc]
    BasePopularAlbumsResponseDTO,
    ItemsResponseDTO[AlbumItemResponseDTO],
    BaseModel,
):
    pass


class ArtistAlbumsRequestDTO(BaseArtistAlbumsRequestDTO, BaseModel):
    artist_id: int


class ArtistAlbumsResponseDTO(  # type: ignore[misc]
    BaseArtistAlbumsResponseDTO,
    ItemsResponseDTO[AlbumItemResponseDTO],
    BaseModel,
):
    pass


class LikeAlbumRequestDTO(BaseLikeAlbumRequestDTO):
    album_id: int
    user_id: int


class UnlikeAlbumRequestDTO(BaseUnlikeAlbumRequestDTO):
    album_id: int
    user_id: int


class UpdateAlbumCoverRequestDTO(BaseUpdateAlbumCoverRequestDTO):
    album_id: int
    user_id: int
    data: bytes


class CreateAlbumRequestDTO(BaseCreateAlbumRequestDTO, BaseModel):
    title: str
    user_id: int
    description: str | None
    tags: list[str]


class CreateAlbumResponseDTO(BaseCreateAlbumResponseDTO, BaseModel):
    id: int


class UpdateAlbumRequestDTO(BaseUpdateAlbumRequestDTO, BaseModel):
    id: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None

    artists_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateAlbumResponseDTO(BaseUpdateAlbumResponseDTO, BaseModel):
    id: int


class DeleteAlbumRequestDTO(BaseDeleteAlbumRequestDTO, BaseModel):
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
