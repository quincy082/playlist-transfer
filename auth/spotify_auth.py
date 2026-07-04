import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

SCOPES = (
    "playlist-read-private "
    "playlist-modify-private "
    "playlist-modify-public"
)


class SpotifyClient:

    def __init__(self, spotify, auth_manager):
        self.spotify = spotify
        self.auth_manager = auth_manager


def authenticate():

    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPES
    )

    spotify = spotipy.Spotify(
        auth_manager=auth_manager
    )

    return spotify