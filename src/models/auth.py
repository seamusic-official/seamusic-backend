from datetime import date

from sqlalchemy import ForeignKey, Date, Table, Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums.auth import Role, AccessLevel
from src.models.albums import Album, artist_profile_album_association
from src.models.base import Base
from src.models.squads import Squad, squad_producer_profile_association, squad_artist_profile_association
from src.models.tags import Tag, artist_tags_association, producer_tags_association, listener_tags_association
from src.models.tracks import Track, artist_profile_track_association

user_to_licenses_association = Table(
    "user_to_licenses_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("license_id", ForeignKey("licenses.id"), primary_key=True),
)

user_comments_association = Table(
    "user_comments_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("comment_id", ForeignKey("comments.id"), primary_key=True),
)


user_to_playlists_association = Table(
    "user_to_playlists_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String,nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String,nullable=True)
    artist_profile: Mapped["ArtistProfile"] = relationship(backref="user")  # type: ignore[name-defined]
    producer_profile: Mapped["ProducerProfile"] = relationship(backref="user")  # type: ignore[name-defined]
    licenses: Mapped[list["licenses"]] = relationship("licenses")
    access_level: Mapped[str] = mapped_column(String, nullable=False)
    followed_artists: Mapped[list["ArtistsProfile"]] = relationship("ArtistsProfile",back_populates="user")
    saved_playlists: Mapped[list["playlists"]] = relationship("playlists",back_populates="user")
    followed_producers: Mapped[list["Producers_profiles"]] = relationship("Producers_profiles", back_populates="user")
    saved_albums: Mapped[list["Album"]] = relationship("Album", overlaps="user")  # type: ignore[name-defined]
    liked_tracks: Mapped[list["Track"]] = relationship("Track", back_populates="user")
    followed_tags: Mapped[list["Tags"]] = relationship("Tags", back_populates="users")
    comments: Mapped[list["BaseComment"]] = relationship("BaseComment",back_populates="users")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_adult: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="ArtistProfile")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)

    tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_profile_track_association,
        back_populates="artist_profiles"
    )
    albums: Mapped[list["Album"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_profile_album_association,
        back_populates="artist_profiles"
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_tags_association,
        back_populates="artist_profiles"
    )


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="ProducerProfile")
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=False)
    beats: Mapped[list["Beat"]] = relationship(
        back_populates="producer_profiles"
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]
        secondary=producer_tags_association,
        back_populates="producer_profiles"
    )
    squads: Mapped[list["Squad"]] = (relationship(  # type: ignore[name-defined]
        secondary=squad_producer_profile_association,
        back_populates="producer_profiles"
    ))
    beatpacks: Mapped[list["Beatpack"]] = relationship(
        back_populates="producer_profiles"
    )
    soundkits: Mapped[list["Soundkit"]] = relationship(
        back_populates="producer_profiles"
    )