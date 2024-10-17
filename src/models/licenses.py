from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class License(Base):
    __tablename__ = "licenses"

    text: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
