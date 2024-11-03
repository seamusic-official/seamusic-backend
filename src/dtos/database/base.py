from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

from src.utils.pages import get_page, get_has_next, get_has_previous

ItemType = TypeVar("ItemType")


class BaseDTO(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)


class BaseRequestDTO(BaseDTO):
    pass


class BaseResponseDTO(BaseDTO):
    pass


class ItemsRequestDTO(BaseRequestDTO):
    offset: int = 0
    limit: int = 10


class ItemsResponseDTO(BaseModel, Generic[ItemType]):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    items: list[ItemType]


def get_items_response(  # type: ignore[no-untyped-def]
    offset: int,
    limit: int,
    total: int,
    items: list[ItemType],
    response_dto: type[ItemsResponseDTO]
):
    return response_dto(
        total=total,
        page=get_page(start=offset, size=limit),
        has_next=get_has_next(total=total, start=offset, size=limit),
        has_previous=get_has_previous(start=offset, size=limit),
        size=limit,
        items=items,
    )
