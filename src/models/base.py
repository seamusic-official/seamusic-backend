from datetime import date

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    is_availible: Mapped[bool] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
