from src.models.albums import Album, album_track_association, artist_profile_album_association
from src.models.auth import User, artist_profile_tags_association, producer_profile_tags_association, ArtistProfile, \
    ProducerProfile, user_to_playlists_association, user_comments_association, squad_producer_profile_association, \
    artist_profile_album_association, artist_profile_track_association
from src.models.beatpacks import Beatpack, beats_to_beatpacks_association_table
from src.models.beats import Beat
from src.models.comments import BaseComment
from src.models.licenses import License, user_to_licenses_association
from src.models.playlists import Playlists, user_to_playlists_association
from src.models.soundkits import Soundkit, user_to_soundkits_association_table
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear
