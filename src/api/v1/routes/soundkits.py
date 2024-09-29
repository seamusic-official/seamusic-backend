from fastapi import UploadFile, File, APIRouter, Depends, status

from src.api.v1.schemas.auth import User
from src.api.v1.schemas.base import Page, get_items_response
from src.api.v1.schemas.soundkits import (
    SSoundkitResponse,
    SUpdateSoundkitRequest,
    SSoundkitDeleteResponse,
    SAllSoundkitsResponse,
    SCreateSoundkitResponse,
    SUpdateSoundkitResponse,
    SMySoundkitsResponse,
)
from src.api.v1.utils.auth import get_current_user
from src.dtos.database.soundkits import UpdateSoundkitRequestDTO
from src.services.soundkits import SoundkitsService, get_soundkits_service
from src.utils.files import unique_filename, get_file_stream

soundkits = APIRouter(prefix="/soundkits", tags=["Soundkits"])


@soundkits.get(
    path="/my",
    summary="soundkits by current user",
    status_code=status.HTTP_200_OK,
    response_model=SMySoundkitsResponse,
)
async def get_my_soundkits(
    page: Page = Depends(Page),
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SMySoundkitsResponse:

    response = await service.get_user_soundkits(user_id=user.id, start=page.start, size=page.size)

    items = list(map(
        lambda soundkit: SSoundkitResponse(
            id=soundkit.id,
            name=soundkit.name,
            picture_url=soundkit.picture_url,
            description=soundkit.description,
            file_url=soundkit.file_url,
            co_prod=soundkit.co_prod,
            prod_by=soundkit.prod_by,
            user_id=soundkit.user_id,
            created_at=soundkit.created_at,
            updated_at=soundkit.updated_at,
            is_available=soundkit.is_available,
        ),
        response.soundkits
    ))

    total = await service.get_user_soundkits_count(user_id=user.id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SMySoundkitsResponse,
    )


@soundkits.get(
    path="/",
    summary="Get all soundkits",
    status_code=status.HTTP_200_OK,
    response_model=SAllSoundkitsResponse,
)
async def all_soundkits(
    page: Page = Depends(Page),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SAllSoundkitsResponse:

    response = await service.get_all_soundkits(start=page.start, size=page.size)

    items = list(map(
        lambda soundkit: SSoundkitResponse(
            id=soundkit.id,
            name=soundkit.name,
            picture_url=soundkit.picture_url,
            description=soundkit.description,
            file_url=soundkit.file_url,
            co_prod=soundkit.co_prod,
            prod_by=soundkit.prod_by,
            user_id=soundkit.user_id,
            created_at=soundkit.created_at,
            updated_at=soundkit.updated_at,
            is_available=soundkit.is_available,
        ),
        response.soundkits
    ))

    total = await service.get_all_soundkits_count()

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SAllSoundkitsResponse,
    )


@soundkits.get(
    path="/{soundkit_id}",
    summary="Get one soundkit by id",
    response_model=SSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitResponse}},
)
async def get_one_soundkit(
    soundkit_id: int,
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SSoundkitResponse:

    soundkit = await service.get_soundkit_by_id(soundkit_id=soundkit_id)

    return SSoundkitResponse(
        id=soundkit.id,
        name=soundkit.name,
        picture_url=soundkit.picture_url,
        description=soundkit.description,
        file_url=soundkit.file_url,
        co_prod=soundkit.co_prod,
        prod_by=soundkit.prod_by,
        user_id=soundkit.user_id,
        is_available=soundkit.is_available,
        created_at=soundkit.created_at,
        updated_at=soundkit.updated_at,
    )


@soundkits.post(
    path="/",
    summary="Init a soundkit with file",
    response_model=SCreateSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SCreateSoundkitResponse}},
)
async def add_soundkit(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SCreateSoundkitResponse:

    soundkit_id = await service.add_soundkit(
        user_id=user.id,
        prod_by=user.username,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file),
    )

    return SCreateSoundkitResponse(id=soundkit_id)


@soundkits.post(
    path="/{soundkits_id}/picture",
    summary="Update a picture for one soundkit by id",
    response_model=SUpdateSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateSoundkitResponse}},
)
async def update_pic_soundkits(
    soundkit_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SUpdateSoundkitResponse:

    soundkit_id = await service.update_soundkit_picture(
        soundkit_id=soundkit_id,
        file_stream=await get_file_stream(file),
        file_info=unique_filename(file),
        user_id=user.id,
    )

    return SUpdateSoundkitResponse(id=soundkit_id)


@soundkits.post(
    path="/{soundkit_id}/release",
    summary="Release one soundkit by id",
    response_model=SUpdateSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateSoundkitResponse}},
)
async def release_soundkits(
    soundkit_id: int,
    data: SUpdateSoundkitRequest,
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SUpdateSoundkitResponse:

    soundkit_id = await service.update_soundkit(
        soundkit_id=soundkit_id,
        user_id=user.id,
        data=UpdateSoundkitRequestDTO(
            title=data.title,
            description=data.description,
            co_prod=data.co_prod,
            prod_by=data.prod_by,
            user_id=user.id,
        ),
    )

    return SUpdateSoundkitResponse(id=soundkit_id)


@soundkits.put(
    path="/{soundkit_id}",
    summary="Edit soundkit",
    response_model=SUpdateSoundkitResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateSoundkitResponse}},
)
async def update_soundkits(
    soundkit_id: int,
    data: SUpdateSoundkitRequest,
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SUpdateSoundkitResponse:

    soundkit_id = await service.update_soundkit(
        soundkit_id=soundkit_id,
        user_id=user.id,
        data=UpdateSoundkitRequestDTO(
            title=data.title,
            description=data.description,
            co_prod=data.co_prod,
            prod_by=data.prod_by,
            user_id=user.id,
        ),
    )

    return SUpdateSoundkitResponse(id=soundkit_id)


@soundkits.delete(
    path="/{soundkit_id}",
    summary="Delete soundkit",
    response_model=SSoundkitDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SSoundkitDeleteResponse}},
)
async def delete_soundkits(
    soundkit_id: int,
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service)
) -> SSoundkitDeleteResponse:

    await service.delete_soundkits(soundkit_id=soundkit_id, user_id=user.id)
    return SSoundkitDeleteResponse()
