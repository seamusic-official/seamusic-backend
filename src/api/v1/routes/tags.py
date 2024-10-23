from fastapi import APIRouter, Depends, status

from src.api.v1.schemas.auth import User
from src.api.v1.schemas.base import Page, get_items_response
from src.api.v1.schemas.tags import (
    SAddTagResponse,
    SAddTagRequest,
    SMyListenerTagsResponse,
    SMyProducerTagsResponse,
    Tag,
    SMyArtistTagsResponse
)
from src.api.v1.utils.auth import get_current_user
from src.services.tags import TagsService, get_tags_service

tags = APIRouter(prefix="/tags", tags=["All tags"])


@tags.post(
    path="/",
    summary="Add tags",
    response_model=SAddTagResponse,
    responses={status.HTTP_200_OK: {"model": SAddTagResponse}},
)
async def add_tag(
    tag: SAddTagRequest,
    service: TagsService = Depends(get_tags_service),
) -> SAddTagResponse:

    tag_id = await service.add_tag(name=tag.name)
    return SAddTagResponse(id=tag_id)


@tags.get(
    path="/listener/my",
    summary="Get my listener tags",
    response_model=SMyListenerTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyListenerTagsResponse}},
)
async def get_my_listener_tags(
    page: Page = Depends(Page),
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyListenerTagsResponse:

    response = await service.get_listener_tags(user_id=user.id, start=page.start, size=page.size)
    items = list(map(
        lambda tag: Tag(name=tag.title),
        response.tags
    ))
    total = await service.get_listener_tags_count(user_id=user.id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SMyListenerTagsResponse,
    )


@tags.get(
    path="/producer/my",
    summary="Get my producer tags",
    response_model=SMyProducerTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyProducerTagsResponse}},
)
async def get_my_producer_tags(
    page: Page = Depends(Page),
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyProducerTagsResponse:

    response = await service.get_producer_tags(user_id=user.id, start=page.start, size=page.size)
    items = list(map(
        lambda tag: Tag(name=tag.title),
        response.tags
    ))
    total = await service.get_producer_tags_count(user_id=user.id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SMyProducerTagsResponse,
    )


@tags.get(
    path="/artist/my",
    summary="Get my artist tags",
    response_model=SMyArtistTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyArtistTagsResponse}},
)
async def get_my_artist_tags(
    page: Page = Depends(Page),
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyArtistTagsResponse:

    response = await service.get_artist_tags(user_id=user.id, start=page.start, size=page.size)
    items = list(map(
        lambda tag: Tag(name=tag.title),
        response.tags
    ))
    total = await service.get_producer_tags_count(user_id=user.id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SMyArtistTagsResponse,
    )
