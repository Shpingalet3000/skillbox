violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_of_songs = int(input("Сколько песен выбрать? "))
total_duration = 0

for i in range(1, num_of_songs + 1):
    song_name = input(f"Название {i}-й песни: ")
    if song_name in violator_songs:
        total_duration += violator_songs[song_name]

print(f"Общее время звучания песен: {round(total_duration, 2)} минуты.")
