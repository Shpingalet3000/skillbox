string = input('Введите строку: ').split()
word_length_list = [len(word) for word in string]
max_word = string[word_length_list.index(max(word_length_list))]

print('Самое длинное слово: {}'.format(max_word))
print('Длина этого слова: {}'.format(len(max_word)))
