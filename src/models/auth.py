from datetime import date, datetime

from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.albums import album_to_artist_association
from src.models.base import Base
from src.models.beats import producer_to_beat_association
from src.models.squads import follower_to_squads_association, artist_to_squad_association, producer_to_squad_association

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

producer_to_beatpacks_association = Table(
    "producer_to_beatpacks_association",
    Base.metadata,
    Column("producer_profile_id", ForeignKey("producer_profiles.id")),
    Column("beatpack_id", ForeignKey("beatpacks.id"))
)

producer_to_soundkits_association = Table(
    "producer_to_soundkits_association",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)

producer_to_tags_association = Table(
    'producer_to_tags_association',
    Base.metadata,
    Column("producer_id", ForeignKey('producer_profiles.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)

artist_to_track_association = Table(
    "artist_to_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)

artist_to_tags_association = Table(
    'artist_to_tags_association',
    Base.metadata,
    Column("artist_id", ForeignKey('artist_profiles.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
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
    followed_producers: Mapped[list["ProducerProfile"]] = relationship(secondary=user_to_producer_association)
    followed_albums: Mapped[list["Album"]] = relationship(secondary=user_to_albums_association)  # type: ignore[name-defined]  # noqa: F821
    followed_tags: Mapped[list["Tag"]] = relationship(secondary=user_to_tag_association)  # type: ignore[name-defined]  # noqa: F821


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    username: Mapped[str]
    description: Mapped[str]
    picture_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped[list["User"]] = relationship(secondary=user_to_artist_association, viewonly=True)
    followers: Mapped[list["User"]] = relationship(
        secondary=user_to_artist_association,
        back_populates="followed_artists"
    )
    tracks: Mapped[list["Track"]] = relationship(secondary=artist_to_track_association)  # type: ignore[name-defined]  # noqa: F821
    squads: Mapped[list["Squad"]] = relationship(secondary=artist_to_squad_association)  # type: ignore[name-defined]  # noqa: F821
    album: Mapped[list['Album']] = relationship(secondary=album_to_artist_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=artist_to_tags_association)  # type: ignore[name-defined]  # noqa: F821


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    username: Mapped[str]
    description: Mapped[str]
    picture_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    followers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_producer_association,
        back_populates="followed_producers"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=producer_to_beat_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
    squads: Mapped[list["Squad"]] = relationship(secondary=producer_to_squad_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=producer_to_tags_association)  # type: ignore[name-defined]  # noqa: F821
    beatpacks: Mapped[list["Beatpack"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beatpacks_association,
        back_populates="producers"
    )
    soundkits: Mapped[list["Soundkit"]] = relationship(secondary=producer_to_soundkits_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
