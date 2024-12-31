from dataclasses import dataclass
from typing import Self

from sqlalchemy import select, func

from src.app.auth.artists.models import ArtistProfile
from src.app.music.albums.da.models import Album
from src.domain.music.albums.da.dao import DAO
from src.infrastructure.postgres.client import PostgresSessionMixin


@dataclass
class PostgresDAOImplementation(PostgresSessionMixin, DAO):
    table: type[Album] = Album

    async def get_album_by_id(self, album_id: int) -> Album | None:
        response: Album | None = await self.read(obj_id=album_id)
        return response

    async def get_album_existance(self, title: str, artist_id: int) -> bool:
        return bool(await self.run(select(Album).filter(Album.title == title, Album.artists.any() == artist_id), 'scalar'))

    async def get_popular_albums(self, offset: int, limit: int) -> list[Album]:
        return await self.run(select(Album).order_by(func.count(Album.viewers_ids)).offset(offset).limit(limit), 'scalars')

    async def count_albums(self) -> int:
        return await self.run(select(func.count(Album)), 'scalar')

    async def get_artist_id_by_user_id(self, user_id: int) -> int | None:
        return await self.run(select(ArtistProfile.id).filter(ArtistProfile.user_id == user_id), 'scalar')

    async def create_album(self, album: Album) -> int:
        await self.write(album)
        return album.id

    async def update_album(self, album: Album) -> int:
        await self.update(album)
        return album.id

    async def delete_album(self, album_id: int) -> None:
        await self.remove(obj_id=album_id)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.commit()
        await self.close()


def get_postgres_dao_implementation() -> type[PostgresDAOImplementation]:
    return PostgresDAOImplementation
