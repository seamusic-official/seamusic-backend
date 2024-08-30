from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base

squad_artist_profile_association = Table(
    "squad_artist_profile_association",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id")),
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id")),
)

squad_producer_profile_association = Table(
    "squad_producer_profile_association",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id")),
    Column("producer_profile_id", Integer, ForeignKey("producer_profiles.id")),
)


class Squad(Base):
    __tablename__ = "squads"

    name: Mapped[str] = mapped_column(nullable=False)
    picture: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    file_path: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    artist_profiles: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]
        secondary=squad_artist_profile_association, back_populates="squads"
    )
    producer_profiles: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]
        secondary=squad_producer_profile_association, back_populates="squads"
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User")  # type: ignore[name-defined]
