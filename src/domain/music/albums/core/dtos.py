from abc import ABC
from datetime import date, datetime
from typing import Literal


class BaseUserDTO(ABC):
    id: int
    username: str
    description: str | None = None
    email: str
    password: str
    picture_url: str | None = None
    access_level: Literal['user', 'admin', 'superuser'] = 'user'
    telegram_id: int | None = None
    premium_level: Literal['none', 'bot', 'full'] = 'none'

    is_active: bool
    is_adult: bool
    is_verified: bool

    created_at: date
    updated_at: datetime


class BaseArtistDTO(ABC):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class BaseTrackDTO(ABC):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class BaseItemsRequestDTO(ABC):
    start: int = 1
    size: int = 10


class BaseAlbumRequestDTO(ABC):
    album_id: int
    user_id: int


class BaseAlbumResponseDTO(ABC):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    type: Literal['album', 'single']
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    artists: list[BaseArtistDTO]
    tracks: list[BaseTrackDTO]
    tags: list[str]


class BaseAlbumItemResponseDTO(ABC):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    views: int
    likes: int
    type: Literal['album', 'single']

    created_at: date
    updated_at: datetime


class BasePopularAlbumsRequestDTO(ABC):
    user_id: int


class BasePopularAlbumsResponseDTO(ABC):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[BaseAlbumItemResponseDTO]


class BaseCountAlbumsResponseDTO(ABC):
    amount: int


class BaseArtistAlbumsRequestDTO(ABC):
    artist_id: int


class BaseArtistAlbumsResponseDTO(ABC):
    total: int
    items: list[BaseAlbumItemResponseDTO]


class BaseLikeAlbumRequestDTO(ABC):
    album_id: int
    user_id: int


class BaseUnlikeAlbumRequestDTO(ABC):
    album_id: int
    user_id: int


class BaseUpdateAlbumCoverRequestDTO(ABC):
    album_id: int
    user_id: int
    data: bytes


class BaseCreateAlbumRequestDTO(ABC):
    title: str
    user_id: int
    description: str | None
    tags: list[str]


class BaseCreateAlbumResponseDTO(ABC):
    id: int


class BaseUpdateAlbumRequestDTO(ABC):
    id: int
    user_id: int
    title: str | None = None
    description: str | None = None

    artists_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    tags: list[str] | None = None


class BaseUpdateAlbumResponseDTO(ABC):
    id: int


class BaseDeleteAlbumRequestDTO(ABC):
    album_id: int
    user_id: int
