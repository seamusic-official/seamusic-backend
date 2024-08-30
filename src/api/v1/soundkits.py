from fastapi import UploadFile, File, APIRouter, Depends, status

from src.dtos.database.soundkits import UpdateSoundkitRequestDTO
from src.schemas.auth import User
from src.schemas.soundkits import (
    Soundkit,
    SSoundkitResponse,
    SUpdateSoundkitRequest,
    SSoundkitDeleteResponse,
    SSoundkitsResponse, SCreateSoundkitResponse, SUpdateSoundkitResponse,
)
from src.services.soundkits import SoundkitsService, get_soundkits_service
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream


soundkits = APIRouter(prefix="/soundkits", tags=["Soundkits"])


@soundkits.get(
    path="/my",
    summary="soundkits by current user",
    status_code=status.HTTP_200_OK,
    response_model=SSoundkitsResponse,
)
async def get_user_soundkits(
    user: User = Depends(get_current_user),
    service: SoundkitsService = Depends(get_soundkits_service),
) -> SSoundkitsResponse:

    response = await service.get_user_soundkits(user_id=user.id)

    soundkits_ = list(map(
        lambda soundkit: Soundkit(
            id=soundkit.id,
            title=soundkit.title,
            picture=soundkit.picture_url,
            description=soundkit.description,
            file_path=soundkit.file_path,
            co_prod=soundkit.co_prod,
            prod_by=soundkit.prod_by,
            playlist_id=soundkit.playlist_id,
            user_id=soundkit.user_id,
            beat_pack_id=soundkit.beat_pack_id,
        ),
        response.soundkits
    ))

    return SSoundkitsResponse(soundkits=soundkits_)


@soundkits.get(
    path="/",
    summary="Get all soundkits",
    status_code=status.HTTP_200_OK,
    response_model=SSoundkitsResponse,
)
async def all_soundkits(service: SoundkitsService = Depends(get_soundkits_service)) -> SSoundkitsResponse:

    response = await service.get_all_soundkits()

    soundkits_ = list(map(
        lambda soundkit: Soundkit(
            id=soundkit.id,
            title=soundkit.title,
            picture=soundkit.picture_url,
            description=soundkit.description,
            file_path=soundkit.file_path,
            co_prod=soundkit.co_prod,
            prod_by=soundkit.prod_by,
            playlist_id=soundkit.playlist_id,
            user_id=soundkit.user_id,
            beat_pack_id=soundkit.beat_pack_id,
        ),
        response.soundkits
    ))

    return SSoundkitsResponse(soundkits=soundkits_)


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
