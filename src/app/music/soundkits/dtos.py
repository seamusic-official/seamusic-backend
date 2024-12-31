from datetime import datetime, date
from typing import Generic, TypeVar

from src.domain.music.soundkits.dtos import BaseDTO, BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")


class BeatDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class ProducerDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int


class ItemsRequestDTO(BaseRequestDTO):
    offset: int = 0
    limit: int = 10


class ItemsResponseDTO(BaseResponseDTO, Generic[ItemType]):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


class SoundkitResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    producers: list[ProducerDTO]
    beats: list[BeatDTO]
    tags: list[str]


class SoundkitItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    file_url: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime


class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list[SoundkitItemResponseDTO]


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    description: str | None
    picture_url: str | None
    file_url: str

    created_at: date
    updated_at: datetime

    tags: list[str]


class CreateSoundkitResponseDTO(BaseResponseDTO):
    id: int


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None

    updated_at: datetime

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    producers_ids: list[int] | None = None
    beats_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateSoundkitResponseDTO(BaseResponseDTO):
    id: int


def get_items_response(  # type: ignore[no-untyped-def]
    offset: int,
    limit: int,
    total: int,
    items: list[ItemType],
    response_dto: type[ItemsResponseDTO]
):
    return response_dto(
        total=total,
        page=get_page(start=offset, size=limit),
        has_next=get_has_next(total=total, start=offset, size=limit),
        has_previous=get_has_previous(start=offset, size=limit),
        size=limit,
        items=items,
    )
