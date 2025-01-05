from datetime import date, datetime
from typing import Literal

from fastapi import UploadFile
from pydantic import BaseModel, EmailStr

from src.domain.music.albums.api.schemas import (
    BaseSUser,
    BaseSArtist,
    BaseSTrack,
    BaseSItemsRequest,
    BaseSAlbumRequest,
    BaseSAlbumResponse,
    BaseSAlbumItemResponse,
    BaseSPopularAlbumsResponse,
    BaseSCountAlbumsResponse,
    BaseSArtistAlbumsRequest,
    BaseSArtistAlbumsResponse,
    BaseSLikeAlbumRequest,
    BaseSUnlikeAlbumRequest,
    BaseSUpdateAlbumCoverRequest,
    BaseSCreateAlbumRequest,
    BaseSCreateAlbumResponse,
    BaseSUpdateAlbumRequest,
    BaseSUpdateAlbumResponse,
    BaseSDeleteAlbumRequest,
)


class SUser(BaseSUser, BaseModel):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
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


class SArtist(BaseSArtist, BaseModel):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class STrack(BaseSTrack, BaseModel):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class SItemsRequest(BaseSItemsRequest, BaseModel):
    start: int = 1
    size: int = 10


class SAlbumRequest(BaseSAlbumRequest, BaseModel):
    album_id: int


class SAlbumResponse(BaseSAlbumResponse, BaseModel):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    type: Literal['album', 'single']
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    artists: list[SArtist]
    tracks: list[STrack]
    tags: list[str]


class SAlbumItemResponse(BaseSAlbumItemResponse, BaseModel):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    views: int
    likes: int
    type: Literal['album', 'single']

    created_at: date
    updated_at: datetime


class SPopularAlbumsResponse(BaseSPopularAlbumsResponse, BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[SAlbumItemResponse]


class SCountAlbumsResponse(BaseSCountAlbumsResponse, BaseModel):
    amount: int


class SArtistAlbumsRequest(BaseSArtistAlbumsRequest, BaseModel):
    artist_id: int


class SArtistAlbumsResponse(BaseSArtistAlbumsResponse, BaseModel):
    total: int
    items: list[SAlbumItemResponse]


class SLikeAlbumRequest(BaseSLikeAlbumRequest, BaseModel):
    album_id: int


class SUnlikeAlbumRequest(BaseSUnlikeAlbumRequest, BaseModel):
    album_id: int


class SUpdateAlbumCoverRequest(BaseSUpdateAlbumCoverRequest, BaseModel):
    album_id: int
    file: UploadFile


class SCreateAlbumRequest(BaseSCreateAlbumRequest, BaseModel):
    title: str
    description: str | None
    tags: list[str]


class SCreateAlbumResponse(BaseSCreateAlbumResponse, BaseModel):
    id: int


class SUpdateAlbumRequest(BaseSUpdateAlbumRequest, BaseModel):
    id: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None

    artists_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    tags: list[str] | None = None


class SUpdateAlbumResponse(BaseSUpdateAlbumResponse, BaseModel):
    id: int


class SDeleteAlbumRequest(BaseSDeleteAlbumRequest, BaseModel):
    album_id: int
