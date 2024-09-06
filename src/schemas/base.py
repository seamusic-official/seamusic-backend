from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class DetailMixin:
    detail: str | None = None


class Page(BaseModel):
    start: int = 1
    size: int = 10
