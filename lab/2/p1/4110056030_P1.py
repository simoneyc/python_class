# 讀入
with open("data.txt", "r") as f:
    m, n, a, b = map(int, f.readline().split())
    fan_preferences = [list(map(int, f.readline().split())) for _ in range(a)]

# 喜歡程度加總
song_preferences = [0] * m
for fan in fan_preferences:
    for i, preference in enumerate(fan):
        song_preferences[i] += preference

# sort
sorted_songs = sorted(enumerate(song_preferences, start=1), key=lambda x: x[1], reverse=True)

# 前n首
selected_songs = sorted_songs[:n]
selected_song_indices = [song[0] for song in selected_songs]
selected_song_values = [song[1] for song in selected_songs]

# 輸出
with open('output.txt', 'w') as f:
    f.write("like: {}\n".format(song_preferences))
    f.write("songList: {}\n".format(selected_song_indices))

# 讀粉絲(哪一個)
fan_preference = fan_preferences[b-1]

# 找到最喜歡的
favorite_song = max(enumerate(fan_preference, start=1), key=lambda x: x[1])[0]

# 歌單有的話 往前一格
if favorite_song in selected_song_indices:
    selected_song_indices.remove(favorite_song)
    selected_song_indices.insert(0, favorite_song)
else:
    # 替換最後一個
    selected_song_indices[-1] = favorite_song

# 輸出
with open('output2.txt', 'w') as f:
    f.write("Favor: {}\n".format(favorite_song))
    f.write("SongList: {}\n".format(selected_song_indices))