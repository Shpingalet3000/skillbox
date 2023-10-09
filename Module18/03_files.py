file_name = input('Название файла: ')
special_symbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
file_extension = ('.txt', '.docx')
if file_name.startswith(special_symbols):
    print('Ошибка: название начинается недопустимым символом.')
elif not file_name.endswith(file_extension):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.', file_name)
