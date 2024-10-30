from datetime import datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


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

    created_at: datetime = datetime.now()


class CreateNotificationResponseDTO(BaseResponseDTO):
    id: int


class NotificationDTO(BaseDTO):
    id: int
    title: str
    description: str | None

    created_at: datetime
