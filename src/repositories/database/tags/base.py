from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.tags import AddTagRequestDTO, TagsResponseDTO, AddTagsRequestDTO


@dataclass
class BaseTagsRepository(ABC):
    @abstractmethod
    async def add_tag(self, tag: AddTagRequestDTO) -> int:
        ...

    @abstractmethod
    async def add_tags(self, tags: AddTagsRequestDTO) -> None:
        ...

    @abstractmethod
    async def get_listener_tags(self, user_id: int) -> TagsResponseDTO:
        ...

    @abstractmethod
    async def get_producer_tags(self, producer_id: int) -> TagsResponseDTO:
        ...

    @abstractmethod
    async def get_artist_tags(self, artist_id: int) -> TagsResponseDTO:
        ...
