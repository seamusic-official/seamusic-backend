from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO


class SquadResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None

    created_at: date
    updated_at: datetime

    viewers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    followers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    artists: list["ArtistDTO"]  # type: ignore[name-defined]  # noqa: F821
    producers: list["ProducerDTO"]  # type: ignore[name-defined]  # noqa: F821


class SquadItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None

    created_at: date
    updated_at: datetime


class SquadsResponseDTO(BaseResponseDTO):
    squads: list[SquadItemResponseDTO]


class CreateSquadRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None

    created_at: date = date.today()
    updated_at: datetime = datetime.now()


class CreateSquadResponseDTO(BaseResponseDTO):
    id: int


class UpdateSquadRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int] | None = None
    followers_ids: list[int] | None = None
    artists_ids: list[int] | None = None
    producers_ids: list[int] | None = None


class UpdateSquadResponseDTO(BaseResponseDTO):
    id: int
