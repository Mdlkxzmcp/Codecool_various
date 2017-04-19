def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = []
    if songs[0][2] > max_size:
        return playlist
    else:
        current_size = songs[0][2]
        playlist.append(songs[0][0])
        other_songs = sorted(songs[1:], key=lambda x: x[2])
        for song in other_songs:
            if song[0] not in playlist and current_size + song[2] <= max_size:
                playlist.append(song[0])
                current_size += song[2]
        return playlist

songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 12.2
assert song_playlist(songs, max_size) == ['Roar', 'Wannabe', 'Timber']
songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 11
assert song_playlist(songs, max_size) == ['Roar', 'Wannabe']
print("win")
