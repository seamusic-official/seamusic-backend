from datetime import date, datetime

from sqlalchemy import Table, ForeignKey, Integer, Column
from sqlalchemy.orm import Mapped, relationship

from src.infrastructure.postgres.orm import Base

user_to_licenses_association = Table(
    "user_to_licenses_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("license_id", Integer, ForeignKey("licenses.id"), primary_key=True)
)

user_to_artist_association = Table(
    "user_to_artist_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("artist_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True)
)

user_to_producer_association = Table(
    "user_to_producer_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True)
)

user_to_albums_association = Table(
    "user_to_albums_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
)

user_to_tag_association = Table(
    "user_to_tag_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

user_to_playlists_association = Table(
    "user_to_playlists_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("playlist_id", Integer, ForeignKey("playlists.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    username: Mapped[str]
    description: Mapped[str | None]
    email: Mapped[str]
    password: Mapped[str]
    picture_url: Mapped[str | None]
    access_level: Mapped[str]
    telegram_id: Mapped[int | None]
    premium_level: Mapped[str]

    is_active: Mapped[bool]
    is_adult: Mapped[bool]
    is_verified: Mapped[bool]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    messages: Mapped["Message"] = relationship("Message", back_populates="author")  # type: ignore[name-defined]  # noqa: F821
    licenses: Mapped[list["License"]] = relationship(secondary=user_to_licenses_association)  # type: ignore[name-defined]  # noqa: F821
    followed_squads: Mapped[list["Squad"]] = relationship(secondary=follower_to_squads_association, back_populates="followers")  # type: ignore[name-defined]  # noqa: F821
    followed_artists: Mapped[list["ArtistProfile"]] = relationship(secondary=user_to_artist_association, back_populates="users")  # type: ignore[name-defined]  # noqa: F821
    saved_playlists: Mapped[list["Playlist"]] = relationship(secondary=user_to_playlists_association)  # type: ignore[name-defined]  # noqa: F821
    followed_producers: Mapped[list["ProducerProfile"]] = relationship(secondary=user_to_producer_association)  # type: ignore[name-defined]  # noqa: F821
    followed_albums: Mapped[list["Album"]] = relationship(secondary=user_to_albums_association)  # type: ignore[name-defined]  # noqa: F821
    followed_tags: Mapped[list["Tag"]] = relationship(secondary=user_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
