phone_dict = dict()

def add_contacts():
    name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if name not in phone_dict:
        phone_number = int(input('Введите номер телефона: '))
        phone_dict[name] = phone_number
        print('Текущий словарь контактов:', phone_dict)
    else:
        print('Такой человек уже есть в контактах.')


def search_contact(contacts_dict):
    found_contacts = []
    search = input('Введите фамилию для поиска: ').lower()
    for name, surname in contacts_dict.keys():
        if surname.lower() == search:
            found_contacts.append((name, surname, contacts_dict[(name, surname)]))

    if found_contacts:
        print("Найденные контакты:")
        for name, surname, phone in found_contacts:
            print(name, surname, phone)
    else:
        print("Контакты с такой фамилией не найдены.")


while True:
    # print("Введите номер действия:")
    # print("1. Добавить контакт.")
    # print("2. Найти человека.")
    #
    # command = input()

    command = int(input('Введите номер действия (1. Добавить контакт; 2. Найти контакт): '))

    if command == 1:
        print(f'При выборе действия {command}:')
        add_contacts()
    elif command == 2:
        print(f'При выборе действия {command}:')
        search_contact(phone_dict)
    else:
        print("Некорректный ввод. Попробуйте ещё раз.")
