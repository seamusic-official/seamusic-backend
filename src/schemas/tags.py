from pydantic import BaseModel

from src.schemas.base import ItemsResponse


class Tag(BaseModel):
    name: str


class SAddTagRequest(BaseModel):
    name: str


class SAddTagResponse(BaseModel):
    id: int


class SMyListenerTagsResponse(ItemsResponse[Tag]):
    pass


class SMyProducerTagsResponse(ItemsResponse[Tag]):
    pass


class SMyArtistTagsResponse(ItemsResponse[Tag]):
    pass
