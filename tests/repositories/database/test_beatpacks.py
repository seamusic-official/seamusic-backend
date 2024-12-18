# import pytest
#
# from src_.dtos.database.beatpacks import (
#     BeatpackResponseDTO,
#     BeatpacksResponseDTO,
#     CreateBeatpackRequestDTO,
#     UpdateBeatpackRequestDTO
# )
# from src_.repositories.database.beatpacks import BeatpacksRepository, init_beatpacks_repository
#
#
# class TestBeatpacksRepository:
#     repository: BeatpacksRepository = init_beatpacks_repository()
#
#     @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
#     async def test_get_user_beatpacks(self, user_id: int, offset: int, limit: int) -> None:
#         response = await self.repository.get_user_beatpacks(user_id=user_id, offset=offset, limit=limit)
#         assert isinstance(response, BeatpacksResponseDTO)
#
#     async def test_get_user_beatpacks_count(self, user_id: int) -> None:
#         response = await self.repository.get_user_beatpacks_count(user_id=user_id)
#         assert isinstance(response, int)
#
#     @pytest.mark.parametrize("offset,limit", [(i, 10 - i) for i in range(10)])
#     async def test_get_all_beatpacks(self, offset: int, limit: int) -> None:
#         response = await self.repository.get_all_beatpacks(offset=offset, limit=limit)
#         assert isinstance(response, BeatpacksResponseDTO)
#
#     async def test_get_beatpacks_count(self) -> None:
#         response = await self.repository.get_beatpacks_count()
#         assert isinstance(response, int)
#
#     async def test_get_one_beatpack(self, beatpack_id: int) -> None:
#         response = await self.repository.get_one_beatpack(beatpack_id=beatpack_id)
#         assert isinstance(response, BeatpackResponseDTO | None)
#
#     async def test_add_beatpack(self, beatpack: CreateBeatpackRequestDTO) -> None:
#         response = await self.repository.add_beatpack(beatpack=beatpack)
#         assert isinstance(response, int)
#
#     async def test_update_beatpack(self, beatpack: UpdateBeatpackRequestDTO) -> None:
#         response = await self.repository.update_beatpack(beatpack=beatpack)
#         assert isinstance(response, int)
#
#     async def test_delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
#         await self.repository.delete_beatpack(beatpack_id=beatpack_id, user_id=user_id)
