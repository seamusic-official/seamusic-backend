from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any


class BaseStorageRepositoryMixinSession(ABC):
    @abstractmethod
    async def read(self, **kwargs) -> Any | None:
        raise NotImplementedError

    @abstractmethod
    async def write(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    async def run(self, **kwargs) -> Any | None:
        raise NotImplementedError


class BaseStorageRepositoryMixin(ABC):
    @staticmethod
    @abstractmethod
    async def start() -> AsyncGenerator[BaseStorageRepositoryMixinSession]:
        raise NotImplementedError
