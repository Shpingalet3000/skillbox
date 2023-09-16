guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'гостей', guests)
    command = input('Гость пришел или ушел? ')
    if command == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', name + '!')
            guests.append(name)
        else:
            print('Прости, ' + name + ', но мест нет.')
    elif command == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
            print('Пока,', name + '!')
            guests.remove(name)
        else:
            print('Такого гостя на вечеринке нет.')
    elif command == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
