def search_key(struct, key, depth=None):
    if depth < 1 and depth is not None:
        return None

    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = search_key(sub_struct, key, None if depth is None else (int(depth) - 1))
            if result:
                return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Введите искомый ключ: ')
quest_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if quest_deep == "y":
    max_deep = int(input('Введите глубину поиска: '))

else:
    max_deep = None

value = search_key(site, user_key, max_deep)
if value:
    print("Значение ключа:", value)
else:
    print("Такого ключа в структуре сайта нет.")
