from datetime import datetime

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class Tag(BaseDTO):
    name: str


class Track(BaseDTO):
    id: int
    title: str
    description: str | None = None
    picture_url: str | None = None
    views: int
    file_url: str
    tag: list["Tag"]


class TrackResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None = None
    picture_url: str | None = None
    views: int
    file_url: str
    tag: list["Tag"]
    created_at: datetime
    updated_at: datetime


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[Track]


class CreateTrackRequestDTO(BaseRequestDTO):
    id: int
    title: str
    description: str | None = None
    picture_url: str | None = None
    views: int | None = None
    file_url: str
    tag: list["Tag"]


class UpdateTrackRequestDTO(BaseRequestDTO):
    id: int | None = None
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    views: int | None = None
    file_url: str | None = None
    tag: list["Tag"] | None = None


class UpdateTrackResponseDTO(BaseResponseDTO):
    id: int
