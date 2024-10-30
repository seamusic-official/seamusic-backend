from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO


class SearchRequestDTO(BaseRequestDTO):
    text: str


class SearchResponseDTO(BaseResponseDTO):
    albums: list["AlbumDTO"]  # type: ignore[name-defined]  # noqa: F821
    users: list["UserDTO"]  # type: ignore[name-defined]  # noqa: F821
    artists: list["ArtistDTO"]  # type: ignore[name-defined]  # noqa: F821
    beatpacks: list["BeatpackDTO"]  # type: ignore[name-defined]  # noqa: F821
    beats: list["BeatDTO"]  # type: ignore[name-defined]  # noqa: F821
    soundkits: list["SoundkitDTO"]  # type: ignore[name-defined]  # noqa: F821
    squads: list["SquadDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list["TagDTO"]  # type: ignore[name-defined]  # noqa: F821
    tracks: list["TrackDTO"]  # type: ignore[name-defined]  # noqa: F821
