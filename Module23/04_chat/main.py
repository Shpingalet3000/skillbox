user_name = input('Введите имя пользователя: ')

while True:
    print('\n1. Посмотреть текущий текст чата.\n'
          '2. Отправить сообщение.')
    answer = input('Ваш выбор: ')
    if answer == '1':
        try:
            with open('chat_history.txt', 'r', encoding='utf-8') as chat_file:
                messages = chat_file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Пока сообщений нет.')

    elif answer == '2':
        user_message = input('\nВведите сообщение: ')
        with open('chat_history.txt', 'a', encoding='utf-8') as chat_file:
            chat_file.write('{name}: {message}\n'.format(name=user_name, message=user_message))
    else:
        print('Такой команды нет. Введите 1 или 2.')
