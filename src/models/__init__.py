from src.models.albums import (Album, album_track_association,
                               album_user_association,
                               artist_profile_album_association)
from src.models.auth import (ArtistProfile, ProducerProfile, User,
                             user_comments_association)
from src.models.beatpacks import (Beatpack,
                                  beats_to_beatpacks_association_table,
                                  producer_profile_beatpack_association,
                                  user_to_beatpacks_association_table)
from src.models.beats import (Beat, playlist_beat_association,
                              producer_profile_beat_association)
from src.models.comments import BaseComment
from src.models.licenses import License, user_to_licenses_association
from src.models.playlists import Playlist, user_to_playlists_association
from src.models.soundkits import (Soundkit,
                                  producer_profile_soundkit_association,
                                  user_to_soundkits_association_table)
from src.models.squads import (Squad, squad_admin_association,
                               squad_artist_profile_association,
                               squad_producer_profile_association)
from src.models.subscriptions import (OnlyTelegramSubscribeMonth,
                                      OnlyTelegramSubscribeYear,
                                      TelegramAccount)
from src.models.tags import (Tag, album_tags_association,
                             artist_profile_tags_association,
                             playlist_tags_association,
                             producer_profile_tags_association,
                             track_tags_association,
                             user_followed_tags_association)
from src.models.tracks import (Track, artist_profile_track_association,
                               playlist_track_association,
                               user_liked_track_association)
