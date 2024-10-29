from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class BeatpackResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None = None

    created_at: date
    updated_at: datetime

    viewers: list["UserDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    likers: list["UserDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    producers: list["ProducerDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    beats: list["BeatDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    tags: list[str] = list()


class BeatpackItemResponseDTO(BaseResponseDTO):
    title: str
    description: str | None = None

    created_at: date
    updated_at: datetime

    tags: list[str] = list()


class BeatpacksResponseDTO(BaseResponseDTO):
    beatpacks: list[BeatpackItemResponseDTO]


class CreateBeatpackRequestDTO(BaseRequestDTO):
    title: str
    description: str | None = None

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    tags: list[str] = list()


class CreateBeatpackResponseDTO(BaseResponseDTO):
    id: int


class UpdateBeatpackRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    description: str | None = None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    producers_ids: list[int] | None = None
    beats_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateBeatpackResponseDTO(BaseResponseDTO):
    id: int


class BeatpackDTO(BaseDTO):
    id: int
    title: str
    description: str | None = None

    created_at: date
    updated_at: datetime

    tags: list[str] = list()
