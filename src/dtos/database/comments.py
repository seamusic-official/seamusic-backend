from datetime import datetime

from pydantic import EmailStr

from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO


class Author(BaseDTO):
    id: int
    username: str
    picture_url: str
    email: EmailStr


class CommentDTO(BaseDTO):
    id: int
    comment: str
    comment_creator_id: int
    beat_id: int | None = None
    beat_pack_id: int | None = None
    soundkit_id: int | None = None
    created_at: datetime
    updated_at: datetime
    comment_author: Author


class CommentResponseDTO(BaseResponseDTO):
    id: int
    comment: str
    comment_creator_id: int
    beat_id: int | None = None
    beat_pack_id: int | None = None
    soundkit_id: int | None = None
    created_at: datetime
    updated_at: datetime
    comment_author: Author


class CreateCommentRequestDTO(BaseRequestDTO):
    comment: str
    comment_creator_id: int
    beat_id: int | None = None
    beat_pack_id: int | None = None
    soundkit_id: int | None = None
    updated_at: datetime
    comment_author: Author


class UpdateCommentRequestDTO(BaseRequestDTO):
    id: int
    comment: str
    comment_creator_id: int
    beat_id: int | None = None
    beat_pack_id: int | None = None
    soundkit_id: int | None = None
    updated_at: datetime
    comment_author: Author
