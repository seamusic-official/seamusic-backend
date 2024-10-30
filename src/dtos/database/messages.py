from datetime import datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class MessageResponseDTO(BaseResponseDTO):
    id: int
    text: str

    created_at: datetime
    updated_at: datetime

    chat: "ChatDTO"  # type: ignore[name-defined]  # noqa: F821
    author: "UserDTO"   # type: ignore[name-defined]  # noqa: F821


class MessageItemResponseDTO(BaseResponseDTO):
    id: int
    text: str

    created_at: datetime
    updated_at: datetime

    author: "UserDTO"   # type: ignore[name-defined]  # noqa: F821


class ChatMessagesResponseDTO(BaseResponseDTO):
    messages: list[MessageItemResponseDTO]


class CreateMessageRequestDTO(BaseRequestDTO):
    id: int
    text: str

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    chat_id: int
    author_id: int


class CreateMessageResponseDTO(BaseResponseDTO):
    id: int


class UpdateMessageRequestDTO(BaseRequestDTO):
    id: int
    text: str


class UpdateMessageResponseDTO(BaseResponseDTO):
    id: int


class MessageDTO(BaseDTO):
    id: int
    text: str

    created_at: datetime
    updated_at: datetime

    author: "UserDTO"   # type: ignore[name-defined]  # noqa: F821
