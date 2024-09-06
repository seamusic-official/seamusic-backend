from fastapi import APIRouter, Depends, status

from src.schemas.auth import User
from src.schemas.base import Page
from src.schemas.tags import (
    SAddTagResponse,
    SAddTagRequest,
    SMyListenerTagsResponse,
    SMyProducerTagsResponse,
    Tag,
    SMyArtistTagsResponse
)
from src.services.tags import TagsService, get_tags_service
from src.utils.auth import get_current_user

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
    page: Page,
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyListenerTagsResponse:

    response = await service.get_listener_tags(user_id=user.id, start=page.start, size=page.size)
    tags_ = list(map(
        lambda tag: Tag(name=tag.name),
        response.tags
    ))
    total = await service.get_listener_tags_count(user_id=user.id)

    return SMyListenerTagsResponse(
        total=total,
        page=page.start // page.size if page.start % page.size == 0 else page.start // page.size + 1,
        has_next=page.start + page.size < total,
        has_previous=page.start - page.size >= 0,
        size=page.size,
        items=tags_,
    )


@tags.get(
    path="/producer/my",
    summary="Get my producer tags",
    response_model=SMyProducerTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyProducerTagsResponse}},
)
async def get_my_producer_tags(
    page: Page,
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyProducerTagsResponse:

    response = await service.get_producer_tags(user_id=user.id, start=page.start, size=page.size)
    tags_ = list(map(
        lambda tag: Tag(name=tag.name),
        response.tags
    ))
    total = await service.get_producer_tags_count(user_id=user.id)

    return SMyProducerTagsResponse(
        total=total,
        page=page.start // page.size if page.start % page.size == 0 else page.start // page.size + 1,
        has_next=page.start + page.size < total,
        has_previous=page.start - page.size >= 0,
        size=page.size,
        items=tags_,
    )


@tags.get(
    path="/artist/my",
    summary="Get my artist tags",
    response_model=SMyArtistTagsResponse,
    responses={status.HTTP_200_OK: {"model": SMyArtistTagsResponse}},
)
async def get_my_artist_tags(
    page: Page,
    user: User = Depends(get_current_user),
    service: TagsService = Depends(get_tags_service),
) -> SMyArtistTagsResponse:

    response = await service.get_artist_tags(user_id=user.id, start=page.start, size=page.size)
    tags_ = list(map(
        lambda tag: Tag(name=tag.name),
        response.tags
    ))
    total = await service.get_producer_tags_count(user_id=user.id)

    return SMyArtistTagsResponse(
        total=total,
        page=page.start // page.size if page.start % page.size == 0 else page.start // page.size + 1,
        has_next=page.start + page.size < total,
        has_previous=page.start - page.size >= 0,
        size=page.size,
        items=tags_,
    )
