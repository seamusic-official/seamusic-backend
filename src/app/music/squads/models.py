from datetime import date, datetime

from sqlalchemy import Table, ForeignKey, Integer, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.postgres import Base

follower_to_squads_association = Table(
    "follower_to_squads_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)

artist_to_squad_association = Table(
    "artist_to_squad_association",
    Base.metadata,
    Column("artist_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)

producer_to_squad_association = Table(
    "producer_to_squad_association",
    Base.metadata,
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
)


class Squad(Base):
    __tablename__ = "squads"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    followers: Mapped[list["User"]] = relationship(secondary=follower_to_squads_association)  # type: ignore[name-defined]  # noqa: F821
    artists: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=artist_to_squad_association,
        back_populates="squads",
    )
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_squad_association,
        back_populates="squads",
    )
