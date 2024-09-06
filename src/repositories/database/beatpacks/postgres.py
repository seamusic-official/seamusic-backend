from dataclasses import dataclass

from sqlalchemy import select, delete, func

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, model_to_response_dto, models_to_dto
from src.dtos.database.beatpacks import (
    Beatpack as _Beatpack,
    BeatpackResponseDTO,
    BeatpacksResponseDTO,
    CreateBeatpackRequestDTO,
    UpdateBeatpackRequestDTO
)
from src.models.beatpacks import Beatpack
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.beatpacks.base import BaseBeatpacksRepository


@dataclass
class BeatpacksRepository(BaseBeatpacksRepository, SQLAlchemyRepository):
    async def get_user_beatpacks(self, user_id: int, offset: int = 0, limit: int = 10) -> BeatpacksResponseDTO:
        query = select(Beatpack).filter_by(user_id=user_id).offset(offset).limit(limit).order_by(Beatpack.id.desc())
        beatpacks = list(await self.scalars(query))
        return BeatpacksResponseDTO(beatpacks=models_to_dto(models=beatpacks, dto=_Beatpack))

    async def get_user_beatpacks_count(self, user_id: int) -> int:
        query = select(func.count(Beatpack.id)).filter_by(user_id=user_id)
        return await self.scalar(query)

    async def get_all_beatpacks(self, offset: int = 0, limit: int = 10) -> BeatpacksResponseDTO:
        query = select(Beatpack).offset(offset).limit(limit).order_by(Beatpack.id.desc())
        beatpacks = list(await self.scalars(query))
        return BeatpacksResponseDTO(beatpacks=models_to_dto(models=beatpacks, dto=_Beatpack))

    async def get_beatpacks_count(self) -> int:
        query = select(func.count(Beatpack.id))
        return await self.scalar(query)

    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackResponseDTO | None:
        return model_to_response_dto(
            model=await self.get(Beatpack, beatpack_id),
            response_dto=BeatpackResponseDTO
        )

    async def add_beatpack(self, beatpack: CreateBeatpackRequestDTO) -> int:
        model = request_dto_to_model(model=Beatpack, request_dto=beatpack)
        await self.add(model)
        return model.id

    async def update_beatpack(self, beatpack: UpdateBeatpackRequestDTO) -> int:
        model = request_dto_to_model(model=Beatpack, request_dto=beatpack)
        await self.merge(model)
        return model.id

    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        query = delete(Beatpack).filter_by(id=beatpack_id, user_id=user_id)
        await self.execute(query)


def init_postgres_repository() -> BeatpacksRepository:
    return BeatpacksRepository()
