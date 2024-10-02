from datetime import date

from src.dtos.database.base import BaseDTO, BaseResponseDTO
from src.enums.spotify import SpotifyType, SpotifyAlbumType


class SpotifyImage(BaseDTO):
    url: str
    height: int
    width: int


class SpotifyArtist(BaseDTO):
    external_urls: dict[str, str]
    images: list[SpotifyImage]
    genres: list[str]
    href: str
    id: str
    name: str
    type: SpotifyType
    popularity: int
    uri: str


class SpotifyArtistResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    images: list[SpotifyImage]
    genres: list[str]
    href: str
    id: str
    name: str
    type: SpotifyType
    popularity: int
    uri: str


class SpotifyAlbumTrack(BaseDTO):
    href: str
    next: str
    previous: str
    popularity: int
    items: list['SpotifyTrack']
    total: int


class SpotifyAlbumTracksResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    tracks: list[SpotifyAlbumTrack]


class SpotifyAlbum(BaseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImage]
    tracks: list[SpotifyAlbumTrack]
    artists: list[SpotifyArtist]
    name: str
    release_date: date
    type: str
    uri: str


class SpotifyTrack(BaseDTO):
    external_urls: dict[str, str]
    external_ids: dict[str, str]
    album: SpotifyAlbum
    artists: list[SpotifyArtist]
    duration_ms: int
    explicit: bool
    href: str
    id: str
    name: str
    popularity: int
    image_url: str
    preview_url: str
    track_number: int
    type: SpotifyType
    uri: str


class SpotifyTrackResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    external_ids: dict[str, str]
    album: SpotifyAlbum
    artists: list[SpotifyArtist]
    duration_ms: int
    explicit: bool
    href: str
    id: str
    name: str
    popularity: int
    preview_url: str
    image_url: str
    track_number: int
    type: SpotifyType
    uri: str


class SpotifyTracksResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    tracks: list[SpotifyTrack]


class SpotifyAlbumResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImage]
    tracks: list[SpotifyAlbumTrack]
    artists: list[SpotifyArtist]
    name: str
    release_date: date
    type: SpotifyAlbumType
    uri: str


class SpotifyAlbumsResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items: list[SpotifyAlbum]


class SearchTracks(BaseDTO):
    id: str
    type: str
    name: str
    preview_url: str
    images: list[SpotifyImage]
    external_urls: dict[str, str]


class SearchArtists(BaseDTO):
    id: str
    type: str
    name: str
    artists: list[SpotifyArtist]
    preview_url: str
    external_urls: dict[str, str]
    duration_ms: int


class SearchAlbums(BaseDTO):
    id: str
    name: str
    images: list[SpotifyImage]
    external_urls: dict[str, str]
    release_date: str
    artists: list[SpotifyArtist]
    uri: str
    album_type: str
    total_tracks: int


class SearchResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    tracks: list[SpotifyTrack] | None = None
    artists: list[SpotifyTrack] | None = None
    albums: list[SpotifyAlbum] | None = None
