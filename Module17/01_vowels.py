vowel_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

final_vowels = [symbol for symbol in input('Введите текст: ') if symbol in vowel_list]

print('Список глаcных букв:', final_vowels)
print('Длина списка:', len(final_vowels))

