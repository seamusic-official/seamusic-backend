from src.dtos.database.auth import User
from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.dtos.database.beats import Beat


class Beatpack(BaseDTO):
    name: str
    description: str | None = None
    users: list[User]
    beats: list[Beat]


class BeatpackResponseDTO(BaseResponseDTO):
    name: str
    description: str | None = None
    users: list[User]
    beats: list[Beat]


class BeatpacksResponseDTO(BaseResponseDTO):
    beatpacks: list[Beatpack]


class CreateBeatpackRequestDTO(BaseRequestDTO):
    name: str
    description: str | None = None
    beats: list[Beat]


class UpdateBeatpackRequestDTO(BaseRequestDTO):
    name: str
    description: str | None = None
    beats: list[Beat]
