from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.models.auth import producer_to_squad_association
from src.models.base import Base

admin_producer_to_squad = Table(
    "admin_producer_to_squad",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True)
)

user_to_squads_likes = Table(
    "user_to_squads_likes",
    Base.metadata,
    Column("squad_id", ForeignKey("squads.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

producer_to_squad_subs = Table(
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)

artist_to_squad_subs = Table(
    Column("artist_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True)
)


class Squad(Base):
    __tablename__ = "squads"

    title: Mapped[str]
    views: Mapped[int]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    liked_users: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_squads_likes
    )
    producer_sub: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_squad_subs
    )
    artist_sub: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=artist_to_squad_subs
    )
    admins: Mapped[list["ProducerProfile"]] = relationship(secondary=admin_producer_to_squad)  # type: ignore[name-defined]  # noqa: F821
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_squad_association,
        back_populates="squads"
    )
