from enum import Enum


class SpotifyType(str, Enum):
    album = "album"
    artist = "artist"
    track = "track"


class SpotifyAlbumType(str, Enum):
    album = "album"
    single = "single"
    compilation = "compilation"
