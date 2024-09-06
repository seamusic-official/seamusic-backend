from enum import Enum


class Type(str, Enum):
    album = 'album'
    artist = 'artist'
    beat = 'beat'
    beatpack = 'beatpack'
    license = 'license'
    soundkit = 'soundkit'
    producer = 'producer'
    track = 'track'
    user = 'user'
