from pydantic import BaseModel


class Tag(BaseModel):
    name: str


class SAddTagRequest(BaseModel):
    name: str


class SAddTagResponse(BaseModel):
    id: int


class SMyListenerTagsResponse(BaseModel):
    tags: list[Tag]


class SMyProducerTagsResponse(BaseModel):
    tags: list[Tag]


class SMyArtistTagsResponse(BaseModel):
    tags: list[Tag]
