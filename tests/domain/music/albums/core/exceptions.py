class AlbumNotFoundError(Exception):
    """Album not found"""


class AlbumAlreasyExistsError(Exception):
    """Album already exists"""


class NoArtistRightsError(Exception):
    """You are not an artist"""


class ArtistNotFoundError(Exception):
    """Artist not found"""
