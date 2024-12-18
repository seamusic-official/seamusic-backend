from src.services.auth.artists.models import ArtistProfile, artist_to_tags_association, artist_to_track_association, \
    user_to_artist_association  # noqa: F821
from src.services.auth.producers.models import ProducerProfile, producer_to_tags_association, \
    producer_to_beatpacks_association, producer_to_soundkits_association, user_to_producer_association  # noqa: F821
from src.services.auth.users.models import User, user_to_tag_association, user_to_albums_association, \
    user_to_playlists_association, user_to_licenses_association, user_to_artist_association, \
    user_to_producer_association  # noqa: F821
from src.services.music.albums.models import Album, album_to_artist_association, album_to_tag_association, \
    album_to_track_association, user_to_albums_views_association, user_to_albums_likes  # noqa: F821
from src.services.music.beatpacks.models import Beatpack, user_to_beatpacks_likes, user_to_beatpacks_views_association, \
    beatpack_to_tag_association, beatpack_to_beat_association_table, producer_to_beatpacks_association  # noqa: F821
from src.services.music.beats.models import Beat, tag_to_beat_association, producer_to_beat_association, \
    user_to_beats_views_association, user_to_beats_likes  # noqa: F821
from src.services.music.soundkits.models import Soundkit, user_to_soundkits_likes, user_to_soundkits_views_association, \
    tag_to_soundkits_association, beat_to_soundkits_association, producer_to_soundkits_association  # noqa: F821
from src.services.music.squads.models import Squad, follower_to_squads_association, artist_to_squad_association, \
    producer_to_squad_association  # noqa: F821
from src.services.music.tracks.models import Track, track_to_tag_association, track_to_producer_association, \
    user_to_tracks_views_association, user_to_tracks_likes  # noqa: F821
from src.services.social.chats.models import Chat, user_to_chat_association, message_to_chat_association  # noqa: F821
from src.services.social.comments.models import Comment, user_to_comments_association  # noqa: F821
from src.services.social.licenses.models import License, user_to_licenses_association  # noqa: F821
from src.services.social.messages.models import Message, user_to_message_association, \
    message_to_chat_association  # noqa: F821
from src.services.social.notifications.models import Notification  # noqa: F821
from src.services.social.playlists.models import Playlist, playlists_to_tag_association, playlists_to_beat_association, \
    playlists_to_track_association, author_to_playlists_association, user_to_playlists_views_association, \
    user_to_playlists_likes  # noqa: F821
from src.services.social.tags.models import Tag  # noqa: F821
