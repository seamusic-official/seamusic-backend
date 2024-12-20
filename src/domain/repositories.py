from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any, Self


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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        pass


class BaseStorageRepositoryMixin(ABC):
    @abstractmethod
    async def start(self) -> AsyncGenerator[BaseStorageRepositoryMixinSession]:
        raise NotImplementedError
