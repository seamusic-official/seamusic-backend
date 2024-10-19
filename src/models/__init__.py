from src.models.albums import Album, album_to_track_association, album_to_tag_association, album_to_artist_association
from src.models.auth import (
    ArtistProfile,
    ProducerProfile,
    User,
    album_to_artist_association,
    artist_to_tags_association,
    artist_to_track_association,
    producer_to_beat_association,
    producer_to_beatpacks_association,
    producer_to_soundkits_association,
    producer_to_squad_association,
    producer_to_tags_association,
    user_to_albums_association,
    user_to_artist_association,
    user_to_licenses_association,
    user_to_playlists_association,
    user_to_producer_association,
)
from src.models.beatpacks import Beatpack, beatpack_to_tag_association, beatpack_to_beat_association_table
from src.models.beats import Beat, tag_to_beat_association
from src.models.chat import Chat, user_to_chat_association
from src.models.comments import Comment, user_to_comments_association
from src.models.licenses import License
from src.models.messages import Message, user_to_message_association
from src.models.notifications import Notification
from src.models.playlists import (
    Playlist,
    playlists_to_tag_association,
    playlists_to_track_association,
    playlists_to_beat_association,
    user_to_playlists_association,
)
from src.models.soundkits import (
    Soundkit,
    tag_to_soundkits_association,
    beat_to_soundkits_association,
    producer_to_soundkits_association,
)
from src.models.squads import Squad, admin_producer_to_squad, producer_to_squad_association
from src.models.tags import Tag
from src.models.tracks import Track, track_to_tag_association, track_to_producer_association
