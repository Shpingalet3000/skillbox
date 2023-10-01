people_count = int(input('Количество человек: '))
number = int(input('Какое число в считалке?: '))
print(f'Значит выбывает каждый {number}-й человек')
people = list(range(1, people_count + 1))
index_eliminated = 0

while len(people) > 1:
    print('\nТекущйи круг людей:', people)
    start_count = index_eliminated % len(people)
    print('Начало счёта с номера:', people[start_count])
    index_eliminated = (start_count + number - 1) % len(people)
    print('Выбывает человек под номером', people[index_eliminated])
    people.remove(people[index_eliminated])

print('\nОстался человек под номером', people[0])

