from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.music.albums.da.dao import DAO


@dataclass
class BaseConverter(ABC):
    dao_implementation: DAO

    @staticmethod
    @abstractmethod
    async def album_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def album_existance_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def count_albums_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def popular_albums_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def artist_id_by_user_id_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def create_album_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def update_album_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def delete_album_request(*args, **kwargs):  # type: ignore[no-untyped-def]
        raise NotImplementedError
