from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    producers: list["ProducerDTO"] = list()  # noqa: F821
    beat: list["BeatDTO"] = list()  # noqa: F821
    tags: list[str] = list()  # noqa: F821


class SoundkitResponseDTO(BaseResponseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    likers: list["UserDTO"] = list()  # noqa: F821
    producers: list["ProducerDTO"] = list()  # noqa: F821
    beat: list["BeatDTO"] = list()  # noqa: F821
    tags: list[str] = list()  # noqa: F821


class SoundkitItemResponseDTO(BaseResponseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str

class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list[SoundkitItemResponseDTO]  # noqa: F821


class CreateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    title: str | None
    picture_url: str | None
    description: str | None
    file_path: str | None
    likers: list["UserDTO"] | None # type: ignore[name-defined]
    producers: list["ProducerDTO"] | None   # type: ignore[name-defined]
    beat: list["BeatDTO"] | None   # type: ignore[name-defined]
    tags: list[str] | None   # type: ignore[name-defined]


class UpdateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class SoundkitDTO(BaseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    likers: list["UserDTO"] = list()  # type: ignore[name-defined]
    producers: list["ProducerDTO"] = list()  # type: ignore[name-defined]
    beat: list["BeatDTO"] = list()  # type: ignore[name-defined]
    tags: list[str] = list()  # type: ignore[name-defined]
