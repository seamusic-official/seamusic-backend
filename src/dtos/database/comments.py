from datetime import datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class CommentResponseDTO(BaseResponseDTO):
    id: int
    text: str
    author: "UserDTO"  # type: ignore[name-defined]  # noqa: F821

    created_at: datetime
    updated_at: datetime


class CreateCommentRequestDTO(BaseRequestDTO):
    text: str
    author_id: int

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CreateCommentResponseDTO(BaseResponseDTO):
    id: int


class UpdateCommentRequestDTO(BaseRequestDTO):
    text: str
    updated_at: datetime = datetime.now()


class UpdateCommentResponseDTO(BaseResponseDTO):
    id: int


class CommentDTO(BaseDTO):
    id: int
    text: str
    author: "UserDTO"  # type: ignore[name-defined]  # noqa: F821

    created_at: datetime
    updated_at: datetime
