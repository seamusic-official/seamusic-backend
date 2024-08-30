from dataclasses import dataclass

from sqlalchemy import select, delete

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, models_to_dto, model_to_response_dto
from src.dtos.database.tracks import (
    Track as _Track,
    UpdateTrackRequestDTO,
    TrackResponseDTO,
    TracksResponseDTO,
    CreateTrackRequestDTO,
)
from src.models.tracks import Track
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.tracks.base import BaseTracksRepository


@dataclass
class TracksRepository(SQLAlchemyRepository, BaseTracksRepository):

    async def create_track(self, track: CreateTrackRequestDTO) -> int:
        model = request_dto_to_model(model=Track, request_dto=track)
        await self.add(model)
        return model.id

    async def get_user_tracks(self, user_id: int) -> TracksResponseDTO:
        query = select(Track).filter_by(user_id=user_id)
        tracks = list(await self.scalars(query))
        return TracksResponseDTO(tracks=models_to_dto(models=tracks, dto=_Track))

    async def get_all_tracks(self) -> TracksResponseDTO:
        query = select(Track)
        tracks = list(await self.scalars(query))
        return TracksResponseDTO(tracks=models_to_dto(models=tracks, dto=_Track))

    async def get_track_by_id(self, track_id: int) -> TrackResponseDTO | None:
        track = await self.get(Track, track_id)
        return model_to_response_dto(model=track, response_dto=TrackResponseDTO)

    async def update_track(self, track: UpdateTrackRequestDTO) -> int:
        model = request_dto_to_model(model=Track, request_dto=track)
        await self.merge(model)
        return model.id

    async def delete_track(self, track_id: int, user_id: int) -> None:
        query = delete(Track).filter_by(id=track_id, user_id=user_id)
        await self.execute(query)


def init_postgres_repository() -> TracksRepository:
    return TracksRepository()
