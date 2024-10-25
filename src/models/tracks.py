from datetime import datetime, date

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base

track_to_tag_association = Table(
    'track_to_tag_association',
    Base.metadata,
    Column("track_id", ForeignKey('tracks.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)

track_to_producer_association = Table(
    'track_to_producer_association',
    Base.metadata,
    Column("producer_id", ForeignKey('producer_profiles.id'), primary_key=True),
    Column("track_id", ForeignKey('tracks.id'), primary_key=True),
)

user_to_tracks_likes = Table(
    "user_to_tracks_likes",
    Base.metadata,
    Column("track_id", ForeignKey("tracks.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)


class Track(Base):
    __tablename__ = "tracks"

    title: Mapped[str]
    views: Mapped[int]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    file_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    likers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_tracks_likes
    )
    producers: Mapped[list["ProducerProfile"]] = relationship(secondary=track_to_producer_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=track_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
