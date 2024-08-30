from dataclasses import dataclass

from src.repositories.api.base import BaseAPIRepository
from src.repositories.database.base import BaseDatabaseRepository
from src.repositories.media.base import BaseMediaRepository


@dataclass
class DatabaseRepositories:
    ...


@dataclass
class Repositories:
    database: DatabaseRepositories | None = None
    media: BaseMediaRepository | None = None
    api: BaseAPIRepository | None = None
