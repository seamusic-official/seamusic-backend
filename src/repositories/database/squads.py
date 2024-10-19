from dataclasses import dataclass

from sqlalchemy import select, delete, func

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, models_to_dto, model_to_response_dto
from src.dtos.database.squads import (
    Squad as _Squad,
    SquadResponseDTO,
    SquadsResponseDTO,
    CreateSquadRequestDTO,
    UpdateSquadRequestDTO
)
from src.models.squads import Squad
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class SquadRepository(SQLAlchemyRepository):
    async def add_squad(self, squad: CreateSquadRequestDTO) -> int:
        model = request_dto_to_model(model=Squad, request_dto=squad)
        await self.add(model)
        return model.id

    async def get_squads_count(self) -> int:
        query = select(func.count(Squad.id))
        return await self.scalar(query)

    async def update_squad(self, squad: UpdateSquadRequestDTO) -> int:
        model = request_dto_to_model(model=Squad, request_dto=squad)
        await self.merge(model)
        return model.id

    async def get_squad_by_id(self, squad_id: int) -> SquadResponseDTO | None:
        squad = await self.get(Squad, squad_id)
        return model_to_response_dto(model=squad, response_dto=SquadResponseDTO)

    async def get_all_squads(self, offset: int = 0, limit: int = 10) -> SquadsResponseDTO:
        query = select(Squad).offset(offset).limit(limit)
        squads = list(await self.scalar(query))
        return SquadsResponseDTO(squads=models_to_dto(models=squads, dto=_Squad))

    async def delete_squad(self, squad_id: int) -> None:
        query = delete(Squad).filter_by(id=squad_id)
        await self.execute(query)


def init_squads_repository() -> SquadRepository:
    return SquadRepository()
