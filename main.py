from auth.youtube_auth import authenticate as youtube_auth
from auth.spotify_auth import authenticate as spotify_auth

from services import youtube_service
from services import spotify_service

from engine.transfer_engine import transfer_playlist


print("========================================")
print("   UNIVERSAL PLAYLIST TRANSFER")
print("========================================")
print("1. YouTube  → YouTube")
print("2. YouTube  → Spotify")
print("3. Spotify  → YouTube")
print("4. Spotify  → Spotify")
print("========================================")

choice = int(input("Enter your choice: "))


# ==========================
# YouTube -> YouTube
# ==========================

if choice == 1:

    source_client = youtube_auth()
    destination_client = youtube_auth()

    source_service = youtube_service
    destination_service = youtube_service

    playlists = source_service.get_playlists(source_client)

    print("\nYour YouTube Playlists:\n")

    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['title']}")

    index = int(input("\nEnter playlist number: "))
    source_playlist_id = playlists[index - 1]["id"]

    destination_playlist_name = input(
        "\nEnter new YouTube playlist name: "
    )


# ==========================
# YouTube -> Spotify
# ==========================

elif choice == 2:

    source_client = youtube_auth()
    destination_client = spotify_auth()

    source_service = youtube_service
    destination_service = spotify_service

    playlists = source_service.get_playlists(source_client)

    print("\nYour YouTube Playlists:\n")

    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['title']}")

    index = int(input("\nEnter playlist number: "))
    source_playlist_id = playlists[index - 1]["id"]

    destination_playlist_name = input(
        "\nEnter Spotify playlist name: "
    )


# ==========================
# Spotify -> YouTube
# ==========================

elif choice == 3:

    source_client = spotify_auth()
    destination_client = youtube_auth()

    source_service = spotify_service
    destination_service = youtube_service

    playlists = source_service.get_playlists(source_client)

    print("\nYour Spotify Playlists:\n")

    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['name']}")

    index = int(input("\nEnter playlist number: "))
    source_playlist_id = playlists[index - 1]["id"]

    destination_playlist_name = input(
        "\nEnter YouTube playlist name: "
    )


# ==========================
# Spotify -> Spotify
# ==========================

elif choice == 4:

    source_client = spotify_auth()
    destination_client = spotify_auth()

    source_service = spotify_service
    destination_service = spotify_service

    playlists = source_service.get_playlists(source_client)

    print("\nYour Spotify Playlists:\n")

    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['name']}")

    index = int(input("\nEnter playlist number: "))
    source_playlist_id = playlists[index - 1]["id"]

    destination_playlist_name = input(
        "\nEnter new Spotify playlist name: "
    )


else:
    print("\nInvalid Choice!")
    exit()


# ==========================
# Transfer Playlist
# ==========================

report = transfer_playlist(
    source_client,
    source_service,
    destination_client,
    destination_service,
    source_playlist_id,
    destination_playlist_name
)


# ==========================
# Final Report
# ==========================

print("\n========== TRANSFER REPORT ==========")
print(f"Total Songs      : {report['total']}")
print(f"Transferred      : {report['transferred']}")
print(f"Failed           : {report['failed']}")