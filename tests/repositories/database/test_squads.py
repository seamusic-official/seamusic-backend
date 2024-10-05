import logging

import pytest

from src.dtos.database.squads import (
    CreateSquadRequestDTO,
    SquadsResponseDTO,
    SquadResponseDTO,
    UpdateSquadRequestDTO
)

from src.repositories.database.squads import SquadRepository, init_squads_repository


class TestSquadRepository:
    repostirory: SquadRepository = init_squads_repository()

    async def test_add_squad(self, squad: CreateSquadRequestDTO) -> None:
        add_squad_request = await self.repostirory.add_squad(squad)
        assert isinstance(add_squad_request, int)

    async def test_get_squad_by_id(self, squad_id: int) -> None:
        get_squad_by_id = await self.repostirory.get_squad_by_id(squad_id)
        assert isinstance(get_squad_by_id, SquadResponseDTO | None)

    async def test_get_squads_count(self) -> None:
        get_squads_count = await self.repostirory.get_squads_count()
        assert get_squads_count >= 0

    async def test_update_squad(self, squad: UpdateSquadRequestDTO) -> None:
        update_squad = await self.repostirory.update_squad(squad)
        assert isinstance(update_squad, int)

    @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
    async def test_get_all_squads(self, offset: int, limit: int) -> None:
        all_squads = await self.repostirory.get_all_squads(offset, limit)
        assert isinstance(all_squads, SquadsResponseDTO)

    async def test_delete_squad(self, squad_id: int) -> None:
        await self.repostirory.delete_squad(squad_id)
