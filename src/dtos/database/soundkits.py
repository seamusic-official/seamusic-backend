from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    producers: list["Producer"] = list()  # noqa: F821
    beat: list["Beat"] = list()  # noqa: F821
    tags: list["Tag"] = list()  # noqa: F821


class SoundkitResponseDTO(BaseResponseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    likers: list["User"] = list()  # noqa: F821
    producers: list["Producer"] = list()  # noqa: F821
    beat: list["Beat"] = list()  # noqa: F821
    tags: list["Tag"] = list()  # noqa: F821


class SoundkitItemResponseDTO(BaseResponseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    likers: list["User"] = list()  # noqa: F821
    producers: list["Producer"] = list()  # noqa: F821
    beat: list["Beat"] = list()  # noqa: F821
    tags: list["Tag"] = list()  # noqa: F821


class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list["SoundkitItemResponseDTO"]  # noqa: F821


class CreateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    title: str | None
    picture_url: str | None
    description: str | None
    file_path: str | None
    likers: list["User"] = list()  # noqa: F821
    producers: list["Producer"] = list()  # noqa: F821
    beat: list["Beat"] = list()  # noqa: F821
    tags: list["Tag"] = list()  # noqa: F821


class UpdateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class Soundkit(BaseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    likers: list["User"] = list()  # noqa: F821
    producers: list["Producer"] = list()  # noqa: F821
    beat: list["Beat"] = list()  # noqa: F821
    tags: list["Tag"] = list()  # noqa: F821
