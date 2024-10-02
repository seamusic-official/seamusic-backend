from abc import ABC
from dataclasses import dataclass

from src.repositories.api.base import BaseAPIRepository
from src.repositories.database.base import DatabaseRepositories
from src.repositories.media.base import BaseMediaRepository


@dataclass
class Repositories(ABC):
    database: DatabaseRepositories | None = None
    media: BaseMediaRepository | None = None
    api: BaseAPIRepository | None = None
