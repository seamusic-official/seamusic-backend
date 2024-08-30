from fastapi import UploadFile, File, APIRouter, Depends, status

from src.schemas.auth import User
from src.schemas.tracks import (
    Track,
    STrackResponse,
    SMyTracksResponse,
    SAddTracksResponse,
    SUpdateTrackPictureResponse,
    SReleaseTrackRequest,
    SReleaseTrackResponse,
    SUpdateTrackResponse,
    SUpdateTrackRequest,
    SDeleteTrackResponse, SAllTracksResponse,
)
from src.services.tracks import TracksService, get_tracks_service
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream


tracks = APIRouter(prefix="/tracks", tags=["Tracks"])


@tracks.get(
    path="/my",
    summary="tracks by current user",
    response_model=SMyTracksResponse,
    responses={status.HTTP_200_OK: {"model": SMyTracksResponse}},
)
async def get_my_tracks(
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service)
) -> SMyTracksResponse:

    response = await service.get_user_tracks(user_id=user.id)

    return SMyTracksResponse(tracks=list(map(
        lambda track: Track(
            id=track.id,
            name=track.name,
            prod_by=track.prod_by,
            description=track.description,
            co_prod=track.co_prod,
            type=track.type,
            user_id=track.user_id,
            is_available=track.is_available,
            file_url=track.file_url,
            picture_url=track.picture_url,
            created_at=track.created_at,
            updated_at=track.updated_at,
        ),
        response.tracks
    )))


@tracks.get(
    path="/all",
    summary="Get all tracks",
    response_model=SMyTracksResponse,
    responses={status.HTTP_200_OK: {"model": SMyTracksResponse}},
)
async def all_tracks(
    service: TracksService = Depends(get_tracks_service)
) -> SAllTracksResponse:

    response = await service.all_tracks()

    return SAllTracksResponse(tracks=list(map(
        lambda track: Track(
            id=track.id,
            name=track.name,
            prod_by=track.prod_by,
            description=track.description,
            co_prod=track.co_prod,
            type=track.type,
            user_id=track.user_id,
            is_available=track.is_available,
            file_url=track.file_url,
            picture_url=track.picture_url,
            created_at=track.created_at,
            updated_at=track.updated_at,
        ),
        response.tracks
    )))


@tracks.get(
    path="/{track_id}",
    summary="Get one track by id",
    response_model=STrackResponse,
    responses={status.HTTP_200_OK: {"model": STrackResponse}},
)
async def get_one_track(
    track_id: int,
    service: TracksService = Depends(get_tracks_service),
) -> STrackResponse:

    track = await service.get_one_track(track_id=track_id)

    return STrackResponse(
        id=track.id,
        name=track.name,
        prod_by=track.prod_by,
        description=track.description,
        co_prod=track.co_prod,
        type=track.type,
        user_id=track.user_id,
        is_available=track.is_available,
        file_url=track.file_url,
        picture_url=track.picture_url,
        created_at=track.created_at,
        updated_at=track.updated_at,
    )


@tracks.post(
    path="/new",
    summary="Init a track with file",
    response_model=SAddTracksResponse,
    responses={status.HTTP_200_OK: {"model": SAddTracksResponse}},
)
async def add_track(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service)
) -> SAddTracksResponse:

    track_id = await service.add_track(
        username=user.username,
        track_title="Title",
        description="Description",
        user_id=user.id,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file)
    )

    return SAddTracksResponse(id=track_id)


@tracks.post(
    path="/{tracks_id}/picture",
    summary="Update a picture for one track by id",
    response_model=SUpdateTrackPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateTrackPictureResponse}},
)
async def update_pic_tracks(
    track_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service),
) -> SUpdateTrackPictureResponse:

    track_id = await service.update_pic_tracks(
        track_id=track_id,
        user_id=user.id,
        file_stream=await get_file_stream(file),
        file_info=unique_filename(file)
    )

    return SUpdateTrackPictureResponse(id=track_id)


@tracks.post(
    path="/{track_id}/release",
    summary="Release one track by id",
    response_model=SReleaseTrackResponse,
    responses={status.HTTP_200_OK: {"model": SReleaseTrackResponse}},
)
async def release_track(
    track_id: int,
    data: SReleaseTrackRequest,
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service),
) -> SReleaseTrackResponse:

    track_id = await service.release_track(
        track_id=track_id,
        user_id=user.id,
        title=data.title,
        picture_url=data.picture,
        description=data.description,
        co_prod=data.co_prod,
        prod_by=data.prod_by,
        playlist_id=data.playlist_id,
        track_pack_id=data.Track_pack_id,
    )

    return SReleaseTrackResponse(id=track_id)


@tracks.put(
    path="/{track_id}/update",
    summary="Edit track",
    response_model=SUpdateTrackResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateTrackResponse}},
)
async def update_track(
    track_id: int,
    data: SUpdateTrackRequest,
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service),
) -> SUpdateTrackResponse:

    track_id = await service.update_track(
        track_id=track_id,
        user_id=user.id,
        title=data.title,
        description=data.description,
        prod_by=data.prod_by,
        picture_url=data.picture_url,
        file_url=data.file_path,
        co_prod=data.co_prod,
        playlist_id=data.playlist_id,
        track_pack_id=data.track_pack_id,
    )

    return SUpdateTrackResponse(id=track_id)


@tracks.delete(
    path="/{track_id}/delete",
    summary="Delete track",
    response_model=SDeleteTrackResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteTrackResponse}},
)
async def delete_tracks(
    track_id: int,
    user: User = Depends(get_current_user),
    service: TracksService = Depends(get_tracks_service),
) -> SDeleteTrackResponse:

    await service.delete_track(track_id=track_id, user_id=user.id)

    return SDeleteTrackResponse()
