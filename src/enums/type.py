from enum import Enum


class Type(str, Enum):
    album = 'album'
    track = 'track'
    beat = 'beat'
