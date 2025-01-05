from abc import abstractmethod
from dataclasses import dataclass

from src.domain.music.albums.interfaces.base import BaseInterface


@dataclass
class MAO(BaseInterface):
    """
    Media Access Object (MAO) is an abstract class created
    to define and describe necessary functions for files acess.

    It's used in services' layer to manage files.

    As an abstraction, MAO cannot be used directly - that will
    cause `NotImplementedError` and crash the application. So,
    to provide the files access, a MAO implementation is required.

    MAO implementation is a MAO's subclass designed in a unique way
    for an exact type of media storage. It can only be used for
    files operations with data in that type of storage. The implementation
    must be provided to the service's layer via factory to avoid using
    globals.
    """

    @abstractmethod
    async def update_cover(self, data: bytes, album_id: int) -> str:
        """
        Changes album cover

        :param album_id: album's numeric identificator
        :param data: file data in bytes format
        :return: cover's URL
        :raise NotImplementedError: when called directly by abstract class instance
        """
        raise NotImplementedError
