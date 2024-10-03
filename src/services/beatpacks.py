from dataclasses import dataclass

from src.dtos.database.beatpacks import (
    CreateBeatpackRequestDTO,
    UpdateBeatpackRequestDTO,
    BeatpacksResponseDTO,
    BeatpackResponseDTO
)
from src.exceptions import NotFoundException, NoRightsException
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.beatpacks import init_beatpacks_repository, BeatpacksRepository
from src.repositories.media.s3 import S3Repository, init_s3_repository


@dataclass
class BeatpacksDatabaseRepositories(DatabaseRepositories):
    beatpacks: BeatpacksRepository


@dataclass
class BeatpacksRepositories(Repositories):
    database: BeatpacksDatabaseRepositories
    media: S3Repository


@dataclass
class BeatpackService:
    respositories: BeatpacksRepositories

    async def get_user_beatpacks(self, user_id: int, start: int = 1, size: int = 10) -> BeatpacksResponseDTO:
        return await self.respositories.database.beatpacks.get_user_beatpacks(user_id=user_id, offset=start - 1, limit=size)

    async def get_user_beatpacks_count(self, user_id: int) -> int:
        return await self.respositories.database.beatpacks.get_user_beatpacks_count(user_id=user_id)

    async def get_all_beatpacks(self, start: int = 1, size: int = 10) -> BeatpacksResponseDTO:
        return await self.respositories.database.beatpacks.get_all_beatpacks(offset=start - 1, limit=size)

    async def get_beatpacks_count(self) -> int:
        return await self.respositories.database.beatpacks.get_beatpacks_count()

    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackResponseDTO:
        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        return beatpack

    async def add_beatpack(self, title: str, description: str) -> int:
        beatpack = CreateBeatpackRequestDTO(
            title=title,
            description=description,
            beats=[]
        )

        return await self.respositories.database.beatpacks.add_beatpack(beatpack=beatpack)

    async def update_beatpack(
        self,
        beatpack_id: int,
        user_id: int,
        beat_ids: list[int] | None = None,
        title: str | None = None,
        description: str | None = None,
    ) -> int:

        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        if user_id in list(map(lambda user: user.id, beatpack.users)):
            updated_beatpack = UpdateBeatpackRequestDTO(
                title=title,
                description=description,
                beat_ids=beat_ids,
            )
            return await self.respositories.database.beatpacks.update_beatpack(beatpack=updated_beatpack)

        raise NoRightsException()

    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        beatpack = await self.respositories.database.beatpacks.get_one_beatpack(beatpack_id=beatpack_id)

        if not beatpack:
            raise NotFoundException()

        if user_id in list(map(lambda user: user.id, beatpack.users)):
            return await self.respositories.database.beatpacks.delete_beatpack(beatpack_id=beatpack_id, user_id=user_id)

        raise NoRightsException()


def get_beatpacks_repositories() -> BeatpacksRepositories:
    return BeatpacksRepositories(
        database=BeatpacksDatabaseRepositories(beatpacks=init_beatpacks_repository()),
        media=init_s3_repository()
    )


def get_beatpack_service() -> BeatpackService:
    return BeatpackService(respositories=get_beatpacks_repositories())
