def caesar_cipher(string, user_shift):
    new_str = ''
    letter_code = [upper_case_alphabet[(upper_case_alphabet.index(sym) + user_shift) % len(upper_case_alphabet)]
                   if sym not in lower_case_alphabet and sym not in punctuation_marks and sym != ' ' else
                   lower_case_alphabet[(lower_case_alphabet.index(sym) + user_shift) % len(lower_case_alphabet)]
                   if sym not in upper_case_alphabet and sym not in punctuation_marks and sym != ' ' else
                   '.' if sym in punctuation_marks else ' ' for sym in string]

    for letter in letter_code:
        new_str += letter
    return new_str


upper_case_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_case_alphabet = 'абвгдеёжзийклмнопрстуфзцчшщъыьэюя'
punctuation_marks = ['"', ',', '.', '!', ';', ':', '?', ')', '(', '-']
input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))
output_str = caesar_cipher(input_str, shift)
print('Зашифрованное сообщение (все знаков препинания заменены на точку):', output_str)
