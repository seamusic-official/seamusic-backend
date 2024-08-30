from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.models.auth import User


user_to_soundkits_association_table = Table(
    "user_to_soundkits_association_table",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
)


class Soundkit(Base):
    __tablename__ = "soundkits"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")  # type: ignore[name-defined]
