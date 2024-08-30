from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.tracks import TracksResponseDTO, TrackResponseDTO, UpdateTrackRequestDTO, CreateTrackRequestDTO


@dataclass
class BaseTracksRepository(ABC):

    @abstractmethod
    async def create_track(self, track: CreateTrackRequestDTO) -> int:
        ...

    @abstractmethod
    async def get_user_tracks(self, user_id: int) -> TracksResponseDTO:
        ...

    @abstractmethod
    async def get_all_tracks(self) -> TracksResponseDTO:
        ...

    @abstractmethod
    async def get_track_by_id(self, track_id: int) -> TrackResponseDTO | None:
        ...

    @abstractmethod
    async def update_track(self, track: UpdateTrackRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_track(self, track_id: int, user_id: int) -> None:
        ...
