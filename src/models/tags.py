from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base


class Tag(Base):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
