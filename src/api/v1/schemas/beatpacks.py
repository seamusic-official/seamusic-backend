from typing import Literal

from pydantic import BaseModel

from src.api.v1.schemas.auth import SUserResponse
from src.api.v1.schemas.base import DetailMixin, ItemsResponse
from src.api.v1.schemas.beats import SBeatResponse
from src.enums.type import Type


class SBeatpackResponse(BaseModel):
    title: str
    description: str
    user_id: int
    users: list[SUserResponse]
    beats: list[SBeatResponse]
    type: Literal[Type.beatpack] = Type.beatpack


class SBeatpacksResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[SBeatpackResponse]


class SMyBeatpacksResponse(ItemsResponse[SBeatpackResponse]):
    pass


class SCreateBeatpackRequest(BaseModel):
    title: str
    description: str


class SCreateBeatpackResponse(BaseModel):
    id: int


class SEditBeatpackRequest(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None
    beat_ids: list[int] | None = None


class SEditBeatpackResponse(BaseModel):
    id: int


class SDeleteBeatpackResponse(BaseModel, DetailMixin):
    detail: str = "Beatpack deleted"
