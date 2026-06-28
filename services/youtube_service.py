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

def get_playlist_songs(youtube, playlist_id):

    songs = []

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )

    response = request.execute()

    for item in response["items"]:

        song = {
            "video_id": item["snippet"]["resourceId"]["videoId"],
            "title": item["snippet"]["title"]
        }

        songs.append(song)

    return songs

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

    return {
        "id": response["id"],
        "title": response["snippet"]["title"]
    }

def search_song(youtube, query):

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=1
    )

    response = request.execute()

    if len(response["items"]) == 0:
        return None

    item = response["items"][0]

    return {
        "video_id": item["id"]["videoId"],
        "title": item["snippet"]["title"]
    }

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