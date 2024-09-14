import datetime

from pydantic import BaseModel

from src.enums.spotify import SpotifyAlbumType, SpotifyType
from src.schemas.base import ItemsResponse


class SpotifyTrack(BaseModel):
    id: str
    type: SpotifyType
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyTrackResponse(BaseModel):
    id: str
    type: SpotifyType
    name: str
    preview_url: str
    image_url: str
    spotify_url: str


class SSpotifyTracksResponse(ItemsResponse[SSpotifyTrackResponse]):
    pass


class SpotifyAlbum(BaseModel):
    id: str
    name: str
    image_url: str | None = None
    spotify_url: str


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


class SSpotifyAlbumsResponse(ItemsResponse[SpotifyAlbum]):
    pass


class SpotifyAlbumTrack(BaseModel):
    id: str
    type: SpotifyType
    name: str
    artists: list[SpotifyArtist]
    preview_url: str
    spotify_url: str
    duration_ms: int


class SSpotifyAlbumTracksResponse(BaseModel):
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
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
    total: int
    page: int
    has_next: bool
    has_previous: bool
    size: int
    tracks: list[SpotifyTrack] | None = None
    artists: list[SpotifyArtist] | None = None
    albums: list[SpotifyAlbum] | None = None
