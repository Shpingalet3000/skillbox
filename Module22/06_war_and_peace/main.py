import zipfile

with zipfile.ZipFile('voina-i-mir.zip', 'r') as zip_ref:
    zip_ref.extractall()

with open('voina-i-mir.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()
dict_letter = {}
for i_letter in text:
    if i_letter.isalpha():
        num = dict_letter.get(i_letter, 0)
        dict_letter[i_letter] = num + 1


total_dict_letter = sum(dict_letter.values())

frequency_dict = [(i_elem, count) for i_elem, count in dict_letter.items()]
frequency_dict.sort(key=lambda i_elem: (i_elem[1]))

for i_elem, count in frequency_dict:
    print(f"{i_elem}: {count}")

