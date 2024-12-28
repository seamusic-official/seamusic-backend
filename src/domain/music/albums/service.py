from abc import ABC, abstractmethod

from src.domain.music.albums.dao import BaseDAO
from src.domain.music.albums.dtos import BaseRequestDTO, BaseResponseDTO


class BaseService(ABC):
    dao: BaseDAO

    @abstractmethod
    async def get_album(self, request: BaseRequestDTO) -> BaseResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, page: BaseRequestDTO) -> BaseResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def create_album(self, request: BaseRequestDTO) -> BaseResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def update_album(self, request: BaseRequestDTO) -> BaseResponseDTO:
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, request: BaseRequestDTO) -> None:
        raise NotImplementedError
