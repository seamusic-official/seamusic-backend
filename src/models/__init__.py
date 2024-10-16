from src.models.albums import Album, album_to_track_association, \
    album_to_tag_association, album_to_artist_association
from src.models.auth import User, artist_to_tags_association, producer_to_tags_association, ArtistProfile, \
    ProducerProfile, user_to_playlists_association, \
    artist_to_album_association, artist_to_track_association, user_to_albums_association, user_to_artist_association
from src.models.beatpacks import Beatpack, beatpack_to_tag_association, beatpack_to_beat_association_table, \
    beatpacks_to_producer_association_table
from src.models.beats import Beat, producer_to_beat_association, tag_to_beat_association
from src.models.comments import BaseComment , user_to_comments_association
from src.models.licenses import License
from src.models.playlists import Playlists, playlists_to_tag_association, playlists_to_track_association, \
    playlists_to_beat_association, playlist_to_user_association
from src.models.soundkits import Soundkit, tag_to_soundkits_association, beat_to_soundkits_association
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear
