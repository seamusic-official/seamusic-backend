from sqlalchemy.orm import Mapped

from src.models.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    title: Mapped[str]
    description: Mapped[str | None]
