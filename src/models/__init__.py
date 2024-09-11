from src.models.albums import Album, album_track_association, artist_profile_album_association
from src.models.beatpacks import Beatpack, user_to_beatpacks_association_table, beats_to_beatpacks_association_table
from src.models.beats import Beat
from src.models.comments import BaseComment
from src.models.licenses import License, user_to_licenses_association
from src.models.messages import Message, Chat
from src.models.notifications import Notification
from src.models.soundkits import Soundkit, user_to_soundkits_association_table
from src.models.squads import Squad, squad_producer_profile_association, squad_artist_profile_association
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear
from src.models.tags import Tag, artist_tags_association, producer_tags_association, listener_tags_association
from src.models.tracks import Track, artist_profile_track_association, album_track_association
