from datetime import date, datetime
from typing import Literal


class BaseAlbumModel:
    id: int
    title: str
    description: str | None
    picture_url: str | None
    type: Literal['album', 'single']

    created_at: date
    updated_at: datetime

    viewers_ids: list[int]
    likers_ids: list[int]
    artists: list['BaseArtistModel']  # type: ignore[name-defined]  # noqa: F821
    tracks: list['BaseTrackModel']  # type: ignore[name-defined]  # noqa: F821
    tags: list['BaseTagModel']  # type: ignore[name-defined]  # noqa: F821
