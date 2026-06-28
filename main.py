from auth.youtube_auth import authenticate
from services.youtube_service import get_playlists
from engine.transfer_engine import transfer_playlist

youtube = authenticate()

playlists = get_playlists(youtube)

print("\n===== YOUR PLAYLISTS =====")

for i, playlist in enumerate(playlists, start=1):
    print(f"{i}. {playlist['title']}")

choice = int(input("\nSelect playlist to transfer: "))

playlist_id = playlists[choice - 1]["id"]

new_title = input("Enter new playlist name: ")

report = transfer_playlist(
    youtube,
    playlist_id,
    new_title
)

print("\n========== TRANSFER REPORT ==========")
print(f"Total Songs : {report['total']}")
print(f"Transferred : {report['transferred']}")
print(f"Failed      : {report['failed']}")
print("=====================================")