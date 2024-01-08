zen_file = open('zen.txt', 'r', encoding='utf-8')
list_file_strings = zen_file.readlines()
print(''.join(reversed(list_file_strings)))
zen_file.close()
