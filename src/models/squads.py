from sqlalchemy import Column, Table, ForeignKey, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

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
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    admins: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
