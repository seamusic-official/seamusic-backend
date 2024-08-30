from pydantic import BaseModel

from src.schemas.auth import User
from src.schemas.base import DetailMixin
from src.schemas.beats import Beat


class Beatpack(BaseModel):
    title: str
    description: str
    user_id: int
    users: list[User]
    beats: list[Beat]


class SBeatpackResponse(BaseModel):
    title: str
    description: str
    user_id: int
    users: list[User]
    beats: list[Beat]


class SBeatpacksResponse(BaseModel):
    beatpacks: list[Beatpack]


class SMyBeatpacksResponse(BaseModel):
    beatpacks: list[Beatpack]


class SCreateBeatpackRequest(BaseModel):
    title: str
    description: str


class SCreateBeatpackResponse(BaseModel):
    id: int


class SEditBeatpackRequest(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None
    beats: list[Beat]


class SEditBeatpackResponse(BaseModel):
    id: int


class SDeleteBeatpackResponse(BaseModel, DetailMixin):
    detail: str = "Beatpack deleted"
