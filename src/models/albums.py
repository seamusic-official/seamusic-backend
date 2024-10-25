from datetime import date, datetime

from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base
from src.models.views import user_to_albums_views_association

album_to_track_association = Table(
    "album_to_track_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True)
)

album_to_artist_association = Table(
    "album_to_artist_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", ForeignKey("artist_profiles.id"), primary_key=True)
)

album_to_tag_association = Table(
    "album_to_tag_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)

user_to_albums_likes = Table(
    "user_to_albums_likes",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)


class Album(Base):
    __tablename__ = "albums"

    title: Mapped[str]
    picture_url: Mapped[str | None]
    description: Mapped[str | None]
    type: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    viewers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_albums_views_association
    )
    likers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_albums_likes
    )
    artists: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=album_to_artist_association,
        back_populates="albums"
    )
    tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=album_to_track_association
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=album_to_tag_association
    )
