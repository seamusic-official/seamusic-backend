from datetime import datetime, date
from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class CreateTrackRequestDTO(BaseRequestDTO):
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    likers: list["UserDTO"] = list()  # type: ignore[name-defined]
    producers: list["ProducerDTO"] = list()  # type: ignore[name-defined]
    tags: list[str]


class TrackResponseDTO(BaseResponseDTO):
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    likers: list["UserDTO"]   # type: ignore[name-defined]
    producers: list["ProducerDTO"]   # type: ignore[name-defined]
    tags: list[str]
    created_at: date
    updated_at: datetime


class TrackItemResponseDTO(BaseResponseDTO):
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    created_at: date
    updated_at: datetime


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[TrackItemResponseDTO]    # type: ignore[name-defined]


class UpdateTrackRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    views: int | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None
    tags: list[str] | None = None


class Track(BaseDTO):
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    tags: list[str]
