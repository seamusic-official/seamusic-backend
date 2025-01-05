from datetime import date, datetime

from sqlalchemy import Table, Integer, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.auth.users.models import user_to_artist_association
from src.app.music.albums.interfaces.da.models import album_to_artist_association
from src.app.music.squads.models import artist_to_squad_association
from src.infrastructure.postgres.orm import Base

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


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    description: Mapped[str]
    picture_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped[list["User"]] = relationship(secondary=user_to_artist_association, viewonly=True)  # type: ignore[name-defined]  # noqa: F821
    followers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_artist_association,
        back_populates="followed_artists"
    )
    tracks: Mapped[list["Track"]] = relationship(secondary=artist_to_track_association)  # type: ignore[name-defined]  # noqa: F821
    squads: Mapped[list["Squad"]] = relationship(secondary=artist_to_squad_association)  # type: ignore[name-defined]  # noqa: F821
    albums: Mapped[list['Album']] = relationship(secondary=album_to_artist_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=artist_to_tags_association)  # type: ignore[name-defined]  # noqa: F821
