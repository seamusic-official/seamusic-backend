from dataclasses import dataclass

from src.dtos.api.spotify import (
    SpotifyTracksResponseDTO,
    SpotifyTrackResponseDTO,
    SpotifyAlbumsResponseDTO,
    SpotifyAlbumResponseDTO,
    SpotifyArtistResponseDTO,
    SearchResponseDTO
)
from src.enums.spotify import SpotifyType
from src.exceptions.services import NotFoundException
from src.repositories import Repositories
from src.repositories.api.spotify.base import BaseSpotifyRepository


class SpotifyRepositories(Repositories):
    api: BaseSpotifyRepository


@dataclass
class SpotifyService:
    repositories: SpotifyRepositories

    async def get_recommendations(self, start: int = 1, size: int = 10) -> SpotifyTracksResponseDTO:
        return await self.repositories.api.get_recommendations(offset=start - 1, limit=size)

    async def get_top_artist_tracks(self, artist_id: str, start: int = 1, size: int = 10) -> SpotifyTracksResponseDTO:
        return await self.repositories.api.get_top_artist_tracks(artist_id=artist_id, offset=start - 1, limit=size)

    async def get_spotify_track(self, track_id: str) -> SpotifyTrackResponseDTO:
        track = await self.repositories.api.get_track(track_id=track_id)

        if not track:
            raise NotFoundException()

        return track

    async def get_artist_albums(self, artist_id: str, start: int = 1, size: int = 10) -> SpotifyAlbumsResponseDTO:
        albums = await self.repositories.api.get_artist_albums(artist_id=artist_id, offset=start - 1, limit=size)

        if not albums:
            raise NotFoundException()

        return albums

    async def get_spotify_album(self, album_id: str) -> SpotifyAlbumResponseDTO:
        album = await self.repositories.api.get_album(album_id=album_id)

        if not album:
            raise NotFoundException()

        return album

    async def get_album_tracks_count(self, album_id: str) -> int:
        return await self.repositories.api.get_album_tracks_count(album_id=album_id)

    async def get_spotify_artist(self, artist_id: str) -> SpotifyArtistResponseDTO:
        artist = await self.repositories.api.get_artist(artist_id=artist_id)

        if not artist:
            raise NotFoundException

        return artist

    async def get_spotify_search(self, query: str, type_: SpotifyType, start: int = 1, size: int = 10) -> SearchResponseDTO:
        return await self.repositories.api.search(query=query, type_=type_, offset=start - 1, limit=size)


def get_spotify_repositories() -> SpotifyRepositories:
    return SpotifyRepositories()


def get_spotify_service() -> SpotifyService:
    return SpotifyService(repositories=get_spotify_repositories())
