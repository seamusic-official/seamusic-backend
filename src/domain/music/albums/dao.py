from abc import abstractmethod, ABC
from typing import AsyncGenerator, Self


class BaseDAOSession(ABC):
    async def get_album_by_id(self, **kwargs) -> dict | None:
        ...

    async def get_album_existance(self, **kwargs) -> bool:
        ...

    async def get_popular_albums(self, **kwargs) -> list[dict]:
        ...

    async def count_albums(self) -> int:
        ...

    async def get_artist_id_by_user_id(self, **kwargs) -> int | None:
        ...

    async def create_album(self, **kwargs) -> int:
        ...

    async def update_album(self, **kwargs) -> int:
        ...

    async def delete_album(self, **kwargs) -> None:
        ...

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        pass


class BaseDAO(ABC):
    @abstractmethod
    async def open(self) -> AsyncGenerator[BaseDAOSession]:
        raise NotImplementedError
