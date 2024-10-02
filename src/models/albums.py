from sqlalchemy import Date, Column, Table, ForeignKey, Integer, String, DATETIME
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base

artist_profile_album_association = Table(
    "artist_profile_album_association",
    Base.metadata,
    Column("artist_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
)

album_track_association = Table(
    "album_track_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(DATETIME, nullable=False)
    updated_at: Mapped[date] = mapped_column(DATETIME, nullable=False)
    tags: Mapped[list["Tags"]] = relationship(
        "Tags"
    )
    artists: Mapped[list["ArtistProfile"]] = relationship(
        "ArtistProfile"
    )