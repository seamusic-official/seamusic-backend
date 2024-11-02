from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class SoundkitResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    viewers: list["User"]  # type: ignore[name-defined]  # noqa: F821
    likers: list["User"]  # type: ignore[name-defined]  # noqa: F821
    producers: list["ProducerDTO"]  # type: ignore[name-defined]  # noqa: F821
    beats: list["BeatDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list[str]


class SoundkitItemResponseDTO(BaseResponseDTO):
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


class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list[SoundkitItemResponseDTO]


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    tags: list[str]


class CreateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    producers_ids: list[int] | None = None
    beats_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class SoundkitDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime
