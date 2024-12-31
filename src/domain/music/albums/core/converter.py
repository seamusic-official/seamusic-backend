from abc import ABC, abstractmethod

from src.domain.music.albums.da.dao import DAO


class BaseConverter(ABC):
    dao_implementation: DAO

    @staticmethod
    @abstractmethod
    async def album_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def album_existance_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def popular_albums_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def count_albums_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def artist_id_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def create_album_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def update_album_response(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def delete_album_response(*args, **kwargs):
        raise NotImplementedError
