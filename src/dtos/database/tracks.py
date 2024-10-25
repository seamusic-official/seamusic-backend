from datetime import datetime, date

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class TrackResponseDTO(BaseResponseDTO):
    id: int
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    liked_users: list["UserDTO"] = list()
    producers: list["ProducerDTO"] = list()
    tags: list[str] = list()
    created_at: date
    updated_at: datetime


class TrackItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    tags: list[str] = list()
    created_at: date
    updated_at: datetime


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[TrackItemResponseDTO]


class CreateTrackRequestDTO(BaseRequestDTO):
    title: str
    views: int
    description: str | None
    picture_url: str | None
    file_url: str
    tags: list[str]
    created_at: date
    updated_at: datetime


class UpdateTrackRequestDTO(BaseRequestDTO):
    id: int | None = None
    title: str | None = None
    views: int | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None
    liked_users: list["UserDTO"] | None = None
    producers: list["ProducerDTO"] | None = None
    tags: list[str] | None = None
    created_at: date | None = None
    updated_at: datetime | None = None


class TrackDTO(BaseDTO):
    id: int
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    liked_users: list["UserDTO"] = list()
    producers: list["ProducerDTO"] = list()
    tags: list[str] = list()
    created_at: date
    updated_at: datetime
