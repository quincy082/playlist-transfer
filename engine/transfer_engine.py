from services.youtube_service import (
    get_playlist_songs,
    create_playlist,
    search_song,
    add_song_to_playlist
)


def transfer_playlist(
    youtube,
    source_playlist_id,
    destination_title
):

    songs = get_playlist_songs(youtube, source_playlist_id)

    new_playlist = create_playlist(youtube, destination_title)

    success = 0
    failed = 0

    for i, song in enumerate(songs, start=1):

        print(f"[{i}/{len(songs)}] Searching: {song['title']}")

        try:
            result = search_song(youtube, song["title"])

            if result is None:
                print(f"[{i}/{len(songs)}] ❌ Song not found")
                failed += 1
                continue

            add_song_to_playlist(
                youtube,
                new_playlist["id"],
                result["video_id"]
            )

            print(f"[{i}/{len(songs)}] ✅ Added: {song['title']}")
            success += 1

        except Exception as e:
            print(f"[{i}/{len(songs)}] ❌ Failed: {song['title']}")
            print(e)
            failed += 1

    report = {
    "total": len(songs),
    "transferred": success,
    "failed": failed
    }

    return report