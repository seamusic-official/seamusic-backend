from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base


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
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True)
)

user_to_playlists_association = Table(
    "user_to_playlists_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("playlist_id", Integer, ForeignKey("playlists.id"), primary_key=True)
)

producer_to_beatpacks_association_table = Table(
    "producer_to_beatpacks_association_table",
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
    Column("tag.id", ForeignKey('tags.id'), primary_key=True),
)

producer_to_squad_association = Table(
    "producer_to_squad_association",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("producer_profile_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)

artist_to_track_association = Table(
    "artist_to_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)

artist_to_album_association = Table(
    "artist_to_album_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", ForeignKey("artist_profiles.id"), primary_key=True),
)

artist_to_tags_association = Table(
    'artist_to_tags_association',
    Base.metadata,
    Column("artist_id", ForeignKey('artist_profiles.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    access_level: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    is_adult: Mapped[bool] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False)


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=False)


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=False)
