from datetime import date, datetime
from typing import Literal, Sequence


class BaseAlbumModel:
    id: int
    title: str
    description: str | None
    picture_url: str | None
    type: Literal['album', 'single']

    created_at: date
    updated_at: datetime

    viewers_ids: Sequence[int]
    likers_ids: Sequence[int]
    artists: Sequence['BaseArtistModel']  # type: ignore[name-defined]  # noqa: F821
    tracks: Sequence['BaseTrackModel']  # type: ignore[name-defined]  # noqa: F821
    tags: Sequence['BaseTagModel']  # type: ignore[name-defined]  # noqa: F821
