from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ProducerProfile
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
    producers: Mapped[list["ProducerProfile"]] = relationship(
        secondary=producer_to_squad_association,
        back_populates="squads"
    )
    admins: Mapped[list["ProducerProfile"]] = relationship(secondary=admin_producer_to_squad)
    name: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
