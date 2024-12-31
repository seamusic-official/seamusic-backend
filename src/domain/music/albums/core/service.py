from abc import ABC, abstractmethod

from src.domain.music.albums.core.converter import BaseConverter as CoreConverter
from src.domain.music.albums.core.dtos import BaseRequestDTO, BaseResponseDTO
from src.domain.music.albums.da.converter import BaseConverter as DAConverter
from src.domain.music.albums.da.dao import DAO


class BaseService(ABC):
    dao_impl: type[DAO]
    dao_converter: type[DAConverter]
    core_converter: type[CoreConverter]

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
