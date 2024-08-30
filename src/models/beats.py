from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class Beat(Base):
    __tablename__ = "beats"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)

    type: Mapped[str] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")  # type: ignore[name-defined]
