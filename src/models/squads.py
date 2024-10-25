from datetime import date, datetime

from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.models.auth import producer_to_squad_association, follower_to_squads_association
from src.models.base import Base

admin_producer_to_squad = Table(
    "admin_producer_to_squad",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True)
)

producer_to_squads_association = Table(
    "producer_to_squad_association",
    Base.metadata,
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)

artist_to_squad_association = Table(
    "artist_to_squad_association",
    Base.metadata,
    Column("artist_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)


class Squad(Base):
    __tablename__ = "squads"

    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    followers: Mapped[list["User"]] = relationship(secondary=follower_to_squads_association)  # type: ignore[name-defined]  # noqa: F821
    artists: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=artist_to_squad_association,
        back_populates="squads"

    )
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_squad_association,
        back_populates="squads"
    )
