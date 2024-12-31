from abc import abstractmethod, ABC
from typing import Self


class DAO(ABC):
    @abstractmethod
    async def get_album_by_id(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def get_album_existance(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def count_albums(self):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def get_artist_id_by_user_id(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def create_album(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def update_album(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self) -> Self:
        return self

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        pass
