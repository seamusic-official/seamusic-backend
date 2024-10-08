from src.models.albums import Album, album_to_track_association, \
    album_to_tag_association, album_to_artist_association
from src.models.auth import User, artist_to_tags_association, producer_to_tags_association, ArtistProfile, \
    ProducerProfile, user_to_playlists_association, user_to_comments_association, squad_to_producer_association, \
    artist_to_album_association, artist_to_track_association
from src.models.beatpacks import Beatpack, beats_to_beatpacks_association_table
from src.models.beats import Beat
from src.models.comments import BaseComment
from src.models.licenses import License, user_to_licenses_association
from src.models.playlists import Playlists, playlists_to_tag_association, playlists_to_track_association, \
    playlists_to_beat_association
from src.models.soundkits import Soundkit, user_to_soundkits_association_table
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear
