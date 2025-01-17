from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.postgres import Base


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
