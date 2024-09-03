from pydantic import BaseModel


class Tag(BaseModel):
    name: str


class SAddTagRequest(BaseModel):
    name: str


class SAddTagResponse(BaseModel):
    id: int


class SMyListenerTagsResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[Tag]


class SMyProducerTagsResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[Tag]


class SMyArtistTagsResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[Tag]
