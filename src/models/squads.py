from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.models.auth import producer_to_squad_association
from src.models.base import Base

admin_producer_to_squad = Table(
    "admin_producer_to_squad",
    Base.metadata,
    Column("squad_id", Integer, ForeignKey("squads.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)


class Squad(Base):
    __tablename__ = "squads"

    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    admins: Mapped[list["ProducerProfile"]] = relationship(secondary=admin_producer_to_squad)  # type: ignore[name-defined]  # noqa: F821
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_squad_association,
        back_populates="squads"
    )
