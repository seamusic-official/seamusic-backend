import datetime

from pydantic import BaseModel

from src.enums.type import Type
from src.schemas.base import DetailMixin


class Album(BaseModel):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_available: bool
    title: str
    picture_url: str | None = None
    description: str
    co_prod: str | None = None
    type: Type = Type.album


class SMyAlbumsResponse(BaseModel):
    albums: list[Album]


class SAllAlbumsResponse(BaseModel):
    albums: list[Album]


class SAlbumResponse(BaseModel):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_available: bool
    title: str
    picture_url: str
    description: str
    co_prod: str
    type: Type = Type.album


class SAddAlbumResponse(BaseModel):
    id: int


class SUpdateAlbumPictureResponse(BaseModel):
    id: int


class SReleaseAlbumsRequest(BaseModel):
    title: str
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SReleaseAlbumsResponse(BaseModel):
    id: int


class SUpdateAlbumRequest(BaseModel):
    title: str
    description: str
    co_prod: str
    prod_by: str
    type: str = "album"


class SUpdateAlbumResponse(BaseModel):
    id: int


class SDeleteAlbumResponse(BaseModel, DetailMixin):
    detail: str = "Album was deleted."
