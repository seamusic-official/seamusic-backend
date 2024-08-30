from datetime import datetime

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class Track(BaseDTO):
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


class TrackResponseDTO(BaseResponseDTO):
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


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[Track]


class CreateTrackRequestDTO(BaseRequestDTO):
    title: str
    picture: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    track_pack_id: int | None = None


class UpdateTrackRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None = None
    file_url: str | None = None
    description: str | None = None
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    track_pack_id: int | None = None
