def get_channel_name(youtube):
    request = youtube.channels().list(
        part="snippet",
        mine=True
    )

    response = request.execute()

    return response["items"][0]["snippet"]["title"]

def get_playlists(youtube):

    playlists = []

    request = youtube.playlists().list(
        part="snippet",
        mine=True
    )

    response = request.execute()

    for item in response["items"]:

        playlist = {
            "id": item["id"],
            "title": item["snippet"]["title"]
        }

        playlists.append(playlist)

    return playlists

# ==========================
# Clean Song Title
# ==========================

import re

def clean_title(title):

    patterns = [
        r"\(Official Video\)",
        r"\(Official Music Video\)",
        r"\(Official MV\)",
        r"\(Lyrics\)",
        r"\(Lyric Video\)",
        r"\(Audio\)",
        r"\(Visualizer\)",
        r"\[Official Video\]",
        r"\[Lyrics\]",
        r"\[Audio\]",
        r"\|.*",
        r"HD",
        r"4K"
    ]

    for pattern in patterns:
        title = re.sub(
            pattern,
            "",
            title,
            flags=re.IGNORECASE
        )

    return title.strip()

# ==========================
# Extract Artist
# ==========================

# ==========================
# Clean Artist
# ==========================

def clean_artist(artist):

    artist = artist.replace("- Topic", "")

    return artist.strip()

# ==========================
# Get Playlist Songs
# ==========================

def get_playlist_songs(youtube, playlist_id):

    songs = []

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )

    response = request.execute()

    for item in response["items"]:

        title = clean_title(
            item["snippet"]["title"]
        )

        artist = clean_artist(
            item["snippet"].get(
                "videoOwnerChannelTitle",
                ""
            )
        )

        songs.append({
            "title": title,
            "artist": artist
        })

    return songs

# ==========================
# Create Playlist
# ==========================

def create_playlist(youtube, title):

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )

    response = request.execute()

    return response["id"]

# ==========================
# Search Song
# ==========================

def search_song(youtube, title, artist):

    request = youtube.search().list(
        part="snippet",
        q=f"{title} {artist}",
        type="video",
        maxResults=1
    )

    response = request.execute()

    if len(response["items"]) == 0:
        return None

    return response["items"][0]["id"]["videoId"]

def add_song_to_playlist(youtube, playlist_id, video_id):

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )

    request.execute()

    return True