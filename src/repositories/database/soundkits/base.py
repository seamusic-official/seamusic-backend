from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.soundkits import (
    SoundkitsResponseDTO,
    SoundkitResponseDTO,
    CreateSoundkitRequestDTO,
    UpdateSoundkitRequestDTO
)


@dataclass
class BaseSoundkitsRepository(ABC):
    @abstractmethod
    async def get_user_soundkits(self, user_id: int, offset: int = 0, limit: int = 10) -> SoundkitsResponseDTO:
        ...

    @abstractmethod
    async def get_users_soundkits_count(self, user_id: int) -> int:
        ...

    @abstractmethod
    async def get_all_soundkits(self, offset: int = 0, limit: int = 10) -> SoundkitsResponseDTO:
        ...

    @abstractmethod
    async def get_soundkits_count(self) -> int:
        ...

    @abstractmethod
    async def get_soundkit_by_id(self, soundkit_id: int) -> SoundkitResponseDTO | None:
        ...

    @abstractmethod
    async def add_soundkit(self, soundkit: CreateSoundkitRequestDTO) -> int:
        ...

    @abstractmethod
    async def update_soundkit(self, soundkit: UpdateSoundkitRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_soundkit(self, soundkit_id: int, user_id: int) -> None:
        ...
