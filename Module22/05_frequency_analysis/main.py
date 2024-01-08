import string

text_file = open('text.txt', 'r', encoding='utf-8')

text = text_file.read().lower()
dict_letter = {}
for i_letter in text:
    if i_letter in string.ascii_letters:
        num = dict_letter.get(i_letter, 0)
        dict_letter[i_letter] = num + 1
text_file.close()

total_dict_letter = sum(dict_letter.values())

frequency_dict = [(i_elem, round((count / total_dict_letter), 3)) for i_elem, count in dict_letter.items()]
frequency_dict.sort(key=lambda i_elem: i_elem[0])
frequency_dict.sort(key=lambda i_elem: i_elem[1], reverse=True)

with open('analysis.txt', 'w') as file:
    for i_elem, freq in frequency_dict:
        file.write(f"{i_elem}: {freq}\n")
