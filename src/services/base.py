from dataclasses import dataclass

from src.repositories import Repositories


@dataclass
class BaseService:
    repositories: Repositories
