from datetime import date

from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.beatpacks import producer_to_beatpacks_association_table
from src.models.albums import artist_to_album_association
from src.models.base import Base
from src.models.soundkits import producer_to_soundkits_association_table
from src.models.squads import squad_to_producer_association, Squad
from src.models.tags import producer_to_tags_association, artist_to_tags_association
from src.models.tracks import artist_to_track_association
from src.models.beats import producer_to_beat_association


user_to_comments_association = Table(
    "user_to_comments_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("comment_id", ForeignKey("comments.id"), primary_key=True),
)

user_to_albums_association = Table(
    "user_to_albums_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
)

user_to_tag_association = Table(
    "user_to_tag_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("album_id", ForeignKey("tags.id"), primary_key=True),

)

user_to_tracks_association = Table(
    "user_to_tracks_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("album_id", ForeignKey("tracks.id"), primary_key=True),
)

user_to_playlists_association = Table(
    "user_to_playlists_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    access_level: Mapped[str] = mapped_column(nullable=False)
    artist_profile: Mapped["ArtistProfile"] = relationship("ArtistProfile", back_populates="user")  # type: ignore[name-defined]
    producer_profile: Mapped["ProducerProfile"] = relationship(back_populates="user")  # type: ignore[name-defined]
    licenses: Mapped[list["License"]] = relationship(argument="License")  # type: ignore[name-defined]  # noqa: F821
    followed_artists: Mapped[list["ArtistProfile"]] = relationship(overlaps="artist_profile", back_populates="user")  # type: ignore[name-defined]  # noqa: F821
    saved_playlists: Mapped[list["Playlists"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_playlists_association
    )
    followed_producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]
        argument="ProducerProfile",
        back_populates="user",
        overlaps="producer_profile"
    )
    saved_albums: Mapped[list["Album"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_albums_association
    )
    liked_tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_tracks_association
    )
    followed_tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_tag_association
    )
    comments: Mapped[list["BaseComment"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_comments_association
    )
    is_active: Mapped[bool] = mapped_column(nullable=False)
    is_adult: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"
    squad_id: Mapped[list["Squad"]] = mapped_column(Integer, ForeignKey("squads.id"))
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="artist_profile")
    tracks: Mapped[list["Track"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=artist_to_track_association
    )
    albums: Mapped[list["Album"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=artist_to_album_association,
        back_populates="artist_profiles"
    )
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="Tag",
        secondary=artist_to_tags_association
    )


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    user: Mapped["User"] = relationship(back_populates="producer_profile")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=False)
    beats: Mapped[list["Beat"]] = relationship(secondary=producer_to_beat_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_tags_association
    )
    squads: Mapped[list["Squad"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=squad_to_producer_association)
    beatpacks: Mapped[list["Beatpack"]] = relationship(secondary=producer_to_beatpacks_association_table)  # type: ignore[name-defined]  # noqa: F821
    soundkits: Mapped[list["Soundkit"]] = relationship(secondary=producer_to_soundkits_association_table)  # type: ignore[name-defined]  # noqa: F821
