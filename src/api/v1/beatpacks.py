from fastapi import APIRouter, Depends, status

from src.dtos.database.beats import Beat as _Beat
from src.enums.type import Type
from src.schemas.auth import User
from src.schemas.base import Page
from src.schemas.beatpacks import (
    SBeatpackResponse,
    SCreateBeatpackRequest,
    SEditBeatpackResponse,
    SDeleteBeatpackResponse,
    SMyBeatpacksResponse,
    SBeatpacksResponse,
    SCreateBeatpackResponse,
    SEditBeatpackRequest,
)
from src.schemas.beats import Beat, SBeatResponse
from src.services.beatpacks import BeatpackService, get_beatpack_service
from src.utils.auth import get_current_user

beatpacks = APIRouter(prefix="/beatpacks", tags=["Beatpacks"])


@beatpacks.post(
    path="/my",
    summary="Get beat packs by current user",
    response_model=SMyBeatpacksResponse,
    responses={status.HTTP_200_OK: {"model": SMyBeatpacksResponse}},
)
async def get_my_beatpacks(
    page: Page,
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service),
) -> SMyBeatpacksResponse:

    response = await service.get_user_beatpacks(user_id=user.id, start=page.start, size=page.size)

    beatpacks_ = list(map(
        lambda beatpack: SBeatpacksResponse(
            title=beatpack.title,
            description=beatpack.description,
            user_id=beatpack.user_id,
            users=list(map(
                lambda user_: User(
                    id=user_.id,
                    username=user_.username,
                    email=user_.email,
                    picture_url=user_.picture_url,
                    birthday=user_.birthday,
                ),
                beatpack.users
            )),
            beats=list(map(
                lambda beat: SBeatResponse(
                    id=beat.id,
                    title=beat.title,
                    description=beat.description,
                    picture_url=beat.picture_url,
                    file_url=beat.file_url,
                    co_prod=beat.co_prod,
                    prod_by=beat.prod_by,
                    user_id=beat.user_id,
                    is_available=beat.is_available,
                    created_at=beat.created_at,
                    updated_at=beat.updated_at,
                ),
                beatpack.beats
            )),
        ),
        response.beatpacks
    ))

    total = await service.get_user_beatpacks_count(user_id=user.id)

    return SMyBeatpacksResponse(
        total=total,
        page=page.start // page.size if page.start % page.size == 0 else page.start // page.size + 1,
        has_next=page.start + page.size < total,
        has_previous=page.start - page.size >= 0,
        size=page.size,
        items=beatpacks_,
    )


@beatpacks.get(
    path="/all",
    summary="Get all beat packs",
    response_model=SBeatpacksResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpacksResponse}},
)
async def all_beatpacks(
    page: Page,
    service: BeatpackService = Depends(get_beatpack_service),
) -> SBeatpacksResponse:

    response = await service.get_all_beatpacks(start=page.start, size=page.size)

    beatpacks_ = list(map(
        lambda beatpack: SBeatpackResponse(
            title=beatpack.title,
            description=beatpack.description,
            user_id=beatpack.user_id,
            users=list(map(
                lambda user_: User(
                    id=user_.id,
                    username=user_.username,
                    email=user_.email,
                    picture_url=user_.picture_url,
                    birthday=user_.birthday,
                ),
                beatpack.users
            )),
            beats=list(map(
                lambda beat: SBeatResponse(
                    id=beat.id,
                    title=beat.title,
                    description=beat.description,
                    picture_url=beat.picture_url,
                    file_url=beat.file_url,
                    co_prod=beat.co_prod,
                    prod_by=beat.prod_by,
                    user_id=beat.user_id,
                    is_available=beat.is_available,
                    created_at=beat.created_at,
                    updated_at=beat.updated_at,
                ),
                beatpack.beats
            )),
        ),
        response.beatpacks
    ))

    total = await service.get_beatpacks_count()

    return SBeatpacksResponse(
        total=total,
        page=page.start // page.size if page.start % page.size == 0 else page.start // page.size + 1,
        has_next=page.start + page.size < total,
        has_previous=page.start - page.size >= 0,
        size=page.size,
        items=beatpacks_,
    )


@beatpacks.get(
    path="/{beatpack_id}",
    summary="Get one beat pack by id",
    response_model=SBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SBeatpackResponse}},
)
async def get_one(
    beatpack_id: int,
    service: BeatpackService = Depends(get_beatpack_service)
) -> SBeatpackResponse:
    beatpack = await service.get_one_beatpack(beatpack_id=beatpack_id)

    return SBeatpackResponse(
        title=beatpack.title,
        description=beatpack.description,
        user_id=beatpack.user_id,
        users=list(map(
            lambda user_: User(
                id=user_.id,
                username=user_.username,
                email=user_.email,
                picture_url=user_.picture_url,
                birthday=user_.birthday,
            ),
            beatpack.users
        )),
        beats=list(map(
            lambda beat: Beat(
                id=beat.id,
                title=beat.title,
                description=beat.description,
                picture_url=beat.picture_url,
                file_url=beat.file_url,
                co_prod=beat.co_prod,
                prod_by=beat.prod_by,
                user_id=beat.user_id,
                is_available=beat.is_available,
                created_at=beat.created_at,
                updated_at=beat.updated_at,
            ),
            beatpack.beats
        ))
    )


@beatpacks.post(
    path="/new",
    summary="Add a file for new beat",
    response_model=SCreateBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SCreateBeatpackResponse}},
)
async def add_beatpack(
    data: SCreateBeatpackRequest,
    service: BeatpackService = Depends(get_beatpack_service)
) -> SCreateBeatpackResponse:

    beatpack_id: int = await service.add_beatpack(
        title=data.title,
        description=data.description
    )
    return SCreateBeatpackResponse(id=beatpack_id)


@beatpacks.put(
    path="/{beatpack_id}/update",
    summary="Edit beat pack",
    response_model=SEditBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SEditBeatpackResponse}},
)
async def update_beatpacks(
    beatpack_id: int,
    data: SEditBeatpackRequest,
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service)
) -> SEditBeatpackResponse:

    beatpack_id = await service.update_beatpack(
        title=data.title,
        description=data.description,
        beatpack_id=beatpack_id,
        beats=list(map(
            lambda beat: _Beat(
                id=beat.id,
                title=beat.title,
                description=beat.description,
                picture_url=beat.picture_url,
                file_url=beat.file_url,
                co_prod=beat.co_prod,
                prod_by=beat.prod_by,
                user_id=beat.user_id,
                is_available=beat.is_available,
                created_at=beat.created_at,
                updated_at=beat.updated_at,
                type=Type.beat,
            ),
            data.beats
        )),
        user_id=user.id,
    )

    return SEditBeatpackResponse(id=beatpack_id)


@beatpacks.delete(
    path="/{beatpack_id}/delete",
    summary="Delete beat pack",
    response_model=SDeleteBeatpackResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteBeatpackResponse}},
)
async def delete_beatpacks(
    beatpack_id: int,
    user: User = Depends(get_current_user),
    service: BeatpackService = Depends(get_beatpack_service)
) -> SDeleteBeatpackResponse:

    await service.delete_beatpack(beatpack_id=beatpack_id, user_id=user.id)
    return SDeleteBeatpackResponse()
