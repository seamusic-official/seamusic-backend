from fastapi import UploadFile, File, APIRouter, Depends, status

from src.schemas.auth import User
from src.schemas.beats import (
    Beat,
    SBeatResponse,
    SDeleteBeatResponse,
    SMyBeatsResponse,
    SBeatsResponse,
    SCreateBeatResponse,
    SUpdateBeatPictureResponse,
    SBeatReleaseRequest,
    SBeatReleaseResponse,
)
from src.schemas.beats import SBeatUpdateRequest, SBeatUpdateResponse
from src.services.beats import BeatsService, get_beats_service
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream


beats = APIRouter(prefix="/beats", tags=["Beats"])


@beats.get(
    path="/my",
    summary="Beats by current user",
    status_code=status.HTTP_200_OK,
    response_model=SMyBeatsResponse,
    responses={status.HTTP_200_OK: {"model": SMyBeatsResponse}},
)
async def get_user_beats(
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SMyBeatsResponse:

    response = await service.get_user_beats(user_id=user.id)

    beats_ = list(map(
        lambda beat: Beat(
            id=beat.id,
            title=beat.title,
            description=beat.description,
            picture_url=beat.picture_url,
            file_url=beat.file_url,
            co_prod=beat.co_prod,
            prod_by=beat.co_prod,
            user_id=beat.user_id,
            is_available=beat.is_available,
            created_at=beat.created_at,
            updated_at=beat.updated_at,
        ),
        response.beats
    ))
    return SMyBeatsResponse(beats=beats_)


@beats.get(
    path="/",
    summary="Get all beats",
    response_model=SBeatsResponse,
    responses={status.HTTP_200_OK: {"model": SBeatsResponse}},
)
async def all_beats(service: BeatsService = Depends(get_beats_service)) -> SBeatsResponse:

    response = await service.get_all_beats()

    beats_ = list(map(
        lambda beat: Beat(
            id=beat.id,
            title=beat.title,
            description=beat.description,
            picture_url=beat.picture_url,
            file_url=beat.file_url,
            co_prod=beat.co_prod,
            prod_by=beat.co_prod,
            user_id=beat.user_id,
            is_available=beat.is_available,
            created_at=beat.created_at,
            updated_at=beat.updated_at,
        ),
        response.beats
    ))

    return SBeatsResponse(beats=beats_)


@beats.get(
    path="/{beat_id}",
    summary="Get one beat by id",
    response_model=SBeatResponse,
    responses={status.HTTP_200_OK: {"model": SBeatResponse}},
)
async def get_one_beat(
    beat_id: int,
    service: BeatsService = Depends(get_beats_service)
) -> SBeatResponse:

    beat = await service.get_beat_by_id(beat_id=beat_id)
    return SBeatResponse(
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
        updated_at=beat.updated_at
    )


@beats.post(
    path="/",
    summary="Init a beat with file",
    response_model=SCreateBeatResponse,
    responses={status.HTTP_200_OK: {"model": SCreateBeatResponse}},
)
async def add_beats(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SCreateBeatResponse:

    file_info = unique_filename(file)
    file_stream = await get_file_stream(file)

    beat_id = await service.add_beat(
        file_stream=file_stream,
        user_id=user.id,
        prod_by=user.username,
        co_prod=None,
        file_info=file_info,
    )

    return SCreateBeatResponse(id=beat_id)


@beats.put(
    path="/{beat_id}/picture",
    summary="Update a picture for one beat by id",
    response_model=SUpdateBeatPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateBeatPictureResponse}},
)
async def update_pic_beats(
    beat_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SUpdateBeatPictureResponse:

    beat_id = await service.update_pic_beats(
        beat_id=beat_id,
        user_id=user.id,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file)
    )

    return SUpdateBeatPictureResponse(id=beat_id)


@beats.post(
    path="/{beat_id}/release",
    summary="Release one beat by id",
    response_model=SBeatReleaseResponse,
    responses={status.HTTP_200_OK: {"model": SBeatReleaseResponse}},
)
async def release_beats(
    beat_id: int,
    data: SBeatReleaseRequest,
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SBeatReleaseResponse:

    beat_id = await service.release_beat(
        beat_id=beat_id,
        user_id=user.id,
        title=data.title,
        description=data.description,
        co_prod=data.co_prod,
        prod_by=data.co_prod
    )

    return SBeatReleaseResponse(id=beat_id)


@beats.put(
    path="/{beat_id}",
    summary="Edit beat by id",
    response_model=SBeatUpdateResponse,
    responses={status.HTTP_200_OK: {"model": SBeatUpdateResponse}},
)
async def update_beats(
    beat_id: int,
    data: SBeatUpdateRequest,
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SBeatUpdateResponse:

    beat_id = await service.update_beat(
        beat_id=beat_id,
        user_id=user.id,
        title=data.title,
        description=data.description,
        co_prod=data.co_prod,
        prod_by=data.prod_by
    )

    return SBeatUpdateResponse(id=beat_id)


@beats.delete(
    path="/{beat_id}",
    summary="delete beat by id",
    response_model=SDeleteBeatResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteBeatResponse}},
)
async def delete_beats(
    beat_id: int,
    user: User = Depends(get_current_user),
    service: BeatsService = Depends(get_beats_service)
) -> SDeleteBeatResponse:

    await service.delete_beat(beat_id=beat_id, user_id=user.id)

    return SDeleteBeatResponse()
