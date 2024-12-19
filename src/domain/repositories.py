from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any


class BaseStorageRepositoryMixinSession(ABC):
    @abstractmethod
    async def read(self, **kwargs) -> Any | None:  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def write(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def remove(self, **kwargs) -> None:  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def run(self, **kwargs) -> Any | None:  # type: ignore[no-untyped-def]
        raise NotImplementedError


class BaseStorageRepositoryMixin(ABC):
    @abstractmethod
    async def start(self) -> AsyncGenerator[BaseStorageRepositoryMixinSession]:
        raise NotImplementedError
