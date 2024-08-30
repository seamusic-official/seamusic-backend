from src.models.albums import Album, album_track_association, artist_profile_album_association # type: ignore
from src.models.beatpacks import Beatpack, user_to_beatpacks_association_table, beats_to_beatpacks_association_table # type: ignore
from src.models.beats import Beat # type: ignore
from src.models.comments import BaseComment # type: ignore
from src.models.licenses import License, user_to_licenses_association # type: ignore
from src.models.messages import Message, Chat # type: ignore
from src.models.notifications import Notification # type: ignore
from src.models.soundkits import Soundkit # type: ignore 
from src.models.squads import Squad, squad_producer_profile_association, squad_artist_profile_association # type: ignore 
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear # type: ignore 
from src.models.tags import Tag, artist_tags_association, producer_tags_association, listener_tags_association # type: ignore
from src.models.tracks import Track, artist_profile_track_association, album_track_association # type: ignore
