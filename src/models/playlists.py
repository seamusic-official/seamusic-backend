from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import user_to_playlists_association
from src.models.base import Base
from src.models.beats import playlist_beat_association
from src.models.tags import playlist_tags_association
from src.models.tracks import playlist_track_association


class Playlist(Base):
    __tablename__ = "playlists"

    author: Mapped["User"] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_playlists_association,
    )
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    beats: Mapped[list["Beat"]] = relationship(
        argument="Beat",
        secondary=playlist_beat_association
    )  # type: ignore[name-defined]  # noqa: F821
    tracks: Mapped[list["Track"]] = relationship(
        argument="Track",
        secondary=playlist_track_association
    )  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(
        argument="Tag",
        secondary=playlist_tags_association
    )  # type: ignore[name-defined]  # noqa: F821
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
