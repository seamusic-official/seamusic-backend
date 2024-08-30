from datetime import datetime

from pydantic import BaseModel

from src.schemas.base import DetailMixin


class Soundkit(BaseModel):
    id: int
    title: str
    picture: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None


class SCreateSoundkitResponse(BaseModel):
    id: int


class SUpdateSoundkitResponse(BaseModel):
    id: int


class SSoundkitsResponse(BaseModel):
    soundkits: list[Soundkit]


class SUpdateSoundkitRequest(BaseModel):
    title: str | None
    picture: str | None
    description: str | None
    co_prod: str | None
    prod_by: str | None


class SSoundkitCreateRequest(BaseModel):
    title: str
    picture: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None


class SSoundkitResponse(BaseModel):
    id: int
    name: str
    co_prod: str
    prod_by: str
    description: str
    picture_url: str
    file_url: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime


class SSoundkitDeleteResponse(BaseModel, DetailMixin):
    detail: str = "Soundkit deleted"
