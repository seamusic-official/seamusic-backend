import datetime
from typing import Literal

from pydantic import BaseModel

from src.enums.type import Type
from src.schemas.base import DetailMixin, ItemsResponse


class SAlbumResponse(BaseModel):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_available: bool
    title: str
    picture_url: str
    description: str
    co_prod: str
    type: Literal[Type.album] = Type.album


class SMyAlbumsResponse(ItemsResponse[SAlbumResponse]):
    pass


class SAllAlbumsResponse(ItemsResponse[SAlbumResponse]):
    pass


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
    type: Literal[Type.album] = Type.album


class SReleaseAlbumsResponse(BaseModel):
    id: int


class SUpdateAlbumRequest(BaseModel):
    title: str
    description: str
    co_prod: str
    prod_by: str
    type: Literal[Type.album] = Type.album


class SUpdateAlbumResponse(BaseModel):
    id: int


class SDeleteAlbumResponse(BaseModel, DetailMixin):
    detail: str = "Album was deleted."
