from dataclasses import dataclass
from typing import TypeVar, Generic

from pydantic import BaseModel

from src.utils.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")


@dataclass
class DetailMixin:
    detail: str | None = None


class Page(BaseModel):
    start: int = 1
    size: int = 10


class ItemsResponse(BaseModel, Generic[ItemType]):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


def get_items_response(  # type: ignore[no-untyped-def]
    start: int,
    size: int,
    total: int,
    items: list[ItemType],
    response_model: type[ItemsResponse]
):
    return response_model(
        total=total,
        page=get_page(start=start, size=size),
        has_next=get_has_next(total=total, start=start, size=size),
        has_previous=get_has_previous(start=start, size=size),
        size=size,
        items=items,
    )
