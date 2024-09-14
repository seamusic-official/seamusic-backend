from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from src.dtos.database.base import BaseRequestDTO
from src.enums.type import Type
from src.schemas.base import DetailMixin, ItemsResponse


class Beat(BaseModel):
    id: int
    title: str
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    co_prod: str | None = None
    prod_by: str | None = None
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime
    type: Literal[Type.beat] = Type.beat


class SCreateBeatRequest(BaseRequestDTO):
    title: str
    description: str | None = None
    co_prod: str | None = None


class SBeatResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    picture_url: str | None = None
    file_url: str
    co_prod: str | None = None
    prod_by: str | None = None
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime
    type: Literal[Type.beat] = Type.beat


class SBeatsResponse(ItemsResponse[SBeatResponse]):
    pass


class SMyBeatsResponse(ItemsResponse[SBeatResponse]):
    pass


class SCreateBeatResponse(BaseModel):
    id: int


class SUpdateBeatPictureResponse(BaseModel):
    id: int


class SBeatReleaseRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    co_prod: str | None = None
    prod_by: str | None = None


class SBeatReleaseResponse(BaseModel):
    id: int


class SBeatUpdateRequest(BaseModel):
    title: str | None
    description: str | None
    picture_url: str | None
    co_prod: str | None
    prod_by: str | None


class SBeatUpdateResponse(BaseModel):
    id: int


class SDeleteBeatResponse(BaseModel, DetailMixin):
    detail: str = "Beat deleted"
