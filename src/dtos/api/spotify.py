from datetime import date

from src.dtos.database.base import BaseDTO, BaseResponseDTO
from src.enums.spotify import SpotifyType, SpotifyAlbumType


class SpotifyImageDTO(BaseDTO):
    url: str
    height: int
    width: int


class SpotifyArtistDTO(BaseDTO):
    external_urls: dict[str, str]
    images: list[SpotifyImageDTO]
    genres: list[str]
    href: str
    id: str
    name: str
    type: SpotifyType
    popularity: int
    uri: str


class SpotifyArtistResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    images: list[SpotifyImageDTO]
    genres: list[str]
    href: str
    id: str
    name: str
    type: SpotifyType
    popularity: int
    uri: str


class SpotifyAlbumTrackDTO(BaseDTO):
    href: str
    next: str
    previous: str
    popularity: int
    items: list["SpotifyTrackDTO"]
    total: int


class SpotifyAlbumTracksResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    tracks: list[SpotifyAlbumTrackDTO]


class SpotifyAlbumDTO(BaseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImageDTO]
    tracks: list[SpotifyAlbumTrackDTO]
    artists: list[SpotifyArtistDTO]
    name: str
    release_date: date
    type: str
    uri: str


class SpotifyTrackDTO(BaseDTO):
    external_urls: dict[str, str]
    external_ids: dict[str, str]
    album: SpotifyAlbumDTO
    artists: list[SpotifyArtistDTO]
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
    album: SpotifyAlbumDTO
    artists: list[SpotifyArtistDTO]
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
    tracks: list[SpotifyTrackDTO]


class SpotifyAlbumResponseDTO(BaseResponseDTO):
    external_urls: dict[str, str]
    album_type: str
    total_tracks: int
    genres: list[str]
    href: str
    id: str
    images: list[SpotifyImageDTO]
    tracks: list[SpotifyAlbumTrackDTO]
    artists: list[SpotifyArtistDTO]
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
    items: list[SpotifyAlbumDTO]


class SearchTracksDTO(BaseDTO):
    id: str
    type: str
    name: str
    preview_url: str
    images: list[SpotifyImageDTO]
    external_urls: dict[str, str]


class SearchArtistsDTO(BaseDTO):
    id: str
    type: str
    name: str
    artists: list[SpotifyArtistDTO]
    preview_url: str
    external_urls: dict[str, str]
    duration_ms: int


class SearchAlbumsDTO(BaseDTO):
    id: str
    name: str
    images: list[SpotifyImageDTO]
    external_urls: dict[str, str]
    release_date: str
    artists: list[SpotifyArtistDTO]
    uri: str
    album_type: str
    total_tracks: int


class SearchResponseDTO(BaseResponseDTO):
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    tracks: list[SpotifyTrackDTO] | None = None
    artists: list[SpotifyTrackDTO] | None = None
    albums: list[SpotifyAlbumDTO] | None = None
