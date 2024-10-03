from dataclasses import dataclass

from src.dtos.database.tags import AddTagRequestDTO, TagsResponseDTO
from src.exceptions import NotFoundException
from src.repositories import Repositories, BaseMediaRepository, DatabaseRepositories
from src.repositories.database.auth import (
    init_artists_repository as init_artists_repository,
    init_producers_repository as init_producers_repository, ArtistsRepository, ProducersRepository
)
from src.repositories.database.tags import init_tags_repository as init_tags_repository, TagsRepository
from src.repositories.media.s3 import init_s3_repository


@dataclass
class TagsDatabaseRepositories(DatabaseRepositories):
    tags: TagsRepository
    artists: ArtistsRepository
    producers: ProducersRepository


@dataclass
class TagsRepositories(Repositories):
    database: TagsDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class TagsService:
    repositories: TagsRepositories

    async def add_tag(self, name: str) -> int:
        tag = AddTagRequestDTO(name=name)
        return await self.repositories.database.tags.add_tag(tag=tag)

    async def get_listener_tags(self, user_id: int, start: int = 1, size: int = 10) -> TagsResponseDTO:
        return await self.repositories.database.tags.get_listener_tags(user_id=user_id, offset=start - 1, limit=size)

    async def get_listener_tags_count(self, user_id: int) -> int:
        return await self.repositories.database.tags.get_listener_tags_count(user_id=user_id)

    async def get_producer_tags(self, user_id: int, start: int = 1, size: int = 10) -> TagsResponseDTO:
        producer_id: int | None = await self.repositories.database.producers.get_producer_id_by_user_id(user_id=user_id)

        if not producer_id:
            raise NotFoundException("Producer profile not found")

        return await self.repositories.database.tags.get_producer_tags(producer_id=producer_id, offset=start - 1, limit=size)

    async def get_producer_tags_count(self, user_id: int) -> int:
        producer_id = await self.repositories.database.producers.get_producer_id_by_user_id(user_id=user_id)

        if not producer_id:
            raise NotFoundException("Producer profile not found")

        return await self.repositories.database.tags.get_producer_tags_count(producer_id=producer_id)

    async def get_artist_tags(self, user_id: int, start: int = 1, size: int = 10) -> TagsResponseDTO:
        artist_id: int | None = await self.repositories.database.artists.get_artist_id_by_user_id(user_id=user_id)

        if not artist_id:
            raise NotFoundException("Artist profile not found")

        return await self.repositories.database.tags.get_artist_tags(artist_id=artist_id, offset=start - 1, limit=size)

    async def get_artist_tags_count(self, user_id: int) -> int:
        artist_id = await self.repositories.database.producers.get_producer_id_by_user_id(user_id=user_id)

        if not artist_id:
            raise NotFoundException("Producer profile not found")

        return await self.repositories.database.tags.get_artist_tags_count(artist_id=artist_id)


def get_tags_repositories() -> TagsRepositories:
    return TagsRepositories(
        database=TagsDatabaseRepositories(
            tags=init_tags_repository(),
            artists=init_artists_repository(),
            producers=init_producers_repository(),
        ),
        media=init_s3_repository()
    )


def get_tags_service() -> TagsService:
    return TagsService(repositories=get_tags_repositories())
