from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class CreateSquadRequestDTO(BaseRequestDTO):
    title: str
    views: int
    description: str | None = None
    picture_url: str | None = None
    artists: list["ArtistDTO"] = list()  # noqa: F821
    producers: list["ProducerDTO"] = list()  # noqa: F821


class SquadResponseDTO(BaseResponseDTO):
    id: int
    views: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    followers: list["UserDTO"] = list()  # noqa: F821
    artists: list["ArtistDTO"] = list()  # noqa: F821
    producers: list["ProducerDTO"] = list()  # noqa: F821


class SquadItemResponse(BaseResponseDTO):
    id: int
    views: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None


class SquadsResponseDTO(BaseResponseDTO):
    squads: list[SquadItemResponse]  # noqa: F821


class CreateSquadResponseDTO(BaseResponseDTO):
    id: int


class UpdateSquadRequestDTO(BaseRequestDTO):
    id: int
    views: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    followers: list["UserDTO"] = None  # noqa: F821
    artists: list["ArtistDTO"] = None  # noqa: F821
    producers: list["ProducerDTO"] = None  # noqa: F821


class UpdateSquadResponseDTO(BaseResponseDTO):
    id: int


class SquadDTO(BaseDTO):
    views: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    followers: list["UserDTO"] = list()  # noqa: F821
    artists: list["ArtistDTO"] = list()  # noqa: F821
    producers: list["ProducerDTO"] = list()  # noqa: F821
