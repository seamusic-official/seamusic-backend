from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import BytesIO


@dataclass
class BaseMediaRepository(ABC):
    @abstractmethod
    async def upload_file(self, folder: str, filename: str, file_stream: BytesIO) -> str:
        ...

    @abstractmethod
    async def delete_file(self, folder: str, filename: str) -> None:
        ...
