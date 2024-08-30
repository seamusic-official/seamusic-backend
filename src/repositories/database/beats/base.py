from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.beats import BeatResponseDTO, CreateBeatRequestDTO, UpdateBeatRequestDTO
from src.dtos.database.beats import BeatsResponseDTO


@dataclass
class BaseBeatsRepository(ABC):
    @abstractmethod
    async def get_user_beats(self, user_id: int) -> BeatsResponseDTO:
        ...

    @abstractmethod
    async def all_beats(self) -> BeatsResponseDTO:
        ...

    @abstractmethod
    async def get_beat_by_id(self, beat_id: int) -> BeatResponseDTO | None:
        ...

    @abstractmethod
    async def create_beat(self, beat: CreateBeatRequestDTO) -> int:
        ...

    @abstractmethod
    async def update_beat(self, beat: UpdateBeatRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        ...
