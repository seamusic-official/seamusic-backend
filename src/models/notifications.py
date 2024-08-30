from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
