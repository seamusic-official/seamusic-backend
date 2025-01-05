from src.domain.music.albums.interfaces.ma.mao import MAO
from src.infrastructure.s3 import Session, unique_filename, get_file_stream


class S3MAOImplementation(MAO, Session):
    async def update_cover(self, data: bytes, album_id: int) -> str:
        cover_url = await self.update(
            path=f'/albums/',
            filename=unique_filename(str(album_id)),
            file_stream=get_file_stream(data=data),
        )
        return cover_url


def get_s3_mao_implementation() -> S3MAOImplementation:
    return S3MAOImplementation()
