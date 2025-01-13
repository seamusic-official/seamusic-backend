from datetime import datetime
from typing import Generic, TypeVar

from src.domain.social.notifications.dtos import BaseRequestDTO, BaseResponseDTO
from src.infrastructure.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")


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


class NotificationItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None

    created_at: datetime


class MyNotificationsResponseDTO(BaseResponseDTO):
    notifications: list[NotificationItemResponseDTO]


class CreateNotificationRequestDTO(BaseRequestDTO):
    title: str
    description: str | None

    created_at: datetime


class CreateNotificationResponseDTO(BaseResponseDTO):
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
