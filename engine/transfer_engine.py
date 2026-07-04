# ==========================
# Transfer Playlist
# ==========================

def transfer_playlist(
    source_client,
    source_service,
    destination_client,
    destination_service,
    source_playlist_id,
    destination_playlist_name
):

    songs = source_service.get_playlist_songs(
        source_client,
        source_playlist_id
    )

    destination_playlist_id = destination_service.create_playlist(
        destination_client,
        destination_playlist_name
    )

    total = len(songs)
    transferred = 0
    failed = 0

    for song in songs:

        track_id = destination_service.search_song(
            destination_client,
            song["title"],
            song["artist"]
        )

        if track_id is None:
            failed += 1
            continue

        success = destination_service.add_song_to_playlist(
            destination_client,
            destination_playlist_id,
            track_id
        )

        if success:
            transferred += 1
        else:
            failed += 1

    return {
        "total": total,
        "transferred": transferred,
        "failed": failed
    }