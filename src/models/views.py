from sqlalchemy import Column, Table, ForeignKey

from src.models.base import Base


user_to_albums_views_association = Table(
    "user_to_views_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("album_id", ForeignKey("albums.id"), primary_key=True)
)

user_to_beatpacks_views_association = Table(
    "user_to_beatpacks_views_association",
    Base.metadata,
    Column("beatpacks_id", ForeignKey("beatpacks.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

user_to_beats_views_association = Table(
    "user_to_beats_views_association",
    Base.metadata,
    Column("beat_id", ForeignKey("beats.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

user_to_playlists_views_association = Table(
    "user_to_playlists_views_association",
    Base.metadata,
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

user_to_soundkits_views_association = Table(
    "user_to_soundkits_views_association",
    Base.metadata,
    Column("soundkit_id", ForeignKey("soundkits.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

user_to_tracks_views_association = Table(
    "user_to_tracks_views_association",
    Base.metadata,
    Column("track_id", ForeignKey("tracks.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)
