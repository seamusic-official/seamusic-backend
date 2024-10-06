from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.albums import album_track_association
from src.models.base import Base
from src.models.tags import track_tags_association

artist_profile_track_association = Table(
    "artist_profile_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey(
        "artist_profiles.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


user_liked_track_association = Table(
    "user_liked_track_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey(
        "users.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


playlist_track_association = Table(
    "playlist_track_association",
    Base.metadata,
    Column("playlist_id", ForeignKey(
        "playlists.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True),
)


class Track(Base):
    __tablename__ = "tracks"
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    album: Mapped["Album"] = relationship(
        argument="Album",
        secondary=album_track_association
    )  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(
        argument="Tag",
        secondary=track_tags_association
    )  # type: ignore[name-defined]  # noqa: F821
