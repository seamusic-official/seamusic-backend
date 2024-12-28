from dataclasses import dataclass
from typing import AsyncGenerator

from sqlalchemy import select, func

from src.app.auth.artists.models import ArtistProfile
from src.app.music.albums.models import Album
from src.app.social.tags.models import Tag
from src.domain.music.albums.dao import BaseDAO, BaseDAOSession
from src.infrastructure.postgres.client import PostgresSessionMixin


@dataclass
class PostgresDAOImplementationSession(PostgresSessionMixin, BaseDAOSession):
    table = Album

    async def get_album_by_id(self, **kwargs) -> dict | None:
        """
        :type album_id: int
        """

        response: Album | None = await self.read(obj_id=kwargs['album_id'])
        return {
            'id': response.id,
            'title': response.title,
            'picture_url': response.picture_url,
            'description': response.description,
            'type': response.type,
            'views': len(response.viewers_ids),
            'likes': len(response.likers_ids),
            'viewers_ids': response.viewers_ids,
            'likers_ids': response.likers_ids,
            'created_at': response.created_at,
            'updated_at': response.updated_at,
            'artists': list(map(lambda artist: {
                'id': artist.id,
                'username': artist.username,
                'description': artist.description,
                'picture_url': artist.picture_url,
                'user_id': artist.user_id,
            }, response.artists)),
            'tracks': list(map(lambda track: {
                'id': track.id,
                'title': track.title,
                'description': track.description,
                'picture_url': track.picture_url,
                'file_url': track.file_url,
                'views': len(track.viewers_ids),
                'likes': len(track.likers_ids),
                'created_at': track.created_at,
                'updated_at': track.updated_at,
            }, response.artists)),
            'tags': list(map(lambda tag: tag.title, response.tags))
        } if response else None

    async def get_album_existance(self, **kwargs) -> bool:
        """
        :type title: str
        :type artist_id: int
        """

        return bool(await self.run(
            select(Album).filter(Album.title == kwargs['title'], Album.artists.any() == kwargs['artist_id']), 'scalar'))

    async def get_popular_albums(self, **kwargs) -> list[dict]:
        """
        :type start: int
        :type size: int
        """

        return list(map(
            lambda album: {
                'id': album.id,
                'title': album.title,
                'picture_url': album.picture_url,
                'description': album.description,
                'views': len(album.viewers_ids),
                'likes': len(album.likers_ids),
                'type': album.type,
                'created_at': album.created_at,
                'updated_at': album.updated_at
            },
            await self.run(
                select(Album).order_by(func.count(Album.viewers_ids)).offset(kwargs['start'] - 1).limit(kwargs['size']),
                'scalars')
        ))

    async def count_albums(self) -> int:
        return await self.run(select(func.count(Album)), 'scalar')

    async def get_artist_id_by_user_id(self, **kwargs) -> int | None:
        """
        :type user_id: int
        """

        return await self.run(select(ArtistProfile.id).filter(ArtistProfile.user_id == kwargs['user_id']), 'scalar')

    async def create_album(self, **kwargs) -> int:
        """
        :type title: str
        :type picture_url: str | None
        :type description: str | None
        :type type: AlbumType
        :type created_at: date
        :type updated_at: datetime
        :type artists_ids: list[int]
        :type tags: list[str]
        """

        artists = list(
            await self.run(select(ArtistProfile).filter(ArtistProfile.id.in_(kwargs['artists_ids'])), 'scalars'))
        tags = list(await self.run(select(Tag).filter(Tag.name.in_(kwargs['tags'])), 'scalars'))
        album = Album(
            title=kwargs['title'],
            picture_url=kwargs['picture_url'],
            description=kwargs['description'],
            type=kwargs['type'],
            created_at=kwargs['created_at'],
            updated_at=kwargs['updated_at'],
            viewers_ids=list(),
            likers_ids=list(),
            artists=artists,
            tracks=list(),
            tags=tags,
        )
        await self.write(album)
        return album.id

    async def update_album(self, **kwargs) -> int:
        """
        :type album_id: int
        :type title: str | None
        :type picture_url: str | None
        :type description: str | None
        :type type: AlbumType | None
        :type updated_at: datetime | None
        :type viewer_ids: list[int] | None
        :type likers_ids: list[int] | None
        :type artists_ids: list[int] | None
        :type tracks_ids: list[int] | None
        :type tags: list[str] | None
        """

        request = dict(filter(lambda item: item[1] is not None, {
            'id': kwargs.get('album_id'),
            'title': kwargs.get('title'),
            'picture_url': kwargs.get('picture_url'),
            'description': kwargs.get('description'),
            'type': kwargs.get('type'),
            'updated_at': kwargs.get('updated_at'),
            'viewers_ids': kwargs.get('viewer_ids'),
            'likers_ids': kwargs.get('likers_ids'),
            'artists_ids': kwargs.get('artists_ids'),
            'tracks_ids': kwargs.get('tracks_ids'),
            'tags': list(await self.run(select(Tag).filter(Tag.name.in_(kwargs['tags'])), 'scalars')) if kwargs.get(
                'tags') else None,
        }.items()))
        album = Album(**request)
        await self.update(album)
        return album.id

    async def delete_album(self, **kwargs) -> None:
        """
        :type album_id: int
        """

        album = await self.read(obj_id=kwargs['album_id'])
        if album:
            await self.remove(obj_id=kwargs['album_id'])


@dataclass
class PostgresDAOImplementation(BaseDAO):
    async def open(self) -> AsyncGenerator[PostgresDAOImplementationSession]:
        async with PostgresDAOImplementationSession(table=Album) as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()


def get_postgres_dao() -> PostgresDAOImplementation:
    return PostgresDAOImplementation()
