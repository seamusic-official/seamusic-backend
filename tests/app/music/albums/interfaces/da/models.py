from datetime import date, datetime
from typing import Literal

from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.domain.music.albums.interfaces.da.models import BaseAlbumModel
from src.infrastructure.postgres.orm import Base

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


class Album(BaseAlbumModel, Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True)  # type: ignore[assignment]
    title: Mapped[str]  # type: ignore[assignment]
    picture_url: Mapped[str | None]  # type: ignore[assignment]
    description: Mapped[str | None]  # type: ignore[assignment]
    type: Mapped[Literal['album', 'single']]  # type: ignore[assignment]

    created_at: Mapped[date]  # type: ignore[assignment]
    updated_at: Mapped[datetime]  # type: ignore[assignment]

    viewers_ids: Mapped[list[int]]  # type: ignore[assignment]
    likers_ids: Mapped[list[int]]  # type: ignore[assignment]
    artists: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined, assignment]  # noqa: F821
        secondary=album_to_artist_association,
        back_populates="album",
        lazy="selectin",
    )
    tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined, assignment]  # noqa: F821
        secondary=album_to_track_association,
        lazy="selectin",
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined, assignment]  # noqa: F821
        secondary=album_to_tag_association,
        lazy="selectin",
    )
