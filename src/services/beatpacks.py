from dataclasses import dataclass

from src.dtos.database.beatpacks import (
    CreateBeatpackRequestDTO,
    UpdateBeatpackRequestDTO,
    BeatpacksResponseDTO,
    BeatpackResponseDTO
)
from src.dtos.database.beats import Beat
from src.exceptions.services import NotFoundException, NoRightsException
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.beatpacks.base import BaseBeatpacksRepository
from src.repositories.database.beatpacks.postgres import init_postgres_repository
from src.repositories.media.s3 import S3Repository, init_s3_repository


@dataclass
class BeatpacksDatabaseRepositories(DatabaseRepositories):
    beatpacks: BaseBeatpacksRepository


@dataclass
class BeatpacksRepositories(Repositories):
    database: BeatpacksDatabaseRepositories
    media: S3Repository


@dataclass
class BeatpackService:
    respositories: BeatpacksRepositories

    async def get_user_beatpacks(self, user_id: int) -> BeatpacksResponseDTO:
        return await self.respositories.database.beatpacks.get_user_beatpacks(user_id=user_id)

    async def get_all_beatpacks(self) -> BeatpacksResponseDTO:
        return await self.respositories.database.beatpacks.get_all_beatpacks()

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
        beats: list[Beat],
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
                beats=beats
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
        database=BeatpacksDatabaseRepositories(beatpacks=init_postgres_repository()),
        media=init_s3_repository()
    )


def get_beatpack_service() -> BeatpackService:
    return BeatpackService(respositories=get_beatpacks_repositories())
