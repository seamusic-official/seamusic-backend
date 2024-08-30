from dataclasses import dataclass
from io import BytesIO

from src.dtos.database.tracks import TracksResponseDTO, CreateTrackRequestDTO, UpdateTrackRequestDTO, TrackResponseDTO
from src.exceptions.services import NoRightsException, NotFoundException
from src.repositories import Repositories, BaseMediaRepository, DatabaseRepositories
from src.repositories.database.tracks.base import BaseTracksRepository
from src.repositories.database.tracks.postgres import init_postgres_repository
from src.repositories.media.s3 import init_s3_repository


@dataclass
class TracksDatabaseRepositories(DatabaseRepositories):
    tracks: BaseTracksRepository


@dataclass
class TracksRepositories(Repositories):
    database: TracksDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class TracksService:
    repositories: TracksRepositories

    async def get_user_tracks(self, user_id: int) -> TracksResponseDTO:
        return await self.repositories.database.tracks.get_user_tracks(user_id=user_id)

    async def all_tracks(self) -> TracksResponseDTO:
        return await self.repositories.database.tracks.get_all_tracks()

    async def get_one_track(self, track_id: int) -> TrackResponseDTO:
        track = await self.repositories.database.tracks.get_track_by_id(track_id=track_id)

        if not track:
            raise NotFoundException('track not found')

        return track

    async def add_track(
        self,
        username: str,
        track_title: str,
        description: str,
        user_id: int,
        file_info: str,
        file_stream: BytesIO
    ) -> int:

        file_url = await self.repositories.media.upload_file("AUDIOFILES", file_info, file_stream)

        track = CreateTrackRequestDTO(
            title=track_title,
            description=description,
            file_path=file_url,
            prod_by=username,
            user_id=user_id
        )

        return await self.repositories.database.tracks.create_track(track=track)

    async def update_pic_tracks(
        self,
        track_id: int,
        user_id: int,
        file_info: str,
        file_stream: BytesIO,
    ) -> int:
        file_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)

        track = await self.repositories.database.tracks.get_track_by_id(track_id=track_id)

        if not track:
            raise NotFoundException()

        if track.user_id != user_id:
            raise NoRightsException()

        updated_track = UpdateTrackRequestDTO(
            title=track.name,
            file_url=file_url,
            user_id=user_id
        )
        return await self.repositories.database.tracks.update_track(track=updated_track)

    async def release_track(
        self,
        track_id: int,
        user_id: int,
        title: str,
        picture_url: str | None,
        description: str | None,
        co_prod: str | None,
        prod_by: str | None,
        playlist_id: int | None,
        track_pack_id: int | None,
    ) -> int:

        track = await self.repositories.database.tracks.get_track_by_id(track_id=track_id)

        if not track:
            raise NotFoundException()

        if track.user_id != user_id:
            raise NoRightsException()

        updated_track = UpdateTrackRequestDTO(
            title=title,
            picture_url=picture_url,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            playlist_id=playlist_id,
            user_id=user_id,
            track_pack_id=track_pack_id,
        )

        return await self.repositories.database.tracks.update_track(track=updated_track)

    async def update_track(
        self,
        track_id: int,
        user_id: int,
        title: str,
        description: str | None,
        prod_by: str | None,
        picture_url: str | None,
        file_url: str,
        co_prod: str | None,
        playlist_id: int | None,
        track_pack_id: int | None,
    ) -> int:

        track = await self.repositories.database.tracks.get_track_by_id(track_id=track_id)

        if not track:
            raise NotFoundException()

        if track.user_id != user_id:
            raise NoRightsException()

        updated_track = UpdateTrackRequestDTO(
            title=title,
            picture_url=picture_url,
            file_url=file_url,
            description=description,
            co_prod=co_prod,
            prod_by=prod_by,
            playlist_id=playlist_id,
            user_id=user_id,
            track_pack_id=track_pack_id
        )

        return await self.repositories.database.tracks.update_track(track=updated_track)

    async def delete_track(self, track_id: int, user_id: int) -> None:
        track = await self.repositories.database.tracks.get_track_by_id(track_id=track_id)

        if not track:
            raise NotFoundException()

        if track.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.tracks.delete_track(track_id=track_id, user_id=user_id)


def get_tracks_repositories() -> TracksRepositories:
    return TracksRepositories(
        database=TracksDatabaseRepositories(tracks=init_postgres_repository()),
        media=init_s3_repository()
    )


def get_tracks_service() -> TracksService:
    return TracksService(repositories=get_tracks_repositories())
