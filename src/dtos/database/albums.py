from datetime import datetime, date

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class AlbumResponseDTO(BaseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    type: str

    created_at: date
    updated_at: datetime

    artists: list["ArtistDTO"] = list()
    tracks: list["TrackDTO"] = list()
    tags: list[str] = list()


class CreateAlbumRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None = None
    description: str | None = None

    artists: list["ArtistDTO"] = list()
    tracks: list["TrackDTO"] = list()
    tags: list[str] = list()


class UpdateAlbumRequestDTO(BaseRequestDTO):
    id: int
    title: str | None = None
    picture_url: str | None = None
    description: str | None = None
    type: str | None = None

    artists: list["ArtistDTO"] | None = None
    tracks: list["TrackDTO"] | None = None
    tags: list["TagDTO"] | None = None


class AlbumItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    type: str

    created_at: date
    updated_at: datetime

    artists: list["ArtistDTO"] = list()
    tracks: list["TrackDTO"] = list()
    tags: list["TagDTO"] = list()


class AlbumsResponseDTO(BaseResponseDTO):
    albums: list[AlbumItemResponseDTO]
