from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.beatpacks import (
    BeatpackResponseDTO,
    BeatpacksResponseDTO,
    CreateBeatpackRequestDTO,
    UpdateBeatpackRequestDTO
)


@dataclass
class BaseBeatpacksRepository(ABC):
    @abstractmethod
    async def get_user_beatpacks(self, user_id: int) -> BeatpacksResponseDTO:
        ...

    @abstractmethod
    async def get_all_beatpacks(self) -> BeatpacksResponseDTO:
        ...

    @abstractmethod
    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackResponseDTO | None:
        ...

    @abstractmethod
    async def add_beatpack(self, beatpack: CreateBeatpackRequestDTO) -> int:
        ...

    @abstractmethod
    async def update_beatpack(self, beatpack: UpdateBeatpackRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        ...
