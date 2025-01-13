from types import TracebackType
from typing import Self

from src.domain.music.albums.interfaces.ma.mao import MAO
from src.infrastructure.s3 import Session, unique_filename, get_file_stream


class S3MAOImplementation(MAO, Session):
    async def update_cover(self, data: bytes, album_id: int) -> str:
        cover_url = await self.update(
            path='/albums/',
            filename=unique_filename(str(album_id)),
            file_stream=get_file_stream(data=data),
        )
        return cover_url

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[Exception] | None = None,
        exc_val: Exception | None = None,
        exc_tb: TracebackType | None = None,
    ) -> None:
        pass


def get_s3_mao_implementation() -> S3MAOImplementation:
    return S3MAOImplementation()
