from datetime import date

from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

squad_artist_profile_association = Table(
    "squad_artist_profile_association",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
)

squad_producer_profile_association = Table(
    "squad_producer_profile_association",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("producer_profile_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)


class Squad(Base):
    __tablename__ = "squads"

    name: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    admins_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    artists_id: Mapped[int] = mapped_column(ForeignKey("artist_profiles.id"), nullable=True)
    admins: Mapped[list["User"]] = relationship(argument="User", foreign_keys=[admins_id])  # type: ignore[name-defined]  # noqa: F821
    artists: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="ArtistProfile",
        secondary=squad_artist_profile_association,
        foreign_keys=[artists_id]
    )
    created_at: Mapped[date] = mapped_column(nullable=False)
