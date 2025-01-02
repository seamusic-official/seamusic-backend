from dataclasses import dataclass

from src.app.music.albums.core.dtos import AlbumResponseDTO, AlbumItemResponseDTO
from src.app.music.albums.da.models import Album
from src.domain.music.albums.core.converter import BaseConverter
from src.domain.music.albums.da.dao import DAO


@dataclass
class ModelsConverter(BaseConverter):
    dao_implementation: DAO

    @staticmethod
    async def album_response(album: Album) -> AlbumResponseDTO:
        return AlbumResponseDTO(
            id=album.id,
            title=album.title,
            picture_url=album.picture_url,
            description=album.description,
            type=album.type,
            views=len(album.viewers_ids),
            likes=len(album.likers_ids),
            created_at=album.created_at,
            updated_at=album.updated_at,
            artists=album.artists,
            tracks=album.tracks,
            tags=album.tags,
        )

    @staticmethod
    async def album_existance_response(existance: bool) -> bool:
        return existance

    @staticmethod
    async def popular_albums_response(albums: list[Album]) -> list[AlbumItemResponseDTO]:
        return list(map(
            lambda album: AlbumItemResponseDTO(
                id=album.id,
                title=album.title,
                picture_url=album.picture_url,
                description=album.description,
                views=len(album.viewers_ids),
                likes=len(album.likers_ids),
                type=album.type,
                created_at=album.created_at,
                updated_at=album.updated_at,
            ),
            albums,
        ))

    @staticmethod
    async def count_albums_response(amount: int) -> dict:
        return {'amount': amount}

    @staticmethod
    async def artist_id_response(artist_id: int | None) -> int | None:
        return artist_id

    @staticmethod
    async def create_album_response(album_id: int) -> dict:
        return {'album_id': album_id}

    @staticmethod
    async def update_album_response(album_id: int) -> dict:
        return {'album_id': album_id}

    @staticmethod
    async def delete_album_response() -> None:
        return None


def get_from_models_converter() -> type[ModelsConverter]:
    return ModelsConverter
