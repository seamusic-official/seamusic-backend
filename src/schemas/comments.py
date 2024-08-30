from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

from src.schemas.base import DetailMixin


class SCommentDeleteResponse(BaseModel, DetailMixin):
    detail: str = "Comment deleted"


class CommentCreate(BaseModel):
    comment: str


class CommentUpdate(BaseModel):
    comment: str


class CommentUpdateResponse(BaseModel, DetailMixin):
    detail: str = "Comment updated"


class GetAuthor(BaseModel):
    id: int
    username: str
    picture_url: str
    email: EmailStr


class CommentResponse(BaseModel):
    id: int
    comment: str
    comment_creator_id: int
    beat_id: int | None = None
    beat_pack_id: int | None = None
    soundkit_id: int | None = None
    created_at: datetime
    updated_at: datetime
    is_available: bool
    comment_author: GetAuthor

    model_config = ConfigDict(from_attributes=True)
