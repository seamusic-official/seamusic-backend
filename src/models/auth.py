from datetime import date

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.albums import artist_profile_album_association
from src.models.base import Base
from src.models.squads import squad_producer_profile_association
from src.models.tags import artist_profile_tags_association, producer_profile_tags_association
from src.models.tracks import artist_profile_track_association

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

    username: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    access_level: Mapped[str] = mapped_column(nullable=False)

    artist_profile: Mapped["ArtistProfile"] = relationship(back_populates="user")  # type: ignore[name-defined]
    producer_profile: Mapped["ProducerProfile"] = relationship(back_populates="user")  # type: ignore[name-defined]
    licenses: Mapped[list["License"]] = relationship(argument="License")  # type: ignore[name-defined]  # noqa: F821
    followed_artists: Mapped[list["ArtistsProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="ArtistsProfile",
        back_populates="user",
    )
    saved_playlists: Mapped[list["Playlist"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="Playlist",
        back_populates="user"
    )
    followed_producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]
        argument="ProducerProfile",
        back_populates="user"
    )
    saved_albums: Mapped[list["Album"]] = relationship(  # type: ignore[name-defined]
        argument="Album",
        overlaps="user"
    )
    liked_tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]
        argument="Track",
        back_populates="user"
    )
    followed_tags: Mapped[list["Tags"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="Tags",
        back_populates="users"
    )
    comments: Mapped[list["BaseComment"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="BaseComment",
        back_populates="users"
    )
    is_active: Mapped[bool] = mapped_column(nullable=False)
    is_adult: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship(
        argument="User",
        back_populates="artist_profile",
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_profile_track_association,
        back_populates="artist_profiles"
    )
    albums: Mapped[list["Album"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_profile_album_association,
        back_populates="artist_profiles"
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]
        argument="Tag",
        secondary=artist_profile_tags_association,
    )


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    user: Mapped["User"] = relationship(
        argument='User',
        back_populates="producer_profile",
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=False)
    beats: Mapped[list["Beat"]] = relationship(argument="Beat")  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]
        argument='Tag',
        secondary=producer_profile_tags_association,
    )
    squads: Mapped[list["Squad"]] = (relationship(  # type: ignore[name-defined]
        secondary=squad_producer_profile_association,
        back_populates="producer_profiles",
    ))
    beatpacks: Mapped[list["Beatpack"]] = relationship(argument="Beatpack")  # type: ignore[name-defined]  # noqa: F821
    soundkits: Mapped[list["Soundkit"]] = relationship(argument="Soundkit")  # type: ignore[name-defined]  # noqa: F821
