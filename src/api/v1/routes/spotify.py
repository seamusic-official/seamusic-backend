import jmespath
from fastapi import APIRouter, status, Depends

from src.api.v1.schemas.base import Page, get_items_response
from src.api.v1.schemas.spotify import (
    SSpotifyTracksResponse,
    SpotifyTrack,
    SSpotifyTrackResponse,
    SSpotifyAlbumsResponse,
    SpotifyAlbum,
    SSpotifyAlbumResponse,
    SSpotifyAlbumTracksCountResponse,
    SSpotifyArtistResponse,
    SSpotifySearchResponse,
    SpotifyArtist,
)
from src.api.v1.utils.pages import get_page, get_has_next, get_has_previous
from src.enums.spotify import SpotifyType
from src.services.spotify import SpotifyService, get_spotify_service

spotify = APIRouter(prefix="/inspiration", tags=["Music & Albums"])


@spotify.get(
    path="/recommendations",
    summary="Get recommendations",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyTracksResponse,
)
async def get_recommendations(
    page: Page = Depends(Page),
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyTracksResponse:

    response = await service.get_recommendations(start=page.start, size=page.size)

    items = list(map(
        lambda track: SSpotifyTrackResponse(
            id=track.id,
            type=SpotifyType.track,
            name=track.title,
            preview_url=track.preview_url,
            image_url=track.image_url,
            spotify_url=track.href,
        ),
        response.tracks
    ))

    total = await service.get_recommendations_count()

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SSpotifyTracksResponse,
    )


@spotify.get(
    path="/tracks",
    summary="Get Spotify tracks by specified artist",
    response_model=SSpotifyTracksResponse,
    status_code=status.HTTP_200_OK,
)
async def get_top_artist_tracks(
    spotify_artist_id: str,
    page: Page = Depends(Page),
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyTracksResponse:

    response = await service.get_top_artist_tracks(artist_id=spotify_artist_id)

    items = list(map(
        lambda track: SpotifyTrack(
            id=track.id,
            type=SpotifyType.track,
            name=track.title,
            preview_url=track.preview_url,
            image_url=track.image_url,
            spotify_url=track.href,
        ),
        response.tracks
    ))

    total = await service.get_top_artist_tracks_count(artist_id=spotify_artist_id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SSpotifyTracksResponse,
    )


@spotify.get(
    path="/albums",
    summary="Get Spotify albums by artist",
    response_model=SSpotifyAlbumsResponse,
    status_code=status.HTTP_200_OK,
)
async def get_artist_albums(
    artist_id: str,
    page: Page = Depends(Page),
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyAlbumsResponse:

    response = await service.get_artist_albums(artist_id=artist_id, start=page.start, size=page.size)

    items = list(map(
        lambda album: SpotifyAlbum(
            id=album.id,
            name=album.title,
            image_url=jmespath.search('0', album.images),
            spotify_url=album.href,
        ),
        response.items
    ))

    total = await service.get_artist_albums_count(artist_id=artist_id)

    return get_items_response(
        start=page.start,
        size=page.size,
        total=total,
        items=items,
        response_model=SSpotifyAlbumsResponse,
    )


@spotify.get(
    path="/album/{album_id}",
    summary="Get Spotify album by ID",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyAlbumResponse,
)
async def get_spotify_album(
    album_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyAlbumResponse:

    album = await service.get_spotify_album(album_id=album_id)

    return SSpotifyAlbumResponse(
        id=album.id,
        name=album.name,
        image_url=jmespath.search('0', album.images),
        spotify_url=album.href,
        release_date=album.release_date,
        artists=list(map(
            lambda artist:
                SpotifyArtist(
                    id=artist.id,
                    type=artist.type,
                    name=artist.title,
                    image_url=jmespath.search('0', artist.images),
                    popularity=artist.popularity,
                ),
            album.artists
        )),
        external_urls=album.external_urls,
        uri=album.uri,
        album_type=album.type,
        total_tracks=album.total_tracks,
    )


@spotify.get(
    path="/tracks/{track_id}",
    summary="Get spotify track",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyTracksResponse,
)
async def get_spotify_track(
    track_id: str,
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifyTrackResponse:

    track = await service.get_spotify_track(track_id=track_id)

    return SSpotifyTrackResponse(
        id=track.id,
        type=track.type,
        name=track.name,
        preview_url=track.preview_url,
        image_url=track.image_url,
        spotify_url=track.href,
    )


@spotify.get(
    path="/album/{album_id}/tracks",
    summary="Get amount of tracks in album",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyAlbumTracksCountResponse,
)
async def get_album_tracks_count(
    album_id: str,
    service: SpotifyService = Depends(get_spotify_service)
) -> SSpotifyAlbumTracksCountResponse:

    return SSpotifyAlbumTracksCountResponse(count=await service.get_album_tracks_count(album_id=album_id))


@spotify.get(
    path="/artist/{artist_id}",
    summary="Get Spotify artist by ID",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifyArtistResponse,
)
async def get_spotify_artist(
    artist_id: str,
    service: SpotifyService = Depends(get_spotify_service)
) -> SSpotifyArtistResponse:

    artist = await service.get_spotify_artist(artist_id=artist_id)

    return SSpotifyArtistResponse(
        id=artist.id,
        external_urls=artist.external_urls,
        type=artist.type,
        name=artist.name,
        image_url=jmespath.search('0', artist.images),
        popularity=artist.popularity,
    )


@spotify.get(
    path="/spotify/search",
    summary="Search in spotify",
    status_code=status.HTTP_200_OK,
    response_model=SSpotifySearchResponse,
)
async def search(
    query: str,
    type_: SpotifyType,
    page: Page = Depends(Page),
    service: SpotifyService = Depends(get_spotify_service),
) -> SSpotifySearchResponse:

    result = await service.get_spotify_search(query=query, type_=type_, start=page.start, size=page.size)

    total = await service.get_spotify_search_count(query=query, type_=type_)

    return SSpotifySearchResponse(
        total=total,
        page=get_page(start=page.start, size=page.size),
        has_next=get_has_next(total=total, start=page.start, size=page.size),
        has_previous=get_has_previous(start=page.start, size=page.size),
        size=page.size,
        tracks=list(map(
            lambda track: SpotifyTrack(
                id=track.id,
                type=track.type,
                name=track.title,
                preview_url=track.preview_url,
                image_url=track.image_url,
                spotify_url=track.href,
            ),
            result.tracks
        )) if result.tracks else None,
        artists=list(map(
            lambda artist: SpotifyArtist(
                id=artist.id,
                type=artist.type,
                name=artist.title,
                image_url=artist.image_url,
                popularity=artist.popularity,
            ),
            result.artists
        )) if result.artists else None,
        albums=list(map(
            lambda album: SpotifyAlbum(
                id=album.id,
                name=album.title,
                image_url=jmespath.search('0', album.images),
                spotify_url=album.href,
            ),
            result.albums
        )) if result.albums else None,
    )
