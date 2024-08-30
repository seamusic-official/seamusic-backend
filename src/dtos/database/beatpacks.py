from src.dtos.database.auth import User
from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.dtos.database.beats import Beat


class Beatpack(BaseDTO):
    title: str
    description: str
    user_id: int
    users: list[User]
    beats: list[Beat]


class BeatpackResponseDTO(BaseResponseDTO):
    title: str
    description: str
    user_id: int
    users: list[User]
    beats: list[Beat]


class BeatpacksResponseDTO(BaseResponseDTO):
    beatpacks: list[Beatpack]


class CreateBeatpackRequestDTO(BaseRequestDTO):
    title: str
    description: str
    beats: list[Beat]


class UpdateBeatpackRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    beats: list[Beat] = list()
