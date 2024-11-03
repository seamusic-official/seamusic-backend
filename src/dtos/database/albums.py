from datetime import datetime, date

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class AlbumRequestDTO(BaseRequestDTO):
    id: int


class AlbumResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    type: str
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    viewers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    likers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    artists: list["ArtistDTO"]  # type: ignore[name-defined]  # noqa: F821
    tracks: list["TrackDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list[str]


class AlbumItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None
    description: str | None
    views: int
    likes: int
    type: str

    created_at: date
    updated_at: datetime


class AlbumsResponseDTO(BaseResponseDTO):
    albums: list[AlbumItemResponseDTO]


class CountAlbumResponseDTO(BaseResponseDTO):
    amount: int


class ArtistAlbumsRequestDTO(BaseRequestDTO):
    artist_id: int


class ArtistAlbumsResponseDTO(BaseResponseDTO):
    albums: list[AlbumItemResponseDTO]


class CreateAlbumRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    type: str

    created_at: date = date.today()
    updated_at: datetime = datetime.now()


class CreateAlbumResponseDTO(BaseResponseDTO):
    id: int


class UpdateAlbumRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    type: str | None = None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int] | None = None
    likers_ids: list[int] | None = None
    artists_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    tags: list[str] | None = None


class UpdateAlbumResponseDTO(BaseResponseDTO):
    id: int


class DeleteAlbumRequestDTO(BaseRequestDTO):
    album_id: int


class AlbumDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int
    type: str

    created_at: date
    updated_at: datetime
