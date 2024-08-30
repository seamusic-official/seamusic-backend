from dataclasses import dataclass
from datetime import datetime
from io import BytesIO

from src.dtos.database.beats import BeatsResponseDTO, CreateBeatRequestDTO, UpdateBeatRequestDTO, BeatResponseDTO
from src.enums.type import Type
from src.exceptions.services import NoRightsException, NotFoundException
from src.repositories import DatabaseRepositories, Repositories
from src.repositories.database.beats.base import BaseBeatsRepository
from src.repositories.database.beats.postgres import init_postgres_repository
from src.repositories.media.base import BaseMediaRepository
from src.repositories.media.s3 import init_s3_repository
from src.services.base import BaseService


@dataclass
class BeatsDatabaseRepositories(DatabaseRepositories):
    beats: BaseBeatsRepository


@dataclass
class BeatsRepositories(Repositories):
    database: BeatsDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class BeatsService(BaseService):
    repositories: BeatsRepositories

    async def get_user_beats(self, user_id: int) -> BeatsResponseDTO:
        return await self.repositories.database.beats.get_user_beats(user_id=user_id)

    async def get_all_beats(self) -> BeatsResponseDTO:
        return await self.repositories.database.beats.all_beats()

    async def get_beat_by_id(self, beat_id: int) -> BeatResponseDTO:
        beat = await self.repositories.database.beats.get_beat_by_id(beat_id=beat_id)

        if not beat:
            raise NotFoundException("beat not found")

        return beat

    async def add_beat(
        self,
        file_stream: BytesIO,
        user_id: int,
        prod_by: str,
        file_info: str,
        description: str = "Description",
        co_prod: str | None = None,
    ) -> int:

        file_url = await self.repositories.media.upload_file("AUDIOFILES", file_info, file_stream)

        beat = CreateBeatRequestDTO(
            title="Title",
            description=description,
            file_url=file_url,
            prod_by=prod_by,
            co_prod=co_prod,
            user_id=user_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        return await self.repositories.database.beats.create_beat(beat=beat)

    async def update_pic_beats(
        self,
        beat_id: int,
        user_id: int,
        file_info: str,
        file_stream: BytesIO
    ) -> int:

        beat = await self.repositories.database.beats.get_beat_by_id(beat_id=beat_id)

        if not beat:
            raise NotFoundException()

        if beat.user_id != user_id:
            raise NoRightsException()

        file_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)
        updated_beat = UpdateBeatRequestDTO(picture_url=file_url)
        return await self.repositories.database.beats.update_beat(beat=updated_beat)

    async def release_beat(
        self,
        beat_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None,
        co_prod: str | None = None,
        prod_by: str | None = None
    ) -> int:
        beat = await self.repositories.database.beats.get_beat_by_id(beat_id=beat_id)

        if not beat:
            raise NotFoundException()

        if beat.user_id != user_id:
            raise NoRightsException()

        updated_beat = UpdateBeatRequestDTO(
            title=title,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            type=Type.beat,
            user_id=user_id
        )

        return await self.repositories.database.beats.update_beat(beat=updated_beat)

    async def update_beat(
        self,
        beat_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None,
        co_prod: str | None = None,
        prod_by: str | None = None
    ) -> int:
        beat = await self.repositories.database.beats.get_beat_by_id(beat_id=beat_id)

        if not beat:
            raise NotFoundException()

        if beat.user_id != user_id:
            raise NoRightsException()

        updated_beat = UpdateBeatRequestDTO(
            title=title,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            type=Type.beat,
            user_id=user_id
        )

        return await self.repositories.database.beats.update_beat(beat=updated_beat)

    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        beat = await self.repositories.database.beats.get_beat_by_id(beat_id=beat_id)

        if not beat:
            raise NotFoundException()

        if beat.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.beats.delete_beat(beat_id=beat_id, user_id=user_id)


def get_beats_service() -> BeatsService:
    return BeatsService(repositories=BeatsRepositories(
        database=BeatsDatabaseRepositories(beats=init_postgres_repository()),
        media=init_s3_repository()
    ))
