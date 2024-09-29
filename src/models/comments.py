from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class BaseComment(Base):
    __tablename__ = "comments"

    comment: Mapped[str] = mapped_column(String, nullable=False)

    comment_creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment_author: Mapped["User"] = relationship("User")  # type: ignore[name-defined]  # noqa: F821

    beat_id: Mapped[int] = mapped_column(Integer, ForeignKey("beats.id"))
    beat_pack_id: Mapped[int] = mapped_column(Integer, ForeignKey("beatpacks.id"))
    soundkit_id: Mapped[int] = mapped_column(Integer, ForeignKey("soundkits.id"))
