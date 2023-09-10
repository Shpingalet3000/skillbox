films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']

favorite_films = []

num_films = int(input("Сколько фильмов хотите добавить? "))

for i in range(num_films):
    film = input("Введите название фильма: ")
    if film in films:
        favorite_films.append(film)
    else:
        print("Ошибка: фильма", film, "у нас нет :(")

print("Ваш список любимых фильмов:", favorite_films)
print("Ваш список любимых фильмов:", ", ".join(favorite_films))
