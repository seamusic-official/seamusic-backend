from datetime import datetime

from pydantic import BaseModel

from src.schemas.base import DetailMixin


class Track(BaseModel):
    id: int
    name: str
    prod_by: str
    description: str
    co_prod: str
    type: str
    user_id: int
    is_available: bool
    file_url: str
    picture_url: str
    created_at: datetime
    updated_at: datetime


class STrackResponse(BaseModel):
    id: int
    name: str
    prod_by: str
    description: str
    co_prod: str
    type: str
    user_id: int
    is_available: bool
    file_url: str
    picture_url: str
    created_at: datetime
    updated_at: datetime


class SMyTracksResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[STrackResponse]


class SAllTracksResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[STrackResponse]


class SAddTracksResponse(BaseModel):
    id: int


class SUpdateTrackPictureResponse(BaseModel):
    id: int


class SReleaseTrackRequest(BaseModel):
    title: str
    picture: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    Track_pack_id: int | None = None


class SReleaseTrackResponse(BaseModel):
    id: int


class SUpdateTrackRequest(BaseModel):
    title: str
    picture: str | None = None
    description: str | None = None
    picture_url: str | None = None
    track_pack_id: int | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int


class SUpdateTrackResponse(BaseModel):
    id: int


class SDeleteTrackResponse(BaseModel, DetailMixin):
    detail: str = "Track deleted"
