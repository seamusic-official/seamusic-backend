from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class ChatResponseDTO(BaseResponseDTO):
    id: int
    messages: list["MessageDTO"]  # type: ignore[name-defined]  # noqa: F821
    participants: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821


class ChatItemResponseDTO(BaseResponseDTO):
    id: int
    participants: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821


class MyChatsResponseDTO(BaseResponseDTO):
    chats: list[ChatItemResponseDTO]


class CreateChatRequestDTO(BaseRequestDTO):
    participants_ids: list[int]


class CreateChatResponseDTO(BaseResponseDTO):
    id: int


class ChatDTO(BaseDTO):
    id: int
    participants: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
