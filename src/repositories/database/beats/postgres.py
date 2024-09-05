from sqlalchemy import select, delete

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, model_to_response_dto, models_to_dto
from src.dtos.database.beats import (
    Beat as _Beat,
    BeatResponseDTO,
    BeatsResponseDTO,
    CreateBeatRequestDTO,
    UpdateBeatRequestDTO,
)
from src.models.beats import Beat
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.beats.base import BaseBeatsRepository


class BeatsRepository(BaseBeatsRepository, SQLAlchemyRepository):
    async def get_user_beats(self, user_id: int, offset: int = 0, limit: int = 10) -> BeatsResponseDTO:
        query = select(Beat).filter_by(user_id=user_id).offset(offset).limit(limit).order_by(Beat.id.desc())
        beats = list(await self.scalars(query))
        return BeatsResponseDTO(beats=models_to_dto(models=beats, dto=_Beat))

    async def get_user_beats_count(self, user_id: int) -> int:
        query = select(Beat.id).filter_by(user_id=user_id)
        return len(list(await self.scalars(query)))

    async def all_beats(self, offset: int = 0, limit: int = 10) -> BeatsResponseDTO:
        query = select(Beat).offset(offset).limit(limit).order_by(Beat.id.desc())
        beats = list(await self.scalars(query))
        return BeatsResponseDTO(beats=models_to_dto(models=beats, dto=_Beat))

    async def get_beats_count(self) -> int:
        query = select(Beat.id)
        return len(list(await self.scalars(query)))

    async def get_beat_by_id(self, beat_id: int) -> BeatResponseDTO | None:
        return model_to_response_dto(
            model=await self.get(Beat, beat_id),
            response_dto=BeatResponseDTO
        )

    async def create_beat(self, beat: CreateBeatRequestDTO) -> int:
        model = request_dto_to_model(model=Beat, request_dto=beat)
        await self.add(model)
        return model.id

    async def update_beat(self, beat: UpdateBeatRequestDTO) -> int:
        model = request_dto_to_model(model=Beat, request_dto=beat)
        await self.merge(model)
        return model.id

    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        query = delete(Beat).filter_by(id=beat_id, user_id=user_id)
        await self.execute(query)


def init_postgres_repository() -> BeatsRepository:
    return BeatsRepository()
