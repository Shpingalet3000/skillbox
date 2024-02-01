import os

try:
    with open('people.txt', 'r', encoding='utf-8') as peoples, open('errors.log', 'w', encoding='utf8') as log_file:
        line_count = 0
        sym_result = 0
        for line in peoples:
            try:
                len_line = len(line)
                line_count += 1
                if line.endswith('\n'):
                    len_line -= 1
                sym_result += len_line
                if len_line < 3:
                    raise ValueError
            except ValueError:
                error_msg = 'Ошибка: менее трёх символов в строке {}.'.format(line_count)
                print(error_msg)
                log_file.write(error_msg + "\n")
        print('Общее количество символов: {}.'.format(sym_result))
except FileNotFoundError:
    print('Файл не найден.')