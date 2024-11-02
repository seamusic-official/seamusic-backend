from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class TrackResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    viewers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    likers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    producers: list["ProducerDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list[str]


class TrackItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    tags: list[str]


class TracksResponseDTO(BaseResponseDTO):
    tracks: list[TrackItemResponseDTO]


class CreateTrackRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    tags: list[str]


class CreateTrackResponseDTO(BaseResponseDTO):
    id: int


class UpdateTrackRequestDTO(BaseRequestDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    updated_at: datetime = datetime.now()

    viewers_ids: list[int]
    likers_ids: list[int]
    producers_ids: list[int]
    tags: list[str]


class UpdateTrackResponseDTO(BaseResponseDTO):
    id: int


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
