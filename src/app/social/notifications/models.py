from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.postgres.orm import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]

    created_at: Mapped[datetime]
