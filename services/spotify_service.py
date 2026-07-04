import requests

# ==========================
# Get Request Headers
# ==========================

def get_headers(spotify):

    token = spotify.auth_manager.get_access_token(as_dict=False)

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# ==========================
# Get User Playlists
# ==========================

def get_playlists(spotify):

    url = "https://api.spotify.com/v1/me/playlists"

    response = requests.get(
        url,
        headers=get_headers(spotify)
    )

    if response.status_code != 200:
        return None

    data = response.json()

    playlists = []

    for playlist in data["items"]:
        playlists.append({
            "id": playlist["id"],
            "name": playlist["name"]
        })

    return playlists

# ==========================
# Get Playlist Songs
# ==========================

def get_playlist_songs(spotify, playlist_id):


    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/items"

    response = requests.get(
        url,
        headers=get_headers(spotify)
    )

    if response.status_code != 200:
        return None

    data = response.json()

    songs = []

    for item in data["items"]:

        track = item["item"]

        if track is None:
            continue

        songs.append({
            "title": track["name"],
            "artist": track["artists"][0]["name"]
        })

    return songs

# ==========================
# Create Playlist
# ==========================

def create_playlist(spotify, title):

    url = "https://api.spotify.com/v1/me/playlists"

    data = {
        "name": title,
        "description": "Created using Universal Playlist Transfer",
        "public": False
    }

    response = requests.post(
        url,
        headers=get_headers(spotify),
        json=data
    )

    if response.status_code != 201:
        return None

    return response.json()["id"]

# ==========================
# Search Song
# ==========================

def search_song(spotify, title, artist):

    url = "https://api.spotify.com/v1/search"

    params = {
        "q": f"{title} {artist}",
        "type": "track",
        "limit": 1
    }

    response = requests.get(
        url,
        headers=get_headers(spotify),
        params=params
    )

    if response.status_code != 200:
        return None

    data = response.json()

    tracks = data["tracks"]["items"]

    if len(tracks) == 0:
        return None

    return tracks[0]["id"]

# ==========================
# Add Song To Playlist
# ==========================

def add_song_to_playlist(spotify, playlist_id, track_id):

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/items"

    data = {
        "uris": [
            f"spotify:track:{track_id}"
        ]
    }

    response = requests.post(
        url,
        headers=get_headers(spotify),
        json=data
    )

    if response.status_code != 201:
        return False

    return True