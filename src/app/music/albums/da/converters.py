from dataclasses import dataclass
from datetime import date, datetime

from sqlalchemy import select

from src.app.auth.artists.models import ArtistProfile
from src.app.music.albums.da.dao import PostgresDAOImplementation
from src.app.music.albums.da.models import Album
from src.app.music.tracks.models import Track
from src.app.social.tags.models import Tag
from src.domain.music.albums.da.converter import BaseConverter


@dataclass
class DTOConverter(BaseConverter):
    dao_implementation: PostgresDAOImplementation

    @staticmethod
    async def album_request(album_id: int) -> dict:
        return {'album_id': album_id}

    @staticmethod
    async def album_existance_request(title: str, artist_id: int) -> dict:
        return {'title': title, 'artist_id': artist_id}

    @staticmethod
    async def count_albums_request() -> dict:
        return dict()

    @staticmethod
    async def popular_albums_request(start: int, size: int) -> dict:
        return {'offset': start - 1, 'limit': size}

    @staticmethod
    async def artist_id_by_user_id_request(user_id: int) -> dict:
        return {'user_id': user_id}

    async def create_album_request(
        self,
        title: str,
        picture_url: str,
        description: str,
        album_type: str,
        created_at: date,
        updated_at: datetime,
        viewers_ids: list[int],
        likers_ids: list[int],
        artists_ids: list[int],
        tracks_ids: list[int],
        tags: list[str],
    ) -> dict:
        return {'album': Album(
            title=title,
            picture_url=picture_url,
            description=description,
            type=album_type,
            created_at=created_at,
            updated_at=updated_at,
            viewers_ids=viewers_ids,
            likers_ids=likers_ids,
            artists=await self.dao_implementation.run(select(ArtistProfile).filter(ArtistProfile.id.in_(artists_ids)), 'scalars'),
            tracks=await self.dao_implementation.run(select(Track).filter(Track.id.in_(tracks_ids)), 'scalars'),
            tags=await self.dao_implementation.run(select(Tag).filter(Tag.name.in_(tags)), 'scalars'),
        )}

    async def update_album_request(
        self,
        album_id: int,
        title: str | None = None,
        picture_url: str | None = None,
        description: str | None = None,
        album_type: str | None = None,
        updated_at: datetime | None = None,
        viewers_ids: list[int] | None = None,
        likers_ids: list[int] | None = None,
        artists_ids: list[int] | None = None,
        tracks_ids: list[int] | None = None,
        tags: list[str] | None = None,
    ) -> dict:
        return dict(filter(
            lambda item: bool(item),
            {'album': Album(
                id=album_id,
                title=title,
                picture_url=picture_url,
                description=description,
                type=album_type,
                updated_at=updated_at,
                viewers_ids=viewers_ids,
                likers_ids=likers_ids,
                artists=await self.dao_implementation.run(select(ArtistProfile).filter(ArtistProfile.id.in_(artists_ids)), 'scalars') if artists_ids else None,
                tracks=await self.dao_implementation.run(select(Track).filter(Track.id.in_(tracks_ids)), 'scalars') if tracks_ids else None,
                tags=await self.dao_implementation.run(select(Tag).filter(Tag.name.in_(tags)), 'scalars') if tags else None,
            )}.items()
        ))

    @staticmethod
    async def delete_album_request(album_id: int) -> dict:
        return {'album_id': album_id}


def get_from_dto_converter() -> type[DTOConverter]:
    return DTOConverter
