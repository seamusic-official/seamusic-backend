from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class PlaylistResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    viewers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    likers: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    authors: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    beats: list["BeatDTO"]  # type: ignore[name-defined]  # noqa: F821
    tracks: list["TrackDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list[str]


class PlaylistItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int

    created_at: date
    updated_at: datetime

    tags: list[str]


class PlaylistsResponseDTO(BaseResponseDTO):
    playlists: list[PlaylistItemResponseDTO]


class CreatePlaylistRequestDTO(BaseRequestDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    tags: list[str]


class CreatePlaylistResponseDTO(BaseResponseDTO):
    id: int


class UpdatePlaylistRequestDTO(BaseRequestDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None

    updated_at: datetime = datetime.now()

    viewers_ids: list[int]
    likers_ids: list[int]
    authors_ids: list[int]
    beats_ids: list[int]
    tracks_ids: list[int]
    tags: list[str]


class UpdatePlaylistResponseDTO(BaseResponseDTO):
    id: int


class PlaylistDTO(BaseDTO):
    id: int
    title: str
    description: str | None
    picture_url: str | None
    views: int
    likes: int

    created_at: date
    updated_at: datetime
