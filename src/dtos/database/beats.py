from datetime import datetime, date

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class BeatResponseDTO(BaseResponseDTO):
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


class BeatItemResponseDTO(BaseResponseDTO):
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


class BeatsResponseDTO(BaseResponseDTO):
    beats: list[BeatItemResponseDTO]


class CreateBeatRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    tags: list[str]


class CreateBeatResponseDTO(BaseResponseDTO):
    id: int


class UpdateBeatRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    producers_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateBeatResponseDTO(BaseResponseDTO):
    id: int


class BeatDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime
