import datetime

from pydantic import BaseModel

from src.enums.spotify import SpotifyAlbumType, SpotifyType


class SpotifyTrack(BaseModel):
    id: str
    type: SpotifyType
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyTracksResponse(BaseModel):
    tracks: list[SpotifyTrack]


class SSpotifyTrackResponse(BaseModel):
    id: str
    type: SpotifyType
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SpotifyAlbum(BaseModel):
    id: str
    name: str
    image_url: str | None = None
    spotify_url: str


class SSpotifyAlbumsResponse(BaseModel):
    albums: list[SpotifyAlbum]


class SpotifyArtist(BaseModel):
    id: str
    type: SpotifyType
    name: str
    image_url: str
    popularity: int


class SSpotifyAlbumResponse(BaseModel):
    id: str
    name: str
    image_url: str
    spotify_url: str
    release_date: datetime.date
    artists: list[SpotifyArtist]
    external_urls: dict[str, str]
    uri: str
    album_type: SpotifyAlbumType
    total_tracks: int


class SpotifyAlbumTrack(BaseModel):
    id: str
    type: SpotifyType
    name: str
    artists: list[SpotifyArtist]
    preview_url: str
    spotify_url: str
    duration_ms: int


class SSpotifyAlbumTracksResponse(BaseModel):
    tracks: list[SpotifyAlbumTrack]


class SSpotifyAlbumTracksCountResponse(BaseModel):
    count: int


class SSpotifyArtistResponse(BaseModel):
    id: str
    type: str
    name: str
    image_url: str
    popularity: int
    external_urls: dict[str, str]


class SSpotifySearchResponse(BaseModel):
    tracks: list[SpotifyTrack] | None = None
    artists: list[SpotifyArtist] | None = None
    albums: list[SpotifyAlbum] | None = None
